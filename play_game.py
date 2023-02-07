import pandas as pd
import set
import data_control as dc
import tabulate


def cal_score(team):
    table_for_user = pd.concat([
        dc.GK[dc.GK['Name']==team[0]], 
        dc.DF[dc.DF['Name']==team[1][0]],
        dc.DF[dc.DF['Name']==team[1][1]],
        dc.DF[dc.DF['Name']==team[1][2]],
        dc.DF[dc.DF['Name']==team[1][3]]
        ])
    table_for_user = pd.concat([
        table_for_user,
        dc.MF[dc.MF['Name']==team[2][0]],
        dc.MF[dc.MF['Name']==team[2][1]],
        dc.MF[dc.MF['Name']==team[2][2]]
    ])
    table_for_user = pd.concat([
        table_for_user,
        dc.FW[dc.FW['Name']==team[3][0]],
        dc.FW[dc.FW['Name']==team[3][1]],
        dc.FW[dc.FW['Name']==team[3][2]]
    ])

    sum_result = table_for_user['Total Score'].sum()

    print(tabulate.tabulate(table_for_user, headers='keys', tablefmt = 'pretty'))

    return sum_result
