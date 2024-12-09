import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')
# filepaths = ['invoices/10003-2023.1.18.xlsx', 'invoices/10001-2023.1.18.xlsx', 'invoices/10002-2023.1.18.xlsx']


pdf = FPDF(orientation='P',unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    filename = Path(filepath).stem
    invoice_nr= filename.split('-')[0]
    date= filename.split('-')[1]

    
    pdf.add_page()
    # Header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=f"Invoice nr. {invoice_nr}", align='L', ln=1)

    # Date
    pdf.set_font(family='Times', style='B', size=20)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=f"Date {date}", align='L', ln=1)

    #Save the page into dir pdf_invoices
    pdf.output(f'pdf_invoices/{filename}.pdf')
    
    