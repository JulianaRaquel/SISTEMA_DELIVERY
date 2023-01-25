ARG PYTHON_VERSION=3.11-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/


COPY . /app/


EXPOSE 8000


CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "nazirasdelicia.wsgi"]
