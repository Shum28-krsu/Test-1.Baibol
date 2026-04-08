import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorites = []
    favorite_name = ""

    greeting_text = ft.Text('История заполнения:')
    favorites_text = ft.Text("Любимчики:")

    def load_history():
        try:
            with open("history.txt", "r", encoding="utf-8") as f:
                for line in f.readlines():
                    greeting_history.append(line.strip())
        except:
            pass

    def save_history(text):
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def get_favorites(e):
        nonlocal favorite_name

        if favorite_name and favorite_name not in favorites:
            favorites.append(favorite_name)

        favorites_text.value = "Любимчики:\n" + "\n".join(favorites)
        page.update()

    def text_name(e):
        nonlocal favorite_name

        name = text_input.value.strip()

        if name:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE

            now = datetime.now()
            time_str = now.strftime("%H:%M")

            greeting = f"{time_str} - {name}"

            greeting_history.append(greeting)

            if len(greeting_history) > 5:
                greeting_history[:] = greeting_history[-5:]

            save_history(greeting)

            favorite_name = name

            greeting_text.value = 'История приветствия:\n' + "\n".join(greeting_history)
            text_input.value = ""
        else:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED_900

        page.update()

    def show_morning(e):
        result = []
        for item in greeting_history:
            hour = int(item.split(":")[0])
            if hour < 12:
                result.append(item)

        greeting_text.value = "Утренние:\n" + "\n".join(result)
        page.update()

    def show_evening(e):
        result = []
        for item in greeting_history:
            hour = int(item.split(":")[0])
            if hour >= 12:
                result.append(item)

        greeting_text.value = "Вечерние:\n" + "\n".join(result)
        page.update()

    def show_all(e):
        greeting_text.value = 'История приветствия:\n' + "\n".join(greeting_history)
        page.update()

    def thememode(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        page.update()

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        page.update()

    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    favorite_button = ft.IconButton(icon=ft.Icons.STAR, on_click=get_favorites)

    morning_btn = ft.ElevatedButton("Утро", on_click=show_morning)
    evening_btn = ft.ElevatedButton("Вечер", on_click=show_evening)
    all_btn = ft.ElevatedButton("Все", on_click=show_all)

    main_object = ft.Row(
        controls=[text_input, btn, clear_button],
        alignment=ft.MainAxisAlignment.CENTER
    )

    filter_row = ft.Row(
        controls=[morning_btn, evening_btn, all_btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    load_history()
    greeting_text.value = 'История приветствия:\n' + "\n".join(greeting_history)

    page.add(text_hello, main_object, theme_btn, filter_row, greeting_text, favorite_button, favorites_text)

ft.app(main_page, view=ft.AppView.WEB_BROWSER)