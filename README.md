# fs-explorer

CLI agent that helps you explore a directory and its content (it can also read PDF/PPTX/DOCX/XLSX files!).

## Installation and Usage

Clone this repository:

```bash
git clone https://github.com/run-llama/fs-explorer
cd fs-explorer
```

Install locally:

```bash
uv pip install .
```

Export Azure OpenAI credentials:

```bash
export AZURE_OPENAI_API_KEY="..."
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT="gpt-4o"  # Optional, defaults to gpt-4o
```

Run:

```bash
explore --task "Within the data/ directory, can you help e find the PDF file that contains an order or a complaint, and, once you found them, ask me which one I would like you to summarize"
```

