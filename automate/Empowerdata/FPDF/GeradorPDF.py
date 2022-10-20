# importando a biblioteca
from fpdf import FPDF

projeto = input('Digite o projeto: ')
horas_estimadas = input('Digite a quantidade de horas do projeto: ')
valor_hora = input('Digite o valor da hora trabalhada: ')
prazo = input('Digite o prazo estimado em meses: ')
valor_total = int(valor_hora) * int(horas_estimadas)

pdf = FPDF()


#Organizar texto no template
pdf.add_page()
pdf.set_font("Arial")
pdf.image('template.png', x=0, y=0)


pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))


pdf.output(name = 'Orçamento.pdf')

print('Orçamento gerado com sucesso.')
