import json
from pathlib import Path
from openpyxl import load_workbook

excel_files = Path.cwd().joinpath("EXCEL").glob("*.xlsx")

quantities_dict = {}

for files in excel_files:
    wb = load_workbook(files)
    sheets_names = wb.sheetnames
    for sheet in sheets_names:
        ws = wb[sheet]
        for cols in ws.iter_cols(values_only=True):
            if cols[0]:
                # getting rid of Nones in the tuple
                clean_columns = [data for data in cols[1:] if isinstance(data, int)]
                if quantities_dict.get(cols[0]):
                    quantities_dict[cols[0]] += len(clean_columns)
                else:
                    quantities_dict[cols[0]] = len(clean_columns)


with open("firsttry.txt", "w") as file:
    for key in quantities_dict:
        file.write("Description: " + key + " " + "Amount: " + str(quantities_dict[key]))
        file.write("\n")

