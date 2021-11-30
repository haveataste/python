import sqlite3

db_file = ':memory:'
create_table_sql = '''\
CREATE TABLE test(
name VARCHAR(255) PRIMARY KEY ,
value VARCHAR(255) NOT NULL 
)
'''
insert_table_sql = """\
INSERT INTO test VALUES(?,?)  
"""
query_table_sql = """\
SELECT *
FROM test WHERE name=?
"""
delete_table_sql = """\
DROP TABLE test
"""

# sqlite3 moudle's version and sqlite's version
print('moudle_version:', sqlite3.version, '\n', 'sqlite_version:', sqlite3.sqlite_version)

with sqlite3.connect(db_file) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        cursor.execute(insert_table_sql, ('dog', '100'))
        cursor.execute(insert_table_sql, ('cat', '101'))
        cursor.execute(insert_table_sql, ('pig', '102'))
        connection.commit()

        cursor.execute('select * from test')
        for row in cursor:
            print(row)
        cursor.execute(query_table_sql, ('dog',))
        print(cursor.fetchone())
        cursor.execute(query_table_sql, ('cat',))
        print(cursor.fetchall())
        cursor.execute("select * from test where name='pig'")
        print(cursor.fetchall())

        cursor.execute(delete_table_sql)
        connection.commit()
    finally:
        cursor.close()
