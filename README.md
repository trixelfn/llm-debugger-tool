# Local AI Coding Assistant (Qwen)

This app runs a local AI model on your computer (no internet needed) and lets you chat with it using a simple desktop UI.

---

## What you need

- macOS or Windows
- Python 3.10+
- At least 8GB RAM (16GB recommended)
- About 4–5GB free storage for the AI model

---

## Step 1 – Install Python

Download Python from:
https://www.python.org/downloads/

During install, tick:
✅ Add Python to PATH

---

## Step 2 – Download this project

Download or clone this repo.

Your folder should look like this:

app/
- app/
- models/
- README.md
- requirements.txt

---

## Step 3 – Put the AI model in the models folder

Download a GGUF model (example: Qwen 2.5 Coder 3B)

Put the model file here:

models/qwen2.5-coder-3b-instruct-q4_k_m.gguf

---

## Step 4 – Open terminal in the app folder

On macOS:

Right click the folder → New Terminal at Folder

Or:

```bash
cd path/to/your/app