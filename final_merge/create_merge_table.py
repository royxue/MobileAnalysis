"""
Scripts for create a new table to store the merge category information

reference: category_merge_plan.txt
"""

import MySQLdb

def create_merge_table():
    connection = MySQLdb.connect('localhost', 'root', '', 'mobile_analysis')
    t = connection.cursor()

    category_list =  ['Unknown', 'Communication', 'Social', 'Travel', 'Productivity', 'Weather', 'Finance', 'Entertainment', 'Books', 'Personalization', 'Lifestyle', 'Game', 'Health', 'Libraries', 'Education']
    time_of_day = ['morning', 'afternoon', 'evening']

    # Create new table
    for category in category_list:
        for time in time_of_day:
            column_name = category + '_' + time
            sql = "ALTER TABLE final_merge ADD %s float DEFAULT '0'" % (column_name)
            t.execute(sql)

    connection.commit()

if __name__ == '__main__':
    create_merge_table()


    

