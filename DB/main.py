import pymysql

# mariadb연동을 위한 모듈 import


def query_mysql(table, number, title, content, date, url):
    connect = pymysql.connect(host='localhost', user='h2', password='Rjstw750', db='ict', charset='utf8')
    cur = connect.cursor()
    sql = "insert into " + table + " (number, title, content, date, url) values('" + number + "', '" + title + "', '" + content + "', '" + date + "', '" + url + "');"
    cur.execute(sql)
    connect.commit()
