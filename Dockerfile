FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

ENV UV_NO_DEV=1

RUN uv sync --locked

CMD ["uv", "run", "doot-bot"]
