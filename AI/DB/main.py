import pymysql

# mariadb연동을 위한 모듈 import


def query_mysql(table, number, title, content, date, url, hash_string):
    try:
        connect = pymysql.connect(host='localhost', user='h2', password='Rjstw750', db='ict', charset='utf8')
        cur = connect.cursor()
        sql = "insert into " + table + " (number, title, content, date, url, hash) values('" + number + "', '" + title + "', '" + content + "', '" + date + "', '" + url + "', '" + hash_string + "');"
        # print(sql)
        cur.execute(sql)
        connect.commit()
    except pymysql.err.IntegrityError:
        print("Duplicated entry")
