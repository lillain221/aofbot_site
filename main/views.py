from django.shortcuts import render

from django.http import HttpResponse
import numpy as np
import random
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def achievement(request):
    return render(request, 'achievement.html')

def career(request):
    return render(request, 'career.html')

def contact(request):
    return render(request, 'contact.html')
    
def google2243e3042b43a5c5(request):
    return render(request, 'google2243e3042b43a5c5.html')


def simulater_page(request):
    return render(request, 'simulater_page.html')


def result(request):
    val1=int(request.POST["rake_back"])
    val2=int(request.POST["loop_num"])
    val3=int(request.POST["player1_money"])
    val4=int(request.POST["player1_money"])
    label1=str(request.POST["label1"])
    label2=str(request.POST["label2"])
    handrange_1=request.POST.getlist("animal")
    handrange_2=request.POST.getlist("handrange_2")
    handrange_3=request.POST.getlist("handrange_3")


    money=simulater(val1,val2,val3,val4,handrange_1,handrange_2,handrange_3)
    print(handrange_1)
    return render(request,"result.html",
    {"result1":money[0],"result2":money[1],"result3":list(money[2]),"result4":list(money[3]),"result5":list(money[4]),"label1":label1,"label2":label2,"val3":val3,"val1":val1,"val2":val2})



def simulater(rake_back,loop_num,player1_money,player2_money,handrange_1,handrange_2,handrange_3):
    def heads_sbpush(hand):
        if hand in handrange_1:
            return True
        else:
            return False

    def heads_sbpush2(hand):
        if hand in handrange_2:
            return True
        else:
            return False

    def heads_bbcall(hand):
        #bbcallハンド
        if hand in handrange_3:
            return True
        else:
            return False



    kikker=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    kaisuu=np.array([])
    player1_money_np=np.array([])
    player2_money_np=np.array([])
    def players_hand():
        card_list=['dA','d2','d3','d4','d5','d6','d7','d8','d9','dT','dJ','dQ','dK',
        'cA','c2','c3','c4','c5','c6','c7','c8','c9','cT','cJ','cQ','cK',
        'sA','s2','s3','s4','s5','s6','s7','s8','s9','sT','sJ','sQ','sK',
        'hA','h2','h3','h4','h5','h6','h7','h8','h9','hT','hJ','hQ','hK']
        ns = []
        player1_card=[]
        player2_card=[]
        player3_card=[]
        player4_card=[]
        board_card=[]

        while len(ns) < 13:
            n = random.randint(0, 51)  
            if not n in ns:
                ns.append(n)
        for i in range(5):
            board_card.append(card_list[ns[i]])

        player1_card.append(card_list[ns[5]])
        player1_card.append(card_list[ns[6]])
        player2_card.append(card_list[ns[7]])
        player2_card.append(card_list[ns[8]])
        player3_card.append(card_list[ns[9]])
        player3_card.append(card_list[ns[10]])
        player4_card.append(card_list[ns[11]])
        player4_card.append(card_list[ns[12]])

        player1_hand=player1_card+board_card
        player2_hand=player2_card+board_card
        player3_hand=player3_card+board_card
        player4_hand=player4_card+board_card
        player1_hand = sorted(player1_hand)
        player2_hand = sorted(player2_hand)
        player3_hand = sorted(player3_hand)
        player4_hand = sorted(player4_hand)

        print(player1_card)
        print(player2_card)

        return player1_hand,player2_hand,player3_hand,player4_hand,board_card,player1_card,player2_card,player3_card,player4_card

    def fullhouse_quads_trips(hand):
        point=0
        count=[]
        player_number=[]
        for i in hand:
            player_number.append(i[1])

        if "cA" in hand and "cK" in hand and "cQ" in hand and "cJ" in hand and "cT" in hand:
            count.append(25000)
        if "sA" in hand and "sK" in hand and "sQ" in hand and "sJ" in hand and "sT" in hand:
            count.append(25000)
        if "hA" in hand and "hK" in hand and "hQ" in hand and "hJ" in hand and "hT" in hand:
            count.append(25000)
        if "dA" in hand and "dK" in hand and "dQ" in hand and "dJ" in hand and "dT" in hand:
            count.append(25000)

        if "c9" in hand and "cK" in hand and "cQ" in hand and "cJ" in hand and "cT" in hand:
            count.append(24000)
        if "s9" in hand and "sK" in hand and "sQ" in hand and "sJ" in hand and "sT" in hand:
            count.append(24000)
        if "h9" in hand and "hK" in hand and "hQ" in hand and "hJ" in hand and "hT" in hand:
            count.append(24000)
        if "d9" in hand and "dK" in hand and "dQ" in hand and "dJ" in hand and "dT" in hand:
            count.append(24000)

        if "c9" in hand and "c8" in hand and "cQ" in hand and "cJ" in hand and "cT" in hand:
            count.append(23000)
        if "s9" in hand and "s8" in hand and "sQ" in hand and "sJ" in hand and "sT" in hand:
            count.append(23000)
        if "h9" in hand and "h8" in hand and "hQ" in hand and "hJ" in hand and "hT" in hand:
            count.append(23000)
        if "d9" in hand and "d8" in hand and "dQ" in hand and "dJ" in hand and "dT" in hand:
            count.append(23000)

        if "c9" in hand and "c8" in hand and "c7" in hand and "cJ" in hand and "cT" in hand:
            count.append(22000)
        if "s9" in hand and "s8" in hand and "s7" in hand and "sJ" in hand and "sT" in hand:
            count.append(22000)
        if "h9" in hand and "h8" in hand and "h7" in hand and "hJ" in hand and "hT" in hand:
            count.append(22000)
        if "d9" in hand and "d8" in hand and "d7" in hand and "dJ" in hand and "dT" in hand:
            count.append(22000)

        if "c9" in hand and "c8" in hand and "c7" in hand and "c6" in hand and "cT" in hand:
            count.append(21000)
        if "s9" in hand and "s8" in hand and "s7" in hand and "s6" in hand and "sT" in hand:
            count.append(21000)
        if "h9" in hand and "h8" in hand and "h7" in hand and "h6" in hand and "hT" in hand:
            count.append(21000)
        if "d9" in hand and "d8" in hand and "d7" in hand and "d6" in hand and "dT" in hand:
            count.append(21000)

        if "c9" in hand and "c8" in hand and "c7" in hand and "c6" in hand and "c5" in hand:
            count.append(20000)
        if "s9" in hand and "s8" in hand and "s7" in hand and "s6" in hand and "s5" in hand:
            count.append(20000)
        if "h9" in hand and "h8" in hand and "h7" in hand and "h6" in hand and "h5" in hand:
            count.append(20000)
        if "d9" in hand and "d8" in hand and "d7" in hand and "d6" in hand and "d5" in hand:
            count.append(20000)

        if "c4" in hand and "c8" in hand and "c7" in hand and "c6" in hand and "c5" in hand:
            count.append(19000)
        if "s4" in hand and "s8" in hand and "s7" in hand and "s6" in hand and "s5" in hand:
            count.append(19000)
        if "h4" in hand and "h8" in hand and "h7" in hand and "h6" in hand and "h5" in hand:
            count.append(19000)
        if "d4" in hand and "d8" in hand and "d7" in hand and "d6" in hand and "d5" in hand:
            count.append(19000)

        if "c4" in hand and "c3" in hand and "c7" in hand and "c6" in hand and "c5" in hand:
            count.append(18000)
        if "s4" in hand and "s3" in hand and "s7" in hand and "s6" in hand and "s5" in hand:
            count.append(18000)
        if "h4" in hand and "h3" in hand and "h7" in hand and "h6" in hand and "h5" in hand:
            count.append(18000)
        if "d4" in hand and "d3" in hand and "d7" in hand and "d6" in hand and "d5" in hand:
            count.append(18000)

        if "c4" in hand and "c3" in hand and "c2" in hand and "c6" in hand and "c5" in hand:
            count.append(17000)
        if "s4" in hand and "s3" in hand and "s2" in hand and "s6" in hand and "s5" in hand:
            count.append(17000)
        if "h4" in hand and "h3" in hand and "h2" in hand and "h6" in hand and "h5" in hand:
            count.append(17000)
        if "d4" in hand and "d3" in hand and "d2" in hand and "d6" in hand and "d5" in hand:
            count.append(17000)

        if "c4" in hand and "c3" in hand and "c2" in hand and "cA" in hand and "c5" in hand:
            count.append(16000)
        if "s4" in hand and "s3" in hand and "s2" in hand and "sA" in hand and "s5" in hand:
            count.append(16000)
        if "h4" in hand and "h3" in hand and "h2" in hand and "hA" in hand and "h5" in hand:
            count.append(16000)
        if "d4" in hand and "d3" in hand and "d2" in hand and "dA" in hand and "d5" in hand:
            count.append(16000)

        #Aクアッズ
        if player_number.count('A')==4:
            player_number.remove('A')
            player_number.remove('A')
            player_number.remove('A')
            player_number.remove('A')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("A-quads "+i+" kikker")
                    if i == "K":
                        count.append(10599)
                    if i == "Q":
                        count.append(10598)
                    if i == "J":
                        count.append(10597)
                    if i == "T":
                        count.append(10596)
                    if i == "9":
                        count.append(10595)
                    if i == "8":
                        count.append(10594)
                    if i == "7":
                        count.append(10593)
                    if i == "6":
                        count.append(10592)
                    if i == "5":
                        count.append(10591)
                    if i == "4":
                        count.append(10590)
                    if i == "3":
                        count.append(10589)
                    if i == "2":
                        count.append(10588)
                    break
                
        #Kクアッズ
        if player_number.count('K')==4:
            player_number.remove('K')
            player_number.remove('K')
            player_number.remove('K')
            player_number.remove('K')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("K-quads "+i+" kikker")
                    if i == "A":
                        count.append(10579)
                    if i == "Q":
                        count.append(10578)
                    if i == "J":
                        count.append(10577)
                    if i == "T":
                        count.append(10576)
                    if i == "9":
                        count.append(10575)
                    if i == "8":
                        count.append(10574)
                    if i == "7":
                        count.append(10573)
                    if i == "6":
                        count.append(10572)
                    if i == "5":
                        count.append(10571)
                    if i == "4":
                        count.append(10570)
                    if i == "3":
                        count.append(10569)
                    if i == "2":
                        count.append(10568)
                    break

        #Qクアッズ
        if player_number.count('Q')==4:
            player_number.remove('Q')
            player_number.remove('Q')
            player_number.remove('Q')
            player_number.remove('Q')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("Q-quads "+i+" kikker")
                    if i == "A":
                        count.append(10559)
                    if i == "K":
                        count.append(10558)
                    if i == "J":
                        count.append(10557)
                    if i == "T":
                        count.append(10556)
                    if i == "9":
                        count.append(10555)
                    if i == "8":
                        count.append(10554)
                    if i == "7":
                        count.append(10553)
                    if i == "6":
                        count.append(10552)
                    if i == "5":
                        count.append(10551)
                    if i == "4":
                        count.append(10550)
                    if i == "3":
                        count.append(10549)
                    if i == "2":
                        count.append(10548)
                    break

        #Jクアッズ
        if player_number.count('J')==4:
            player_number.remove('J')
            player_number.remove('J')
            player_number.remove('J')
            player_number.remove('J')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("J-quads "+i+" kikker")
                    if i == "A":
                        count.append(10539)
                    if i == "K":
                        count.append(10538)
                    if i == "Q":
                        count.append(10537)
                    if i == "T":
                        count.append(10536)
                    if i == "9":
                        count.append(10535)
                    if i == "8":
                        count.append(10534)
                    if i == "7":
                        count.append(10533)
                    if i == "6":
                        count.append(10532)
                    if i == "5":
                        count.append(10531)
                    if i == "4":
                        count.append(10530)
                    if i == "3":
                        count.append(10529)
                    if i == "2":
                        count.append(10528)
                    break

        #Tクアッズ
        if player_number.count('T')==4:
            player_number.remove('T')
            player_number.remove('T')
            player_number.remove('T')
            player_number.remove('T')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("T-quads "+i+" kikker")
                    if i == "A":
                        count.append(10519)
                    if i == "K":
                        count.append(10518)
                    if i == "Q":
                        count.append(10517)
                    if i == "J":
                        count.append(10516)
                    if i == "9":
                        count.append(10515)
                    if i == "8":
                        count.append(10514)
                    if i == "7":
                        count.append(10513)
                    if i == "6":
                        count.append(10512)
                    if i == "5":
                        count.append(10511)
                    if i == "4":
                        count.append(10510)
                    if i == "3":
                        count.append(10509)
                    if i == "2":
                        count.append(10508)
                    break

        #9クアッズ
        if player_number.count('9')==4:
            player_number.remove('9')
            player_number.remove('9')
            player_number.remove('9')
            player_number.remove('9')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("9-quads "+i+" kikker")
                    if i == "A":
                        count.append(10499)
                    if i == "K":
                        count.append(10498)
                    if i == "Q":
                        count.append(10497)
                    if i == "J":
                        count.append(10496)
                    if i == "T":
                        count.append(10495)
                    if i == "8":
                        count.append(10494)
                    if i == "7":
                        count.append(10493)
                    if i == "6":
                        count.append(10492)
                    if i == "5":
                        count.append(10491)
                    if i == "4":
                        count.append(10490)
                    if i == "3":
                        count.append(10489)
                    if i == "2":
                        count.append(10488)
                    break

        #8クアッズ
        if player_number.count('8')==4:
            player_number.remove('8')
            player_number.remove('8')
            player_number.remove('8')
            player_number.remove('8')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("8-quads "+i+" kikker")
                    if i == "A":
                        count.append(10479)
                    if i == "K":
                        count.append(10478)
                    if i == "Q":
                        count.append(10477)
                    if i == "J":
                        count.append(10476)
                    if i == "T":
                        count.append(10475)
                    if i == "9":
                        count.append(10474)
                    if i == "7":
                        count.append(10473)
                    if i == "6":
                        count.append(10472)
                    if i == "5":
                        count.append(10471)
                    if i == "4":
                        count.append(10470)
                    if i == "3":
                        count.append(10469)
                    if i == "2":
                        count.append(10468)
                    break

        #7クアッズ
        if player_number.count('7')==4:
            player_number.remove('7')
            player_number.remove('7')
            player_number.remove('7')
            player_number.remove('7')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("7-quads "+i+" kikker")
                    if i == "A":
                        count.append(10459)
                    if i == "K":
                        count.append(10458)
                    if i == "Q":
                        count.append(10457)
                    if i == "J":
                        count.append(10456)
                    if i == "T":
                        count.append(10455)
                    if i == "9":
                        count.append(10454)
                    if i == "8":
                        count.append(10453)
                    if i == "6":
                        count.append(10452)
                    if i == "5":
                        count.append(10451)
                    if i == "4":
                        count.append(10450)
                    if i == "3":
                        count.append(10449)
                    if i == "2":
                        count.append(10448)
                    break

        #6クアッズ
        if player_number.count('6')==4:
            player_number.remove('6')
            player_number.remove('6')
            player_number.remove('6')
            player_number.remove('6')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("6-quads "+i+" kikker")
                    if i == "A":
                        count.append(10439)
                    if i == "K":
                        count.append(10438)
                    if i == "Q":
                        count.append(10437)
                    if i == "J":
                        count.append(10436)
                    if i == "T":
                        count.append(10435)
                    if i == "9":
                        count.append(10434)
                    if i == "8":
                        count.append(10433)
                    if i == "7":
                        count.append(10432)
                    if i == "5":
                        count.append(10431)
                    if i == "4":
                        count.append(10430)
                    if i == "3":
                        count.append(10429)
                    if i == "2":
                        count.append(10428)
                    break

        #5クアッズ
        if player_number.count('5')==4:
            player_number.remove('5')
            player_number.remove('5')
            player_number.remove('5')
            player_number.remove('5')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("5-quads "+i+" kikker")
                    if i == "A":
                        count.append(10419)
                    if i == "K":
                        count.append(10418)
                    if i == "Q":
                        count.append(10417)
                    if i == "J":
                        count.append(10416)
                    if i == "T":
                        count.append(10415)
                    if i == "9":
                        count.append(10414)
                    if i == "8":
                        count.append(10413)
                    if i == "7":
                        count.append(10412)
                    if i == "6":
                        count.append(10411)
                    if i == "4":
                        count.append(10410)
                    if i == "3":
                        count.append(10409)
                    if i == "2":
                        count.append(10408)
                    break

        #4クアッズ
        if player_number.count('4')==4:
            player_number.remove('4')
            player_number.remove('4')
            player_number.remove('4')
            player_number.remove('4')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("4-quads "+i+" kikker")
                    if i == "A":
                        count.append(10399)
                    if i == "K":
                        count.append(10398)
                    if i == "Q":
                        count.append(10397)
                    if i == "J":
                        count.append(10396)
                    if i == "T":
                        count.append(10395)
                    if i == "9":
                        count.append(10394)
                    if i == "8":
                        count.append(10393)
                    if i == "7":
                        count.append(10392)
                    if i == "6":
                        count.append(10391)
                    if i == "5":
                        count.append(10390)
                    if i == "3":
                        count.append(10389)
                    if i == "2":
                        count.append(10388)
                    break

        #3クアッズ
        if player_number.count('3')==4:
            player_number.remove('3')
            player_number.remove('3')
            player_number.remove('3')
            player_number.remove('3')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("3-quads "+i+" kikker")
                    if i == "A":
                        count.append(10379)
                    if i == "K":
                        count.append(10378)
                    if i == "Q":
                        count.append(10377)
                    if i == "J":
                        count.append(10376)
                    if i == "T":
                        count.append(10375)
                    if i == "9":
                        count.append(10374)
                    if i == "8":
                        count.append(10373)
                    if i == "7":
                        count.append(10372)
                    if i == "6":
                        count.append(10371)
                    if i == "5":
                        count.append(10370)
                    if i == "4":
                        count.append(10369)
                    if i == "2":
                        count.append(10368)
                    break

        #2クアッズ
        if player_number.count('2')==4:
            player_number.remove('2')
            player_number.remove('2')
            player_number.remove('2')
            player_number.remove('2')
            for i in kikker:
                if player_number.count(i)!=0:
                    print("2-quads "+i+" kikker")
                    if i == "A":
                        count.append(10359)
                    if i == "K":
                        count.append(10358)
                    if i == "Q":
                        count.append(10357)
                    if i == "J":
                        count.append(10356)
                    if i == "T":
                        count.append(10355)
                    if i == "9":
                        count.append(10354)
                    if i == "8":
                        count.append(10353)
                    if i == "7":
                        count.append(10352)
                    if i == "6":
                        count.append(10351)
                    if i == "5":
                        count.append(10350)
                    if i == "4":
                        count.append(10349)
                    if i == "3":
                        count.append(10348)
                    break



        #Aフルハウス
        if player_number.count('A')==3:
            if player_number.count('K')==2 or player_number.count('K')==3:
                count.append(10330)

            elif player_number.count('Q')==2 or player_number.count('Q')==3:
                count.append(10329)

            elif player_number.count('J')==2 or player_number.count('J')==3:
                count.append(10328)

            elif player_number.count('T')==2 or player_number.count('T')==3:
                count.append(10327)

            elif player_number.count('9')==2 or player_number.count('9')==3:
                count.append(10326)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10325)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10324)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10323)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10322)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10321)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10320)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10319)
            else:
                #トリップス
                count.append(8500)

        #Kフルハウス
        if player_number.count('K')==3:
            if player_number.count('A')==2:
                count.append(10310)

            elif player_number.count('Q')==2 or player_number.count('Q')==3:
                count.append(10319)

            elif player_number.count('J')==2 or player_number.count('J')==3:
                count.append(10318)

            elif player_number.count('T')==2 or player_number.count('T')==3:
                count.append(10317)

            elif player_number.count('9')==2 or player_number.count('9')==3:
                count.append(10316)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10315)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10314)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10313)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10312)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10311)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10310)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10309)
            
            else:
                #トリップス
                count.append(8499)

        #Qフルハウス
        if player_number.count('Q')==3:
            if player_number.count('A')==2:
                count.append(10300)

            elif player_number.count('K')==2:
                count.append(10299)

            elif player_number.count('J')==2 or player_number.count('J')==3:
                count.append(10298)

            elif player_number.count('T')==2 or player_number.count('T')==3:
                count.append(10297)

            elif player_number.count('9')==2 or player_number.count('9')==3:
                count.append(10296)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10295)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10294)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10293)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10292)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10291)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10290)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10289)

            else:
                #トリップス
                count.append(8498)
        #Jフルハウス
        if player_number.count('J')==3:
            if player_number.count('A')==2:
                count.append(10280)

            elif player_number.count('K')==2:
                count.append(10279)

            elif player_number.count('Q')==2:
                count.append(10278)

            elif player_number.count('T')==2 or player_number.count('T')==3:
                count.append(10277)

            elif player_number.count('9')==2 or player_number.count('9')==3:
                count.append(10276)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10275)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10274)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10273)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10272)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10271)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10270)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10269)

            else:
                #トリップス
                count.append(8497)

        #Tフルハウス
        if player_number.count('T')==3:
            if player_number.count('A')==2:
                count.append(10260)

            elif player_number.count('K')==2:
                count.append(10259)

            elif player_number.count('Q')==2:
                count.append(10258)

            elif player_number.count('J')==2:
                count.append(10257)

            elif player_number.count('9')==2 or player_number.count('9')==3:
                count.append(10256)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10255)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10254)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10253)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10252)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10251)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10250)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10249)

            else:
                #トリップス
                count.append(8496)

        #9フルハウス
        if player_number.count('9')==3:
            if player_number.count('A')==2:
                count.append(10240)

            elif player_number.count('K')==2:
                count.append(10239)

            elif player_number.count('Q')==2:
                count.append(10238)

            elif player_number.count('J')==2:
                count.append(10237)

            elif player_number.count('T')==2:
                count.append(10236)

            elif player_number.count('8')==2 or player_number.count('8')==3:
                count.append(10235)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10234)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10233)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10232)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10231)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10230)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10229)

            else:
                #トリップス
                count.append(8495)

        #8フルハウス
        if player_number.count('8')==3:
            if player_number.count('A')==2:
                count.append(10220)

            elif player_number.count('K')==2:
                count.append(10219)

            elif player_number.count('Q')==2:
                count.append(10218)

            elif player_number.count('J')==2:
                count.append(10217)

            elif player_number.count('T')==2:
                count.append(10216)

            elif player_number.count('9')==2:
                count.append(10215)

            elif player_number.count('7')==2 or player_number.count('7')==3:
                count.append(10214)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10213)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10212)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10211)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10210)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10209)

            else:
                #トリップス
                count.append(8494)

        #7フルハウス
        if player_number.count('7')==3:
            if player_number.count('A')==2:
                count.append(10200)

            elif player_number.count('K')==2:
                count.append(10199)

            elif player_number.count('Q')==2:
                count.append(10198)

            elif player_number.count('J')==2:
                count.append(10197)

            elif player_number.count('T')==2:
                count.append(10196)

            elif player_number.count('9')==2:
                count.append(10195)

            elif player_number.count('8')==2:
                count.append(10194)

            elif player_number.count('6')==2 or player_number.count('6')==3:
                count.append(10193)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10192)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10191)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10190)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10189)

            else:
                #トリップス
                count.append(8493)

        #6フルハウス
        if player_number.count('6')==3:
            if player_number.count('A')==2:
                count.append(10180)

            elif player_number.count('K')==2:
                count.append(10179)

            elif player_number.count('Q')==2:
                count.append(10178)

            elif player_number.count('J')==2:
                count.append(10177)

            elif player_number.count('T')==2:
                count.append(10176)

            elif player_number.count('9')==2:
                count.append(10175)

            elif player_number.count('8')==2:
                count.append(10174)

            elif player_number.count('7')==2:
                count.append(10173)

            elif player_number.count('5')==2 or player_number.count('5')==3:
                count.append(10172)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10171)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10170)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10169)

            else:
                #トリップス
                count.append(8492)

        #5フルハウス
        if player_number.count('5')==3:
            if player_number.count('A')==2:
                count.append(10160)

            elif player_number.count('K')==2:
                count.append(10159)

            elif player_number.count('Q')==2:
                count.append(10158)

            elif player_number.count('J')==2:
                count.append(10157)

            elif player_number.count('T')==2:
                count.append(10156)

            elif player_number.count('9')==2:
                count.append(10155)

            elif player_number.count('8')==2:
                count.append(10154)

            elif player_number.count('7')==2:
                count.append(10153)

            elif player_number.count('6')==2:
                count.append(10152)

            elif player_number.count('4')==2 or player_number.count('4')==3:
                count.append(10151)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10150)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10149)

            else:
                #トリップス
                count.append(8491)

        #4フルハウス
        if player_number.count('4')==3:
            if player_number.count('A')==2:
                count.append(10140)

            elif player_number.count('K')==2:
                count.append(10139)

            elif player_number.count('Q')==2:
                count.append(10138)

            elif player_number.count('J')==2:
                count.append(10137)

            elif player_number.count('T')==2:
                count.append(10136)

            elif player_number.count('9')==2:
                count.append(10135)

            elif player_number.count('8')==2:
                count.append(10134)

            elif player_number.count('7')==2:
                count.append(10133)

            elif player_number.count('6')==2:
                count.append(10132)

            elif player_number.count('5')==2:
                count.append(10131)

            elif player_number.count('3')==2 or player_number.count('3')==3:
                count.append(10130)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10129)

            else:
                #トリップス
                count.append(8490)

        #3フルハウス
        if player_number.count('3')==3:
            if player_number.count('A')==2:
                count.append(10120)

            elif player_number.count('K')==2:
                count.append(10119)

            elif player_number.count('Q')==2:
                count.append(10118)

            elif player_number.count('J')==2:
                count.append(10117)

            elif player_number.count('T')==2:
                count.append(10116)

            elif player_number.count('9')==2:
                count.append(10115)

            elif player_number.count('8')==2:
                count.append(10114)

            elif player_number.count('7')==2:
                count.append(10113)

            elif player_number.count('6')==2:
                count.append(10112)

            elif player_number.count('5')==2:
                count.append(10111)

            elif player_number.count('4')==2:
                count.append(10110)

            elif player_number.count('2')==2 or player_number.count('2')==3:
                count.append(10109)

            else:
                #トリップス
                count.append(8489)
        #2フルハウス
        if player_number.count('2')==3:
            if player_number.count('A')==2:
                count.append(10100)

            elif player_number.count('K')==2:
                count.append(10099)

            elif player_number.count('Q')==2:
                count.append(10098)

            elif player_number.count('J')==2:
                count.append(10097)

            elif player_number.count('T')==2:
                count.append(10096)

            elif player_number.count('9')==2:
                count.append(10095)

            elif player_number.count('8')==2:
                count.append(10094)

            elif player_number.count('7')==2:
                count.append(10093)

            elif player_number.count('6')==2:
                count.append(10092)

            elif player_number.count('5')==2:
                count.append(10091)

            elif player_number.count('4')==2:
                count.append(10090)

            elif player_number.count('3')==2:
                count.append(10089)

            else:
                #トリップス
                count.append(8488)

        #フラッシュ
        player_color=[]
        for i in hand:
            player_color.append(i[0])

        c=player_color.count('c')
        d=player_color.count('d')
        s=player_color.count('s')
        h=player_color.count('h')

        if s>4:
            count.append(9500)
        if d>4:
            count.append(9499)
        if h>4:
            count.append(9498)
        if c>4:
            count.append(9497)    


        #ストレート
        if "A" in player_number:
            straight_list=player_number+["1"]
        else:
            straight_list=player_number

        straight_list = ["a" if i=="T" else i for i in straight_list]
        straight_list = ["b" if i=="J" else i for i in straight_list]
        straight_list = ["c" if i=="Q" else i for i in straight_list]
        straight_list = ["d" if i=="K" else i for i in straight_list]
        straight_list = ["e" if i=="A" else i for i in straight_list]
        straight_list = list(set(straight_list))
        straight_list = sorted(straight_list)

        straight_list = ["T" if i=="a" else i for i in straight_list]
        straight_list = ["J" if i=="b" else i for i in straight_list]
        straight_list = ["Q" if i=="c" else i for i in straight_list]
        straight_list = ["K" if i=="d" else i for i in straight_list]
        straight_list = ["A" if i=="e" else i for i in straight_list]

        straight_list = "".join(straight_list)

        if 'TJQKA' in straight_list:
            count.append(8999)
        if '9TJQK' in straight_list:
            count.append(8998)
        if '89TJQ' in straight_list:
            count.append(8997)
        if '789TJ' in straight_list:
            count.append(8996)
        if '6789T' in straight_list:
            count.append(8995)
        if '56789' in straight_list:
            count.append(8994)
        if '45678' in straight_list:
            count.append(8993)
        if '34567' in straight_list:
            count.append(8992)
        if '23456' in straight_list:
            count.append(8991)
        if '12345' in straight_list:
            count.append(8990)


        #high card 1pair 2pair 
        hicard_number = len(list(set(player_number)))
        if hicard_number==7:
            count.append(1000)
        if hicard_number==6:
            if player_number.count('A')==2:
                count.append(1100)

            elif player_number.count('K')==2:
                count.append(1099)

            elif player_number.count('Q')==2:
                count.append(1098)

            elif player_number.count('J')==2:
                count.append(1097)

            elif player_number.count('T')==2:
                count.append(1096)

            elif player_number.count('9')==2:
                count.append(1095)

            elif player_number.count('8')==2:
                count.append(1094)

            elif player_number.count('7')==2:
                count.append(1093)

            elif player_number.count('6')==2:
                count.append(1092)

            elif player_number.count('5')==2:
                count.append(1091)

            elif player_number.count('4')==2:
                count.append(1090)

            elif player_number.count('3')==2:
                count.append(1089)

            elif player_number.count('2')==2:
                count.append(1088)

        if hicard_number==5 or hicard_number==4:
            count.append(3000)


        if max(count)==1000:
            print("high card")

        if max(count)==1100:
            print("A pair")
        if max(count)==1099:
            print("K pair")
        if max(count)==1098:
            print("Q pair")
        if max(count)==1097:
            print("J pair")
        if max(count)==1096:
            print("T pair")
        if max(count)==1095:
            print("9 pair")
        if max(count)==1094:
            print("8 pair")
        if max(count)==1093:
            print("7 pair")
        if max(count)==1092:
            print("6 pair")
        if max(count)==1091:
            print("5 pair")
        if max(count)==1090:
            print("4 pair")
        if max(count)==1089:
            print("3 pair")
        if max(count)==1088:
            print("2 pair")
        
        if max(count)==3000:
            print("2pairs")

        #表示
        if max(count)==25000:
            print("A-hi royal")
        if max(count)==24000:
            print("K-hi royal")
        if max(count)==23000:
            print("Q-hi royal")
        if max(count)==22000:
            print("J-hi royal")
        if max(count)==21000:
            print("T-hi royal")
        if max(count)==20000:
            print("9-hi royal")
        if max(count)==19000:
            print("8-hi royal")
        if max(count)==18000:
            print("7-hi royal")
        if max(count)==17000:
            print("6-hi royal")
        if max(count)==16000:
            print("5-hi royal")


        if max(count)==10330:
            print("A-K fullhouse")
        if max(count)==10329:
            print("A-Q fullhouse")
        if max(count)==10328:
            print("A-J fullhouse")
        if max(count)==10327:
            print("A-T fullhouse")
        if max(count)==10326:
            print("A-9 fullhouse")
        if max(count)==10325:
            print("A-8 fullhouse")
        if max(count)==10324:
            print("A-7 fullhouse")
        if max(count)==10323:
            print("A-6 fullhouse")
        if max(count)==10322:
            print("A-5 fullhouse")
        if max(count)==10321:
            print("A-4 fullhouse")
        if max(count)==10320:
            print("A-3 fullhouse")
        if max(count)==10319:
            print("A-2 fullhouse")

        if max(count)==10310:
            print("K-A fullhouse")
        if max(count)==10319:
            print("K-Q fullhouse")
        if max(count)==10318:
            print("K-J fullhouse")
        if max(count)==10317:
            print("K-T fullhouse")
        if max(count)==10316:
            print("K-9 fullhouse")
        if max(count)==10315:
            print("K-8 fullhouse")
        if max(count)==10314:
            print("K-7 fullhouse")
        if max(count)==10313:
            print("K-6 fullhouse")
        if max(count)==10312:
            print("K-5 fullhouse")
        if max(count)==10311:
            print("K-4 fullhouse")
        if max(count)==10310:
            print("K-3 fullhouse")
        if max(count)==10309:
            print("K-2 fullhouse")

        if max(count)==10300:
            print("Q-A fullhouse")
        if max(count)==10299:
            print("Q-K fullhouse")
        if max(count)==10298:
            print("Q-J fullhouse")
        if max(count)==10297:
            print("Q-T fullhouse")
        if max(count)==10296:
            print("Q-9 fullhouse")
        if max(count)==10295:
            print("Q-8 fullhouse")
        if max(count)==10294:
            print("Q-7 fullhouse")
        if max(count)==10293:
            print("Q-6 fullhouse")
        if max(count)==10292:
            print("Q-5 fullhouse")
        if max(count)==10291:
            print("Q-4 fullhouse")
        if max(count)==10290:
            print("Q-3 fullhouse")
        if max(count)==10289:
            print("Q-2 fullhouse")

        if max(count)==10280:
            print("J-A fullhouse")
        if max(count)==10279:
            print("J-K fullhouse")
        if max(count)==10278:
            print("J-Q fullhouse")
        if max(count)==10277:
            print("J-T fullhouse")
        if max(count)==10276:
            print("J-9 fullhouse")
        if max(count)==10275:
            print("J-8 fullhouse")
        if max(count)==10274:
            print("J-7 fullhouse")
        if max(count)==10273:
            print("J-6 fullhouse")
        if max(count)==10272:
            print("J-5 fullhouse")
        if max(count)==10271:
            print("J-4 fullhouse")
        if max(count)==10270:
            print("J-3 fullhouse")
        if max(count)==10269:
            print("J-2 fullhouse")


        if max(count)==10260:
            print("T-A fullhouse")
        if max(count)==10259:
            print("T-K fullhouse")
        if max(count)==10258:
            print("T-Q fullhouse")
        if max(count)==10257:
            print("T-J fullhouse")
        if max(count)==10256:
            print("T-9 fullhouse")
        if max(count)==10255:
            print("T-8 fullhouse")
        if max(count)==10254:
            print("T-7 fullhouse")
        if max(count)==10253:
            print("T-6 fullhouse")
        if max(count)==10252:
            print("T-5 fullhouse")
        if max(count)==10251:
            print("T-4 fullhouse")
        if max(count)==10250:
            print("T-3 fullhouse")
        if max(count)==10249:
            print("T-2 fullhouse")

        if max(count)==10240:
            print("9-A fullhouse")
        if max(count)==10239:
            print("9-K fullhouse")
        if max(count)==10238:
            print("9-Q fullhouse")
        if max(count)==10237:
            print("9-J fullhouse")
        if max(count)==10236:
            print("9-T fullhouse")
        if max(count)==10235:
            print("9-8 fullhouse")
        if max(count)==10234:
            print("9-7 fullhouse")
        if max(count)==10233:
            print("9-6 fullhouse")
        if max(count)==10232:
            print("9-5 fullhouse")
        if max(count)==10231:
            print("9-4 fullhouse")
        if max(count)==10230:
            print("9-3 fullhouse")
        if max(count)==10229:
            print("9-2 fullhouse")

        if max(count)==10220:
            print("8-A fullhouse")
        if max(count)==10219:
            print("8-K fullhouse")
        if max(count)==10218:
            print("8-Q fullhouse")
        if max(count)==10217:
            print("8-J fullhouse")
        if max(count)==10216:
            print("8-T fullhouse")
        if max(count)==10215:
            print("8-9 fullhouse")
        if max(count)==10214:
            print("8-7 fullhouse")
        if max(count)==10213:
            print("8-6 fullhouse")
        if max(count)==10212:
            print("8-5 fullhouse")
        if max(count)==10211:
            print("8-4 fullhouse")
        if max(count)==10210:
            print("8-3 fullhouse")
        if max(count)==10209:
            print("8-2 fullhouse")

        if max(count)==10200:
            print("7-A fullhouse")
        if max(count)==10199:
            print("7-K fullhouse")
        if max(count)==10198:
            print("7-Q fullhouse")
        if max(count)==10197:
            print("7-J fullhouse")
        if max(count)==10196:
            print("7-T fullhouse")
        if max(count)==10195:
            print("7-9 fullhouse")
        if max(count)==10194:
            print("7-8 fullhouse")
        if max(count)==10193:
            print("7-6 fullhouse")
        if max(count)==10192:
            print("7-5 fullhouse")
        if max(count)==10191:
            print("7-4 fullhouse")
        if max(count)==10190:
            print("7-3 fullhouse")
        if max(count)==10189:
            print("7-2 fullhouse")

        if max(count)==10180:
            print("6-A fullhouse")
        if max(count)==10179:
            print("6-K fullhouse")
        if max(count)==10178:
            print("6-Q fullhouse")
        if max(count)==10177:
            print("6-J fullhouse")
        if max(count)==10176:
            print("6-T fullhouse")
        if max(count)==10175:
            print("6-9 fullhouse")
        if max(count)==10174:
            print("6-8 fullhouse")
        if max(count)==10173:
            print("6-7 fullhouse")
        if max(count)==10172:
            print("6-5 fullhouse")
        if max(count)==10171:
            print("6-4 fullhouse")
        if max(count)==10170:
            print("6-3 fullhouse")
        if max(count)==10169:
            print("6-2 fullhouse")

        if max(count)==10160:
            print("5-A fullhouse")
        if max(count)==10159:
            print("5-K fullhouse")
        if max(count)==10158:
            print("5-Q fullhouse")
        if max(count)==10157:
            print("5-J fullhouse")
        if max(count)==10156:
            print("5-T fullhouse")
        if max(count)==10155:
            print("5-9 fullhouse")
        if max(count)==10154:
            print("5-8 fullhouse")
        if max(count)==10153:
            print("5-7 fullhouse")
        if max(count)==10152:
            print("5-6 fullhouse")
        if max(count)==10151:
            print("5-4 fullhouse")
        if max(count)==10150:
            print("5-3 fullhouse")
        if max(count)==10149:
            print("5-2 fullhouse")

        if max(count)==10140:
            print("4-A fullhouse")
        if max(count)==10139:
            print("4-K fullhouse")
        if max(count)==10138:
            print("4-Q fullhouse")
        if max(count)==10137:
            print("4-J fullhouse")
        if max(count)==10136:
            print("4-T fullhouse")
        if max(count)==10135:
            print("4-9 fullhouse")
        if max(count)==10134:
            print("4-8 fullhouse")
        if max(count)==10133:
            print("4-7 fullhouse")
        if max(count)==10132:
            print("4-6 fullhouse")
        if max(count)==10131:
            print("4-5 fullhouse")
        if max(count)==10130:
            print("4-3 fullhouse")
        if max(count)==10129:
            print("4-2 fullhouse")

        if max(count)==10120:
            print("3-A fullhouse")
        if max(count)==10119:
            print("3-K fullhouse")
        if max(count)==10118:
            print("3-Q fullhouse")
        if max(count)==10117:
            print("3-J fullhouse")
        if max(count)==10116:
            print("3-T fullhouse")
        if max(count)==10115:
            print("3-9 fullhouse")
        if max(count)==10114:
            print("3-8 fullhouse")
        if max(count)==10113:
            print("3-7 fullhouse")
        if max(count)==10112:
            print("3-6 fullhouse")
        if max(count)==10111:
            print("3-5 fullhouse")
        if max(count)==10110:
            print("3-4 fullhouse")
        if max(count)==10109:
            print("3-2 fullhouse")

        if max(count)==10100:
            print("2-A fullhouse")
        if max(count)==10099:
            print("2-K fullhouse")
        if max(count)==10098:
            print("2-Q fullhouse")
        if max(count)==10097:
            print("2-J fullhouse")
        if max(count)==10096:
            print("2-T fullhouse")
        if max(count)==10095:
            print("2-9 fullhouse")
        if max(count)==10094:
            print("2-8 fullhouse")
        if max(count)==10093:
            print("2-7 fullhouse")
        if max(count)==10092:
            print("2-6 fullhouse")
        if max(count)==10091:
            print("2-5 fullhouse")
        if max(count)==10090:
            print("2-4 fullhouse")
        if max(count)==10089:
            print("2-3 fullhouse")


        if max(count)==9500:
            print("flash")
        if max(count)==9499:
            print("flash")
        if max(count)==9498:
            print("flash")
        if max(count)==9497:
            print("flash")

        if max(count)==8999:
            print("A hi straight")
        if max(count)==8998:
            print("K hi straight")
        if max(count)==8997:
            print("Q hi straight")
        if max(count)==8996:
            print("J hi straight")
        if max(count)==8995:
            print("T hi straight")
        if max(count)==8994:
            print("9 hi straight")
        if max(count)==8993:
            print("8 hi straight")
        if max(count)==8992:
            print("7 hi straight")
        if max(count)==8991:
            print("6 hi straight")
        if max(count)==8990:
            print("5 hi straight")

        if max(count)==8500:
            print("A tripps")
        if max(count)==8499:
            print("K tripps")
        if max(count)==8498:
            print("Q tripps")
        if max(count)==8497:
            print("J tripps")
        if max(count)==8496:
            print("T tripps")
        if max(count)==8495:
            print("9 tripps")
        if max(count)==8494:
            print("8 tripps")
        if max(count)==8493:
            print("7 tripps")
        if max(count)==8492:
            print("6 tripps")
        if max(count)==8491:
            print("5 tripps")
        if max(count)==8490:
            print("4 tripps")
        if max(count)==8489:
            print("3 tripps")
        if max(count)==8488:
            print("2 tripps")

        return max(count)

    def hand(hand):
        num="23456789TJQKA"
        if hand[0][0]==hand[1][0]:
            if num.find(hand[0][1])>num.find(hand[1][1]):
                hands=str(hand[0][1])+str(hand[1][1])+"s"
            else:
                hands=str(hand[1][1])+str(hand[0][1])+"s"

        else:
            if num.find(hand[0][1])>num.find(hand[1][1]):
                hands=str(hand[0][1])+str(hand[1][1])+"o"
            else:
                hands=str(hand[1][1])+str(hand[0][1])+"o"
        return hands

    def highcard(player1_hand,player2_hand):
        player_number_1=[]
        player_number_2=[]

        num="23456789TJQKA"
        remove_num_count=0

        for i in player1_hand:
            player_number_1.append(i[1])

        for i in player2_hand:
            player_number_2.append(i[1])


        for i in range(12):
            num="AKQJT98765432"
            if num[i] in player_number_1 and (not num[i] in player_number_2):
                return 3
                break
            elif num[i] in player_number_2 and (not num[i] in player_number_1):
                return 2
                break
            elif num[i] in player_number_1 and  num[i] in player_number_2:
                player_number_1.remove(num[i])
                player_number_2.remove(num[i])
                remove_num_count+=1
            
            if remove_num_count>4:
                return 1
                break

    def pair(player1_hand,player2_hand,x):
        op_num="AKQJT98765432"

        player_number_1=[]
        player_number_2=[]

        num="23456789TJQKA"
        remove_num_count=0

        for i in player1_hand:
            player_number_1.append(i[1])

        for i in player2_hand:
            player_number_2.append(i[1])

        op_num="AKQJT98765432"

        player_number_1.remove(op_num[1100-x])
        player_number_1.remove(op_num[1100-x])
        player_number_2.remove(op_num[1100-x])
        player_number_2.remove(op_num[1100-x])

        for i in range(12):
            num="AKQJT98765432"
            if num[i] in player_number_1 and (not num[i] in player_number_2):
                return 3
                break
            elif num[i] in player_number_2 and (not num[i] in player_number_1):
                return 2
                break
            elif num[i] in player_number_1 and  num[i] in player_number_2:
                player_number_1.remove(num[i])
                player_number_2.remove(num[i])
                remove_num_count+=1
            
            if remove_num_count>2:
                return 1
                break


    def tripps(player1_hand,player2_hand,x):
        op_num="AKQJT98765432"

        player_number_1=[]
        player_number_2=[]

        num="23456789TJQKA"
        remove_num_count=0

        for i in player1_hand:
            player_number_1.append(i[1])

        for i in player2_hand:
            player_number_2.append(i[1])

        op_num="AKQJT98765432"

        player_number_1.remove(op_num[8500-x])
        player_number_1.remove(op_num[8500-x])
        player_number_1.remove(op_num[8500-x])
        player_number_2.remove(op_num[8500-x])
        player_number_2.remove(op_num[8500-x])
        player_number_2.remove(op_num[8500-x])

        for i in range(12):
            num="AKQJT98765432"
            if num[i] in player_number_1 and (not num[i] in player_number_2):
                return 3
                break
            elif num[i] in player_number_2 and (not num[i] in player_number_1):
                return 2
                break
            elif num[i] in player_number_1 and  num[i] in player_number_2:
                player_number_1.remove(num[i])
                player_number_2.remove(num[i])
                remove_num_count+=1
            
            if remove_num_count>1:
                return 1
                break

    def spade_flash(a,b):
        a_spa=[]
        b_spa=[]
        for i in range(7):
            if a[6-i][0]=="s":
                a_spa.append(a[6-i])
            if b[6-i][0]=="s":
                b_spa.append(b[6-i])
        
        return a_spa,b_spa

    def dia_flash(a,b):
        a_dia=[]
        b_dia=[]
        for i in range(7):
            if a[6-i][0]=="d":
                a_dia.append(a[6-i])
            if b[6-i][0]=="d":
                b_dia.append(b[6-i])
        
        return a_dia,b_dia

    def heart_flash(a,b):
        a_hea=[]
        b_hea=[]
        for i in range(7):
            if a[6-i][0]=="h":
                a_hea.append(a[6-i])
            if b[6-i][0]=="h":
                b_hea.append(b[6-i])
        
        return a_hea,b_hea

    def club_flash(a,b):
        a_clb=[]
        b_clb=[]
        for i in range(7):
            if a[6-i][0]=="c":
                a_clb.append(a[6-i])
            if b[6-i][0]=="c":
                b_clb.append(b[6-i])
        
        return a_clb,b_clb

    def twopair(a,b):
        num="AKQJT98765432"
        player1_pair=[]
        player2_pair=[]
        player_number_1=[]
        player_number_2=[]

        for i in a:
            player_number_1.append(i[1])

        for i in b:
            player_number_2.append(i[1])

        for i in range(13):
            if player_number_1.count(num[i])==2:
                player1_pair.append(num[i])
                player_number_1.remove(num[i])
                player_number_1.remove(num[i])
            if player_number_2.count(num[i])==2:
                player2_pair.append(num[i])
                player_number_2.remove(num[i])
                player_number_2.remove(num[i])


        remove_num_count=0
        sec_remove_num_count=0
        for i in range(12):
            sec_num="AKQJT98765432"
            if sec_num[i] in player1_pair and (not sec_num[i] in player2_pair):
                return 3
                break
            elif sec_num[i] in player2_pair and (not sec_num[i] in player1_pair):
                return 2
                break
            elif sec_num[i] in player1_pair and  sec_num[i] in player2_pair:
                player1_pair.remove(sec_num[i])
                player2_pair.remove(sec_num[i])
                remove_num_count+=1
                
            if remove_num_count>1:

                for i in range(12):
                    third_num="AKQJT98765432"
                    if third_num[i] in player_number_1 and (not third_num[i] in player_number_2):
                        return 3
                        break
                    elif third_num[i] in player_number_2 and (not third_num[i] in player_number_1):
                        return 2
                        break
                    elif third_num[i] in player_number_1 and  third_num[i] in player_number_2:
                        player_number_1.remove(third_num[i])
                        player_number_2.remove(third_num[i])
                        sec_remove_num_count+=1
                    
                    if sec_remove_num_count>0:
                        return 1
                        break

    #heads up
    #player1がsb
    for i in range(loop_num):
        loop=players_hand()
        player1_point=fullhouse_quads_trips(loop[0])
        player2_point=fullhouse_quads_trips(loop[1])

        if heads_sbpush(hand(loop[5]))==True and heads_bbcall(hand(loop[6]))==False:
            player1_money+=100
            print("bb fold")
        elif heads_sbpush(hand(loop[5]))==False:
            player1_money-=50
            print("sb fold")
        elif heads_sbpush(hand(loop[5]))==True and heads_bbcall(hand(loop[6]))==True:
            print(loop[4])
            win_price=784+16*(rake_back+50)/100
            if player1_point>player2_point:
                player1_money+=win_price
                print("player1win")
            elif player2_point>player1_point:
                print("player2win")
                player1_money-=800
            elif player1_point==1000 and player2_point==1000:
                if highcard(loop[0],loop[1])==3:
                    player1_money+=win_price
                    print("player1win")     
                elif highcard(loop[0],loop[1])==2:
                    player1_money-=800
                    print("player2win")  
                elif highcard(loop[0],loop[1])==1:
                    print("chop")
            elif player1_point==player2_point and 1101>player1_point>=1080:
                if pair(loop[0],loop[1],player1_point)==3:
                    player1_money+=win_price
                    print("player1win")  
                elif pair(loop[0],loop[1],player1_point)==2:
                    player1_money-=800
                    print("player2win")  
                elif pair(loop[0],loop[1],player1_point)==1:
                    print("chop")
            elif player1_point==player2_point and 8501>player1_point>=8488:
                if tripps(loop[0],loop[1],player1_point)==3:
                    player1_money+=win_price
                    print("player1win")  
                elif tripps(loop[0],loop[1],player1_point)==2:
                    player1_money-=800
                    print("player2win")  
                elif tripps(loop[0],loop[1],player1_point)==1:
                    print("chop")

            elif player1_point==9500 and player2_point==9500:
                flash_hand=spade_flash(loop[0],loop[1])
                if highcard(flash_hand[0],flash_hand[1])==3:
                    player1_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand[0],flash_hand[1])==2:
                    player1_money-=800
                    print("player2win")  
                elif highcard(flash_hand[0],flash_hand[1])==1:
                    print("chop")

            elif player1_point==9499 and player2_point==9499:
                flash_hand=dia_flash(loop[0],loop[1])
                if highcard(flash_hand[0],flash_hand[1])==3:
                    player1_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand[0],flash_hand[1])==2:
                    player1_money-=800
                    print("player2win")  
                elif highcard(flash_hand[0],flash_hand[1])==1:
                    print("chop")

            elif player1_point==9498 and player2_point==9498:
                flash_hand=heart_flash(loop[0],loop[1])
                if highcard(flash_hand[0],flash_hand[1])==3:
                    player1_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand[0],flash_hand[1])==2:
                    player1_money-=800
                    print("player2win")  
                elif highcard(flash_hand[0],flash_hand[1])==1:
                    print("chop")

            elif player1_point==9497 and player2_point==9497:
                flash_hand=club_flash(loop[0],loop[1])
                if highcard(flash_hand[0],flash_hand[1])==3:
                    player1_money+=win_price
                    print("player1win")
                elif highcard(flash_hand[0],flash_hand[1])==2:
                    player1_money-=800
                    print("player2win")  
                elif highcard(flash_hand[0],flash_hand[1])==1:
                    print("chop")

            elif player1_point==3000 and player2_point==3000:
                answer=twopair(loop[0],loop[1])
                if answer==3:
                    player1_money+=win_price
                    print("player1win")
                elif answer==2:
                    player1_money-=800
                    print("player2win")  
                elif answer==1:
                    print("chop")

        if heads_sbpush2(hand(loop[5]))==True and heads_bbcall(hand(loop[6]))==False:
            player2_money+=100
            print("bb fold")
        elif heads_sbpush2(hand(loop[5]))==False:
            player2_money-=50
            print("sb fold")
        elif heads_sbpush2(hand(loop[5]))==True and heads_bbcall(hand(loop[6]))==True:
            print(loop[4])
            win_price=784+16*(rake_back+50)/100
            if player1_point>player2_point:
                player2_money+=win_price
                print("player1win")
            elif player2_point>player1_point:
                print("player2win")
                player2_money-=800
            elif player1_point==1000 and player2_point==1000:
                if highcard(loop[0],loop[1])==3:
                    player2_money+=win_price
                    print("player1win")     
                elif highcard(loop[0],loop[1])==2:
                    player2_money-=800
                    print("player2win")  
                elif highcard(loop[0],loop[1])==1:
                    print("chop")
            elif player1_point==player2_point and 1101>player1_point>=1080:
                if pair(loop[0],loop[1],player1_point)==3:
                    player2_money+=win_price
                    print("player1win")  
                elif pair(loop[0],loop[1],player1_point)==2:
                    player2_money-=800
                    print("player2win")  
                elif pair(loop[0],loop[1],player1_point)==1:
                    print("chop")
            elif player1_point==player2_point and 8501>player1_point>=8488:
                if tripps(loop[0],loop[1],player1_point)==3:
                    player2_money+=win_price
                    print("player1win")  
                elif tripps(loop[0],loop[1],player1_point)==2:
                    player2_money-=800
                    print("player2win")  
                elif tripps(loop[0],loop[1],player1_point)==1:
                    print("chop")

            elif player1_point==9500 and player2_point==9500:
                flash_hand2=spade_flash(loop[0],loop[1])
                if highcard(flash_hand2[0],flash_hand2[1])==3:
                    player2_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand2[0],flash_hand2[1])==2:
                    player2_money-=800
                    print("player2win")  
                elif highcard(flash_hand2[0],flash_hand2[1])==1:
                    print("chop")

            elif player1_point==9499 and player2_point==9499:
                flash_hand2=dia_flash(loop[0],loop[1])
                if highcard(flash_hand2[0],flash_hand2[1])==3:
                    player2_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand2[0],flash_hand2[1])==2:
                    player2_money-=800
                    print("player2win")  
                elif highcard(flash_hand2[0],flash_hand2[1])==1:
                    print("chop")

            elif player1_point==9498 and player2_point==9498:
                flash_hand2=heart_flash(loop[0],loop[1])
                if highcard(flash_hand2[0],flash_hand2[1])==3:
                    player2_money+=win_price
                    print("player1win")   
                elif highcard(flash_hand2[0],flash_hand2[1])==2:
                    player2_money-=800
                    print("player2win")  
                elif highcard(flash_hand2[0],flash_hand2[1])==1:
                    print("chop")

            elif player1_point==9497 and player2_point==9497:
                flash_hand2=club_flash(loop[0],loop[1])
                if highcard(flash_hand2[0],flash_hand2[1])==3:
                    player2_money+=win_price
                    print("player1win")
                elif highcard(flash_hand2[0],flash_hand2[1])==2:
                    player2_money-=800
                    print("player2win")  
                elif highcard(flash_hand2[0],flash_hand2[1])==1:
                    print("chop")

            elif player1_point==3000 and player2_point==3000:
                answer=twopair(loop[0],loop[1])
                if answer==3:
                    player2_money+=win_price
                    print("player1win")
                elif answer==2:
                    player2_money-=800
                    print("player2win")  
                elif answer==1:
                    print("chop")
        kaisuu=np.append(kaisuu,i)
        player1_money_np=np.append(player1_money_np,player1_money)
        player2_money_np=np.append(player2_money_np,player2_money)



    return round(player1_money),round(player2_money),kaisuu,player1_money_np,player2_money_np