
import yaml
import logging
import pandas as pd
import datetime
import numpy as np
from utils.mysql_ctrl import MysqlCtrl
from utils import logs

# log = logging.getLogger(__name__)

#连接数据库，并完成数据提取和存储，主函数
def process_database(script_name,log,business_name):
    """
    script_name:运行的sql脚本文件

    :return: state
    """

    # #路径为绝对路径
    with open('conf/config.yaml', 'r') as f:
        config_info = yaml.load(f.read())

    ob_db_info = config_info[business_name]
    crawler_db = MysqlCtrl(ob_db_info)
    ret = crawler_db.connect()
    if not ret:
        log.error("failed to connect to crawler database, return" )
        return False

    sql_list = read_sql(script_name)

    data_list=[]
    for sql in sql_list:
        state,data=crawler_db.TB_select(sql)

        if data:
            data_list.append(data)

    filepath=''
    sheetnames=[]
    if business_name=="operation_business_weekly":
        filepath, sheetnames=save_bw_xls(data_list)
    crawler_db.close()
    return filepath,sheetnames


#存储运营周报数据到excel
def save_bw_xls(data_list):

    columns1=['','']

    columns2 = []
    columns3=[]
    columns4=[]

    #这里dtype为float，因为希望excel中数字数据都是数字类型的，当然以后可能有问题
    # df1=pd.DataFrame(data_list[0],columns=columns1,dtype="float")
    # df2 = pd.DataFrame(data_list[1], columns=columns2,dtype="float")
    df1=pd.DataFrame(data_list[0],columns=columns1)
    df2 = pd.DataFrame(data_list[1], columns=columns2)
    df3 = pd.DataFrame(data_list[2], columns=columns3)
    df4 = pd.DataFrame(data_list[3], columns=columns4)


    df2['column_name'][0]=int(df2['column_name'][0])
    df2['column_name'][0] = int(df2['column_name'][0])
    df2['column_name'][0] = int(df2['column_name'][0])
    df2['column_name'][0] = int(df2['column_name'][0])

    start_day =(datetime.date.today()-datetime.timedelta(days=7)).strftime('%Y%m%d')
    end_day = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

    timePeriod=start_day+'-'+end_day

    #路径为绝对路径
    filename='./data/weekly/'+'运营业务周报'+timePeriod+".xlsx"

    writer=pd.ExcelWriter(filename)
    #如果用utf-8
    df1.to_excel(writer,"sheetname1",index=False,encoding='utf-8')
    df2.to_excel(writer, "sheetname2", index=False, encoding='utf-8')
    df3.to_excel(writer, "sheetname3", index=False, encoding='utf-8')
    df4.to_excel(writer, "sheetname4", index=False, encoding='utf-8')

    sheetnames=["",""]
    writer.save()
    return filename,sheetnames

#从脚本文件中读取sql语句
def read_sql(script_name):
    """

    :param script_name: sql脚本文件
    :return: 包含sql的list
    """
    with open(script_name, encoding='utf-8', mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        sql_list = f.read().split(';')[:-1]
        result_list=[]
        # print(sql_list)
        for x in sql_list:
            # sql语句添加分号结尾
            sql_item = x + ';'
            result_list.append(sql_item)
            # print(sql_item)
    return result_list

if __name__=="__main__":
    with open('./conf/config.yaml', 'r') as f:
        config_info = yaml.load(f.read())

    ob_log_info = config_info['operation_business_weekly_logger']

    log, _, _ = logs.init_logger(name=ob_log_info.get('name'),
                                 subname=ob_log_info.get('name'),
                                 workspace=ob_log_info.get('path'),
                                 multiproc=True,
                                 stream_level=logging.DEBUG,
                                 file_level=logging.INFO)
    # 指的是业务的名字
    business_name = 'operation_business_weekly'

    script_name = "../conf/运营业务周报_自动邮件SQL_20201020.sql"
    print('select_db :', process_database(script_name,log,business_name))
