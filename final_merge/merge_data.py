"""
Scripts for merge data
"""
import MySQLdb

def merge_data():
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql1 = "SELECT DISTINCT device_id FROM user_app_duration"
    t.execute(sql1)
	
    device_list = t.fetchall()
    for did in device_list:
    	sql2 = "INSERT final_merge (device_id) VALUES('%s')"%(did[0])
    	t.execute(sql2)
    connection.commit()

    category_list =  ['Unknown', 'Communication', 'Social', 'Travel', 'Productivity', 'Weather', 'Finance', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Game', 'Health', 'Libraries', 'Education']
    time_of_day = ['morning', 'afternoon', 'evening']

    for did in device_list:
        time_usage = {c:0 for c in time_of_day}
        for cate in category_list:
            if cate == 'Game':
                sub_list = ['Strategy', 'Racing', 'Action', 'Simulation', 'Puzzle', 'Role', 'Board', 'Arcade', 'Adventure', 'Card', 'Casual', 'Educational', 'Sports',  'Family', 'Trivia', 'Word']
            elif cate == 'Finance':
                sub_list = ['Finance', 'Business', 'Shopping']
            elif cate == 'Lifestyle':
                sub_list = ['Lifestyle', 'Sports']
            elif cate == 'Entertainment':
                sub_list = ['Entertainment', 'Comics', 'Music', 'Photography', 'Media', 'News']
            elif cate == 'Personlization':
                sub_list = ['Personlization', 'Live', 'Widgets', 'Tools']
            elif cate == 'Travel':
                sub_list = ['Travel', 'Transportation']
            else:
                sub_list = []
                sub_list.append(cate)
            for sub in sub_list:
                for time in time_of_day:
                    cate_name = sub + '_' + time
                    sql3 = "SELECT %s FROM final_result WHERE device_id='%s'"%(cate_name, did[0])
                    t.execute(sql3)
                    result = t.fetchall()
                    for line in result:
                        time_usage[time] += line[0]
            
            sum_time = sum(time_usage.values())
	
	    if sum_time == 0:
	        continue
	    morning = time_usage['morning']/float(sum_time)
            afternoon = time_usage['afternoon']/float(sum_time)
            evening = time_usage['evening']/float(sum_time)
            
            cm = cate + '_morning'
            ca = cate + '_afternoon'
            ce = cate + '_evening'

            sql4 = "UPDATE final_merge SET %s=%f,%s=%f,%s=%f where device_id='%s'"%(cm, morning, ca, afternoon, ce, evening, did[0])
            t.execute(sql4)
            sum_time = 0

    connection.commit()      


if __name__ == "__main__":
    merge_data()
