import pandas as pd
import random

# Generate 1000 dummy prompt scores
tools = ['ChatGPT', 'Copilot']
task_types = ['summarization', 'code_generation', 'explanation']

data = []

for i in range(1, 1001):
    task_id = f"task_{i:04}"
    tool = random.choice(tools)
    task_type = random.choice(task_types)
    clarity = random.randint(3, 5)
    accuracy = random.randint(3, 5)
    tone = random.randint(3, 5)
    overall_score = round((clarity + accuracy + tone) / 3, 2)
    data.append([task_id, tool, task_type, clarity, accuracy, tone, overall_score])

# Save inside the results/ folder
df = pd.DataFrame(data, columns=["task_id", "tool", "task_type", "clarity", "accuracy", "tone", "overall_score"])
df.to_csv("/Users/sajanshergill/Desktop/PromptEval/results/prompt_scores_1000.csv", index=False)

print("✅ Dummy data saved to results/prompt_scores_1000.csv")
