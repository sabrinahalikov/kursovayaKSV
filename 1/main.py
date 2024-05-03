#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import threading
import flet as ft
import os
from modules.db import DB
from UI.visual_draw import UI
from modules.config_parser import ConfigParser
from parsers.avito import Avito
############static variables#####################
config_name = 'secrets.json'
#################################################


#парсинг данных о квартирах в случае установленного флага в конфиге
def updater():
    if config.get_config()['update_apartments']:
        threading.Thread(target=Avito, args=(db, config)).start()


if __name__ == '__main__':
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(config_name)
    db = DB(config.get_config()['db_path'])
    updater()
    ui = UI(config.get_config(), db)
    ft.app(target=ui.main, port=999, assets_dir=work_dir, view=ft.AppView.WEB_BROWSER)