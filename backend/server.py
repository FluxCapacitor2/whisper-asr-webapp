import os
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import ffmpeg
import whisper
import numpy as np
import requests

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

download_size_cache = {}


@app.get("/size")
def download_size(model: str):
    url = whisper._MODELS[model]
    if url in download_size_cache:
        return download_size_cache[url]
    res = requests.head(url)
    size = int(res.headers.get("Content-Length"))
    download_size_cache[url] = size
    return size


@app.get("/models")
def models():
    models = {}
    root = os.path.join(
        os.getenv("XDG_CACHE_HOME", os.path.join(os.path.expanduser("~"), ".cache")),
        "whisper",
    )
    for model in whisper.available_models():
        models[model] = os.path.exists(f"{root}/{model}.pt")
        # Some models are aliases for others; e.g. "turbo" -> "large-v3-turbo".
        # If a model file with an aliased name is present, the model is already downloaded and should be marked as such.
        for other, url in whisper._MODELS.items():
            if url == whisper._MODELS[model] and os.path.exists(f"{root}/{other}.pt"):
                models[model] = True
    
    return models


@app.post("/transcribe")
def transcribe(
    file: Annotated[UploadFile, File()],
    task: Annotated[str, Form()] = "transcribe",
    model: Annotated[str, Form()] = "base",
    initial_prompt: Annotated[str, Form()] = None,
    word_timestamps: Annotated[bool, Form()] = False,
    language: Annotated[str, Form()] = None,
):
    bytes = file.file.read()
    np_array = convert_audio(bytes)
    whisper_instance = whisper.load_model(model)
    result = whisper_instance.transcribe(
        audio=np_array,
        verbose=True,
        task=task,
        initial_prompt=initial_prompt,
        word_timestamps=word_timestamps,
        language=language if language != "" else None,
    )
    return result


if os.path.exists("/static"):
    print("Serving static files from /static")
    app.mount("/", StaticFiles(directory="/static", html=True), name="static")


def convert_audio(file):
    """
    Converts audio received as an UploadFile to a numpy array
    compatible with openai-whisper. Adapted from `load_audio` in `whisper/audio.py`.
    """
    try:
        # This launches a subprocess to decode audio while down-mixing and resampling as necessary.
        # Requires the ffmpeg CLI and `ffmpeg-python` package to be installed.
        out, _ = (
            ffmpeg.input("pipe:", threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000)
            .run(cmd=["ffmpeg"], capture_stdout=True, capture_stderr=True, input=file)
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0
