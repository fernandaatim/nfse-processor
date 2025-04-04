import calendar
from datetime import datetime
import locale
import os
import re
import shutil
import pdfplumber
from pdfminer.layout import LAParams
from pdfminer.converter import XMLConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import os

def extract_data(folder_path):
    extracted_data = None
    
    try:
        with pdfplumber.open(folder_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                
                if text:
                    data_nf_match = re.search(r'\d{5}(?= / 99)', text)
                    data_uf_match = re.search(r'(MG|PE) BRASIL', text)
                
                    if data_nf_match and data_uf_match:
                        extracted_data = { 
                                          'data_nf': data_nf_match.group(), 
                                          'data_uf': data_uf_match.group(1) if data_uf_match else None 
                                        }
                        break
    except Exception as e:
        print("ERRO", e)
    
    return extracted_data
    
 
def rename_pdf(pdf_folder_path):
    try:
        for file_name in os.listdir(pdf_folder_path):
            if file_name.endswith('.pdf'): 
                pdf_path = os.path.join(pdf_folder_path, file_name)
                extracted_data = extract_data(pdf_path)
                
                if extracted_data:
                    nf_name_format = f'NF 0{extracted_data["data_nf"]}-99 - FCA {extracted_data["data_uf"]} - PROPULSION.pdf'
                    original_name = os.path.basename(pdf_path)
                    new_name = os.path.join(pdf_folder_path, nf_name_format)
                    
                    try:
                        os.rename(pdf_path, new_name)
                        print(f"OK, arquivo {original_name} == {new_name}")
                    except Exception as e:
                        print(f'ERRO AO RENOMEAR: {e}')
                else:
                    print(f'Dados não encontrados para o arquivo {file_name}')
    except Exception as e:
        print(f'Erro ao renomear arquivos: {e}')
    
def get_documents_folder():
    return os.path.join(os.environ['USERPROFILE'], 'Documents') if os.name == 'nt' else os.path.join(os.environ['HOME'], 'Documents')    

def convert_pdf_to_xlm(pdf_folder_path, output_xml_folder):
    os.makedirs(output_xml_folder, exist_ok=True)

    for file_name in os.listdir(pdf_folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file_name)
            xml_path = os.path.join(output_xml_folder, file_name.replace('.pdf', '.xml'))
            
            try:
                with open(pdf_path, "rb") as pdf_file, open(xml_path, "wb") as xml_file:
                    resource_manager = PDFResourceManager()
                    laparams = LAParams()  
                    converter = XMLConverter(resource_manager, xml_file, laparams=laparams)
                    interpreter = PDFPageInterpreter(resource_manager, converter)
                    
                    for page in PDFPage.get_pages(pdf_file):
                        interpreter.process_page(page)
                    
                    converter.close()

                print(f"PDF {file_name} convertido para XML: {xml_path}")
            
            except Exception as e:
                print(f"Erro ao converter {file_name}: {e}")
                
def zip_folder(folder_path):
    zip_path = f"{folder_path}.zip"
    
    try:
        shutil.make_archive(folder_path, 'zip', folder_path)
        print(f"Pasta zipada com sucesso: {zip_path}")
    except Exception as e:
        print(f"Erro ao zipar a pasta: {e}")
    

def process_pdfs_campinas(pdf_folder_path):
    locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")
    user_documents_folder = get_documents_folder()
    
    current_month = datetime.now().month
    current_year = datetime.now().year % 100
    
    if current_month == 1:
        previous_month = 12
        year_for_folder = current_year - 1
    else:
        previous_month = current_month - 1
        year_for_folder = current_year
    
    month_name = calendar.month_name[previous_month]
    month_name_pt = month_name.capitalize()
    
    folder_name = f"Notas Fiscais_STLA_{month_name_pt}.{year_for_folder}_pdf"
    output_xml_folder = os.path.join(user_documents_folder, folder_name)

    os.makedirs(output_xml_folder, exist_ok=True)
    
    rename_pdf(pdf_folder_path)
    convert_pdf_to_xlm(pdf_folder_path, output_xml_folder)
    
    zip_folder(output_xml_folder)  

    return output_xml_folder