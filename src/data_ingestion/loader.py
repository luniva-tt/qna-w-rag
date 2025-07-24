import os
import json

def load_json_txt_chapters(data_path="data"):
    documents = []

    for subject in os.listdir(data_path):
        subject_path = os.path.join(data_path, subject)
        if os.path.isdir(subject_path):
            for filename in os.listdir(subject_path):
                if filename.endswith(".txt"):
                    chapter_path = os.path.join(subject_path, filename)
                    try:
                        with open(chapter_path, 'r', encoding='utf-8') as f:
                            content = json.load(f)  # treat .txt as json
                            documents.append({
                                "subject": subject,
                                "chapter": filename.replace(".txt", ""),
                                "content": content
                            })
                    except json.JSONDecodeError as e:
                        print(f"❌ Failed to parse {chapter_path} as JSON: {e}")

    return documents

