import pandas as pd
import sys
sys.path.append(".")
from utils import getData, sendEmail,logs
import logging
import yaml

"""
该业务文件为项目主入口
每一个业务对应一个文件，该文件会去调用utils下面的getData 和 sendEmail

"""
def get_data(filepath,sheetname):

    filepath = filepath
    df = pd.read_excel(filepath, sheet_name=sheetname)
    # print('df type',df.dtypes)
    #df.values: 对应的二维NumPy值数组。这里代码很有意思，一部分数据，是numpy类型，一部分数据是另一种类型
    # print(df.head())
    # data = df.values.tolist()
    columns = df.columns.values
    data=[]
    for index, row in df.iterrows():
        inner = []
        for column in columns:
            if '' in column:
                tmp=int(row[column])
                inner.append(tmp)
                continue
            inner.append(row[column])
        data.append(inner)

    #columns是个一层列表，但是data是个二层列表
    return columns,data

def get_html_table(filepath,sheetnames):

    """
    :param filepath: the path of the attached file: string "./weekly/运营业务周报.xlsx"
    :param sheetnames: sheetnames of the excel: list of strings ["",""]
    :return: table in html
    """

    table_list=[]
    # table=""
    for i in range(len(sheetnames)):
        columns,data=get_data(filepath,sheetnames[i])
        table ="""<br/><b>表"""+str(i+1)+": "+sheetnames[i]+"""</b><br/><br/>"""
        table=table+"""<tr>"""
        for i in range(len(columns)):
            table = table + """
                <th width='100'>""" + str(columns[i]) + """</th>
                """
        table = table + """</tr>"""
        for i in range(len(data)):
            table = table + """<tr>"""
            for j in range(len(data[0])):
                table = table + """
                        <td width='100'>""" + str(data[i][j]) + """</td>
                        """
            table = table + """<tr>"""
        # table = table + """<br/><br/><br/>"""
        table_list.append(table)

    result=""
    for i in range(len(table_list)):
        result+="""<br/><table width="100%" border="1" style="table-layout:fixed "> """+table_list[i]+"""</table><br/>"""
    result+="""<br/><b><font color="red">请注意保护数据安全！</font></b>"""
    return result


def get_html(filepath,sheetnames):
    """

    :param filepath: the path of the attached file: string "./weekly/运营业务周报0.xlsx"
    :param sheetnames: sheetnames of the excel: list of strings ["",""]
    :return: html
    """

    sheetnames=sheetnames
    table=get_html_table(filepath,sheetnames)
    html="""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>周报</title>
    </head>
    <body>
        <p><b>  各位好，...。以下是主要数据内容，具体请查看附件，有问题请及时沟通。</b></p> 
        """+table+"""  
    </body>
    </html>
    """
    return html

def main(log,business_name):
    sender="xxx@xx.com" #发送人的邮箱
    receiver=['xxx@xx.com']#接受人的邮箱

    cc=[''] #转发人的邮箱
    subject="运营业务周报"
    #发送人邮箱的
    # 用户名和密码
    # 用来去实现自动发送邮件
    username=r''
    password=''
    script_name = "conf/运营业务周报_自动邮件SQL_20201020.sql"
    #执行脚本去从数据库获得数据，存储到data目录下的文件，并作为附件
    filepath,sheetnames= getData.process_database(script_name,log,business_name)
    mail_body = get_html(filepath, sheetnames)
    #邮件的附件名字
    filename = filepath.split('/')[-1]
    sendEmail.send_mail_html(sender, receiver, cc, subject, username, password, filepath, sheetnames, mail_body,log,filename)

if __name__=="__main__":
    # 路径为绝对路径
    with open('conf/config.yaml', 'r') as f:
        config_info = yaml.load(f.read())

    ob_log_info = config_info['operation_business_weekly_logger']

    log, _, _ = logs.init_logger(name=ob_log_info.get('name'),
                                 subname=ob_log_info.get('name'),
                                 workspace=ob_log_info.get('path'),
                                 multiproc=True,
                                 stream_level=logging.DEBUG,
                                 file_level=logging.INFO)
    #指的是业务的名字
    business_name='operation_business_weekly'
    main(log,business_name)
    """
    #本项目因为都用的绝对路径，所以如果要改项目，需要改以下几处：
    1、脚本文件的python环境，和业务文件的路径
    2、yaml配置文件路径
    3、excel报表文件存储路径
    4、sql脚本文件路径
    5、sys.path.append路径
    
    #服务器需要开放的地方
    1、receiver
    2、crontab 文件内容 记得 30 09 * * 1 command
    
    #上服务器又装了包
    1、pandas
    2、pymysql
    3、openpyxl
    4、因为3有依赖xlrd
    
    #报错
    1、server_hostname cannot be an empty string or start with a leading dot.
    
    """
