FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn langchain langchain-community langchain-mcp streamlit requests

EXPOSE 3333
CMD ["uvicorn", "file_tool:app", "--host", "0.0.0.0", "--port", "3333"]