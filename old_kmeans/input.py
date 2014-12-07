import MySQLdb

def input():
    file = open('input_data.txt','w+')
    
    conn = MySQLdb.connect('localhost','root','','mobile_analysis')
    t = conn.cursor()
    sql = "SELECT * FROM merge_result"
    t.execute(sql)

    result = t.fetchall()

    for line in result:
        print >> file, line[1:]

    file.close()

if __name__ == "__main__":
    input()
