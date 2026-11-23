# AI Interview Preparation Mentor

A conversational interview-preparation assistant powered by a local Ollama model. It can ask role- and technology-focused questions, review your answers, and offer supportive feedback. Run it in a terminal or use the Streamlit chat interface.

## Requirements

- Python 3.13
- [Ollama](https://ollama.com/) installed and running locally

## Setup

From the project directory, create and activate a virtual environment in PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Python dependencies and download the default model:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
ollama pull llama3.2
```

## Run

Start the terminal chat:

```powershell
python main.py
```

Or start the Streamlit web app:

```powershell
streamlit run streamlit_app.py
```

## Configuration

The application loads optional settings from a `.env` file in the project directory. By default, it uses the `llama3.2` model, connects to Ollama at `http://localhost:11434`, and sets temperature to `0`.

| Variable | Default | Description |
| --- | --- | --- |
| `MODEL_NAME` | `llama3.2` | Ollama chat model to use |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama server URL |
| `TEMPERATURE` | `0` | Model response temperature |

For example:

```dotenv
MODEL_NAME=llama3.2
OLLAMA_BASE_URL=http://localhost:11434
TEMPERATURE=0
```

## Project layout

```text
app/
  config.py       Environment-based configuration
  llm.py          Ollama chat model setup
  mentor.py       Chat response and history handling
  prompts.py      Interview mentor instructions
main.py           Terminal chat application
streamlit_app.py  Streamlit chat application
```
