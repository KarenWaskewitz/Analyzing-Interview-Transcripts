import pandas as pd
import re

def hebrew_tokenize(text):
    return re.findall(r'\w+', text)

def classify_utterance(text):
    if not isinstance(text, str):
        return "Unclear"

    tokens = hebrew_tokenize(text)
    tokens = [t.lower() for t in tokens]

    narrative_pronouns = {'אני', 'אנחנו', 'זוכר', 'זכרתי', 'חשבתי', 'רציתי'}
    temporal_words = {'אחרי', 'לפני', 'כאשר', 'כשה', 'ואז'}
    emotional_words = {'אהבתי', 'שמחתי', 'פחדתי', 'התרגשתי', 'רציתי', 'חשבתי'}

    logical_connectives = {'כי', 'אם', 'לכן', 'בגלל'}
    science_words = {'ניסוי', 'תוצאה', 'חומר', 'תגובה', 'חומצה', 'בסיס', 'מדד', 'בדקנו'}

    narrative_score = sum(t in narrative_pronouns for t in tokens) \
                    + sum(t in temporal_words for t in tokens) \
                    + sum(t in emotional_words for t in tokens)

    scientific_score = sum(t in logical_connectives for t in tokens) \
                     + sum(t in science_words for t in tokens)

    if narrative_score > scientific_score:
        return "Narrative"
    elif scientific_score > narrative_score:
        return "Scientific"
    else:
        return "Unclear"

# Load and filter
filename = "students_transcript.xlsx"
df = pd.read_excel(filename)

# Keep only students ב and ג
df = df[df['Student'].isin(['ב', 'ג'])]

# Drop empty utterances
df = df.dropna(subset=['Utterance'])

# Classify
df['Mode'] = df['Utterance'].apply(classify_utterance)

# --- Save one combined file with all utterances and modes ---
df.to_excel("classified_utterances_bg_combined.xlsx", index=False)

# --- Calculate percentages per student ---
mode_counts = df.groupby(['Student', 'Mode']).size().unstack(fill_value=0)

# Calculate percentage of each mode per student
mode_percentages = mode_counts.div(mode_counts.sum(axis=1), axis=0) * 100
mode_percentages = mode_percentages.round(2)  # Round to 2 decimals

# Save percentages to Excel
mode_percentages.to_excel("student_mode_percentages_bg.xlsx")

print("✅ Combined utterances file and mode percentages file saved!")
