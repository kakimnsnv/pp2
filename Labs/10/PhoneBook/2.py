import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='kakimbekn',
    password='Sadasa@2015'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 1
name = 'kakimbek'
number = '87076039179'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()
