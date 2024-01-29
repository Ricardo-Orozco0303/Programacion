import flet as ft

def main(page: ft.Page):
    page.window_width = 350
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "login"

    welcome_text = ft.Text(value="Welcome", size=50, color="green", font_family="Consolas")
    page.add(welcome_text)

    column = ft.Column(
        spacing=20,
        alignment="center",
        controls=[
            ft.Text(value="User", style=ft.TextStyle(size=40,color="green", font_family="Consolas")),
            ft.TextField( width=350, bgcolor=ft.colors.WHITE,),  
            ft.Text(value="Password", style=ft.TextStyle(size=40,color="green", font_family="Consolas")),
            ft.TextField(password=True, width=350, bgcolor=ft.colors.WHITE),
        ],
    ) 
    page.add(column)

ft.app(target=main)




