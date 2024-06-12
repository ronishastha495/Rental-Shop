import DateandTime
import splittingcode


def get_SnNo():
    file_Data = splittingcode.getfile_Data()
    file_Inside = splittingcode.getsplittingcode(file_Data)
    Sn_loop = False
    while Sn_loop == False:
        SN1 = False
        while SN1 == False:
            try:
                SnNo = int(input("-----KINDLY INPUT THE DESIRED ITEM-----: "))
                SN1 = True
            except:
                print("----WE RECOMMEND ENTERING ALPHABETIC CHARACTERS ONLY!-----")
        if SnNo > 0 and SnNo <= len(file_Inside):
            loop = True
            return SnNo
        else:
            print()
            print("WE HAVE ONLY THIS  COUSTUMES AVAILABLE HERE")
            print("THE REQUESTED ITEM IS CURRENTLY UNAVAILABLE. PLEASE CONSIDER CHOOSING AN ALTERNATIVE OPTION FROM THE LIST BELOW:: " )
            splittingcode.TABLECLOTH_data()


def get_QUANTITY(SnNo):
    file_Data = splittingcode.getfile_Data()
    file_Inside = splittingcode.getsplittingcode(file_Data)

    QUANTITY_loop = False
    while QUANTITY_loop == False:
        QUANTITY_SN1 = False
        while QUANTITY_SN1 ==False:
            try:
                quantity = int(input("-----KINDLY SPECIFY THE QUANTITY OF ITEMS YOU WISH TO RETURN----: "))
                QUANTITY_SN1 = True
            except:
                print("KINDLY PROVIDE THE ACCURATE QUANTITY:")
        if quantity > 0 :
            QUANTITY_loop = True
            return quantity
        else:
            print("KINDLY PROVIDE THE ACCURATE QUANTITY:")

def getreturn():
    return_loop = False
    while return_loop == False:
        try:
            no_days = int(input("KINDLY SPECIFY THE NUMBER OF DAYS FOR THE RENTAL RETURN PERIOD "))
            no_days = str(no_days)
            return_loop = False
            return no_days
        except:
            print("-------INVALID ENTRY. PLEASE PROVIDE A VALID NUMBER OF DAYS FOR THE RENTAL RETURN PERIOD.-------")


def SELL():
    cart = []
    continue_loop = True
    while continue_loop == True:
        splittingcode.TABLECLOTH_data()
        SnNo = get_SnNo()
        quantity = get_QUANTITY(SnNo)
        no_days = getreturn()
        cart.append([SnNo,quantity,no_days])

        file_Data = splittingcode.getfile_Data()
        NewcontentData = splittingcode.getsplittingcode(file_Data)
        NewcontentData[SnNo][3] = str(int(NewcontentData[SnNo][3]) + quantity)

        with open("stockdata.txt","w") as file:
            for value in NewcontentData.values():
                writeData = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
                file.write(writeData)
            file.close()
           
       
        loop = True
        while loop == True:
            userInput = input("------IF YOU WISH TO SELECT ADDITIONAL ITEMS, PLEASE ENTER (Yes) . IF YOU ARE READY TO RECEIVE YOUR BILL, PLEASE ENTER (no)(Yes/No)------: ")
            if userInput.lower() == "no":
                loop = False
                continue_loop = False
                file_Data = splittingcode.getfile_Data()
                NewcontentData = splittingcode.getsplittingcode(file_Data)

                Firstname_Loop = False
                while Firstname_Loop == False:
                    try:
                        user_Firstname = input("-----DEAR CUSTOMER COULD YOU PLEASE ENTER YOUR FIRST NAME----: ")
                        if user_Firstname.isalpha():
                            Firstname_Loop = True
                        else:
                            print("DEAR CUSTOMER, KINDLY PROVIDE YOUR FIRST NAME:")
                    except:
                        print("KINDLY INPUT THE CORRECT FIRST NAME:")

                Lastname_Loop = False
                while Lastname_Loop == False:
                    try:
                        user_LastName = input("-----DEAR CUSTOMER, KINDLY PROVIDE YOUR LAST NAME:---- ")
                        if user_LastName.isalpha():
                            Lastname_Loop = True
                        else:
                            print("COULD YOU PLEASE ENTER CORRECT LAST NAME: ")
                    except:
                        print("KINDLY INPUT THE CORRECT LAST NAME: ")

                contactNO_Loop = False
                while contactNO_Loop == False:
                    try:
                        user_ContactNO = int(input("-----DEAR CUSTOMER, PLEASE PROVIDE YOUR CONTACT NUMBER:-----"))
                        user_ContactNO = str(user_ContactNO)
                        contactNO_Loop = True
                    except:
                        print("PLEASE ENTER A VALID CONTACT NUMBER:")

                print()
                print()
                
                print()
                print("Name: "+ user_Firstname+" "+user_LastName)
                print("Contact info: " + user_ContactNO)
                print("DATE: " +DateandTime.getDate())
                print("Time: " +DateandTime.getTime())
                print()
                print("*********************************************************************************************************")
                print("ID", "\t", "ITEM NAME", "\t\t", "ITEM BRAND", "\t\t", "CHARGE", "\t\t", "QUANTITY")
                print("*********************************************************************************************************")
                TotalCharge = 0
                for i in range(len(cart)):
                    TABLECLOTH_ID = int(cart[i][0])
                    TABLECLOTH_QUANTITY = int(cart[i][1])
                    TABLECLOTH_NAME = NewcontentData[TABLECLOTH_ID][0]
                    TABLECLOTH_BRAND = NewcontentData[TABLECLOTH_ID][1]
                    Return = int(cart[i][2])
                    CHARGE = 0
                    if Return > 5:
                        CHARGE = (float(NewcontentData[TABLECLOTH_ID][2].replace("$",""))*(20/100))*(Return - 5)
                        Charge_day = TABLECLOTH_QUANTITY * CHARGE
                        TotalCharge += Charge_day
                    else:
                        Charge_day="0"
                                           
                    print(str(i+1)+"\t"+""+TABLECLOTH_NAME+"\t"+""+TABLECLOTH_BRAND+"\t"+""+("$"+str(Charge_day))+"\t\t\t"+""+str(TABLECLOTH_QUANTITY))
                    print("*********************************************************************************************************")
                print("Total: ","$",TotalCharge)
                print()
                break
            elif userInput.lower() == "yes":
                loop = False
            else:
                print()

            print("-------IF YOU WISH TO SELECT ADDITIONAL ITEMS, PLEASE ENTER (Yes) . IF YOU ARE READY TO RECEIVE YOUR BILL, PLEASE ENTER (no)(Yes/No)--------")


    with open(DateandTime.getDate()+"  "+user_Firstname+" "+user_LastName+".txt","w") as AMOUNTS:
        AMOUNTS.write("NAME: "+ user_Firstname+" "+user_LastName+"\n")
        AMOUNTS.write("CONTACT NO: " + user_ContactNO+"\n")
        AMOUNTS.write("DATE: " +DateandTime.getDate())
        AMOUNTS.write("Time: " +DateandTime.getTime()+"\n")
        AMOUNTS.write("******************************************************************************************"+"\n")
        AMOUNTS.write("ID"+ "\t"+ "ITEM NAME"+ "\t\t\t\t\t"+ "ITEM BRAND"+ "\t\t"+ "CHARGE"+ "\t\t"+ "QUANTITY"+"\n")
        AMOUNTS.write("******************************************************************************************"+"\n")
        TotalCharge = 0
        for i in range(len(cart)):
            TABLECLOTH_Id = int(cart[i][0])
            TABLECLOTH_QUANTITY = int(cart[i][1])
            TABLECLOTH_NAME = NewcontentData[TABLECLOTH_Id][0]
            TABLECLOTH_BRAND = NewcontentData[TABLECLOTH_Id][1]
            Return = int(cart[i][2])
            CHARGE = 0
            if Return > 5:
                CHARGE = (float(NewcontentData[TABLECLOTH_ID][2].replace("$",""))*(20/100))*(Return - 5)
                Charge_day = TABLECLOTH_QUANTITY * CHARGE
                TotalCharge += Charge_day
            else:
                Charge_day="0"
                                           
            AMOUNTS.write(str(i+1)+"\t"+""+TABLECLOTH_NAME+"\t"+""+TABLECLOTH_BRAND+"\t"+""+("$"+str(Charge_day))+"\t\t\t"+""+str(TABLECLOTH_QUANTITY)+"\n")
        AMOUNTS.write("******************************************************************************************"+"\n")
        AMOUNTS.write("TOTAL: "+"$"+str(TotalCharge)+"\n")
        
