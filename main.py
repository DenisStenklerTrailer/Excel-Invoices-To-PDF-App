import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import datetime

# The glob module finds all the pathnames
filepaths = glob.glob("invoices/*xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # Sheet_name je ime lista v Excelu

    pdf = FPDF(orientation="P", unit="mm", format="A4") # Creating PDF document
    pdf.add_page()

    filename = Path(filepath).stem # to nam vrne samo ime datoteke npr "10001-2023.1.18.xlsx"
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1) # ln goes to new line

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=50, h=8, txt=f"Date&Time {invoice_date}", ln=1)

    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    # print(list(df.columns) vrne nam stoplce v excelu oz. imena stolpcev
    pdf.cell(w=30, h=8, txt=columns[0], border=1, align='C')
    pdf.cell(w=60, h=8, txt=columns[1], border=1, align='C')
    pdf.cell(w=40, h=8, txt=columns[2], border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[3], border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[4], border=1, align='C', ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align='C')
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1, align='C')
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, align='C', ln=1)

    pdf.output(f"PDFs/{filename}.pdf")