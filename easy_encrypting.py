import os 
alfabe =[" ","a","A","b","B","c","C","ç","Ç","d","D","e","E","f","F","g","G","ğ","Ğ","h","H","ı","I","i","İ","j","J","k","K","l","L","m","M","n","N","o","O","ö","Ö","p","P","r","R","s","S","ş","Ş","t","T","u","U","ü","Ü","v","V","y","Y","z","Z","w","W","q","Q","x","X","1","2","3","4","5","6","7","8","9","0",".",",",":",";","*","(",")","!","'","^","+","%","&","/","=","?","-","|","_","#","~","{","}","[","]",'"']



def number2binary(sayi,key):
    global binary_yazi 
    binary_yazi = ""
    sayi += key
    while(len(binary_yazi) < 11):
        binary_yazi += str(sayi % 2)
        sayi = sayi // 2
    binary_yazi = binary_yazi[::-1]
    


def binary2number(binary,key):
    binary = binary[::-1]
    list_binary = ([*binary])
    i = len(list_binary)
    global toplam_sayi 
    toplam_sayi = 0
    for i in range(i):
        if int(list_binary[i]) == 0:
            pass
            
        else:
            toplam_sayi += 2**i

    toplam_sayi = toplam_sayi - key
    
    





def encrypt(yazi,key):
    list_yazi = ([*yazi])
    global encrypted_yazi
    encrypted_yazi = ""
    i = len(list_yazi)
    for i in range(i):
        alfabe_sira = alfabe.index(list_yazi[i])
        number2binary(alfabe_sira,key)
        encrypted_yazi += binary_yazi
        encrypted_yazi += " "


def decrypt(yazi,key):
    list_yazi = yazi.split()
    global decrypted_yazi
    decrypted_yazi = ""
    i = len(list_yazi)
    for i in range(i):
        binary2number(list_yazi[i],key)
        harf = alfabe[toplam_sayi]
        decrypted_yazi += harf


input("""
    ###############################################
    #           Easy Encrypting Tool              #
    #                                             #
    #                                by BurakGGM  #
    ###############################################


    Press ENTER to contiune 
    """)

while(True):
    

    os.system("cls")

    sec = input("""
    | 
    | To encryipt anything 1
    | To decrypt anything 2
    | To EXIT 99'a
    | Press the number then press ENTER
    |

    >> """)

    if int(sec) == 1:
        os.system("cls")
        sifrelencek_yazi = input("""
    |
    | 
    | Write the text you want to encrypt then press ENTER
    | 
    | Then write a key (a number between 1-923) then press ENTER
    |

    Note: Try to not use special characters you can use things like /('" but more complicated ones will give error

    >> """)
        key = int(input("    >>"))
        encrypt(sifrelencek_yazi,key)
        print(f"""
    Encrypted text is ready
########################################################
{encrypted_yazi}
########################################################
    """)
        print("Press ENTER to go back to menu")
    


    elif int(sec) == 2:
        os.system("cls")
        sifrelencek_yazi = input("""
    |
    | 
    | Write the text you want to decrypt then press ENTER
    | 
    | Then write a key (a number between 1-923) then press ENTER
    |

    >> """)
        key = int(input("    >>"))
        decrypt(sifrelencek_yazi,key)
        print(f"""
Decrypted text is ready 
########################################################
{decrypted_yazi}
########################################################
    """)
        print("Press ENTER to go back to menu")

    elif int(sec) == 99:
        break
    else:
        print("ERROR : Please just enter 1,2 or 99")

    input()