from DTO import *

prompt = """
=========================
=                       =
=   Cafe Menu Admin     =
=   1. 메뉴 추가         =
=   2. 메뉴 삭제         =
=   3. 메뉴 수정         =
=   4. 메뉴 조회         =
=   5. 끝내기            =
=                       =
=========================
"""

def cafe_admin():
    num = 0
    while(num != 5):
        print(prompt)
        num = int(input('번호를 입력해주세요. : '))
        if num == 1:
            name = input('추가하실 메뉴의 이름을 입력해주세요. : ')
            price = int(input('추가하실 메뉴의 가격을 숫자로 입력해주세요. : '))
            make_newmenu(name, price)
        elif num == 2:
            menulist = list_menu()
            for i in range(len(menulist)):
                print("%s. 메뉴 : %s - 가격 : %s"%(i+1 ,menulist[i][1], menulist[i][2]))
            idd = int(input('삭제하실 메뉴의 번호를 입력해주세요. : '))
            if idd<1 and idd>len(menulist):
                print('올바른 메뉴의 번호를 입력해주세요.')
            else:
                id = menulist[idd-1][0]
                name = menulist[idd-1][1]
                delete_menu(name, id)
        elif num == 3:
            menulist = list_menu()
            for i in menulist:
                print("%s. 메뉴 : %s - 가격 : %s"%(i[0],i[1], i[2]))
            idd = int(input('수정하실 메뉴의 번호를 입력해주세요. : '))
            if idd<1 and idd>len(menulist):
                print('올바른 메뉴의 번호를 입력해주세요.')
            else:
                id = menulist[idd-1][0]
                name = menulist[idd-1][1]
                price = menulist[idd-1][2]
                newname = input("메뉴명을 수정하시겠습니까?\n수정하시려면 수정할 메뉴 명을 입력해주세요.\n건너뛰려면 'N'을 입력해주세요 . :")
                if newname == "N":
                    newname = name
                newprice = int(input("%s의 가격을 수정하시겠습니까?\n수정하시려면 수정할 메뉴 명을 입력해주세요.\n건너뛰려면 '0'을 입력해주세요 . :"%(newname)))
                if newprice == 0:
                    newprice = price
                update_menu(id, newname, newprice)  
        elif num == 4:
            menulist = list_menu()
            for i in menulist:
                print("메뉴 : %s - 가격 : %s"%(i[1], i[2]))
        elif num == 5:
            break
        else:
            print("올바른 메뉴의 번호를 입력해주세요.")