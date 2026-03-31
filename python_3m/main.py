import flet as ft

def main_page(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT 

    text_hello = ft.Text('Hello')
    text_input = ft.TextField(label='Add ur name here!')

    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.GREEN_100, icon_color=ft.Colors.GREEN_900)
    text_button = ft.TextButton('send')
    icon_button = ft.IconButton(icon=ft.Icons.SEND)

    count = 0 

    def click(e):    
        nonlocal count  
        count += 1            
        text_hello.value = f'Нажато: {count} раз'  
        page.update()        

    elevated_button.on_click = click 
    text_button.on_click = click
    icon_button.on_click = click

    page.add(text_hello, text_input, elevated_button, text_button, icon_button)

ft.app(main_page)
