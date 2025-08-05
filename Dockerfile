FROM python:3.10-slim

WORKDIR /llm-chatbot
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ Azure expects the container to serve on port 8000

EXPOSE 8000
CMD ["streamlit", "run", "./index.py", "--server.port=8000", "--server.address=0.0.0.0","--server.enableCORS=false", "--server.headless=true"]
# ✅ Optional healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8000/_stcore/health || exit 1

 

