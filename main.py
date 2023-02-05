import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# The glob module finds all the pathnames
filepaths = glob.glob("invoices/*xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # Sheet_name je ime lista v Excelu
    pdf = FPDF(orientation="P", unit="mm", format="A4") # Creating PDF document
    pdf.add_page()

    filename = Path(filepath).stem # to nam vrne samo ime datoteke npr "10001-2023.1.18.xlsx"
    invoice_nr = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}")

    pdf.output(f"PDFs/{filename}.pdf")