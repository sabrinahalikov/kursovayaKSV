#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import flet as ft
from flet_navigator import VirtualFletNavigator
from UI.pages.login import Login
from UI.pages.registration import Registration
from UI.pages.main import MainPage
############static variables#####################

#################################################


class UI:
    def __init__(self, config, db):
        super(UI, self).__init__()
        self.__vault_keys = ['current_user']
        self.__config = config
        self.__db = db
        self.__login = Login(db)
        self.__pagemain = MainPage(db)
        self.__reg = Registration(db)

    def main(self, page: ft.Page):
        flet_navigator = VirtualFletNavigator(
            {
                '/': self.__login.login,
                'main': self.__pagemain.main_page,
                'registration': self.__reg.registration
            }
        )
        flet_navigator.render(page)