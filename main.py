#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules import ImageDownloader
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

Keys = {
    "API_KEY"               : config_ini.get('Env','API_KEY'),
    "API_SECRET"            : config_ini.get('Env','API_SECRET'),
    "ACCESS_TOKEN"          : config_ini.get('Env','ACCESS_TOKEN'),
    "ACCESS_SECRET"         : config_ini.get('Env','ACCESS_SECRET')
}

Params = {
    "screen_name"           : config_ini.get('Params','SCREEN_NAME'),
    "count"                 : config_ini.get('Params','COUNT'),
    "include_entities"      : 'True',
    "exclude_replies"       : config_ini.get('Params','EXCLUDE_REPLIES'),
    "include_rts"           : config_ini.get('Params','INCLUDE_RTS'),
    "max_id"                : config_ini.get('Params','MAX_ID')
}

def main():
    GetCount = 5
    NewParams = ImageDownloader.run(Keys,Params,GetCount)
    config_ini.set('Params', 'MAX_ID', str(NewParams['max_id']))
    with open('config.ini', 'w') as file:
        config_ini.write(file)
    
if __name__ == '__main__':
    main()
