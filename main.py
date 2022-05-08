from mysql_read import DBRead
from csv_xl_to_mysql import CSVXLToMySQL


############################################################
### LOAD CSV OR EXCEL FILE TO MYSQL (csv_xl_to_mysql.py) ###
############################################################

csv_xl_to_sql = CSVXLToMySQL(file="csv or excel file location",
                             table='table name',
                             host='localhost',
                             database='database_name',
                             username='uname',
                             password='pwd')
csv_xl_to_sql.load_to_db()

#########################################################
### QUERY RESULT DISPLAY (mysql_read.py) ###
#########################################################

db = DBRead(host='localhost', username='uname', password='pwd')
print(db.get_query_result('SELECT * FROM db.table;'))
print(db.get_query_result('DESCRIBE db.table;'))
