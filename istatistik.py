import sqlite3 as sql
import random
from operator import itemgetter
def stats_xp():
    liste=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT username,xp,id,team FROM players")
    data=cursor.fetchall()
    for i in range(len(data)):
        liste.append(list(data[i]))
    for i in liste:
        i[1]=int(i[1])
    liste.sort(reverse=True,key=itemgetter(1))
    for i in range(20):
        print("{}....[{}]{} Tecrübe Puanı:{}".format(i+1,liste[i][3],liste[i][0],liste[i][1]))
def stats_team():
    liste=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT teamname,id FROM teams")
    data=cursor.fetchall()
    for i in range(len(data)):
        liste.append([data[i][0],data[i][1]])
    for i in range(20):
        xp=0
        cursor.execute("SELECT xp FROM players WHERE teamid={}".format(liste[i][1]))
        data2=cursor.fetchall()
        for j in data2:
            xp+=int(j[0])
        liste[i].append(xp)
    liste.sort(reverse=True,key=itemgetter(2))
    for i in range(20):
        print("{}.{} Filosu Toplam Tecrübe Puanı:{}".format(i+1,liste[i][0],liste[i][2]))
def sunk():
    liste=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT username,sunk,id FROM players")
    data=cursor.fetchall()
    for i in range(len(data)):
        liste.append(list(data[i]))
    for i in liste:
        i[1]=int(i[1])
    liste.sort(reverse=True, key=itemgetter(1))
    for i in range(20):
        print("{}.{} Batırma Sayısı:{}".format(i + 1, liste[i][0], liste[i][1]))
def npcsunk():
    liste=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT username,npcsunk,id,team FROM players")
    data=cursor.fetchall()
    for i in range(len(data)):
        liste.append(list(data[i]))
    for i in liste:
        i[1]=int(i[1])
    liste.sort(reverse=True, key=itemgetter(1))
    for i in range(20):
        print("{}....[{}]{} NPC Batırma Sayısı:{}".format(i + 1, liste[i][3], liste[i][0], liste[i][1]))
def money_stats():
    liste=list()
    connect=sql.connect("db.db")
    cursor=connect.cursor()
    cursor.execute("SELECT username,money,id,team FROM players")
    data=cursor.fetchall()
    for i in range(len(data)):
        liste.append(list(data[i]))
    for i in liste:
        i[1]=int(i[1])
    liste.sort(reverse=True, key=itemgetter(1))
    for i in range(20):
        print("{}....[{}]{} Altın:{}".format(i + 1, liste[i][3], liste[i][0], liste[i][1]))
