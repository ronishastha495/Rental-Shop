def getfile_Data():
    file = open("stockdata.txt","r")
    file_Inside = file.readlines()
    file.close()
    return file_Inside


def getsplittingcode(file_Data):
    file_Inside = {}
    for i in range(len(file_Data)):
        file_Inside[i+1] = file_Data[i].replace("\n","").split(",")
    return file_Inside


def TABLECLOTH_data():
    file_Data = getfile_Data()
    file_Inside = getsplittingcode(file_Data)
    print("**********************************************************************************************************")
    print("SN", "\t", "ITEM NAME", "\t\t\t", "ITEM BRAND", "\t\t", "PRICE", "\t\t", "QUANTITY")
    print("**********************************************************************************************************")
    for key, data in file_Inside.items():
        print(key,"\t",data[0],"\t",data[1],"\t\t",data[2],"\t",data[3])
    print("**********************************************************************************************************")
