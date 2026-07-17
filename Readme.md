# Agent Loop

**A lightweight autonomous AI agent built from scratch using the ReAct pattern.**

> No LangChain. No LangGraph. Just Python, an LLM, and a simple execution loop.

---

## Why I Built This

Most AI agent frameworks abstract away the core execution loop.

I wanted to understand **how autonomous agents actually work under the hood**, so I started building one from first principles.

This project is my journey into AI Systems Engineering.

The goal is to build a generic agent that can:

- Think
- Choose tools
- Observe results
- Reason about new information
- Repeat until a task is complete

---

## Architecture

```text
                User Goal
                     │
                     ▼
             Prompt Builder
                     │
                     ▼
                  LLM
                     │
                     ▼
             Response Parser
                     │
                     ▼
          Thought / Action
                     │
                     ▼
              Tool Execution
                     │
                     ▼
              Observation
                     │
                     └───────────────► Next Iteration
```

The engine itself has no knowledge of the task being solved.

Whether the user asks:

- Research Stripe
- Summarize today's AI news
- Research a website

…the execution loop remains exactly the same.

Only the available tools change.

---

## Current Features

- ReAct execution loop
- Agent state management
- Thought / Action / Observation events
- Prompt builder
- Response parser
- Tool execution system
- Current date tool
- Web search tool
- Web page scraping
- Terminal execution logs
- Gemini integration

Example execution:

```text
Goal
────────────────────────────

Get today's AI news

Iteration 1

💭 Thought
Need today's date.

🔧 Action
get_current_date

👀 Observation
2026-07-17

Iteration 2

💭 Thought
Search today's AI news.

🔧 Action
web_search

👀 Observation
Top search results...

Iteration 3

💭 Thought
Summarize findings.

✅ Final Answer
...
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/agent-loop.git

cd agent-loop
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

---

## Running the Agent

Run the agent by providing a goal as a command-line argument.

```bash
python3 main.py "Get today's AI news"
```

More examples:

```bash
python3 main.py "Research Stripe"

python3 main.py "Summarize today's AI news"

python3 main.py "Find the latest Python release"

python3 main.py "Research Model Context Protocol"
```

---

## Tech Stack

- Python
- Gemini API
- Pydantic
- Rich
- BeautifulSoup
- HTTPX
- DDGS (DuckDuckGo Search)

---

## Roadmap

### ✅ Phase 1

- ReAct Engine
- Prompt Builder
- Parser
- Tool System
- Web Search
- Web Scraping

---

## What I Learned

Building an autonomous agent is much more than calling an LLM.

Some of the biggest lessons so far:

- Separating reasoning from tool execution
- Maintaining state across iterations
- Designing prompts that encourage good planning
- Building generic tools instead of task-specific logic
- Treating the LLM as a decision-maker rather than a source of answers

---

## Future Goal

The long-term vision is to evolve Agent Loop into a reusable autonomous agent framework capable of solving a wide variety of tasks by selecting and orchestrating tools dynamically.

---

Contributions, feedback, and discussions are always welcome.
