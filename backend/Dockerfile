FROM python:3.11-slim

WORKDIR /app

COPY backend/require.txt .

RUN pip install --no-cache-dir -r require.txt

COPY backend/main.py .
COPY backend/predictor.py .
COPY backend/schemas.py .
COPY backend/models/ ./models/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]