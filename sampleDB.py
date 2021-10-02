import mysql.connector
from mysql.connector import errorcode
import os

MYSQL_USERNAME = os.environ["MYSQL_USERNAME"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]

# ログインパラメータの設定
config = {
        'user': MYSQL_USERNAME,
        'password': MYSQL_PASSWORD,
        'host': 'localhost',
        'auth_plugin' : 'mysql_native_password'
    }

# try〜except文でエラー対処
try:
    cnx = mysql.connector.connect(**config)
    print("Connection Success")

# ER_ACCESS_DENIED_ERRORは、DBへのアクセスが拒否された場合のエラーコード
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Cannnot connect database.')
    else:
        print(err)
else:
    cnx.close()
