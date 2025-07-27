import pandas as pd
from openai import OpenAI
import os

# ✅ Set your API key
client = OpenAI(api_key="Paste your API here")  # Replace with your actual key

# Load the Excel file
filename = "students_transcript.xlsx"
df = pd.read_excel(filename)

# Filter only students ב and ג
df = df[df['Student'].isin(['ב', 'ג'])]

# Store results
modes = []
reasons = []

# Analyze each utterance with GPT
for idx, row in df.iterrows():
    utterance = str(row['Utterance'])
    print(f"Analyzing utterance {idx + 1}/{len(df)}...")

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in educational psychology analyzing student utterances."},
                {"role": "user", "content": f"""According to Jerome Bruner's theory, classify the following student utterance as 'Narrative', 'Scientific', or 'Mixed/Unclear' mode of thought.
Utterance: {utterance}
Explain briefly why you chose this mode."""}
            ]
        )

        full_response = response.choices[0].message.content.strip()

        # Split response if formatted as Mode + Reason
        if "Reason:" in full_response:
            mode_line, reason_line = full_response.split("Reason:", 1)
            mode = mode_line.replace("Mode:", "").strip()
            reason = reason_line.strip()
        else:
            mode = "Unknown"
            reason = full_response

    except Exception as e:
        mode = "Error"
        reason = f"API error: {e}"

    modes.append(mode)
    reasons.append(reason)

# Add results to the DataFrame
df['Mode'] = modes
df['Reason'] = reasons

# Save detailed results
df.to_excel("students_gpt_analysis_results.xlsx", index=False)
print("✅ Detailed results saved to: students_gpt_analysis_results.xlsx")

# Save summary percentages
summary = df.groupby('Student')['Mode'].value_counts(normalize=True).unstack(fill_value=0) * 100
summary.to_excel("students_gpt_summary_percentages.xlsx")
print("✅ Summary saved to: students_gpt_summary_percentages.xlsx")
