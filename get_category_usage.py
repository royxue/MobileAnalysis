"""
Get User App Category Usage
"""

import MySQLdb

def get_category():
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')

    t = connection.cursor()

    sql1 = "SELECT DISTINCT device_id FROM user_app_duration"
    t.execute(sql1)

    device_list = t.fetchall()
    time_list = (0,1,2)

    category_list = ['Unknown', 'Communication', 'Social', 'Tools', 'Shopping', 'Travel', 'Productivity', 'Weather', 'News', 'Media', 'Photography', 'Finance', 'Casual', 'Arcade', 'Health', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Music', 'Strategy', 'Business', 'Comics', 'Family', 'Transportation', 'Card', 'Word', 'Libraries', 'Board', 'Sports', 'Racing', 'Action', 'Simulation', 'Puzzle', 'Education', 'Role', 'Trivia', 'Medical', 'Adventure', 'Educational']

    for did in device_list:
	print did
	for cate in category_list:
            time_usage = {tod:0 for tod in time_list}
	    for time in time_list:
		sql2 = "SELECT * FROM user_app_duration WHERE device_id='%s' AND category='%s' AND time_of_day=%d"%(did[0], cate, time)
	        t.execute(sql2)
                info = t.fetchall()
                for line in info:
                    time_usage[time] += line[3]

	    sum_time = sum(time_usage.values())
	
	    if sum_time == 0:
	        continue
	    morning = time_usage[0]/float(sum_time)
            afternoon = time_usage[1]/float(sum_time)
            evening = time_usage[2]/float(sum_time)
    
    	    sql3 = "INSERT INTO user_category (category, device_id, morning, afternoon, evening) VALUES('%s', '%s', %f, %f, %f)"%(cate, did[0], morning, afternoon, evening)
            
            t.execute(sql3)
	    sum_time = 0
    
    connection.commit()


if __name__ == "__main__":
    get_category()

