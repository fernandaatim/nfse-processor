import os
import flet as ft
from .config import configs
from .functions.logic import file_selected, folder_selected

def interface(page: ft.Page):
    configs(page)
    
    assets_path = os.path.join(os.path.dirname(__file__), 'assets', 'images')
    
    folder_picker = ft.FilePicker(on_result=lambda e: file_selected(e, page, open_file_button, name_text_control_jlle))
    folder_picker_for_folders = ft.FilePicker(on_result=lambda e: folder_selected(e, page,name_text_control_campinas, open_folder_button))
    
    open_file_button = ft.ElevatedButton(
        "Select a file", 
        on_click=lambda _: folder_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["pdf"]
        ),
        style=ft.ButtonStyle(
            bgcolor="#C0C0C0",  
            color="black", 
            shape=ft.RoundedRectangleBorder(radius=0),
            text_style=ft.TextStyle(size=18),
        ),
        width=200  
    )
    
    open_folder_button = ft.ElevatedButton(
        "Select a folder", 
        on_click=lambda _: folder_picker_for_folders.get_directory_path(),
        style=ft.ButtonStyle(
            bgcolor="#C0C0C0",  
            color="black", 
            shape=ft.RoundedRectangleBorder(radius=0),
            text_style=ft.TextStyle(size=18),
        ),
        width=200  
    )

    name_text_control_jlle = ft.Text(
        "Nenhum arquivo selecionado.",
        color='black', 
        width=400, 
        size=16, 
        text_align=ft.TextAlign.CENTER, 
        no_wrap=False 
    )

    name_text_control_campinas = ft.Text(
        "Nenhuma pasta selecionada.",
        color='black', 
        width=400, 
        size=16, 
        text_align=ft.TextAlign.CENTER, 
        no_wrap=False 
    )

    top_bar = ft.Container(
        content=ft.Image(src=os.path.join(assets_path, 'bosch_bar.png'), fit=ft.ImageFit.FIT_WIDTH),
        width=600,
        height=8,
        padding=0,
        margin=0,
    )

    logo_image = ft.Container(
        content=ft.Image(
            src=os.path.join(assets_path, 'bosch_logo_basic.png'),
            width=150,
        ),
    )

    top_bar_and_logo = ft.Column(
        controls=[top_bar, logo_image],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=0,
    )

    container_jlle = ft.Container(
        alignment=ft.alignment.center,
        bgcolor="#FFFFFF",
        border_radius=20,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ 
                ft.Row(
                    controls=[ft.Text("NFSe Prefeitura de Joinville", color='black', size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=50
                ),
                ft.Row(
                    controls=[open_file_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=25
                ),
                ft.Row(
                    controls=[name_text_control_jlle],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=50
                )
            ],
        ),
    )
    
    container_campinas = ft.Container(
        alignment=ft.alignment.center,
        bgcolor="#FFFFFF",
        border_radius=20,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ 
                ft.Row(
                    controls=[ft.Text("NFSe Prefeitura de Campinas", color='black', size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=50
                ),
                ft.Row(
                    controls=[open_folder_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=25
                ),
                ft.Row(
                    controls=[name_text_control_campinas],
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=50
                )
            ],
        ),
    )

    page.add(
        ft.Column(
            controls=[top_bar_and_logo, container_jlle, container_campinas],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0, 
            expand=True,
        ),
    )
    
    page.add(folder_picker)
    page.add(folder_picker_for_folders)
    page.update()
