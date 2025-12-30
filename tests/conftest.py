from fs_explorer.models import StopAction, Action


class MockChoice:
    def __init__(self):
        self.message = MockMessage()


class MockMessage:
    def __init__(self):
        self.content = Action(
            action=StopAction(final_result="this is a final result"),
            reason="I am done",
        ).model_dump_json()


class MockChatCompletion:
    def __init__(self):
        self.choices = [MockChoice()]


class MockCompletions:
    async def create(self, *args, **kwargs) -> MockChatCompletion:
        return MockChatCompletion()


class MockChat:
    @property
    def completions(self):
        return MockCompletions()


class MockAsyncAzureOpenAI:
    def __init__(self, api_key: str, azure_endpoint: str, api_version: str) -> None:
        return None

    @property
    def chat(self) -> MockChat:
        return MockChat()
