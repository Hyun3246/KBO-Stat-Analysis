import data_control as dc
import tabulate

def cal_ranking(user_data, sum_result):
    # 점수 먼저 저장
    if (dc.user_dataframe["ID"] == user_data.user_id).any():
        dc.user_dataframe.loc[dc.user_dataframe["ID"] == user_data.user_id, "점수"] = sum_result
    else:
        dc.user_dataframe.loc[len(dc.user_dataframe) + 1] = [user_data.user_id, user_data.team_name, sum_result]
    
    dc.user_dataframe.to_excel("Ranking file.xlsx", index=False)

    # 순위 계산
    # new = dc.user_dataframe["점수"].rank()

    # print(new)

    user_dataframe_sorted = dc.user_dataframe.sort_values(by=["점수"], ascending=False)
    print(tabulate.tabulate(user_dataframe_sorted, headers='keys', tablefmt = 'pretty'))

    ranking = str(user_dataframe_sorted[user_dataframe_sorted["ID"] == user_data.user_id].index.values)
    
    print("{}님의 랭킹은 {}위 입니다.".format(user_data.user_id, ranking[1:-1]))