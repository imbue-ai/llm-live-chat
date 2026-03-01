# llm-live-chat

[![PyPI](https://img.shields.io/pypi/v/llm-live-chat.svg)](https://pypi.org/project/llm-live-chat/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/imbue-ai/llm-live-chat/blob/main/LICENSE)

An [LLM](https://llm.datasette.io/) plugin that provides an interactive chat with support for live message injection from external processes.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-live-chat
```

## Usage

### live-chat

Start an interactive chat session:

```bash
llm live-chat
```

This works like `llm chat` but supports live message injection from external processes via SIGUSR1. The session displays its PID and conversation ID on startup so other processes can inject messages into the running conversation.

Options:

- `-m MODEL` — Model to use
- `-s SYSTEM` — System prompt
- `-c` / `--continue` — Continue the most recent conversation
- `--cid ID` — Continue a specific conversation by ID
- `--show-history` — Display previous messages when continuing a conversation
- `-T TOOL` — Make a tool available to the model
- `-t TEMPLATE` — Use a template
- `-o KEY VALUE` — Model options

### inject

Inject a message into a conversation's database:

```bash
llm inject "Your message here" --cid CONVERSATION_ID
```

If `--cid` is given, the message is injected into that conversation and SIGUSR1 is sent to all running `llm live-chat` processes so they pick it up immediately.

If no `--cid` is given, a new conversation is created.

Options:

- `--cid ID` — Conversation ID to inject into
- `--prompt TEXT` — User message to pair with the injected response (default: "...")
- `-m MODEL` — Model name for new conversations
- `-d DATABASE` — Path to log database

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-live-chat
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
