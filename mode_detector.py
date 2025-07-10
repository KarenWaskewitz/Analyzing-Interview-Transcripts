import pandas as pd
import nltk

nltk.download('punkt')

df = pd.read_excel("Transcript.xlsx")  # Hebrew file name OK too
text_column = "טקסט"  # Hebrew column name

narrative_keywords = [ "האור חוזר" ,"בית" ,"הם" ,"הוא", "רוצה", "עושה חור", "אןכל","כמו"]
scientific_keywords = [   "נזונים" ,"סיבה" ,"גורם" ,"מפרק","זה מחזיר את האור" ,"גזי חממה", "מטאן" ,"פחמן דו ממצני","בקטריה","דובי קוטב", "חיידק" ,"בית גידול"]


def detect_mode(text):
    if pd.isna(text):
        return "לא ידוע"

    text_lower = str(text).lower()
    narrative_score = sum(1 for word in narrative_keywords if word in text_lower)
    scientific_score = sum(1 for word in scientific_keywords if word in text_lower)

    if scientific_score > narrative_score:
        return "מדעי"
    elif narrative_score > scientific_score:
        return "נרטיבי"
    else:
        return "לא ברור"


df['סוג טקסט'] = df[text_column].apply(detect_mode)

mode_counts = df['סוג טקסט'].value_counts()

print("\n--- שכיחויות ---")
print(mode_counts)
print(f"\nהסוג הנפוץ ביותר: {mode_counts.idxmax()} ({mode_counts.max()} מופעים)")

df.to_excel("output_hebrew.xlsx", index=False)