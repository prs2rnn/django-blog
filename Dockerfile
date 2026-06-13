FROM python:3.14-slim

ARG BUILD_DATE=unknown
ARG GIT_COMMIT=unknown

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    APP_HOME=/app \
    BUILD_DATE=$BUILD_DATE \
    GIT_COMMIT=$GIT_COMMIT

WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock README.md LICENSE ./

RUN pip install --no-cache-dir poetry && \
    poetry install --only main --no-root --no-interaction

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
