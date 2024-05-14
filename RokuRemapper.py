import requests
import configparser
from pathlib import Path
from xml.etree import ElementTree

config_file = Path("remap.config")
config = configparser.ConfigParser()

if config_file.exists():
    config.read('remap.config')
    print("Listening to app launches...")
    while True:
        activeapp = requests.get(f'http://{config["1"]["ipaddress"]}:8060/query/active-app')
        appxml = ElementTree.fromstring(activeapp.content)
        app = appxml[0].text
        if app == config["1"]["appname"]:
            print(f'App {config["1"]["appname"]} detected!')
            requests.post(f'http://{config["1"]["ipaddress"]}:8060/launch/{config["1"]["appidto"]}')
else:
    appnamefrom = input("Enter your app name to remap from. MUST BE EXACT: ")
    ipaddress = input("Enter your IP address. You can get this from the Roku settings: ")
    appidto = input("Enter your app id to remap to. You can get this from http://your_roku_ip:8060/query/apps: ")
    config['1'] = {}
    config['1']['appname'] = appnamefrom
    config['1']['ipaddress'] = ipaddress
    config['1']['appidto'] = appidto
    with open(config_file, 'w') as configfile:
        config.write(configfile)

