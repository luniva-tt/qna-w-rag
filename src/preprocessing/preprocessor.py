import nltk
from nltk.tokenize import sent_tokenize

def flatten_json(content, parent_key=''):
    """Recursively flatten nested JSON to 'section: text' pairs."""
    flat_sections = []
    if isinstance(content, dict):
        for key, value in content.items():
            new_key = f"{parent_key} > {key}" if parent_key else key
            flat_sections.extend(flatten_json(value, new_key))
    elif isinstance(content, list):
        for idx, item in enumerate(content):
            flat_sections.extend(flatten_json(item, parent_key))
    else:
        flat_sections.append((parent_key, str(content)))
    return flat_sections

def chunk_documents_json(docs, max_tokens=500, overlap=50):
    chunks = []
    for doc in docs:
        subject = doc["subject"]
        chapter = doc["chapter"]
        flat = flatten_json(doc["content"])

        for section_path, text in flat:
            sentences = sent_tokenize(text)
            chunk = ""
            tokens = 0

            for sentence in sentences:
                word_count = len(sentence.split())
                if tokens + word_count > max_tokens:
                    if chunk:
                        chunks.append({
                            "subject": subject,
                            "chapter": chapter,
                            "section": section_path,
                            "text": chunk.strip()
                        })
                    # Overlap handling
                    chunk_words = chunk.split()
                    chunk = " ".join(chunk_words[-overlap:]) + " " + sentence
                    tokens = len(chunk.split())
                else:
                    chunk += sentence + " "
                    tokens += word_count

            if chunk.strip():
                chunks.append({
                    "subject": subject,
                    "chapter": chapter,
                    "section": section_path,
                    "text": chunk.strip()
                })

    return chunks
