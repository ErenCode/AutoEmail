
# -*- coding: utf-8 -*-

# coding: utf-8

import pandas as pd


def excel2list():
    filepath="../weekly/运营业务周报.xlsx"
    dataSet = []
    with open(filepath) as fr:
        for line in fr.readlines():
            # curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            # fltline = list(map(float, curline))  # list函数将其他类型的序列转换成字符串；map函数将序列curline中的每个元素都转为浮点型
            # dataSet.append(fltline)
            # print(line.encode("utf-8").decode())
            # curline = line.strip()
            # print(curline)
            print(line)

def excel2databp():
    filepath = "../weekly/运营业务周报.xlsx"
    # df = pd.read_excel(filepath, sheet_name="")
    df = pd.read_excel(filepath, sheet_name="")
    print(df.head())
    print(len(df))
    columns = df.columns.values
    print(type(columns))
    print(columns)
    # for i in range(len(columns)):
    #     print(columns[i])
    dataSet=[]
    for index, row in df.iterrows():
        # print(index)  # 输出每行的索引值
        # print(row)
        inner=[]
        row=row.tolist()
        print(row)
        print(row[1])
        print(type(row[1]))
        # for column in columns:
        #     # print(type(row[column]))
        #
        #     if '' in column:
        #         print(type(row[column]))
        #         tmp=int(row[column])
        #         print(tmp)
        #         # print(type(tmp))
        #         inner.append(tmp)
        #         continue
        #         # print(column)
        #         # print(type(row[column]))
        #         # print(row[column])
        #     inner.append(row[column])
        # dataSet.append(inner)

    print(dataSet)


if __name__=="__main__":
    # excel2list()
    excel2databp()