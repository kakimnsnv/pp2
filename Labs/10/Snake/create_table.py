import psycopg2
# создаем таблицу телефонной книги
config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='kakimbekn',
    password='Sadasa@2015'
)

current = config.cursor()
sql = '''
        CREATE TABLE users(
            username VARCHAR(100),
            level INT,
            score INT
    );
''' 

current.execute(sql)

current.close()
config.commit()
config.close()