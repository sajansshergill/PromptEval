
import openai
import pandas as pd
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

with open('../prompts/summarization.json', 'r') as f:
    prompts = json.load(f)

outputs = []

for p in prompts:
    if p["tool"] == "ChatGPT":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": p["prompt_text"]}]
        )
        output_text = response['choices'][0]['message']['content']
    else:
        output_text = "[Simulated Copilot Output]"

    outputs.append({
        "task_id": p["task_id"],
        "tool": p["tool"],
        "task_type": p["task_type"],
        "prompt": p["prompt_text"],
        "output": output_text
    })

# Make sure the results folder exists
os.makedirs("../results", exist_ok=True)

df = pd.DataFrame(outputs)
df.to_csv("../results/prompt_outputs.csv", index=False)

print("✅ Saved prompt_outputs.csv to /results")
