import sqlite3

from sqlite3 import Error

#from t1 import im,cr
#from keypad import idmsg as i
#from t1 import im
try:
    
    from weight import crw
except:
        crw=0

try:
    from ultra import cru
except:
    cru=0
from kp import a
    
cr=crw+cru

im=a
con=sqlite3.connect('try.db')

cur=con.cursor()

cur.execute("create table if not exists cp(id text primary key, credits integer)")
con.commit()


cur.execute("select * from cp where id=?",(im,))
con.commit()
rows = cur.fetchall()
flag=-1
#for row in rows:
    #if i in (item for sublist in rows for item in sublist):
if len(rows)==0:
        flag=0
       
      
else:
        flag=1

if flag==1:
    
    cur.execute("update cp set credits=credits+? where id=?",(cr,im))
    con.commit()
else:
    cur.execute("insert into cp values(?,?)",(im,cr))
    con.commit()
    
cur.execute("select * from cp")
con.commit()
rows = cur.fetchall()
 
for row in rows:
 
        print(row)
    
    



            