import random,server,time,istatistik,settings
import sqlite3 as sql
server_list=server.Server()
patlayan_power=6.5;kartopu_power=7;oyuk_power=2
_35power=10;_25power=9;_15power=5
def randomplayer():
    global first,two
    while True:
        first=random.choice(server_list)
        two=random.choice(server_list)
        if first!=two:
            break
    return [first,two]
def fight(a=0,b=0):
    x=a;xx=b
    firstall=list();twoall=list()
    players=randomplayer()
    connect=sql.connect("C:\\Users\Sedat\PycharmProjects\pythonProject\dosya\\denemetaban.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM players WHERE id={}".format(players[0]))
    first=cursor.fetchall()
    for i in range(len(first[0])):
        firstall.append(first[0][i])
    cursor.execute("SELECT * FROM players WHERE id={}".format(players[1]))
    two=cursor.fetchall()
    for i in range(len(two[0])):
        twoall.append(two[0][i])
    first_name=firstall[1];two_name=twoall[1]
    first_35=firstall[5];two_35=twoall[5];first_25=firstall[6];two_25=twoall[6];first_15=firstall[7];two_15=twoall[7];first_kartopu=firstall[9]
    two_kartopu=twoall[9];first_patlayan=firstall[10];two_patlayan=twoall[10];first_oyuk=firstall[11];two_oyuk=twoall[11];first_batirma=firstall[13]
    two_batirma=twoall[13]
    firstpower=((int(first_35)*kartopu_power*_35power+int(first_25)*kartopu_power*_25power+int(first_15)*kartopu_power*_15power))
    twopower=((int(two_35) * kartopu_power * _35power+int(two_25) * kartopu_power * _25power+int(two_15) * kartopu_power * _15power))
    first_hp=10000
    two_hp=10000
    a=6;b=5
    kazanan=""
    while True:
        if first_hp > 0 and two_hp > 0:
            if a % 6 == 0:
                time.sleep(x)
                if two_hp <= firstpower:
                    #print("{} Oyuncusu {} vurdu rakip battı".format(first_name, two_hp))
                    two_hp=0
                    break
                #print("{} Oyuncusu {} vurdu".format(first_name, firstpower))
                two_hp-=int(firstpower)
                #print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(first_name, first_hp, two_name, two_hp))
                time.sleep(x)
            if b % 5 == 0:
                if first_hp <= twopower:
                    #print("{} Oyuncusu {} vurdu rakip battı".format(two_name, first_hp))
                    first_hp=0
                    break
                #print("{} Oyuncusu {} vurdu".format(two_name, twopower))
                first_hp-=int(twopower)
                #print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(first_name, first_hp, two_name, two_hp))
                time.sleep(xx)
                a+=1
                b+=1

            else:
                time.sleep(xx)
                a+=1
                b+=1
        else:
            break
    if first_hp >= two_hp:
        #print("Kazanan {}  {} oyuncusunun gemisi battı".format(first_name, two_name))
        kazanan=first_name
    else:
        #print("Kazanan {}  {} oyuncusunun gemisi battı".format(two_name, first_name))
        kazanan=two_name
    return kazanan
def xpfight():
        try:
            loop=0
            while True:
                print(loop)
                winner=fight()
                connect=sql.connect("C:\\Users\Sedat\PycharmProjects\pythonProject\dosya\\denemetaban.db")
                cursor=connect.cursor()
                cursor.execute("SELECT xp,sunk,money FROM players WHERE username='{}'".format(winner))
                data=cursor.fetchall()
                xp=int(data[0][0]) + random.randint(1000, 1400)
                sunk=int(data[0][1]) + 1
                money=data[0][2] + random.randint(4000, 8000)
                xp=str(xp)
                sunk=str(sunk)
                cursor.execute(
                    "UPDATE players SET xp='{}',sunk='{}',money={} WHERE username='{}'".format(xp, sunk, money, winner))
                connect.commit()
                loop+=1
        except KeyboardInterrupt:
            print("you are not allowed to quit right now")
            exit()
def GetMoney(a=0,b=0):
    x=a;xx=b
    loop=0
    while True:
        for i in range(len(server_list)):
            print(loop)
            connect=sql.connect("C:\\Users\Sedat\PycharmProjects\pythonProject\dosya\\denemetaban.db")
            cursor=connect.cursor()
            cursor.execute("SELECT level,cannon1,cannon2,cannon3,username,xp,money,npcsunk FROM players WHERE id={}".format(server_list[i]))
            data=cursor.fetchall()
            level=(data[0][0])
            cannon1=data[0][1]
            cannon2=data[0][2]
            cannon3=data[0][3]
            playername=data[0][4]
            playerxp=int(data[0][5])
            money=int(data[0][6])
            npcsunk=int(data[0][7])
            playerhp=10000
            power=((int(cannon1)*kartopu_power*_35power+int(cannon2)*kartopu_power*_25power+int(cannon3)*kartopu_power*_15power))
            npc_name=npc_list[0][0]
            npc_hp=int(npc_list[0][1])
            npc_power=140
            npc_prize=int(npc_list[0][2])
            npc_xp=int(npc_list[0][3])
            a=6
            b=5
            while True:
                if playerhp > 0 and npc_hp > 0:
                    if a % 6 == 0:
                        time.sleep(x)
                        if npc_hp <= power:
                            #print("{} Oyuncusu {} vurdu rakip battı".format(playername, npc_hp))
                            npc_hp=0
                            break
                        #print("{} Oyuncusu {} vurdu".format(playername, power))
                        npc_hp-=int(power)
                        #print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(playername, playerhp, npc_name,npc_hp))
                        time.sleep(x)
                    if b % 5 == 0:
                        if playerhp <= npc_power:
                           #print("{} Oyuncusu {} vurdu rakip battı".format(npc_name, playerhp))
                            playerhp=0
                            break
                        #print("{} Oyuncusu {} vurdu".format(npc_name, npc_power))
                        playerhp-=int(npc_power)
                        #print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(playername, playerhp, npc_name,npc_hp))
                        time.sleep(xx)
                        a+=1
                        b+=1

                    else:
                        time.sleep(xx)
                        a+=1
                        b+=1
                else:
                    break
            if playerhp >= npc_hp:
                playerxp+=npc_xp
                money+=npc_prize
                npcsunk+=1
                #print("Kazanan {}  {} oyuncusunun gemisi battı".format(playername, npc_name))
                cursor.execute("UPDATE players SET money={},xp={},npcsunk={} WHERE username='{}'".format(money,playerxp,npcsunk,playername))
                connect.commit()
            else:
                print("Kazanan {}  {} oyuncusunun gemisi battı".format(npc_name, playername))
            loop+=1
        i=0
def Event(a=0,b=0):
    x=a;xx=b
    loop=0
    try:
        while True:
            npc_list=server.Npc()
            print(loop)
            connect=sql.connect("C:\\Users\Sedat\PycharmProjects\pythonProject\dosya\\denemetaban.db")
            cursor=connect.cursor()
            cursor.execute(
                "SELECT level,cannon1,cannon2,cannon3,username,xp,money,npcsunk FROM players WHERE id={}".format(
                    random.choice(server_list)))
            data=cursor.fetchall()
            level=(data[0][0])
            cannon1=data[0][1]
            cannon2=data[0][2]
            cannon3=data[0][3]
            playername=data[0][4]
            playerxp=int(data[0][5])
            money=int(data[0][6])
            npcsunk=int(data[0][7])
            playerhp=10000
            power=((int(cannon1) * kartopu_power * _35power + int(cannon2) * kartopu_power * _25power + int(
                cannon3) * kartopu_power * _15power))

            npc_name=npc_list[9][0]
            npc_hp=int(npc_list[9][1])
            npc_power=4200
            npc_prize=int(npc_list[9][2])
            npc_xp=int(npc_list[9][3])
            a=6
            b=5

            while True:
                if playerhp > 0 and npc_hp > 0:
                    if a % 6 == 0:
                        time.sleep(x)
                        if npc_hp <= power:
                            # print("{} Oyuncusu {} vurdu rakip battı".format(playername, npc_hp))
                            npc_hp=0
                            break
                        # print("{} Oyuncusu {} vurdu".format(playername, power))
                        npc_hp-=int(power)
                        # print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(playername, playerhp, npc_name,npc_hp))
                        time.sleep(x)
                    if b % 5 == 0:
                        if playerhp <= npc_power:
                            # print("{} Oyuncusu {} vurdu rakip battı".format(npc_name, playerhp))
                            playerhp=0
                            break
                        # print("{} Oyuncusu {} vurdu".format(npc_name, npc_power))
                        playerhp-=int(npc_power)
                        # print("{} oyuncusunun canı {}, {} oyuncusunun canı {}".format(playername, playerhp, npc_name,npc_hp))
                        time.sleep(xx)
                        a+=1
                        b+=1

                    else:
                        time.sleep(xx)
                        a+=1
                        b+=1
                else:
                    break
            if playerhp >= npc_hp:
                playerxp+=npc_xp
                money+=npc_prize
                npcsunk+=1
                print("Etkinliği Kazanan {}  {}  gemisi battı.{} {} altın ve {} xp kazandı".format(playername, npc_name,
                                                                                                   playername,
                                                                                                   npc_prize, npc_xp))
                cursor.execute(
                    "UPDATE players SET money={},xp={},npcsunk={} WHERE username='{}'".format(money, playerxp, npcsunk,
                                                                                              playername))
                connect.commit()
                quit()

            else:
                npc_hp=npc_hp
                print("Kazanan {}  {} oyuncusunun gemisi battı".format(npc_name, playername))
                cursor.execute("UPDATE npc SET hp={} WHERE npc='{}'".format(npc_hp, npc_name))
                connect.commit()
                loop+=1
    except KeyboardInterrupt:
        quit()


