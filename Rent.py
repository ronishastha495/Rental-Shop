import DateandTime
import splittingcode


def get_SnNo():
    file_Data = splittingcode.getfile_Data()
    file_Inside = splittingcode.getsplittingcode(file_Data)
    loop = False
    while loop == False:
        SN1 = False
        while SN1 == False:
            try:
                SnNo = int(input("-----KINDLY INPUT THE DESIRED ITEM-----: "))
                SN1 = True
            except:
                print("----WE RECOMMEND ENTERING ALPHABETIC CHARACTERS ONLY-----")
        if SnNo > 0 and SnNo <= len(file_Inside):
            if int(file_Inside[SnNo][3]) <= 0:
                print()
                print("THE SELECTED ITEM IS CURRENTLY UNAVAILABLE")
            else:
                loop = True
                return SnNo
        else:
            print()
            print("WE HAVE ONLY THESE " + str(len(file_Inside)) + " ITEMS AVAILABLE HERE")
            print("THE REQUESTED ITEM IS CURRENTLY UNAVAILABLE. PLEASE CONSIDER CHOOSING AN ALTERNATIVE OPTION FROM THE LIST BELOW: " + str(len(file_Inside)))
            splittingcode.TABLECLOTH_data()


def get_QUANTITY(SnNo):
    file_Data = splittingcode.getfile_Data()
    file_Inside = splittingcode.getsplittingcode(file_Data)

    QUANTITY_loop = False
    while QUANTITY_loop == False:
        QUANTITY_SN1 = False
        while QUANTITY_SN1 ==False:
            try:
                quantity = int(input("-----PLEASE INDICATE THE QUANTITY OF THE PRODUCT YOU WOULD LIKE TO RENT:-----: "))
                QUANTITY_SN1 = True
            except:
                print("PLEASE INPUT THE CORRECT QUANTITY!!!")
        if quantity > 0 and quantity<= int(file_Inside[SnNo][3]):
            QUANTITY_loop = True
            return quantity
        else:
            print("PLEASE INPUT THE CORRECT QUANTITY!!!")



def BillRent():
    cart = []
    continue_loop = True
    while continue_loop == True:
        splittingcode.TABLECLOTH_data()
        SnNo = get_SnNo()
        quantity = get_QUANTITY(SnNo)
        cart.append([SnNo,quantity])

        file_Data = splittingcode.getfile_Data()
        NewcontentData = splittingcode.getsplittingcode(file_Data)
        NewcontentData[SnNo][3] = str(int(NewcontentData[SnNo][3]) - quantity)

        with open("stockdata.txt","w") as file:
            for value in NewcontentData.values():
                writeData = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
                file.write(writeData)
            file.close()
           
       
        loop = True
        while loop == True:
            userInput = input("------IF YOU WISH TO SELECT ADDITIONAL ITEMS, PLEASE ENTER (Yes) . IF YOU ARE READY TO RECEIVE YOUR BILL, PLEASE ENTER (no)  (Yes/No)------: ")
            if userInput.lower() == "no":
                loop = False
                continue_loop = False
                file_Data = splittingcode.getfile_Data()
                NewcontentData = splittingcode.getsplittingcode(file_Data)

                Firstname_Loop = False
                while Firstname_Loop == False:
                    try:
                        user_Firstname = input("-----DEAR CUSTOMER, KINDLY PROVIDE YOUR FIRST NAME:----: ")
                        if user_Firstname.isalpha():
                            Firstname_Loop = True
                        else:
                            print("PLEASE PROVIDE YOUR ACCURATE FIRST NAME:")
                    except:
                        print(" PLEASE PROVIDE CORRECT FIRST NAME:")

                Lastname_Loop = False
                while Lastname_Loop == False:
                    try:
                        user_LastName = input("-----DEAR CUSTOMER, KINDLY PROVIDE YOUR LAST NAME---- ")
                        if user_LastName.isalpha():
                            Lastname_Loop = True
                        else:
                            print(" PLEASE PROVIDE YOUR ACCURATE LAST NAME: ")
                    except:
                        print("COULD YOU PLEASE ENTER CORRECT LAST NAME: ")

                contactNO_Loop = False
                while contactNO_Loop == False:
                    try:
                        user_ContactNO = int(input("-----KINDLY ENTER YOUR CONTACT NUMBER, DEAR CUSTOMER:-----"))
                        user_ContactNO = str(user_ContactNO)
                        contactNO_Loop = True
                    except:
                        print("COULD YOU PLEASE ENTER CORRECT CONTACT NUMBER!!!!")

                print()
                print()
                
                print()
                print("Name: "+ user_Firstname+" "+user_LastName)
                print("CONTACT : " + user_ContactNO)
                print("DATE: " +DateandTime.getDate())
                print("Time: " +DateandTime.getTime())
                print()
                print("********************************************************************************************************")
                print("ID", "\t\t\t\t",  "      ITEM NAME", "\t\t\t\t\t\t", "ITEM BRAND", "\t\t\t","PRICE", "\t\t", "QUANTITY")
                print("********************************************************************************************************")
                Total = 0
                for i in range(len(cart)):
                    TABLECLOTH_ID = int(cart[i][0])
                    TABLECLOTH_QUANTITY = int(cart[i][1])
                    TABLECLOTH_NAME = NewcontentData[TABLECLOTH_ID][0]
                    TABLECLOTH_BRAND = NewcontentData[TABLECLOTH_ID][1]
                    TABLECLOTH_PRICE = float(NewcontentData[TABLECLOTH_ID][2].replace("$","")) * TABLECLOTH_QUANTITY
                    Total += TABLECLOTH_PRICE
                                           
                    print(str(i+1)+"\t"+""+TABLECLOTH_NAME+"\t"+""+TABLECLOTH_BRAND+"\t"+""+("$"+str(TABLECLOTH_PRICE))+"\t\t"+""+str(TABLECLOTH_QUANTITY))
                    print("*******************************************************************************************************")
                print("Total: ","$",Total)
                print()
                print()
                print()
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
        AMOUNTS.write("TIME: " +DateandTime.getTime()+"\n")
        AMOUNTS.write("*************************************************************************************************"+"\n")
        AMOUNTS.write("ID"+ "\t"+ "ITEM NAME"+ "\t\t\t"+ "ITEMBRAND"+ "\t\t\t\t"+ "PRICE"+ "\t\t"+ "QUANTITY"+"\n")
        AMOUNTS.write("*************************************************************************************************"+"\n")
        for i in range(len(cart)):
            TABLECLOTH_Id = int(cart[i][0])
            TABLECLOTH_QUANTITY = int(cart[i][1])
            TABLECLOTH_NAME = NewcontentData[TABLECLOTH_Id][0]
            TABLECLOTH_BRAND = NewcontentData[TABLECLOTH_Id][1]
            TABLECLOTH_PRICE = float(NewcontentData[TABLECLOTH_Id][2].replace("$","")) * TABLECLOTH_QUANTITY
            Total += TABLECLOTH_PRICE
                                           
            AMOUNTS.write(str(i+1)+"\t"+""+TABLECLOTH_NAME+"\t"+""+TABLECLOTH_BRAND+"\t\t"+""+("$"+str(TABLECLOTH_PRICE))+"\t\t\t"+""+str(TABLECLOTH_QUANTITY)+"\n")
        AMOUNTS.write("*************************************************************************************************"+"\n")
        AMOUNTS.write("TOTAL: "+"$"+str(Total)+"\n")
        

