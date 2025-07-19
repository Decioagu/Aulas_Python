from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def criar_pdf_numeros(nome_arquivo="numeros_0_a_1000.pdf"):
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter

    for i in range(1001):  # De 0 a 1000
        c.drawString(largura / 2, altura / 2, str(i))
        c.showPage()  # Inicia uma nova página para o próximo número

    c.save()
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

if __name__ == "__main__":
    criar_pdf_numeros()