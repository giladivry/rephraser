FROM python:3.10-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends libpq-dev

WORKDIR /usr/src/app

COPY . .

EXPOSE 8000
CMD ["/usr/src/app/.venv/bin/uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
