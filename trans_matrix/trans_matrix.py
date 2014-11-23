"""
Scripts for get transfer Matrix
"""
import MySQLdb
import pprint
import re

def trans_matrix():
    result_file = open 
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    sql1 = "SELECT * from user_session"
    t.execute(sql1)
    session = t.fetchall()

    sql1 = "SELECT DISTINCT device_id FROM user_app_duration"
    t.execute(sql1)	
    device_list = t.fetchall()
   
    cate_file = open("app_category.txt", "r")
    pat = r'(.*?),(\w+)'
    category_dict = {}
    for line in cate_file:
        info = ''.join(line)
        infoo = re.findall(pat, info)
        category_dict[infoo[0][0]] = infoo[0][1]

    category_list =  ['Unknown', 'Communication', 'Social', 'Tools', 'Travel', 'Productivity', 'Weather', 'News', 'Media', 'Photography', 'Finance', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Music', 'Game']

    trans_matrix = {}
    for did in device_list:
        trans_matrix[did[0]] = [[0 for x in range(len(category_list))] for y in range(len(category_list))]

    for sess in session:
        # (1L, 1393506484647.0, 'afbaec11-75c4-48df-b43c-3878b3359a04', 1393506485646.0, 999.0)  session sample 
        sql2 = "SELECT * from applications_history WHERE device_id='%s' AND process_importance=100 AND %d<=timestamp AND timestamp<=%d" % (sess[2], sess[1], sess[3])
        t.execute(sql2)
        app_list = t.fetchall()
        pre_cate = ''
        next_cate = ''
        for info in app_list:
        # (1L, 1394367994962.0, '6d4c24e8-80ae-4d0a-a24a-71fce85098b9', 'com.android.settings', 'Settings', 100L, 32259L, 1394368030106.0, 1L) info sample
            cate = category_dict[info[3]]
            if cate in ['Strategy', 'Racing', 'Action', 'Simulation', 'Puzzle', 'Role', 'Board', 'Arcade', 'Adventure', 'Card', 'Casual', 'Educational', 'Sports',  'Family', 'Trivia', 'Word']:
                cate = 'Game'
            elif cate in ['Business', 'Shopping']:
                cate = 'Finance'
            elif cate in ['Medical', 'Health']:
                cate = 'Lifestyle'
            elif cate == 'Comics':
                cate = 'Entertainment'
            elif cate in ['Libraries', 'Education']:
                cate = 'Books'
            elif cate == 'Transportation':
                cate = 'Travel'
            next_cate = cate
            if not pre_cate:
                pre_cate = cate
                next_cate = ''
                continue
            else:
                x = category_list.index(pre_cate)
                y = category_list.index(next_cate)
                trans_matrix[info[2]][x][y] += 1
                pre_cate = next_cate
                next_cate = ''

    for key, value in trans_matrix.iteritems():
        print key
        print
        pprint.pprint(value)


if __name__ == "__main__":
    trans_matrix()
