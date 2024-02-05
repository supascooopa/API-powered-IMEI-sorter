from pathlib import Path
import pandas as pd

excel_files = Path.cwd().joinpath("EXCEL").glob("*.xlsx")

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 20)

combine_template = pd.read_excel("Telefon-Cihaz Başvurusu BOŞ SADECE SAVE AS LE.xlsx")
concat_list = [combine_template]
for files in excel_files:
    df = pd.read_excel(files)
    concat_list.append(df.iloc[:,1:-2])


even_newer_df = pd.concat(concat_list)
even_newer_df["MARKA"].value_counts().to_clipboard()
even_newer_df.to_excel("hello.xlsx")
