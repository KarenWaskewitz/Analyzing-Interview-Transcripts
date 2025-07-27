import pandas as pd
import requests

# Config
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"  # Make sure this matches your installed model name
INPUT_FILE = "students_transcript.xlsx"
OUTPUT_FILE = "students_llama_analysis_results.xlsx"

# Load Excel file
df = pd.read_excel(INPUT_FILE)
df = df[df['Student'].isin(['ב', 'ג'])]  # Filter only students ב and ג

modes = []
reasons = []

for idx, row in df.iterrows():
    utterance = str(row['Utterance'])
    print(f"Analyzing utterance {idx+1}/{len(df)}...")

    prompt = (
        "You are an expert in educational psychology. "
        "Classify the following student utterance according to Jerome Bruner's theory as "
        "'Narrative', 'Scientific', or 'Mixed/Unclear'. Provide the classification and a brief explanation.\n\n"
        f"Utterance: {utterance}"
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            },
            timeout=30  # 30 seconds timeout
        )
        response.raise_for_status()
        content = response.json()['message']['content'].strip()

        # Try to parse mode and reason if formatted that way
        if "Reason:" in content:
            mode_line, reason_line = content.split("Reason:", 1)
            mode = mode_line.replace("Mode:", "").strip()
            reason = reason_line.strip()
        else:
            mode = "Unknown"
            reason = content

    except requests.exceptions.Timeout:
        mode = "Error"
        reason = "Request timed out"
    except Exception as e:
        mode = "Error"
        reason = f"Ollama error: {e}"

    modes.append(mode)
    reasons.append(reason)

# Add to DataFrame
df['Mode'] = modes
df['Reason'] = reasons

# Save results to Excel
df.to_excel(OUTPUT_FILE, index=False)
print(f"\n✅ Results saved to: {OUTPUT_FILE}")
