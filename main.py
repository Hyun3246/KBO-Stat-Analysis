import set as st
import play_game as pg
import data_control as dc
import ranking as rk

print('''
K리그 Fantasy Football에 오신 것을 환영합니다.

K리그 Fantasy Football은 자신만의 스쿼드를 제작하여 다른 사용자와 점수를 겨루는 게임입니다.
매 라운드 선수의 활약에 따라 점수가 계산되며, 해당 점수는 누적됩니다.
''')

new_or_load = input("진행중인 구단이 있으면 L, 새 구단을 생성하려면 N을 입력하세요: ")

if new_or_load == 'L':
    user_id_to_load = input("ID를 입력하세요: ")
    # 저장된 게임 불러오기
    loaded_game = st.load_game(user_id_to_load)
    # change_team() 함수 불러오기
    changed_team = st.change_team(loaded_game)
    loaded_game.squad = changed_team
    st.save_data(loaded_game)
else:
    print("새로운 게임을 시작합니다.")
    # basic_info() 함수 불러오기
    new_player_info = st.basic_info()
    # set_team() 함수 불러오기
    new_team = st.set_new_team()
    game_data = st.Fantasy_Game(new_player_info[0], new_player_info[1], new_team)
    st.save_data(game_data)
    loaded_game = st.load_game(new_player_info[0])
    

# 점수 계산 함수 불러오기
print("설정한 팀으로 점수를 계산합니다.")
sum_result = pg.cal_score(loaded_game.squad)
dc.user_dataframe.loc[dc.user_dataframe["ID"] == loaded_game.user_id, ["점수"]] = sum_result
print("{}팀의 점수는 {}입니다.".format(loaded_game.user_id, sum_result))

# # 점수 비교 함수 불러오기
# rk.cal_ranking(loaded_game.user_id)