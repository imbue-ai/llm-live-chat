import sys

# Must be set before any llm imports to prevent all entry-point plugins
# from being loaded, matching the behavior of the main test suite.
sys._called_from_test = True

import pytest
from tests.conftest import (  # noqa: F401
    embed_demo,
    env_setup,
    logs_db,
    mock_model,
    async_mock_model,
    register_embed_demo_model,
    register_echo_model,
    user_path,
)

import llm.cli
import llm_live_chat
from llm.plugins import pm


@pytest.fixture(autouse=True)
def register_live_chat_plugin():
    if not pm.is_registered(llm_live_chat):
        pm.register(llm_live_chat, name="undo-llm-live-chat")
    # The register_commands hook already fired during llm.cli import,
    # so we must call it manually for our plugin.
    if "live-chat" not in llm.cli.cli.commands:
        llm_live_chat.register_commands(llm.cli.cli)
    yield
