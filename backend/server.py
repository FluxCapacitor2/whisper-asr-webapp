import os
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
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
    return models


@app.post("/transcribe")
def transcribe(
    file: Annotated[UploadFile, File()],
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
        initial_prompt=initial_prompt,
        word_timestamps=word_timestamps,
        language=language,
    )
    return result


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
