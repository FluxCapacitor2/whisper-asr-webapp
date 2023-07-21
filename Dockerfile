FROM node:18 AS build-frontend

WORKDIR /app

COPY frontend/package.json ./
COPY frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim-bookworm

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get -qq install --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry

COPY backend/pyproject.toml backend/poetry.lock ./

RUN --mount=type=cache,target=/root/.cache/pypoetry/cache \
    --mount=type=cache,target=/root/.cache/pypoetry/artifacts \
    poetry install --no-root --no-directory --no-dev

COPY --from=build-frontend /app/dist /static
COPY backend/ ./

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "server:app" ]