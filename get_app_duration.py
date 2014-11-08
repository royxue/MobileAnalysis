"""
get app duration
"""
import MySQLdb
import re
import time

def get_app_duration():
    cate_file = open("app_category.txt", "r")
    
    pat = r'(.*?),(\w+)'
    category_dict = {}
    for line in cate_file:
        info = ''.join(line)
        infoo = re.findall(pat, info)
        category_dict[infoo[0][0]] = infoo[0][1]
    
    connection = MySQLdb.Connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql1 = "SELECT * from user_session"
    t.execute(sql1)
    session = t.fetchall()

    for sess in session:
        # (1L, 1393506484647.0, 'afbaec11-75c4-48df-b43c-3878b3359a04', 1393506485646.0, 999.0)  session sample 
        sql2 = "SELECT * from applications_history WHERE device_id='%s' AND process_importance=100 AND %d<timestamp<%d" % (sess[2], sess[1], sess[3])
        t.execute(sql2)
        app_list = t.fetchall()
        for info in app_list:
            # (1L, 1394367994962.0, '6d4c24e8-80ae-4d0a-a24a-71fce85098b9', 'com.android.settings', 'Settings', 100L, 32259L, 1394368030106.0, 1L) info sample
            category = category_dict[info[3]]
            timestamp = time.gmtime(info[1]/1000.0)
            time_hour = timestamp[3]
            # time_of_day transfer morning:0 afternoon:1 evening:2
            if 4<=time_hour<12:
                time_of_day = 0
            elif 12<=time_hour<18:
                time_of_day = 1
            elif 18<=time_hour<=24 or 0<=time_hour<=3:
                time_of_day = 2
            
            duration = info[7] - info[1]

            sql3 = "INSERT INTO user_app_duration (device_id, category, duration, time_of_day) VALUES('%s', '%s', %d, %d)"%(info[2], category, duration, time_of_day)
            t.execute(sql3)
            
    connection.commit()


if __name__ == "__main__":
    get_app_duration()
