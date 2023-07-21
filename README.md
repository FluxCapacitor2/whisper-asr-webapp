# `whisper-asr-webapp`

## Architecture

The frontend is built with Svelte and builds to static HTML, CSS, and JS. It makes requests to the backend, which is on a separate port but has permissive CORS headers.

The backend is built with FastAPI. The main endpoint, `/transcribe`, pipes an uploaded file into ffmpeg, then into Whisper. Once transcription is complete, it's returned as a JSON payload.

## Running

1. Clone the repository.
2. Run `docker compose up`. This will build and run both the frontend and backend.
3. Open `http://localhost:5000` in your web browser.
