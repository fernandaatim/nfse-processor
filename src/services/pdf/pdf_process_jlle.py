import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")

def get_previous_month_folder():
    current_month = datetime.now().month
    
    if current_month == 1:
        previous_month = 12
    else:
        previous_month = current_month - 1
       
    
    month_name = datetime(2000, previous_month, 1).strftime('%B').capitalize()
    return f"{previous_month:02d} - {month_name}"

def split_pdf(input_pdf, output_folder):
    with pdfplumber.open(input_pdf) as pdf:
        total_pages = len(pdf.pages)
        
    reader = PdfReader(input_pdf)
    
    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        
        output_pdf = os.path.join(output_folder, f"page_{i+1}.pdf")

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Página {i+1} salva como {output_pdf}")

def get_documents_folder():
    return os.path.join(os.environ['USERPROFILE'], 'Documents') if os.name == 'nt' else os.path.join(os.environ['HOME'], 'Documents')

def process_pdfs_jlle(pdf_path):
    user_documents_folder = get_documents_folder()
    output_folder = os.path.join(user_documents_folder, get_previous_month_folder())
    os.makedirs(output_folder, exist_ok=True)
    
    split_pdf(pdf_path, output_folder)
    rename_files(output_folder)
    return output_folder

def extract_name(pdf_path):
    extracted_data = None
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    nf_number_match = re.search(r"Série\s*(\d+)\s*/\s*A1", text)
                    
                    if nf_number_match:
                        extracted_data = nf_number_match.group(1).strip()
                        break
    except Exception as e:
        print(f"Erro ao extrair NF do arquivo {pdf_path}: {e}")
    
    return extracted_data

def rename_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(folder_path, filename)
                nf_number = extract_name(pdf_path)
                
                if nf_number:
                    new_filename = f"{nf_number}-99.pdf"
                    new_path = os.path.join(folder_path, new_filename)
                    
                    os.rename(pdf_path, new_path)
                    print(f"Ok para: {filename} == {new_filename}")
                else:
                    print(f"Não foi possível extrair data: {filename}")                    
                    
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")
