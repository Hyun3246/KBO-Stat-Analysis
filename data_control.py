import pandas as pd
import tabulate

tabulate.WIDE_CHARS_MODE = True
pd.set_option('display.max_rows', None)

# 선수 정보 데이터 준비
a = pd.read_excel('K리그 선수 명단.xlsx', names=[
    'ID', 'Club', 'Back Number', 'Name', 'Birth', 'Position', 'Total Score', 
    'Appearance', '60 mins on pitch', 'Goals from outside the box', 'Assist', 'Every 3 balls recovered', 'Player of the Match', 'Winning penalty', 'Conceding penalty', 'Missing penalty', 'Yellow card', 'Red card', 'Own goal',
    'Scoring a goal', 'Saving a penalty', 'Clean sheet', 'Every 3 saves', 'Every 2 goal conceded'

])

a['Birth'] = a['Birth'].dt.strftime('%Y-%m-%d')
a['Back Number'] = round(a['Back Number'])



GK = a[a['Position'] == 'GK']
DF = a[a['Position'] == 'DF']
MF = a[a['Position'] == 'MF']
FW = a[a['Position'] == 'FW']


# user 데이터 준비
user_dataframe = pd.read_excel("Ranking file.xlsx")
user_dataframe.index = user_dataframe.index + 1
