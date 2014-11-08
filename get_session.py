# _author_: Roy Xue

import MySQLdb

def get_session():

    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql1 = 'SELECT DISTINCT device_id from screen'
    t.execute(sql1)

    device_id = []
    for did in t.fetchall():
        device_id.append(did[0])

    for did in device_id:
        sql2 = "SELECT * from screen where device_id='%s'"%(did)
        t.execute(sql2)
        did_usage = t.fetchall()
        start_time = 0
        end_time = 0
        pre_status = 0
        for line in did_usage:
            if not start_time:
                if line[3] == 1:
                    start_time = line[1]
                    pre_status = 1
            elif start_time:
                if line[3] == 3 and pre_status == 1:
                    start_time = line[1]
                    pre_status = 3
                if line[3] == 0 or line[3] == 2:
                    end_time = line[1]
                    duration = end_time - start_time
                    sql3 = "INSERT INTO user_session (device_id, start_time, end_time, duration) VALUES('%s',%d,%d,%d)"%(did, start_time, end_time, duration)
                    t.execute(sql3)
                    start_time = 0
                    end_time = 0
        
    connection.commit()




if __name__ == "__main__":
    get_session()

