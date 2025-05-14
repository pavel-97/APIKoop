FROM python:3.12.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV POETRY_VERSION=1.8.2
RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app
COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["sh", "-c", "poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload"]