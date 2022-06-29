dict_translate=[]
def load():
   print("LOADING...")
   load=open("translate.txt","r")
   dict_translate=load.read().split("\n")  


   for i in range (len(dict_translate)):
        file_translate={}
        if i % 2 == 0:
           load[i]=file_translate["english"]
        else:
            load[i]=file_translate["pershian"]
            dict_translate.append(file_translate)


def Show_list():
    print("1.Add a word")
    print("2.English to Persian translator")
    print("3.Persian to English translator")
    print("4.Exit the app")

def Add_a_word():
    english=input(" Please type the English word to add to the app : ")
    pershian=input("Please type the meaning of the word  : ")

    dict_translate.append({"english" : english ,"persian" : pershian})
    file_translate=open("translate.txt" , "a")
    file_translate.write("\n" + english) 
    file_translate.write("\n" + pershian )
    print(" Your input has been added to the application :)")
    file_translate.close()

def English_to_Persian_translator():
    sentence =input ("Please type the sentence : ")
    pershian = sentence.split( )

    for x in range(len(dict_translate)):
        for y in range (len(pershian)):
            if pershian[x] == dict_translate[y]["pershian"]:
                print(dict_translate[y]["english"] , end=" ")
                break
            else:
             print(pershian)  

def Persian_to_English_translator():
    sentece = input("Please type the sentence : ")
    english = sentece.split( )

    for x in range(len(dict_translate)):
        for y in range(len(english)):
            if english[x]==dict_translate[y]["english"]:
                print(dict_translate[x]["persian"] , end= " ")
            else:
                print(english)

load()           

while True:
    Show_list()

    select = input("Select one of the number : ")

    if select=="1":
       Add_a_word()
    elif select=="2":
        English_to_Persian_translator()
    elif select=="3":
       Persian_to_English_translator()
    elif select=="4":
       exit()