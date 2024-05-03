#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import flet as ft
from flet_navigator import PageData
from modules.CRUD import CRUD
############static variables#####################

#################################################


class Registration:
    def __init__(self, db):
        super(Registration, self).__init__()
        self.__crud = CRUD(db)
        self.__dlg_modal = None

    def registration(self, pg: PageData):
        def reg_btn(e):
            # Проверям наличие логина\пароля в БД
            if not self.__crud.check_login(login_field.value, pass_field.value):
                self.__crud.add_user([name_field.value, sur_name_field.value, email_field.value, login_field.value, pass_field.value])
                pg.page.session.set('creds', [login_field.value, pass_field.value])
                pg.navigator.navigate('main', pg.page)
            else:
                open_dlg_modal(None)

        def close_dlg(e):
            dlg_modal.open = False
            pg.page.update()

        def open_dlg_modal(e):
            pg.page.dialog = dlg_modal
            dlg_modal.open = True
            pg.page.update()

        def validate(event):
            print([name_field.value, sur_name_field.value, email_field.value, login_field.value, pass_field.value])
            if all([name_field.value, sur_name_field.value, email_field.value, login_field.value, pass_field.value]):
                reg_button.disabled = False
            else:
                reg_button.disabled = True
            pg.page.update()

        pg.page.title = "Страница регистрации"
        pg.page.bgcolor = "#828282"  # Установить белый цвет фона страницы

        logo_text = ft.Text(value='RealtorParser\n'
                                  '\n'
                                  '\n'
                                  '\n'
                                  '\n', text_align=ft.TextAlign.CENTER, size=36, color='black')
        name_page = ft.Text(value='Регистрация', text_align=ft.TextAlign.CENTER, size=32, color='black')
        name_text = ft.Text(value='Имя', text_align=ft.TextAlign.CENTER, size=20, color='black')
        name_field = ft.TextField(width=334, height=41, on_change=validate)
        sur_name_text = ft.Text(value='Фамилия', text_align=ft.TextAlign.CENTER, size=20, color='black')
        sur_name_field = ft.TextField(width=334, height=41, on_change=validate)
        email_text = ft.Text(value='Почта', text_align=ft.TextAlign.CENTER, size=20, color='black')
        email_field = ft.TextField(width=334, height=41, on_change=validate)
        login_text = ft.Text(value='Логин', text_align=ft.TextAlign.CENTER, size=20, color='black')
        login_field = ft.TextField(width=334, height=41, on_change=validate)
        pass_text = ft.Text(value='Пароль', text_align=ft.TextAlign.CENTER, size=20, color='black')
        pass_field = ft.TextField(width=334, height=41, password=True, can_reveal_password=True, on_change=validate)
        reg_button = ft.FilledButton(text='Зарегестрироваться', width=334, height=41, on_click=reg_btn, disabled=True)
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Акквунт с такими данными уже существует"),
            content=ft.Text("Повторите попытку"),
            actions=[
                ft.TextButton("Ok", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        pg.page.add(
            ft.Row([
                logo_text
            ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row([ft.Column([name_page], alignment=ft.MainAxisAlignment.CENTER)], ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Column([
                    name_text,
                    name_field,
                    sur_name_text,
                    sur_name_field,
                    email_text,
                    email_field,
                    login_text,
                    login_field,
                    pass_text,
                    pass_field,
                    reg_button
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )