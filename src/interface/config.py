import os
import flet as ft

def get_icon():
    icon = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'icon_bosch.ico')
    return icon

def configs(page):
    icon = get_icon()
    page.window_icon = icon
    page.bgcolor ="#FFFFFF"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "NFSe Processor"
    page.window.width = 600
    page.window.height = 450
    page.window.maximizable = False
    page.window.resizable = False
    page.padding=0
    page.spacing=0
    page.scroll=None
    page.window.center()
    page.update()