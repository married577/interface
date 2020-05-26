from common.MySqlHelper import *
import json

conn = pymysql.connect(host='47.105.104.233', user='root', passwd='root', db='student_sys', port=3306,
                       charset='utf8')
cur = conn.cursor()


def data_check():
    cur.execute("SELECT create_time FROM server_school WHERE server_school.server = '123'")
    data_a = cur.fetchone()
    data_aa = json.dumps(data_a, default=str)
    data_aaa = data_aa.replace('"', '').replace('[', '').replace(']', '')

    cur.execute("SELECT id FROM server_school WHERE server_school.server = '123'")
    data_b = cur.fetchone()
    data_bb = json.dumps(data_b, default=str)
    data_bbb = data_bb.replace('"', '').replace('[', '').replace(']', '')

    conn.commit()
    return data_aaa, data_bbb


def data_delete():  # Êý¾ÝÇåÏ´
    cur.execute("DELETE FROM server_school WHERE server_school.server = '123'")
    conn.commit()
    conn.close()








