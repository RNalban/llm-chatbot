# LLM ChatBot
An **AI-powered chatbot** built with **Streamlit** and **Retrieval-Augmented Generation (RAG)**, leveraging **Groq API** and **Hugging Face LLMs** for fast and accurate responses from your own documents.

## Features
- 📄 **Document Upload & Search** – Upload PDFs and ask questions about them  
- 🔍 **Retrieval-Augmented Generation (RAG)** – Combines vector search with LLM reasoning  
- ⚡ **Groq API** – Low-latency model inference  
- 🤗 **Hugging Face LLMs** – Support for multiple open-source models  
- 🖥 **Streamlit UI** – Clean, interactive chat interface

## Demo
https://github.com/user-attachments/assets/d3722775-fb37-41aa-92bf-e11ef10bd3a7
## Installation and running locally on PC
- Download the source code with git clone https:///github.com/RNalban/llm-chatbot.git
- Change directory with cd llm-chatbot
-  Build the image with docker build -t llm-chatbot . which will install all libraries
-  Run the container with  docker run -p 8000:8000 llm-chatbot
## Deploying app on Azure
This workflow will:
- Build a Docker image of the application.
- Push the image to Azure Container Registry (ACR).
- Deploy the image from ACR to Azure App Service.

Before running the workflow, ensure that:
- ACR credentials (ACR_USERNAME, ACR_PASSWORD) are stored as GitHub Secrets.
- An Azure App Service Plan is already created — this will define the hosting resources for the app.
- The App Service will be provisioned (or updated) using the existing App Service Plan during deployment.

 This setup enables continuous delivery, so each push to the repository can result in an updated, live application without manual steps.
