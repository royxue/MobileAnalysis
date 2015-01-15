import MySQLdb


def data_analysis():
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    time_of_day = [0, 1, 2]
    category_list = ['Communication', 'Social', 'Travel', 'Productivity', 'Weather', 'Finance', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Game', 'Health', 'Libraries', 'Education'] # Ignore System Apps here

    """
    # Category usage percentage analysis    
    # per_dict = {}
    time_dict = {}
    
    for cate in category_list:
        # per_dict[cate] = {0:0, 1:0, 2:0}
        time_dict[cate] = {0:0, 1:0, 2:0}

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
                sql = "SELECT * FROM user_app_duration WHERE category='%s' AND time_of_day=%d"%(sub, time)
                t.execute(sql)
                result = t.fetchall()
                for r_line in result:
                    #per_dict[cate][time] += r_line[3]
                    time_dict[cate][time] += 1
    
    # print per_dict
    print time_dict
    """

    user_count = {}
    sql_user = 'SELECT DISTINCT device_id from user_app_duration'
    t.execute(sql_user)
    user_list = t.fetchall()
    for user in user_list:
        sql = "SELECT * FROM user_app_duration WHERE device_id='%s'"%(user[0])

        t.execute(sql)
        result = t.fetchall()
        user_count[user[0]] = [len(result), sum([rec[3] for rec in result])]

    """
    user_list_1 = {}
    user_list_2 = {}
    for user in user_list:
        user_list_1[user[0]] = {}
        user_list_2[user[0]] = {}

        for cate in category_list:
            user_list_1[user[0]][cate] = {0:[0, 0], 1:[0, 0], 2:[0, 0]}
            
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
                    sql = "SELECT * FROM user_app_duration WHERE device_id='%s' AND category='%s' AND time_of_day=%d"%(user[0], sub, time)
                    t.execute(sql)
                    result = t.fetchall()
                    for r_line in result:
                        user_list_1[user[0]][cate][time][0] += 1
                        user_list_1[user[0]][cate][time][1] += r_line[3]
    """
    print user_count


if __name__ == '__main__':
    data_analysis()



