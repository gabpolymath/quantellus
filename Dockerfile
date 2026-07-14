FROM python:3.13-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/

# render
EXPOSE 10000

# Avviamo uvicorn dicendogli di usare la porta dinamica passata da Render ($PORT).
# Se la variabile $PORT non esiste, userà la porta 8000.
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
