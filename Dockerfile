FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir "poetry==1.8.3"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY src/ ./src/

RUN mkdir -p /app/logs

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app/src:${PYTHONPATH}

ENTRYPOINT ["python", "-m", "rpa_dolar_poc.__main__"]