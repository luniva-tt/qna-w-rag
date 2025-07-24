import fitz
import pytesseract
from PIL import Image
import io
import re
import json

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(page):
    pix = page.get_pixmap()
    img_bytes = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_bytes))
    text = pytesseract.image_to_string(img)
    return text

def extract_chapters(pdf_path, chapter_titles):
    doc = fitz.open(pdf_path)
    print("Extracting text from PDF...")
    full_text = ""
    for i, page in enumerate(doc):
        print(f"Processing page {i+1}/{len(doc)}")
        full_text += extract_text_from_image(page) + "\n"

    # Normalize chapter titles for splitting
    pattern = '|'.join([re.escape(title.strip()) for title in chapter_titles])
    splits = re.split(f'({pattern})', full_text)

    chapters = {}
    for i in range(1, len(splits), 2):
        title = splits[i].strip()
        content = splits[i+1].strip() if i+1 < len(splits) else ""
        chapters[title] = content

    print("✅ Chapter extraction complete.")
    return chapters

if __name__ == "__main__":
    pdf_path = r"E:\4thsem\rag-pipeline-project\data\Science\chapter_1_scientific_learning.pdf"
    chapter_titles = ["Scientific Learning"]

    chapters = extract_chapters(pdf_path, chapter_titles)

    with open("extracted_chapters.json", "w", encoding="utf-8") as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
