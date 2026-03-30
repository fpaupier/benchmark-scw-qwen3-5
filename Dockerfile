FROM python:3.14-alpine

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY benchmark.py .

CMD ["python", "benchmark.py"]
