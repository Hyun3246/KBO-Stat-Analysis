import pandas as pd
import tabulate
import pickle
from data_control import *

tabulate.WIDE_CHARS_MODE = True
pd.set_option('display.max_rows', None)

# 로드와 저장
def load_game(ID_name):
    with open('{}.p'.format(ID_name), 'rb') as file:
        user_data = pickle.load(file)
    return user_data

def save_data(user_data):
    with open('{}.p'.format(user_data.user_id), 'wb') as file:
        pickle.dump(user_data, file)

class Fantasy_Game():
    def __init__(self, user_id, team_name, squad):
        self.user_id = user_id
        self.team_name = team_name
        self.squad = squad
    
    def set_basic_info():
        pass

    def __str__(self):
        return '{}의 구단 {}입니다'.format(self.user_id, self.team_name)


# 개인정보 세팅을 위한 코드
def basic_info():
    print("기본 정보를 입력합니다.")
    user_id = input("사용자ID를 입력하세요: ")
    team_name = input("사용할 팀 이름을 입력하세요: ")
    return [user_id, team_name]

def print_info(position):
    if position == 'GK':
        GK_score = GK.sort_values("Total Score", ascending=False)
        print(tabulate.tabulate(GK_score.loc[:, :'Total Score'], headers='keys', tablefmt = 'pretty'))
    elif position =='DF':
        DF_score = DF.sort_values("Total Score", ascending=False)
        print(tabulate.tabulate(DF_score.loc[:, :'Total Score'], headers='keys', tablefmt = 'pretty'))
    elif position == 'MF':
        MF_score = MF.sort_values("Total Score", ascending=False)
        print(tabulate.tabulate(MF_score.loc[:, :'Total Score'], headers='keys', tablefmt = 'pretty'))
    elif position == 'FW':
        FW_score = FW.sort_values("Total Score", ascending=False)
        print(tabulate.tabulate(FW_score.loc[:, :'Total Score'], headers='keys', tablefmt = 'pretty'))
    else:
        if (a['Name'] == position).any():
            print(tabulate.tabulate(a.where(a['Name'] == position).dropna(), headers='keys', tablefmt = 'pretty'))
        else:
            print("그 선수는 K리그에 등록되어있지 않거나 해당 포지션이 아닙니다.")
    

def select_gk():    
    position = input("검색하려는 골키퍼를 입력하세요(아무것도 입력하지 않으면 점수가 높은 골키퍼부터 보여집니다.): ")
    if position:
        print_info(position)
    else:
        print_info('GK')
    
    while True:
        goalkeeper = input("골키퍼를 입력하세요: ")
        if (GK['Name'] == goalkeeper).any():
            break
        else:
            print("그 선수는 K리그에 없거나 골키퍼가 아닙니다.")
            continue
    return goalkeeper

def select_df():  
    position = input("검색하려는 수비수를 입력하세요(아무것도 입력하지 않으면 점수가 높은 수비수부터 보여집니다.): ")
    if position:
        print_info(position)
    else:
        print_info('DF')
    defender = []
    for i in range(4):
        while True:
            defender_name = input("{}번째 수비수를 입력하세요: ".format(i + 1))
            if (DF['Name'] == defender_name).any():
                defender.append(defender_name)
                break
            else:
                print("그 선수는 K리그에 없거나 수비수가 아닙니다.")
                continue
    return defender

def select_mf(): 
    position = input("검색하려는 미드필더를 입력하세요(아무것도 입력하지 않으면 점수가 높은 미드필더부터 보여집니다.): ")
    if position:
        print_info(position)
    else:
        print_info('MF')
    midfielder = []
    for i in range(3):
        while True:
            midfielder_name = input("{}번째 미드필더를 입력하세요: ".format(i + 1))
            if (MF['Name'] == midfielder_name).any():
                midfielder.append(midfielder_name)
                break
            else:
                print("그 선수는 K리그에 없거나 미드필더가 아닙니다.")
                continue
    return midfielder

def select_fw():    
    position = input("검색하려는 공격수를 입력하세요(아무것도 입력하지 않으면 점수가 높은 공격수부터 보여집니다.): ")
    if position:
        print_info(position)
    else:
        print_info('FW')
    forward = []
    for i in range(3):
        while True:
            forward_name = input("{}번째 공격수를 입력하세요: ".format(i + 1))
            if (FW['Name'] == forward_name).any():
                forward.append(forward_name)
                break
            else:
                print("그 선수는 K리그에 없거나 공격수가 아닙니다.")
                continue
    return forward


def set_new_team():
    print('''
--팀을 설정합니다.--

  - 골키퍼: 1명
  - 수비수: 4명
  - 미드필더: 3명
  - 공격수: 3명

  동명이인은 알파벳으로 구분되어 있습니다. 명단을 자세히 확인한 후 입력하세요.
  ''')
    # 골키퍼 입력
    goalkeeper = select_gk()
    # 수비수 입력
    defender = select_df()
    # 미드필더 입력
    midfielder = select_mf()
    # 공격수 입력
    forward = select_fw()

    print('''
    명단을 소개합니다

    골키퍼: {}
    수비수: {}
    미드필더: {}
    공격수: {}
    '''.format(goalkeeper, defender, midfielder, forward))
    return [goalkeeper, defender, midfielder, forward]


def change_team(data):
    while True:
        want_to_change = input("바꾸기를 원하는 포지션을 입력하세요(GK, DF, MF, FW, 이외는 종료): ")
        
        if want_to_change == 'GK':
            # 골키퍼 입력
            goalkeeper = select_gk()
            data.squad[0] = goalkeeper
            continue
        elif want_to_change == 'DF':
            defender = select_mf()
            data.squad[1] = defender
            continue
        elif want_to_change == 'MF':
            midfielder = select_mf()
            data.squad[2] = midfielder
            continue
        elif want_to_change == 'FW':
            forward = select_fw()
            data.squad[3] = forward
            continue
        else:
            print(data.squad)
            print('''
            명단을 소개합니다

            골키퍼: {}
            수비수: {}
            미드필더: {}
            공격수: {}
            '''.format(data.squad[0], data.squad[1], data.squad[2], data.squad[3]))

            print("변경 없이 그대로 갑니다.")
            break
    return data.squad
