# Google ADK (Agent Development Kit) - Learning Project

This project is for learning and building AI agents with Google's **Agent Development Kit (ADK)**.

## 1. Introduction

**ADK (Agent Development Kit)** is Google's open-source Python framework for building, running, testing, evaluating and deploying AI agents. It ships with a CLI tool (`adk`) that covers everything from scaffolding an agent template to running it in a web UI and deploying it.

**Key features:**
- Quickly scaffold an agent template (`adk create`)
- Run agents in the terminal or in a Web UI (`adk run`, `adk web`)
- Expose agents as an API through a FastAPI server (`adk api_server`)
- Evaluate and test agents (`adk eval`, `adk test`)
- Deploy to hosted environments (`adk deploy`)

## 2. Prerequisites

- Python 3.10 or higher
- `pip` (Python package manager)
- A Google AI Studio API key (for Gemini): https://aistudio.google.com/apikey
- Git (optional)

## 3. Setup (From Scratch)

### Step 1: Create a project folder

```bash
mkdir adk-project
cd adk-project
```

### Step 2: Create and activate a virtual environment

```bash
# Create
python -m venv .venv

# Activate - Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activate - Windows (CMD)
.venv\Scripts\activate.bat

# Activate - macOS / Linux
source .venv/bin/activate
```

### Step 3: Install ADK

```bash
pip install google-adk
```

Verify the installation:

```bash
adk --version
```

### Step 4: Create a new agent app

```bash
adk create my_agent
```

This creates a `my_agent/` folder with the following files:

```
my_agent/
├── __init__.py
├── agent.py      # Main agent code (root_agent is defined here)
└── .env          # API key and configuration
```

### Step 5: Set your API key

Add your key to `my_agent/.env`:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

> **Important:** Never push your `.env` file to GitHub. It is already listed in `.gitignore`.

## 4. How to Run the Project

### Option A: With the Web UI (easiest, recommended)

Run this from the **project root folder** (the one that contains the `my_agent/` folder):

```bash
adk web
```

Then open http://localhost:8000 in your browser and select your agent from the dropdown.

### Option B: Run in the terminal

```bash
adk run my_agent
```

### Option C: Run as an API server

```bash
adk api_server
```

## 5. ADK Commands

To see the basic help:

```bash
adk --help
```

Output:

```
Usage: adk [OPTIONS] COMMAND [ARGS]...

  Agent Development Kit CLI tools.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  api_server           Starts a FastAPI server for agents.
  conformance          Conformance testing tools for ADK.
  create               Creates a new app in the current folder with prepopulated agent template.
  deploy               Deploys agent to hosted environments.
  eval                 Evaluates an agent given the eval sets.
  eval_set             Manage Eval Sets.
  generate_agent_card  Generates agent cards for all detected agents.
  migrate              ADK migration commands.
  optimize             Optimizes the root agent instructions using the GEPA optimizer.
  run                  Runs an agent.
  telemetry            Manage telemetry settings.
  test                 Runs pytest on agent test JSON files under the specified folder.
  web                  Starts a FastAPI server with Web UI for agents.
```

### Quick command summary

| Command | Purpose |
|---------|---------|
| `adk create <name>` | Creates a new agent app from a template |
| `adk run <agent>` | Runs the agent in the terminal |
| `adk web` | Starts a server with the Web UI |
| `adk api_server` | Starts only the FastAPI server (no UI) |
| `adk eval` | Evaluates the agent against eval sets |
| `adk eval_set` | Manages eval sets |
| `adk test` | Runs pytest on agent test JSON files |
| `adk deploy` | Deploys the agent to a hosted environment |
| `adk optimize` | Optimizes root agent instructions using the GEPA optimizer |
| `adk generate_agent_card` | Generates agent cards for detected agents |
| `adk conformance` | Conformance testing tools for ADK |
| `adk migrate` | ADK migration commands |
| `adk telemetry` | Manages telemetry settings |

For details on any command:

```bash
adk <command> --help
# Example:
adk web --help
```

## 6. Quick Start (Short Version)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install google-adk
adk create my_agent
# Add GOOGLE_API_KEY to my_agent/.env
adk web
```

## 7. Common Problems

- **`adk: command not found`**: Activate your virtual environment, or re-run `pip install google-adk`.
- **Agent not showing in the dropdown**: Run `adk web` from the **parent folder** of your agent, not from inside the agent folder.
- **API key error**: Check that `GOOGLE_API_KEY` is set correctly in your `.env` file.

## 8. Useful Links

- ADK Docs: https://google.github.io/adk-docs/
- ADK Python GitHub: https://github.com/google/adk-python

