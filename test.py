from extractTextFrom2colHTML import getTextFrom2HTML
from main import pdftohtml_test


def extract_text(filepath: str) -> list[str]:
    htmlFilePath = pdftohtml_test(filepath)
    text = getTextFrom2HTML(htmlFilePath)
    return text