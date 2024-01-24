from docx import Document

def create_word_file():
    
    user_text = input("Введите текст: ")

    doc = Document()
    doc.add_paragraph(user_text)

    doc.save("user_text.docx")

create_word_file()