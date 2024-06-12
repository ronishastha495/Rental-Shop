import splittingcode
import DateandTime
import Rent
import Return
import sys

def MainPage_start():
    mainpage=True
    while mainpage == True:
        print("                                  ╔════════════════════════════════════════════════════════════════╗")
        print("                                  ║                                                                ║ ")
        print("==================================║                      WELCOME TO PRIME RENTALS                  ║==========================")
        print("                                  ║                                                                ║   ")
        print("                                  ╚════════════════════════════════════════════════════════════════╝")
    
        print("PRESS 1: TO RENT ANY ITEMS ")
        print("PRESS 2: TO RETURN ANY RENTED ITEMS ")
        print("PRESS 3: TO EXIT FROM THE STORE")
        continue_mainpage = True
        while continue_mainpage ==True:
            try:
                a = int(input("VALUED CUSTOMER, PLEASE MAKE YOUR SELECTION FROM THE OPTIONS ABOVE: "))
                print()
                continue_mainpage =  False
            except :
                print("KINDLY INITIATE THE PROCESS BY SELECTING THE BUTTON INDICATED IN THE ABOVE OPTION")
        if(a == 1):
            print()
            Rent.BillRent()
            
        elif(a == 2):
            print()
            Return.SELL()
        elif(a == 3):
            mainpage=False
            
        else:
                print("VALUED CUSTOMER, PLEASE SELECT THE CORRECT OPTION FROM THE CHOICES PROVIDED ABOVE.")
       
MainPage_start()
