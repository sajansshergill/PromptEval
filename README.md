# PromptEval: Testing and Documenting the Effectiveness of AI Prompts using Python + Power BI

##  Objective:
To evaluate and document the performance of generative AI tools like ChatGPT and Copilot by testing various prompts and scoring their outputs. The results are visualized using Power BI, and prompt guidelines are versioned using Git with proper documentation.

## Tech Stack:
- Python (prompt testing + CSV generation)

- OpenAI API (ChatGPT integration)

- Power BI (data visualization & dashboarding)

- Git (version control)

- Markdown/Google Docs (documentation)

## Folder Structure:
PromptEval/
├── prompts/
│   ├── summarization.json
│   ├── code_generation.json
│   └── explanation.json
│
├── results/
│   ├── prompt_outputs.csv         # Output from ChatGPT
│   └── prompt_scores.csv          # Manual review scores
│
├── scripts/
│   └── run_prompt_tests.py        # Script to call OpenAI API
│
├── powerbi/
│   └── PromptEvalDashboard.pbix   # Power BI Dashboard file
│
├── docs/
│   ├── prompt_guidelines.md
│   └── prompt_improvement_log.md
│
├── .gitignore
├── README.md
└── requirements.txt


