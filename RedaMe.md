##AutoEmail项目
```
--conf 配置文件夹
        ——config.yaml 数据库等配置信息(结合个人的数据库信息)
        ——sql script  sql脚本,用于从数据库中提取数据(大家需要自己实现)
--cron 定时脚本
        --auto_email.cron 定时发送邮件，需要配置crond服务
--data数据(报表excel)存储
        ——`weekly` 存储周报，用于邮件发送的附件
--logs 日志存储目录
        ——`operation_business_weekly` 运营业务的周报日志存储
--scripts 脚本文件目录
        ——`auto_email.sh` 项目执行的脚本文件
-- src 主文件目录(业务文件:每增加一个业务可以在这里面多写一个即可)
        ——`businessWeekly.py` 运营业务周报处理文件
-- utils 工具目录
        ——`getData.py`从数据库获取数据，并存储excel文件
        ——`logs`日志功能实现文件
        ——`mysql_ctrl.py`数据库连接，增删查改操作文件
        ——`sendEmail.py`发送邮件文件 
```
```
本项目主要是实现自动邮件服务，定期向运营或相关需求部门，发送邮件报表。大家需要的可以
通过修改以下文件，即可使用：
    1>config.yaml文件
    2>sql 脚本文件
    3> src中的业务文件，businessWeekly.py
    4>getData.py
    5>sendEmail.py
修改不会很难，逻辑已经打通，有问题可以及时提问就好。
```

      