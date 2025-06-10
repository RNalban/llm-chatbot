FROM python:3.10-slim

WORKDIR /llm-chatbot
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
ARG GROQ_API_KEY
ENV GROQ_API_KEY=$GROQ_API_KEY

ARG HUGGINGFACEHUB_API_TOKEN
ENV HUGGINGFACEHUB_API_TOKEN=$HUGGINGFACEHUB_API_TOKEN

CMD [ "streamlit","run","./index.py","--server.port=8501", "--server.address=0.0.0.0" ]
