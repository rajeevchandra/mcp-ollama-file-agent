# 🧠 Ollama MCP Local Agent

> Local AI Agents with Tool Use (Filesystem) Powered by Ollama + LangChain + MCP

## 🚀 Features

- Run local LLMs like `qwen2:7b`, `mistral`, `phi3`, etc.
- Enable tool use via Model Context Protocol (MCP)
- Fetch and summarize files from your filesystem
- Streamlit UI + Python Agent
- Fully Dockerized & offline-capable

## 📦 Project Structure

```
.
├── agent_runner.py
├── file_tool.py
├── mcp-tool.json
├── streamlit_app.py
├── Dockerfile
├── Dockerfile.agent
├── docker-compose.yml
├── docs/
│   └── example.txt
├── .gitignore
└── README.md
```

## 🐳 Run with Docker

```bash
docker-compose up --build
```

- Visit Streamlit: http://localhost:8501
- Agent output shown in terminal
- MCP API: http://localhost:3333/docs

## 📜 License

[MIT](LICENSE)