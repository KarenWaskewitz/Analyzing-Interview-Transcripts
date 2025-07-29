import pandas as pd
import re

# === Tokenization ===
def hebrew_tokenize(text):
    return re.findall(r'\w+', text)

# === Classification based on tokens and patterns ===
def classify_utterance(text):
    if not isinstance(text, str) or text.strip() == "":
        return "Unclear"

    tokens = hebrew_tokenize(text)
    tokens = [t.lower() for t in tokens]

    # Bruner-like features
    narrative_pronouns = {'אני', 'אנחנו', 'זוכר', 'זכרתי', 'חשבתי', 'רציתי'}
    temporal_words = {'אחרי', 'לפני', 'כאשר', 'כשה', 'ואז'}
    emotional_words = {'אהבתי', 'שמחתי', 'פחדתי', 'התרגשתי', 'רציתי', 'חשבתי'}

    # Lemke-like scientific discourse features
    logical_connectives = {'כי', 'אם', 'לכן', 'בגלל'}
    science_words = {'ניסוי', 'תוצאה', 'חומר', 'תגובה', 'חומצה', 'בסיס', 'מדד', 'בדקנו'}

    # Custom domain-related keywords (from your original list)
    narrative_terms = [
        "זרקתי אוכל", "הפח הריח", "הדוב לא מצא קרח", "הקרח התחיל להימס",
        "גור דובים", "אנשים לא שמרו", "קודם", "אחר כך", "ראיתי סרטון", "פעם היה דוב"
    ]
    scientific_terms = [
        "חומר אורגני", "עיכול אנאירובי", "מתאן", "גז חממה", "מיקרואורגניזמים",
        "פירוק", "פליטות", "התחממות גלובלית", "שינוי אקלים", "מערכת אקולוגית"
    ]

    # Scoring system
    narrative_score = sum(t in narrative_pronouns for t in tokens) \
                    + sum(t in temporal_words for t in tokens) \
                    + sum(t in emotional_words for t in tokens) \
                    + sum(1 for phrase in narrative_terms if phrase in text)

    scientific_score = sum(t in logical_connectives for t in tokens) \
                     + sum(t in science_words for t in tokens) \
                     + sum(1 for phrase in scientific_terms if phrase in text)

    if narrative_score > scientific_score:
        return "Narrative"
    elif scientific_score > narrative_score:
        return "Scientific"
    else:
        return "Unclear"

# === Load Excel file ===
filename = "students_transcript.xlsx"
df = pd.read_excel(filename)

# === Filter only students ב and ג ===
df = df[df['Student'].isin(['ב', 'ג'])]

# === Drop rows without utterances ===
df = df.dropna(subset=['Utterance'])

# === Classify each utterance ===
df['Mode'] = df['Utterance'].apply(classify_utterance)

# === Save all utterances and their mode ===
df.to_excel("classified_utterances_bg_combined.xlsx", index=False)

# === Summary counts per student ===
mode_counts = df.groupby(['Student', 'Mode']).size().unstack(fill_value=0)

# === Percentages ===
mode_percentages = mode_counts.div(mode_counts.sum(axis=1), axis=0) * 100
mode_percentages = mode_percentages.round(2)

# === Save results ===
mode_percentages.to_excel("student_mode_percentages_bg.xlsx")

print("✅ Combined utterance classification and summary saved.")
