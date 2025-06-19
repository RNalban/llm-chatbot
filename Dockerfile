FROM python:3.10

WORKDIR /llm-chatbot
COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
ENV port=8080
EXPOSE 8080
ARG GROQ_API_KEY
ENV GROQ_API_KEY=$GROQ_API_KEY

ARG HUGGINGFACEHUB_API_TOKEN
ENV HUGGINGFACEHUB_API_TOKEN=$HUGGINGFACEHUB_API_TOKEN

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
CMD curl --fail http://localhost:8080/_stcore/health || exit 1

CMD [ "streamlit","run","./index.py","--server.port=8080", "--server.address=0.0.0.0" ]

