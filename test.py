# import mysql.connector

import pymssql

# load_dotenv()  # Load primary env variables

# server = os.getenv("OFFICEKIT_DB")
# database = os.getenv("OFFICEKIT_DATABASE_NAME")
# username = os.getenv("OFFICEKIT_USERNAME")
# password = os.getenv("OFFICEKIT_PASS")
# port = int(os.getenv("OFFICEKIT_DB_PORT", "1433"))


def get_db():
    # if company_code == 'A100':
    #     db_name = database
    # else:
    #     db_name = os.getenv(f"EMPIRE_OFFICEKIT_DATABASE_NAME", database)


# Access Credentials:
# Public IP / DNS: 13.203.121.233
# Username: Administrator
# Password: OMDlNDi$Ft-!hjkOi!GObunpJMzn2P26
# RDP Port: 3389

# DB  Credentials:   SQL Server Web Edition
# User Name   sa
# Password    : helloTHIS4


# sreerag T
# 1:40 PM (2 hours ago)
# to me



# EC2AMAZ-G967G8M

# User Name   sa
# Password    : helloTHIS4
    return pymssql.connect(
        host='13.203.121.233',
        server='EC2AMAZ-G967G8M',
        user='sa',
        password='helloTHIS4',
        database='Officekit_Empire',
        port=1433,
        tds_version='7.4'
    )


conn = get_db()
cursor = conn.cursor()

cursor.execute("SELECT * FROM HR_EMP_MASTER")

for row in cursor:
    print(row)


