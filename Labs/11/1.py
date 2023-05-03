import psycopg2, re

conn = psycopg2.connect(
    host='localhost',
    database='sampledb',
    user='kakimbekn',
    password='Sadasa@2015'
)
cur = conn.cursor()

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_bk(a VARCHAR, b VARCHAR)
      RETURNS SETOF phonebook 
   AS
   $$
      SELECT * FROM phonebook WHERE name = a AND number = b;
   $$
   language sql;
   '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
   IN users TEXT[][]
 )
 
 LANGUAGE plpgsql
 
 AS $$
 
 DECLARE
   i TEXT[];
 
 BEGIN 
 
    Foreach i slice 1 in array users
    LOOP
       INSERT INTO phonebook (name, number) VALUES (i[1], i[2]);
    END LOOP;
 
 
 END
 $$;
 '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_to_phonebook(nm VARCHAR, phon VARCHAR)
       LANGUAGE plpgsql
       AS $$
       DECLARE 
          cnt INTEGER;
       BEGIN
          SELECT INTO cnt (SELECT count(*) FROM phonebook WHERE name = nm);
          IF cnt > 0 THEN
             UPDATE phonebook
                SET number = phon
                WHERE name = nm;
          ELSE
             INSERT INTO book(name, number) VALUES (nm, phon);
             END IF;
       END;
       $$;''')

cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_phonebook(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM phonebook WHERE name = nm);
	IF cnt IS NOT NULL THEN
        DELETE FROM phonebook
		WHERE name=nm;
    END IF;
END;
$$;""")

cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF phonebook
AS $$
   SELECT * FROM phonebook
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;""")

a = input('search\ninsert\ninsertloop\ndelete\npaginating\n')
if a == 'search':
    cur.execute("SELECT search_from_bk('John Doe', '87076002321')")
    result = cur.fetchall()
    print(result)
if a == 'insert':
    cur.execute("CALL insert_to_phonebook('Nyssanov Kakimbek','87774545505')")
if a == 'insertloop':
    cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['Neymar JR', '87076052769'],
    ARRAY['Vini JR', '87079815569'],
    ARRAY['Raphinha', '87074793780']
]);''')
if a == 'delete':
    cur.execute("CALL delete_from_phonebook('Leo Messi')")
if a == 'paginating':
    cur.execute(
        '''SELECT * FROM paginating(6, 2);'''
    )
    print(cur.fetchall())
conn.commit()
cur.close()
conn.close()