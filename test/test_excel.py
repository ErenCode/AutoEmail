
import datetime
import pandas as pd
import numpy as np

def save_xls(data_list):

    columns=['','','']
    print(type(columns))
    print()
    df = pd.DataFrame(data_list,columns=columns)
    print(df.head())

    start_day =(datetime.date.today()-datetime.timedelta(days=7)).strftime('%Y%m%d')
    end_day = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

    timePeriod=start_day+'-'+end_day
    filename=''+timePeriod+'.xlsx'
    df.to_excel(filename,sheet_name="",index=False,encoding='gbk')

#存储运营画像数据到excel
def save_opw_xls(data_list):
    pass
if __name__=="__main__":
    b=((1,2,3),(2,3,4))
    save_xls(b)
    # save_xls([[1,2,3],[2,3,4]])
