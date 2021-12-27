
import gspread
from google.oauth2.service_account import Credentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)  # файл в папке
client = gspread.authorize(creds)
sh = client.create('hmm', folder_id="16Y812yK3Oe63r9Mj1sypBiXXeLcA3xNg")
"""
если создавать в пространстве сервисного аккаунта, нужно открыть доступ с помощью команды ниже
"""
#sh.share('muhindimakzn@gmail.com', perm_type='user', role='writer')