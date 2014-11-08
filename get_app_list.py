"""
Get All App List
"""
import MySQLdb


def get_app_list():

    app_list = open('app_list.txt', 'w+')

    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql = "SELECT DISTINCT package_name FROM applications_history"

    t.execute(sql)
    application = t.fetchall()

    for app in application:
        app_list.write(app[0]+'\n')

    app_list.close()


if __name__ == "__main__":
    get_app_list()
