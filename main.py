# -*- coding: utf-8 -*-

from modules import ImageDownloader
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

Keys = {
    "API_KEY"               : config_ini.get('Env','API_KEY'),
    "API_KEY_SECRET"        : config_ini.get('Env','API_KEY_SECRET'),
    "ACCESS_TOKEN_KEY"      : config_ini.get('Env','ACCESS_TOKEN_KEY'),
    "ACCESS_TOKEN_SECRET"   : config_ini.get('Env','ACCESS_TOKEN_SECRET')
}

Params = {
    "screen_name"           : config_ini.get('Params','SCREEN_NAME'),
    "count"                 : config_ini.get('Params','COUNT'),
    "include_entities"      : config_ini.get('Params','INCLUDE_ENTITIES'),
    "exclude_replies"       : config_ini.get('Params','EXCLUDE_REPLIES'),
    "include_rts"           : config_ini.get('Params','INCLUDE_RTS'),
    "max_id"                : config_ini.get('Params','MAX_ID')
}

def main():
    NewParams = ImageDownloader.run(Keys,Params)
    config_ini.set('Params', 'MAX_ID', str(NewParams['max_id']))
    with open('config.ini', 'w') as file:
        config_ini.write(file)
    
if __name__ == '__main__':
    main()
