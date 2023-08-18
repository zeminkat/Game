import random
import sqlite3 as sql
def Server():
    server_list=list()
    server_list2=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT id FROM players")
    listx=cursor.fetchall()
    for i in listx:
        server_list.append(listx[listx.index(i)][0])
    max=random.randint(1000,2500)
    for i in range(2,max):
        ak=random.choice(server_list)
        if ak not in server_list2:
            server_list2.append(ak)
    return server_list2
def Npc():
    npc_list=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM npc")
    npc_list=cursor.fetchall()
    return npc_list
