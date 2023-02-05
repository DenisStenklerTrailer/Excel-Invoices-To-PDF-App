import glob
from fpdf import FPDF

# Create one PDF document
pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("*txt")

for filepath in filepaths:

    pdf.add_page()
    print(filepath)

    title = filepath.split(".")[0]
    print(title)

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=10, h=10, txt=title.capitalize(), ln=1)

    with open(filepath, "r") as file:
        data = file.read()

    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=190, h=7, txt=data)

pdf.output("PDF_Template.pdf")