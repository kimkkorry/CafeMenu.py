from CafeAdmin import *

prompt = """
=====================
=                   =
=   Cafe Menu       =
=   1. 주문하기      =
=   2. 취소하기      =
=   3. 장바구니 확인 =
=   4. 메뉴 조회     =
=   5. 끝내기        =
=                   =
=====================
"""

things = []

num = 0
while(num != 5):
    print(prompt)
    num = int(input('번호를 입력해주세요. : '))
    if num == 1:
        menulist = list_menu()
        if len(menulist) == 0:
            print("'501'을 눌러 메뉴를 먼저 추가해주세요.")
        else:
            for i in range(len(menulist)):
                print("%s. 메뉴 : %s - 가격 : %s"%(i+1 ,menulist[i][1], menulist[i][2]))
            idd = int(input('주문하실 메뉴의 번호를 입력해주세요. : '))
            if idd<1 or idd>len(menulist):
                print('올바른 메뉴의 번호를 입력해주세요.')
            else:
                id = menulist[idd-1][0]
                name = menulist[idd-1][1]
                price = menulist[idd-1][2]
                thing = int(input("%s의 개수를 입력해주세요."%(name)))
                a = 0
                for i in things:
                    if name == i[0]:
                        a+=1
                if a == 1:
                    for i in things:
                        if name == i[0]:
                            i[1]+=thing
                else:
                    newlist = [name, thing, price]
                    things.append(newlist)
                print("%s %s개가 추가되었습니다."%(name, thing))

    elif num == 2:
        things = []
        print("장바구니가 초기화 되었습니다.")
    elif num == 3:
        if len(things) == 0:
            print("장바구니가 비어있습니다.")
        else:
            Allprice = 0
            for i in things:
                print("%s %s개"%(i[0], i[1]))
                Allprice += i[1]*i[2]
            print("총 %s원 입니다."%(Allprice))
    elif num == 4:
        menulist = list_menu()
        if len(menulist) == 0:
            print("'501'을 눌러 메뉴를 먼저 추가해주세요.")
        else:
            for i in menulist:
                print("메뉴 : %s - 가격 : %s"%(i[1], i[2]))
    elif num == 5:
        break
    elif num == 501:
        cafe_admin()
    else:
        print("올바른 메뉴의 번호를 입력해주세요.")


