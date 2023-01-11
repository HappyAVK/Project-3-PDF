import pandas
from fpdf import FPDF
import pandas as pd

df = pandas.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(50, 50, 150)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(50, 150, 50)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for x in range(20, 290, 10):
        pdf.line(10, x, 200, x)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(50, 150, 50)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")