# Look into this website for creating graph rag :
https://microsoft.github.io/graphrag/posts/get_started/
# GraphRAG Installation and Setup Guide

# 1. Install GraphRAG

## pip install graphrag

# 2. Set Up the Data Project

Create Input Directory and place the pdf in input folder:
## mkdir -p ./ragtest/input

# 3. Set Up Environment Variables
Initialize the Workspace:

## python -m graphrag.index --init --root ./ragtest

This will create two files:
.env - Contains the environment variables for running the GraphRAG pipeline.
settings.yaml - Contains the settings for the pipeline.
Configure API Keys:

For OpenAI: Update the GRAPHRAG_API_KEY in the .env file with your OpenAI API key.
For Azure OpenAI: In settings.yaml, set up the Azure OpenAI configuration under the llm: section. Example:

type: azure_openai_chat # or azure_openai_embedding for embeddings
api_base: https://<instance>.openai.azure.com
api_version: 2024-02-15-preview
deployment_name: <azure_model_deployment_name>

# 4. Run the Indexing Pipeline
To run the indexing pipeline, execute:

## python -m graphrag.index --root ./ragtest
