import re
import pandas as pd

# Define your categories
scientific_terms = [
    "בית גידול",
    "הם פולטים גז",
    "קרני שמש מוזר",
    "הדובי קוטב",
    "ממיס את הקרחונים",
    "אין להם מקום"
]

narrative_terms = [
    "בית",
    "הבקטריות אוכלים",
    "מנסות לחזור",
    "דובים",
    "אנחנו לוקחים להם את המקום",
    "הקרחונים נופלים"
]

def analyze_transcript(text):
    sci_found = [word for word in scientific_terms if re.search(rf"\b{word}\b", text, re.IGNORECASE)]
    nar_found = [word for word in narrative_terms if re.search(rf"\b{word}\b", text, re.IGNORECASE)]

    if len(sci_found) > len(nar_found):
        mode = "Scientific"
    elif len(nar_found) > len(sci_found):
        mode = "Narrative"
    else:
        mode = "Mixed/Unclear"

    return sci_found, nar_found, mode

# Load Excel file
filename = "students_transcript.xlsx"
df = pd.read_excel(filename)

# Filter only students ב and ג
df = df[df['Student'].isin(['ב', 'ג'])]

# Analyze each utterance and collect modes
mode_list = []
students_list = []

for idx, row in df.iterrows():
    utterance = str(row['Utterance'])
    student = row['Student']
    _, _, mode = analyze_transcript(utterance)
    mode_list.append(mode)
    students_list.append(student)

# Add the mode column
df['Dominant_Mode'] = mode_list

# Create a count summary table
summary = df.groupby(['Student', 'Dominant_Mode']).size().unstack(fill_value=0)

# Print results to terminal
print("=== Counts of each mode per student ===\n")
for student in summary.index:
    print(f"Student: {student}")
    for mode in summary.columns:
        print(f"  {mode}: {summary.loc[student, mode]}")
    print()  # blank line between students

# Optionally, print percentages too:
print("=== Percentages of each mode per student ===\n")
for student in summary.index:
    total = summary.loc[student].sum()
    print(f"Student: {student}")
    for mode in summary.columns:
        percent = (summary.loc[student, mode] / total * 100) if total > 0 else 0
        print(f"  {mode}: {percent:.2f}%")
    print()
