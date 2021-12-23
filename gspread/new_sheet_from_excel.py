import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import gspread_dataframe as gd

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)
client = gspread.authorize(creds)
google_sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1SJr8wRfYufQKFIk3pKyqATvAR86Mu6yBcT7CzZREq5M/edit#gid=0")
worksheet = google_sh.get_worksheet(0)
worksheet.clear()
df = pd.read_excel("all_data.xlsx", encoding="UTF-8")

gd.set_with_dataframe(worksheet, df)


