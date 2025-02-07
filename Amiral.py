# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:21:37 2019

@author: HP
"""

# AMIRAL BATTI

#Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer). 
#Bu tabloya 2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin. 
#Yerlestirdiginiz gemileri kullanici gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede 
#bulunmasini isteyin. Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo 
#uzerinde bunu gosterin. Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu gosterin 
#ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin. Kullanici daha once hamle yapmis oldugu bir 
#noktaya tekrar hamlede bulunursa bunu engelleyin. Kullaniciya toplamda 15 yanlis hamle hakki verin. 
#Kullanici tum gemileri vurdugunda oyunu bitirin.
import random
import time
tablo=[]
def oyun():    # Oyun Fonksiyonu 
    hata=0  
    vuruldu=0  
    while hata<15:   # Max bosa 15 atis, veriler girilir satir-sutun olarak
        print("Lutfen vurmak istediginiz noktanin satir ve sutununu yaziniz ;")
        x=int(input("Satir ;"))-1
        y=int(input("Sutun ;"))-1
        if tablogizli[x][y]=='G':  # Geminin basi-govde-kuyruk varsa vurur
            vuruldu +=1
            print("\n")
            print(f'\tHedef vuruldu! Simdilik {vuruldu} isabet / 20')
            tablogor[x][y]='X'
            tablogizli[x][y]='X'
            for i in range(10):   
                print('\t',*[tablogor[i][j] for j in range(10)])
            print('\n'*2)
            if vuruldu==20:
                print("\tTebrikler! Tum gemiler batti...")
                break
        elif tablogizli[x][y]=='X' or tablogizli[x][y]=='K':
            print("\tDaha once vurulmustu ; Tekrar deneyiniz!")
            for i in range(10):
                print('\t',*[tablogor[i][j] for j in range(10)])
            print('\n'*2)
        elif tablogizli[x][y]=='O':
            tablogizli[x][y]='K'
            tablogor[x][y]='K'
            print("\t Karavana!")
            hata+=1
            print('\t',15-hata,"atis hakkiniz kaldi")
            for i in range(10):
                print('\t',*[tablogor[i][j] for j in range(10)])
            print('\n'*2)
            time.sleep(5)
#=======================================================================================================
def gemiler(tablo):   # 8 farkli gemiyi random yerlestiren fonksiyon
    global tablogizli,a
    tablogizli=[['O' for x in range(10)] for y in range(10)]
    a=random.randrange(0,4) 
    tablogizli[a][a]='G' ; tablogizli[a+3][a+5]='G'
    tablogizli[a+4][a+4:a+6]='G','G' ; tablogizli[a+6][a+1:a+3]='G','G'
    tablogizli[a+1][a+1:a+4]='G','G','G' ; tablogizli[a+5][a:a+3]='G','G','G'
    tablogizli[a][a+2:a+6]='G','G','G','G' ; tablogizli[a+2][a:a+4]='G','G','G','G'
    return tablogizli
#=========================================================================================================
while True:   # Oyunu pynatir ya da cikis yapar
    doorgaan=input("Cikmak icin 'q' ya basiniz, Amiral Batti oyunu oynamak icin 'enter' e basiniz ;")
    print("\n"*2)
    if doorgaan=='q':
        print("Cikiliyor...")
        break
    else:
        print("\tAMIRAL BATTI oyunu basliyor...\n")
        print("""2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik (uzunlugunda)
gemilerin batirilmasi icin karavana/bosa hamle sayiniz 15dir,Lutfen dikkatli olun! Buyurun; \n""")
        print("Deniz de yuzen 8 gemi vardir...")
        for x in range(10):
            print('\t',*['O' for y in range(10)]) 
        print('\n'*2) 
        tablogor=[['O' for x in range(10)] for y in range(10)]
        gemiler(tablo)
        for i in range(10):
            print('\t',*[tablogizli[i][j] for j in range(10)])
        oyun()