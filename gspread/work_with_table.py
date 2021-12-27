import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)
client = gspread.authorize(creds)

#sh = client.create('hmm')
#sh.share('muhindimakzn@gmail.com', perm_type='user', role='writer')

google_sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1SJr8wRfYufQKFIk3pKyqATvAR86Mu6yBcT7CzZREq5M/edit#gid=0")
worksheet = google_sh.get_worksheet(0)
df = pd.DataFrame(data=worksheet.get_all_values())
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
insertRow = ['Test', 'Test', 'Test', 'Test','Test', 'Test']
# worksheet.append_row(insertRow, table_range="B2:D7")
# worksheet.delete_rows(68)


cell_list = worksheet.range('A2:G2')
cell_values = [1, 2, 3, 4, 5, 6, 7]

for i, val in enumerate(cell_values):  #gives us a tuple of an index and value
    cell_list[i].value = val    #use the index on cell_list and the val from cell_values


worksheet.update_cells(cell_list)

worksheet.delete_rows(2,80)
worksheet.delete_columns(1, 10)




