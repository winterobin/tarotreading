# 🎴 Tarot Card Reader App

This is a simple interactive **Tarot Card Reader** built with [Marimo](https://www.marimo.io/), a Python-based reactive notebook framework. The app simulates drawing three tarot cards — representing the **Past**, **Present**, and **Future** — and displays them with visual card images and their meanings.

---

## 🧠 Features

- 🔮 Draw 3 random tarot cards with a single button click.
- 🃏 Covers both **Major Arcana** and **Minor Arcana** cards.
- 🎨 Generates simple card images using `PIL` with color-coded suits.
- ↕️ Includes both upright and reversed card meanings.
- 🖥️ Fully interactive with a GUI built using Marimo.
- 🤖 Uses a local LLM via Hugging Face Transformers for creative readings.

---

## 🔧 Requirements

- 🐍 Python 3.12+
- 🦄 Marimo ≥ 0.13.15
- [uv](https://github.com/astral-sh/uv) (for fast package management)
- `Pillow` (for image generation)
- `transformers`, `accelerate`, `vllm` (for local LLM)
- `base64`, `random` (standard library)

---

## 🚀 Local Installation 

1.  🛠️ **Install [uv](https://github.com/astral-sh/uv)**
2. ♊ **Clone this repository**
```bash
git clone https://github.com/winterobin/tarotreading.git
cd tarotreading
```


3. ▶️ **Running the App**

```bash
uvx marimo run tarotreading.py
```


4. ✏️ **Editing the App**


```bash
uvx marimo edit
```

---

Enjoy your mystical tarot readings! ✨