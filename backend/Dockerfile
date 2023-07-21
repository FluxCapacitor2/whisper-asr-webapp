FROM python:3.11-bookworm
RUN apt update && apt install ffmpeg -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "--host", "0.0.0.0", "server:app" ]