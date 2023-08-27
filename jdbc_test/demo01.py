import jaydebeapi

url = 'jdbc:postgresql://localhost:5432/postgres'
user = 'postgres'
password = 'zxz'
dirver = 'org.postgresql.Driver'
jarFile = r'C:\Users\xiaox\AppData\Roaming\DBeaverData\drivers\maven\maven-central\org.postgresql\postgresql-42.2.25.jar'
sqlStr = 'select now()'

conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()
