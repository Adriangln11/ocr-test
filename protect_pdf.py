import pytesseract
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from io import BytesIO


class PDFProtector:
    def __init__(self, file_original, file_to_protect, key):
        self.file_original = file_original
        self.file_to_protect = file_to_protect
        self.key = key

    def protect_pdf(self):
        pages = convert_from_path(original)
        pdf_protected = PdfWriter()
        for page, image in enumerate(pages):
            text_extracted = pytesseract.image_to_string(image)
            print('Texto extraido de la pagina {}'.format(page+1))
            print(text_extracted)
            image_bytes = BytesIO()
            image.save(image_bytes, format="PDF")
            image_bytes.seek(0)
            image_pdf = PdfReader(image_bytes)
            pdf_protected.add_page(image_pdf.pages[0])

        pdf_protected.encrypt(key)
        with open(self.file_to_protect, "wb") as file_protected:
            pdf_protected.write(file_protected)


original = "pdf_to_protect.pdf"
to_protect = "pdf_protected.pdf"
key = "password"

protector = PDFProtector(original, to_protect, key)
protector.protect_pdf()
