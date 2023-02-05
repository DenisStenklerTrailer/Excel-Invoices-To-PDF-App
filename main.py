import pandas as pd
import glob

# The glob module finds all the pathnames
filepaths = glob.glob("invoices/*xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # Sheet_name je ime lista v Excelu
    print(df)