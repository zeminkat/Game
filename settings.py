import random
import sqlite3 as sql
class Players():
    liste=list()
    def __init__(self,isim,xp=0,altin=0,cannon1=0):
        self.id=random.randint(1000000,10000000)
        self.isim=isim
        self.password=random.randint(10000,999999)
        self.xp=xp
        self.money=altin
        self.cannon1=cannon1
        self.cannon2=1
        self.cannon3=10
        self.cannon4=0
        self.ball1=0;self.ball2=0;self.ball3=0;self.ball4=0;self.sunk=0
        self.addtuple()
    def addtuple(self):
                self.liste.append([self.id,self.isim,self.password,self.xp,self.money,self.cannon1,self.cannon2,self.cannon3,self.cannon4,self.ball1,
                     self.ball2,self.ball3,self.ball4,self.sunk])
class Bots():
    bot_list=list()
    def __init__(self,name,hp,prize,xp):
        self.name=name
        self.hp=hp
        self.prize=prize
        self.xp=xp

        self.addbotlist()
    def addbotlist(self):
        self.bot_list.append([self.name,self.hp,self.prize,self.xp])

def AddPlayersDB():
    with open("C:\\Users\path\PycharmProjects\pythonProject\dosya\kullanici2.txt", "r") as dosya:
        readtxt=dosya.read().split()
    for i in readtxt:
        Players(i)
    for i in range(len(Players.liste)):
        Players.liste[i]=tuple(Players.liste[i])
    data=Players.liste
    connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\\denemetaban.db")
    cursor=connect.cursor()
    for i in data:
        cursor.execute("INSERT INTO players VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,0)", i)
        connect.commit()
def GetPlayers():
    connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\\denemetaban.db")
    cursor=connect.cursor()
    search=input("Search for Usernames")
    cursor.execute("SELECT * FROM players WHERE cannon3>5")
    data=cursor.fetchall()
    print(data)
def CreatePlayer():
    ad=input("Kullanıcı Adı Girin:")
    xp=int(input("Tecrübe puanı gir:"))
    altin=int(input("Altın miktarı gir:"))
    cannon1=int(input("35lik adet gir:"))
    newplayer=Players(ad,xp,altin,cannon1)
    connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\\denemetaban.db")
    cursor=connect.cursor()
    cursor.execute("INSERT INTO players VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,0)",Players.liste[0])
    connect.commit()
def AddAdmins():
    liste1=["TR", "DE", "RU", "NL", "GR", "IT", "UK", "PL", "USA", "RO", "LT", "SW", "CH", "FN"]
    liste2=["SystemAdmin", "AdminTeamLeader"]
    for i in range(len(liste1)):
        admin1="GameLeader" + liste1[i]
        admin="ForumAdmin" + liste1[i]
        forummod="ForumMod" + liste1[i]
        chatmod="ChatMod" + liste1[i]
        gamemod="GameModerator" + liste1[i]
        chatmod2="ChatMod" + liste1[i] + "2"
        liste2.append(admin)
        liste2.append(admin1)
        liste2.append(forummod)
        liste2.append(chatmod)
        liste2.append(chatmod2)
        liste2.append(gamemod)
    for i in liste2:
            Players(i)
    for i in range(len(Players.liste)):
        Players.liste[i]=tuple(Players.liste[i])
    data=Players.liste
    for i in data:
        connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\\denemetaban.db")
        cursor=connect.cursor()
        cursor.execute("INSERT INTO players VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,0)", i)
        connect.commit()
def DeletePlayer():
    username=input("Enter the username you want to remove:")
    connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\\denemetaban.db")
    cursor=connect.cursor()
    cursor.execute("DELETE FROM players WHERE username = ?",(username,))
    connect.commit()
def AddPlayersTeams():
    connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\denemetaban.db")
    cursor=connect.cursor()
    cursor.execute("SELECT id FROM teams")
    data=cursor.fetchall()
    liste=list()
    for i in range(len(data)):
        liste.append(data[i][0])
    cursor.execute("SELECT username FROM players")
    data=cursor.fetchall()
    for i in range(len(data)):
        randomteam=random.choice(liste)
        cursor.execute("UPDATE players SET teamid={} WHERE username='{}'".format(randomteam, data[i][0]))
        connect.commit()
def CreateTeams():
    with open("C:\\Users\path\PycharmProjects\pythonProject\dosya\klan2.txt") as dosya:
        data=dosya.read().split("\n")
        liste=list()
        ak=0
        while ak < 20:
            randomid=random.randint(100000, 1000000)
            if randomid not in liste:
                liste.append(randomid)
                ak+=1
        for i in range(len(data)):
            connect=sql.connect("C:\\Users\path\PycharmProjects\pythonProject\dosya\denemetaban.db")
            cursor=connect.cursor()
            cursor.execute("INSERT INTO teams VALUES({},'{}',{})".format(liste[i], data[i], 0))
            connect.commit()
    
