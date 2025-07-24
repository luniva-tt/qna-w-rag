import fitz  # PyMuPDF
import os

def manual_split(pdf_path, chapter_ranges, save_dir):
    doc = fitz.open(pdf_path)
    os.makedirs(save_dir, exist_ok=True)  # Ensure output folder exists

    for title, (start, end) in chapter_ranges.items():
        new_doc = fitz.open()
        for i in range(start - 1, end):
            new_doc.insert_pdf(doc, from_page=i, to_page=i)
        file_path = os.path.join(save_dir, f"{title}.pdf")
        new_doc.save(file_path)
        print(f"✅ Saved: {file_path}")

# Input path
pdf_path = r"E:\4thsem\rag-pipeline-project\data\Science.pdf"

# Example chapter ranges
ranges = {
    "chapter_1_scientific_learning": (5, 18),
    "chapter_2_classification_of_living_beings": (19, 62),
    "chapter_3_honey_bee": (63, 76),
    "chapter_4_heredity": (77, 114),
    "chapter_5_physiological_structure_and_life_process": (115, 145),
    "chapter_6_nature_and_environment": (146, 170),
    "chapter_7_motion_and_force": (171, 200),
}

manual_split(pdf_path, ranges, "output_chapters")
