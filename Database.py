import sqlite3
class db:
   def __init__(self):
      self.conn=sqlite3.connect("firewall.db")
   def close(self):
      self.conn.close()

   def createTable(self):
      self.conn.cursor().execute('''CREATE TABLE if not exists VIOLATOR
               (ID INT PRIMARY KEY      NOT NULL,
                IP              TEXT    NOT NULL,
               COUNT            INT     NOT NULL);
               ''')
   def getRecord(self,id):
      for row in self.conn.cursor().execute("SELECT * FROM VIOLATOR WHERE ID=?;",(id,)):
         return row
   def getIp(self,id):
      for row in self.conn.cursor().execute("SELECT IP FROM VIOLATOR WHERE ID=?;",(id,)):
         return row[0]
   def getCount(self,id):
      for row in self.conn.cursor().execute("SELECT COUNT FROM VIOLATOR WHERE ID=?;", (id,)):
         return row[0]
   def addRecord(self,id,ip,count):
      self.conn.cursor().execute("INSERT INTO VIOLATOR(ID,IP,COUNT) VALUES(?,?,?)",(id,ip,count))
      self.conn.commit()
   def lastID(self):
      for row in self.conn.cursor().execute("select max(id) from VIOLATOR"):
         return row[0]


d=db()
#print(type(type(d.lastID())))
#print(d.lastID())
#print(type(5))
#d.addRecord(d.lastID()+1,"62.212.230.45",3)



