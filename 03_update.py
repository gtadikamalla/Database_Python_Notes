# use sqlite3 package
import sqlite3
folder_name = '.'
file_name = 'ecars.db'
connection = sqlite3.connect(folder_name +'/' + file_name)
my_cursor = connection.cursor()
#print(my_cursor.execute('select * from sales where country = 'United States'))
update_sql_statement = """
    update sales 
    set sales = ? 
    where country = ? and 
    year = ?
    """
try:
    values = (200000, 'United States', 2017)
    my_cursor.execute(update_sql_statement, values )
    connection.commit()
except sqlite3.Error as e:
    print(e)
else:
    print('Update completed')
