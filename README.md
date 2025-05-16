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

⚙️ **Workflow Use** is the easiest way to create and execute deterministic workflows which have the ability to fallback to [Browser Use](https://github.com/browser-use/browser-use) if something fails.

📚 **How it works**: The recorder uses rr-web events to record the actions and then uses a LLM to convert the actions into a deterministic workflow and automatically exposes the variables the workflow needs. If any of the steps fail, the workflow will fallback to Browser Use for that step and then continue with the next step.

❗ This project is in very early development so we don't recommend using this in production. Lots of things will change and we don't have a release schedule yet. Originally, the project was born out of customer demand to make Browser Use more reliable and deterministic.

# Quick start

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
```

```bash
playwright install chromium
```

## Run the cli

```bash
python cli.py --help
```

# Demos

# Vision

Show computer what it needs to do once, and it will do it over and over again without any human intervention.

# Roadmap

## Workflows

- [ ] Improve LLM fallback when step fails (currently really bad)
- [ ] Self healing, if it fails automatically agent kicks in and updates the workflow file
- [ ] Better support for LLM steps
- [ ] Take output from previous steps and use it as input for next steps
- [ ] Expose workflows as MCP tools

## Developer experience

- [ ] Improve CLI
- [ ] Improve extension
- [ ] Step editor

## Agent

- [ ] Allow Browser Use to use the workflows as MCP tools
- [ ] Use workflows as website caching layer
