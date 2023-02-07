import data_control as dc

def cal_ranking(user_id):
    user_dataframe_sorted = dc.user_dataframe.sort_values(by=["점수"], ascending=False)
    ranking = user_dataframe_sorted.index(user_dataframe_sorted["ID"] == user_id)
    print(user_dataframe_sorted)
    print("{}님의 랭킹은 {}위 입니다.".format(user_id, ranking))