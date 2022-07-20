import random,_thread
import sqlite3,istatistik,settings,savas
def fun():
    try:
        while True:
            print("""Savaş için 1
Filo Sıralaması 2
Oyuncu TP Sıralaması 3
Batırma Sıralama 4""")
            secim=input("Seçim:")
            if secim == "1":
                savas.xpfight()
            elif secim == "2":
                istatistik.stats_team()
            elif secim == "3":
                istatistik.stats_xp()
            elif secim == "4":
                istatistik.sunk()
            elif secim=="5":
                savas.GetMoney()
            else:quit()
    except KeyboardInterrupt:
        exit()
fun()