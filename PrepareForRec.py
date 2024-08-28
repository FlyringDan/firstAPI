from docx import Document
from docx.shared import Pt


# increase size of font
def prepare_for_rec(path_to_document):
    output_file = 'Files/changedFile.docx'
    document = Document(path_to_document)
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            run.font.name = 'Arial'
            run.font.size = Pt(13)
    document.save(output_file)
    return output_file


