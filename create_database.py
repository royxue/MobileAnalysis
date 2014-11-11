import MySQLdb

connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')

category_list = ['Unknown', 'Communication', 'Social', 'Tools', 'Shopping', 'Travel', 'Productivity', 'Weather', 'News', 'Media', 'Photography', 'Finance', 'Casual', 'Arcade', 'Health', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Music', 'Strategy', 'Business', 'Comics', 'Family', 'Transportation', 'Card', 'Word', 'Libraries', 'Board', 'Sports', 'Racing', 'Action', 'Simulation', 'Puzzle', 'Education', 'Role', 'Trivia', 'Medical', 'Adventure', 'Educational']

time_of_day = ['morning', 'afternoon', 'evening']

t = connection.cursor()

for category in category_list:
    for time in time_of_day:
        column_name = category + '_' + time
        sql = "ALTER TABLE final_result ADD %s float DEFAULT '0'" % (column_name)
        t.execute(sql)

connection.commit()
