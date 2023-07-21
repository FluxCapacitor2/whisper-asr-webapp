docker build . -t fluxcapacitor2/whisper-asr-webapp:local-dev &&
    docker run -p 8000:8000 --rm -it fluxcapacitor2/whisper-asr-webapp:local-dev
