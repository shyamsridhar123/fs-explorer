import pytest
import os

from unittest.mock import patch
from openai import AsyncAzureOpenAI
from fs_explorer.agent import FsExplorerAgent, SYSTEM_PROMPT
from fs_explorer.models import Action, StopAction
from .conftest import MockAsyncAzureOpenAI


@patch.dict(
    os.environ,
    {
        "AZURE_OPENAI_API_KEY": "test-api-key",
        "AZURE_OPENAI_ENDPOINT": "https://test.openai.azure.com/",
    },
)
def test_agent_init():
    agent = FsExplorerAgent()
    assert isinstance(agent._client, AsyncAzureOpenAI)
    assert len(agent._chat_history) == 1
    assert agent._chat_history[0]["role"] == "system"
    assert agent._chat_history[0]["content"] == SYSTEM_PROMPT
    del os.environ["AZURE_OPENAI_API_KEY"]
    del os.environ["AZURE_OPENAI_ENDPOINT"]
    with pytest.raises(ValueError):
        FsExplorerAgent()


@patch.dict(
    os.environ,
    {
        "AZURE_OPENAI_API_KEY": "test-api-key",
        "AZURE_OPENAI_ENDPOINT": "https://test.openai.azure.com/",
    },
)
def test_agent_configure_task():
    agent = FsExplorerAgent()
    agent.configure_task("this is a task")
    assert len(agent._chat_history) == 2
    assert agent._chat_history[1]["role"] == "user"
    assert agent._chat_history[1]["content"] == "this is a task"


@pytest.mark.asyncio
@patch.dict(
    os.environ,
    {
        "AZURE_OPENAI_API_KEY": "test-api-key",
        "AZURE_OPENAI_ENDPOINT": "https://test.openai.azure.com/",
    },
)
async def test_agent_take_action():
    agent = FsExplorerAgent()
    agent.configure_task("this is a task")
    agent._client = MockAsyncAzureOpenAI(  # type: ignore
        api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        api_version="2024-08-01-preview",
    )
    result = await agent.take_action()
    assert result is not None
    action, action_type = result
    assert isinstance(action, Action)
    assert isinstance(action.action, StopAction)
    assert action.action.final_result == "this is a final result"
    assert action.reason == "I am done"
    assert action_type == "stop"
