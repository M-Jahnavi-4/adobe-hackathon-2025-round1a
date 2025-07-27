import fitz  # PyMuPDF
import os
import json

def extract_outline_from_pdf(file_path):
    doc = fitz.open(file_path)
    title = os.path.splitext(os.path.basename(file_path))[0]
    outline = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"]]).strip()
                if len(text) < 4:
                    continue

                span = line["spans"][0]
                size = span["size"]
                flags = span["flags"]

                if size > 20 and flags == 20:
                    level = "H1"
                elif 16 < size <= 20:
                    level = "H2"
                elif 13 < size <= 16:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_dir, filename)
            outline_data = extract_outline_from_pdf(file_path)
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(output_path, "w") as f:
                json.dump(outline_data, f, indent=2)

if __name__ == "__main__":
    main()
