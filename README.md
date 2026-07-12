# 🤖 AI Code Agent

An autonomous multi-agent AI system that transforms natural language project ideas into complete software projects. Built using **LangGraph**, **LangChain**, and **Groq LLM**, the agent plans, designs, generates, reviews, and debugs code automatically.

---

# 📋 Table of Contents

- Overview
- Features
- Prerequisites
- Installation
- Setup
- Usage
- Project Structure
- Workflow
- Agent Architecture
- Configuration
- Troubleshooting
- Future Roadmap
- Contributing
- License

---

# 🎯 Overview

AI Code Agent is an autonomous multi-agent coding system that accepts a software project idea from the user and automatically generates a complete project.

Unlike traditional code generators, this project follows an agentic workflow where each AI agent has a dedicated responsibility.

Current workflow:

- 🧠 Planner Agent
- 🏗️ Architect Agent
- 💻 Coder Agent
- 🔍 Reviewer Agent
- 🐞 Debugger Agent

The generated project is automatically saved inside the **projects/** directory.

---

# ✨ Features

✅ Autonomous Software Generation

✅ Multi-Agent Workflow

✅ Project Planning

✅ Software Architecture Generation

✅ Automatic Code Generation

✅ Code Review

✅ Automatic Debugging

✅ File & Project Management

✅ LangGraph State Management

✅ Groq LLM Integration

✅ Modular Agent Architecture

---

# 📦 Prerequisites

Before running the project ensure you have:

- Python 3.10+
- Git
- Groq API Key
- pip
- Virtual Environment

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/charankumarreddy46/AI-Code-Agent.git
```

```bash
cd AI-Code-Agent
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Setup

Create a `.env` file

```text
GROQ_API_KEY=YOUR_API_KEY
```

Never commit this file.

---

# ▶️ Usage

Run

```bash
python main.py
```

Example

```
Enter your project idea

> Build a Todo List using HTML CSS and JavaScript
```

The agent automatically executes:

```
Planner

↓

Architect

↓

Coder

↓

Reviewer

↓

Debugger
```

Generated project

```
projects/

└── Build_a_Todo_List/

    ├── index.html

    ├── style.css

    └── script.js
```

---

# 📂 Project Structure

```
AI-Code-Agent/

│

├── agent/

│   ├── graph.py

│   ├── llm.py

│   ├── nodes.py

│   ├── prompts.py

│   ├── schemas.py

│   ├── states.py

│   └── tools.py

│

├── projects/

│

├── logs/

│

├── config.py

├── main.py

├── requirements.txt

├── README.md

└── .gitignore
```

---

# 🔄 Workflow

```
User Request

      │

      ▼

 Planner Agent

      │

      ▼

 Architect Agent

      │

      ▼

 Coder Agent

      │

      ▼

 Reviewer Agent

      │

      ▼

 Debugger Agent

      │

      ▼

 Generated Project
```

---

# 🧠 Agent Architecture

## 🧠 Planner

**Input**

User Request

**Output**

Detailed Project Plan

**Responsibilities**

- Understand user requirements
- Select technology stack
- Define folder structure
- Identify project features

---

## 🏗️ Architect

**Input**

Project Plan

**Output**

JSON Task List

Example

```json
[
  {
    "file_name": "index.html",
    "instructions": "Create homepage"
  },
  {
    "file_name": "style.css",
    "instructions": "Style homepage"
  }
]
```

Responsibilities

- Break project into files
- Generate coding instructions
- Create structured tasks

---

## 💻 Coder

Input

Architect Tasks

Output

Source Code

Responsibilities

- Generate source code
- Create project folders
- Save generated files
- Handle multiple files

---

## 🔍 Reviewer

Input

Generated Code

Output

Code Review

Checks

- Syntax
- Imports
- Best Practices
- Code Quality
- Security
- Missing Logic

---

## 🐞 Debugger

Input

Review Report

Output

Improved Source Code

Responsibilities

- Fix bugs
- Resolve syntax errors
- Improve code quality
- Rewrite problematic files

---

# ⚙️ Configuration

Main configuration lives in

```
config.py
```

Example

```python
MODEL_NAME = "openai/gpt-oss-120b"

TEMPERATURE = 0.2

MAX_RETRIES = 3
```

---

# 🛠 Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- Pydantic
- python-dotenv

---

# 🐛 Troubleshooting

### Missing Packages

```bash
pip install -r requirements.txt
```

---

### Invalid API Key

Verify

```
GROQ_API_KEY
```

inside

```
.env
```

---

### Rate Limit Error

Wait a few seconds and retry.

Or use a lighter model.

---

# 🚀 Future Roadmap

- Runtime Code Execution

- Unit Testing Agent

- Git Agent

- Docker Agent

- Memory

- RAG Integration

- Multi-LLM Support

- FastAPI Backend

- React Dashboard

- Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Commit

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Create Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Charan Kumar**

GitHub

https://github.com/charankumarreddy46

---

⭐ If you found this project useful, consider giving it a Star.
