# PromptEval: Testing and Documenting the Effectiveness of AI Prompts using Python + Power BI

## 🔍 Overview
PromptEval is a lightweight evaluation framework for testing and documenting the effectiveness of prompts across AI tools like ChatGPT and GitHub Copilot. It automates prompt execution using Python and visualizes results in Power BI, allowing users to iterate, score, and refine prompt strategies for tasks like summarization, explanation, and code generation.

---

## 📁 Project Structure
PromptEval/
├── prompts/                         # Prompt templates in JSON format
│   ├── summarization.json
│   └── code_generation.json
│
├── results/                         # AI outputs and evaluation scores
│   ├── prompt_outputs.csv           # Raw AI-generated outputs
│   └── prompt_scores_1000.csv       # ✅ Your 1000-record scoring dataset
│
├── powerbi/                         # Power BI dashboard file(s)
│   └── PromptEvalDashboard.pbix     # Power BI file (link data to prompt_scores_1000.csv)
│
├── scripts/                         # Python scripts for testing prompts
│   └── run_prompt_tests.py
│
├── docs/                            # Markdown documentation
│   ├── prompt_guidelines.md
│   └── prompt_improvement_log.md
│
├── README.md                        # Project overview and setup instructions
├── requirements.txt                 # Python dependencies
└── .gitignore                       # Ignore .pyc, API keys, etc.


---

## ⚙️ Technologies Used
- **Python** for running prompt tests and storing results
- **OpenAI API** for ChatGPT integration
- **Power BI** for data visualization
- **Git** for version control and collaboration
- **Markdown** for documenting best practices and prompt iterations

---
