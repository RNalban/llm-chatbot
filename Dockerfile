FROM python:3.10-slim

WORKDIR /llm-chatbot
COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ Azure expects the container to serve on port 80
ENV port=80
EXPOSE 80

# ✅ Environment variables for Hugging Face and Groq
ARG GROQ_API_KEY
ENV GROQ_API_KEY=$GROQ_API_KEY

ARG HUGGINGFACEHUB_API_TOKEN
ENV HUGGINGFACEHUB_API_TOKEN=$HUGGINGFACEHUB_API_TOKEN

# ✅ Optional healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:80/_stcore/health || exit 1

# ✅ Run Streamlit on port 80