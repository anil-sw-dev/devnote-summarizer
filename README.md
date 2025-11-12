# 📘 DevNote Summarizer

A clean, modular CLI tool that uses **Gemini via LangChain** to summarize developer notes and extract actionable TODOs. Built with modern LangChain best practices and ready to scale into a full agent or RAG pipeline.

---

## 🚀 Features

- 🔹 Summarizes `.md` or `.txt` files using Gemini (`gemini-pro`)
- 🔹 Extracts TODOs and action items from messy dev notes
- 🔹 CLI interface for fast local use
- 🔹 Modular chain logic using LangChain’s `RunnableSequence` (`prompt | llm`)
- 🔹 `.env`-based API key management
- 🔹 Future-proof architecture: ready for agents, memory, or RAG

---

## 🛠️ Tech Stack

| Component        | Description                                  |
|------------------|----------------------------------------------|
| LangChain        | `langchain` with `RunnableSequence`          |
| Gemini           | via `langchain-google-genai`                 |
| Python           | CLI + modular chain logic                    |
| dotenv           | Secure API key loading                       |

---

## 📦 Setup

```bash
git clone https://github.com/your-username/devnote-summarizer.git
cd devnote-summarizer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GOOGLE_API_KEY=your-gemini-api-key-here
```

---

## 📄 Usage

Create a sample note:

```bash
mkdir sample_notes
echo "This is a test note. TODO: Add error handling. Also, update the README." > sample_notes/example.md
```

Run the summarizer:

```bash
python cli.py --file sample_notes/example.md
```

Output:

```
🧠 Summary Output:

**Summary:**
This is a test note that outlines two action items.

**TODOs/Action Items:**
* Add error handling.
* Update the README.
```

---

## 🧠 Architecture

```
cli.py
│
├── chains/
│   └── summarize_chain.py  ← defines prompt | Gemini chain
│
└── sample_notes/
    └── example.md          ← input file
```

- `summarize_chain.py`: defines the Gemini-powered summarization chain  
- `cli.py`: reads file, invokes chain, prints output

---

## 🔮 Future Enhancements

- ✅ Output parsing: structured summary + TODOs  
- ✅ Logging to file or database  
- ✅ Agent scaffolding with tools (e.g., Git inspection)  
- ✅ RAG pipeline with vector DB + retrieval  
- ✅ Web UI or Slack bot interface  

---

## 👨‍💻 Author

Built by [Anil Tomar](https://github.com/anil-sw-dev), Senior Software Engineer. Passionate about scalable GenAI architecture, clean code, and developer productivity.