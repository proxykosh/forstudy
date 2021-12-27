import string
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import gspread_dataframe as gd
import gspread_formatting as gf

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)  # файл в папке
client = gspread.authorize(creds)

def add_new_list_and_authorization():
    """
    Для добавления новой таблицы в гугл листы и добавления пользовательской почты в список редакторов
    Без этого не видно будет документ, потому что по умолчанию сервисные аккаунты создают приватные листы
    Вызывать стоит один раз самостоятельно, а потом работать с гугл листом по прямой ссылке, добавил сюда только для
    того, чтобы не потерялось
    :return:
    """
    sh = client.create('hmm')
    sh.share('muhindimakzn@gmail.com', perm_type='user', role='writer')

google_sh = client.open("hmm")
#google_sh = client.open_by_url(
    #"https://docs.google.com/spreadsheets/d/1SJr8wRfYufQKFIk3pKyqATvAR86Mu6yBcT7CzZREq5M/edit#gid=0")  # ссылка на таблицу
worksheet = google_sh.get_worksheet(0)  # получение первого листа гугл листа
worksheet.clear()  # очистка таблицы


"""
удаление существующего форматирования
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(1, 1, 1),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0, 0, 0)),
    horizontalAlignment='CENTER')
gf.format_cell_range(worksheet, "[", fmt)

try:
    worksheet.delete_columns(1, worksheet.col_count)
except:
    pass

df = pd.read_excel("all_data.xlsx", encoding="UTF-8")
last_row_index = str(list(df.shape)[0] + 1)


def get_last_column(indent=None):
    """
    функция нахождения адреса  столбца
    indent - отступ от последнего столбца
    :return: адрес столбца(строка)
    """
    alph = list(string.ascii_uppercase)
    max_column = int(list(df.shape)[1])
    df_columns = list(df.columns)
    if indent == None:
        if max_column // 26 != 0:
            mod = max_column // 26
        else:
            mod = 1
        return alph[max_column % 26 - 1] * mod
    else:
        if (max_column - indent) // 26 != 0:
            mod = (max_column - indent) // 26
        else:
            mod = 1
        return alph[(max_column - indent) % 26 - 1] * mod


gd.set_with_dataframe(worksheet, df)  # датафрейм в гугл лист

"""
форматирование наименований столбцов 
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(1, 1, 1),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0, 0, 0)),
    horizontalAlignment='CENTER',
    verticalAlignment='MIDDLE')
gf.format_cell_range(worksheet, '1', fmt)

"""
форматирование 1 и 2 столбцов
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(1, 1, 1),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0, 0, 0)),
    horizontalAlignment='LEFT',
    verticalAlignment='MIDDLE'
    )
gf.format_cell_range(worksheet, 'A2:' + get_last_column(worksheet.col_count - 2) + str(int(last_row_index) - 1), fmt)

"""
форматирование строки подсчета суммы (последней строки)
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(0.66, 0.83, 0.627),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0, 0, 0)),
    horizontalAlignment='CENTER',
    verticalAlignment='MIDDLE')
gf.format_cell_range(worksheet, last_row_index, fmt)

"""
форматирование ячеек с данными 
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(1, 1, 1),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0.07, 0.478, 0.04)),
    horizontalAlignment='CENTER',
    verticalAlignment='MIDDLE'
)
gf.format_cell_range(worksheet, "C2:" + get_last_column() + str(int(last_row_index) - 1), fmt)
"""
форматирование столбца с суммой
"""
fmt = gf.CellFormat(
    backgroundColor=gf.color(0.66, 0.83, 0.627),
    textFormat=gf.textFormat(bold=True, foregroundColor=gf.color(0, 0, 0)),
    horizontalAlignment='CENTER',
    verticalAlignment='MIDDLE')
gf.format_cell_range(worksheet, get_last_column(), fmt)
worksheet.resize(rows=int(last_row_index), cols=int(list(df.shape)[1]))  # удаление лишних строк

b = gf.Border("DOTTED", gf.Color(0.66, 0.83, 0.627))
fmt = gf.CellFormat(borders=gf.borders(bottom=gf.border('SOLID'), left=gf.border('SOLID'), right=gf.border('SOLID'),
                                       top=gf.border('SOLID')))
gf.format_cell_range(worksheet, '[', fmt)
# неработающие команды, не знаю почему
worksheet.format("1", {"wrapStrategy": "WRAP"})

gf.set_column_width(worksheet, 'A:' + get_last_column(), 200)
worksheet.columns_auto_resize(0, worksheet.col_count)
#for i in range(worksheet.col_count):





