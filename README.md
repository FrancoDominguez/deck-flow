<picture>
  <img alt="Workflow Use logo - a product by Browser Use." src="./static/workflow-use.png"  width="full">
</picture>

<br />

<h1 align="center">Deterministic, Self Healing Workflows (RPA 2.0)</h1>

[![GitHub stars](https://img.shields.io/github/stars/browser-use/workflow-use?style=social)](https://github.com/browser-use/workflow-use/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Cloud](https://img.shields.io/badge/Cloud-☁️-blue)](https://cloud.browser-use.com)
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)

⚙️ **Workflow Use** is the easiest way to create and execute deterministic workflows with variables which fallback to [Browser Use](https://github.com/browser-use/browser-use) if a step fails. You just _show_ the recorder the workflow, we automatically generate the workflow.

❗ This project is in very early development so we don't recommend using this in production. Lots of things will change and we don't have a release schedule yet. Originally, the project was born out of customer demand to make Browser Use more reliable and deterministic.

# Quick start

```bash
git clone https://github.com/browser-use/workflow-use
```

## Build the extension

```bash
cd extension
npm install
npm run build
```

## Setup workflow environment

```bash
cd workflows
uv sync
playwright install chromium
cp .env.example .env
```

## Run the cli

```bash
python cli.py --help
```

# Demos

## Workflow Use filling out form instantly

https://github.com/user-attachments/assets/cf284e08-8c8c-484a-820a-02c507de11d4

## Gregor's explanation

https://github.com/user-attachments/assets/379e57c7-f03e-4eb9-8184-521377d5c0f9

# Features

- 🔁 **Record Once, Reuse Forever**: Record browser interactions once and replay them indefinitely.
- ⏳ **Show, don't prompt**: No need to spend hours prompting Browser Use to do the same thing over and over again.
- ⚙️ **Structured & Executable Workflows**: Converts recordings into deterministic, fast, and reliable workflows which automatically extract variables from forms.
- 🪄 **Human-like Interaction Understanding**: Intelligently filters noise from recordings to create meaningful workflows.
- 🔒 **Enterprise-Ready Foundation**: Built for future scalability with features like self-healing and workflow diffs.

# Vision and roadmap

Show computer what it needs to do once, and it will do it over and over again without any human intervention.

## Workflows

- [ ] Nice way to use the `.json` files inside python code
- [ ] Improve LLM fallback when step fails (currently really bad)
- [ ] Self healing, if it fails automatically agent kicks in and updates the workflow file
- [ ] Better support for LLM steps
- [ ] Take output from previous steps and use it as input for next steps
- [ ] Expose workflows as MCP tools
- [ ] Use Browser Use to automatically create workflows from websites

## Developer experience

- [ ] Improve CLI
- [ ] Improve extension
- [ ] Step editor

## Agent

- [ ] Allow Browser Use to use the workflows as MCP tools
- [ ] Use workflows as website caching layer
