"""
Scripts for merge data
"""


def merge_data():
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql1 = "SELECT DISTINCT device_id FROM user_app_duration"
    t.execute(sql1)
	
    device_list = t.fetchall()
    for did in device_list:
    	sql2 = "INSERT merge_result (device_id) VALUES('%s')"%(did[0])
    	t.execute(sql2)
    connection.commit()

    category_list =  ['Unknown', 'Communication', 'Social', 'Tools', 'Travel', 'Productivity', 'Weather', 'News', 'Media', 'Photography', 'Finance', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Music', 'Game']
    time_of_day = ['morning', 'afternoon', 'evening']
    time_list = [0, 1, 2]

    for did in device_list:
        time_usage = {c:0 for c in time_list}
        for cate in category_list:
            if cate == 'Game':
                sub_list = ['Strategy', 'Racing', 'Action', 'Simulation', 'Puzzle', 'Role', 'Board', 'Arcade', 'Adventure', 'Card', 'Casual', 'Educational', 'Sports',  'Family', 'Trivia', 'Word']
            elif cate == 'Finance':
                sub_list = ['Finance', 'Business', 'Shopping']
            elif cate == 'Lifestyle':
                sub_list = ['Lifestyle', 'Medical', 'Health']
            elif cate == 'Entertainment':
                sub_list = ['Entertainment', 'Comics']
            elif cate == 'Books':
                sub_list = ['Books', 'Libraries', 'Education']
            elif cate == 'Travel':
                sub_list = ['Travel', 'Transportation']
            else:
                sub_list = []
                sub_list.append(cate)
            for sub in sub_list:
                for time in time_list:
                    sql3 = "SELECT * FROM user_app_duration WHERE device_id='%s' AND category='%s' AND time_of_day=%d"%(did[0], sub, time)
                    t.execute(sql3)
                    result = t.fetchall()
                    for line in result:
                        time_usage[time] += line[3]
            
            sum_time = sum(time_usage.values())
	
	    if sum_time == 0:
	        continue
	    morning = time_usage[0]/float(sum_time)
            afternoon = time_usage[1]/float(sum_time)
            evening = time_usage[2]/float(sum_time)
            
            cm = cate + '_morning'
            ca = cate + '_afternoon'
            ce = cate + '_evening'

            sql4 = "UPDATE merge_result SET %s=%f,%s=%f,%s=%f where device_id='%s'"%(cm, morning, ca, afternoon, ce, evening, did[0])
            t.execute(sql4)
            sum_time = 0

    connection.commit()      
	
