import flet as ft
from services.pdf.pdf_process_jlle import process_pdfs_jlle
from services.pdf.pdf_process_campinas import process_pdfs_campinas

def file_selected(e, page, open_file_button, name_text_control):
    if e.files:
        name_text_control.value = f"Arquivo selecionado: {e.files[0].name}"
        open_file_button.disabled = True
        page.update()
        process_pdf_and_update(e.files[0].path, page, open_file_button)
    else:
        name_text_control.value = "Nenhum arquivo selecionado."
    page.update()  

def folder_selected(e, page, name_text_control, open_folder_button):
    if e.path:
        name_text_control.value = f"Pasta selecionada: {e.path}"
        open_folder_button.disabled = True
        page.update()
        convert_pdfs(e.path, page, open_folder_button)
    else:
        name_text_control.value = "Nenhuma pasta selecionada."
    page.update()  

def show_success_dialog(message, page):
    snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor="green")
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()
    
def show_processing_dialog(message, page):
    snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor="blue")
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()

def process_pdf_and_update(pdf_path, page, open_file_button):
    show_processing_dialog(f"Processing...",page)
    output_folder = process_pdfs_jlle(pdf_path)
    show_success_dialog(f"PDFs salvos em: {output_folder}", page)
    open_file_button.disabled = False
    page.update()  

def convert_pdfs(pdf_path, page, open_folder_button):
    show_processing_dialog(f"Processing...",page)
    output_folder = process_pdfs_campinas(pdf_path)
    show_success_dialog(f"PDFs salvos em: {output_folder}", page)
    open_folder_button.disabled = False
    page.update()
    