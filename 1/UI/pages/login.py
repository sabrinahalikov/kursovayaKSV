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


class Login:
    def __init__(self, db):
        super(Login, self).__init__()
        self.__crud = CRUD(db)

    def login(self, pg: PageData):
        def login_btn(e):
            if len(user_login.value) > 0 and len(user_password.value) > 0:
                # Проверям наличие логина\пароля в БД
                if self.__crud.check_login(user_login.value, user_password.value):
                    pg.page.session.set('creds', [user_login.value, user_password.value])
                    pg.navigator.navigate('main', pg.page)
                else:
                    open_dlg_modal(None)
            else:
                open_dlg_modal(None)

        def close_dlg(e):
            dlg_modal.open = False
            pg.page.update()

        def redirect_on_reg(e):
            pg.navigator.navigate('registration', pg.page)

        def open_dlg_modal(e):
            pg.page.dialog = dlg_modal
            dlg_modal.open = True
            pg.page.update()

        pg.page.title = "Страница входа"
        pg.page.bgcolor = "#828282"  # Установить белый цвет фона страницы

        logo_text = ft.Text(value='RealtorParser\n'
                                  '\n'
                                  '\n'
                                  '\n'
                                  '\n', text_align=ft.TextAlign.CENTER, size=36, color='black')
        name_page = ft.Text(value='Вход', text_align=ft.TextAlign.CENTER, size=32, color='black')
        login_text = ft.Text(value='Логин', text_align=ft.TextAlign.CENTER, size=20, color='black')
        user_login = ft.TextField(width=334, height=41)
        password_text = ft.Text(value='Пароль', text_align=ft.TextAlign.CENTER, size=20, color='black')
        user_password = ft.TextField(width=334, height=41, password=True, can_reveal_password=True)
        login_button = ft.FilledButton(text='Войти', width=334, height=41, on_click=login_btn)
        reg_button = ft.FilledButton(text='Зарегестрироваться', width=334, height=41, on_click=redirect_on_reg)

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Вы ввели неверные данные"),
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
                    login_text,
                    user_login,
                    password_text,
                    user_password,
                    login_button,
                    reg_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )