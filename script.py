#Module
import os
global user_login

#Functionen
def u_l_d_c():
    if not os.path.exists("user.txt"):
        print("Datei nicht vorhanden.\n Datei wird erstellt.") 
        user_login = open("user.txt", "w")
        user_login.close





#def user_login(name, pwd):
    
def user_create(name, pwd, security_lvl):
    locked = False
    u_l_d_c()
    user_login = open("user.txt", "r")
    for zeile in user_login:
        print(zeile)
        print("Name: " + name)
        if zeile == "Name: " + name:
            locked = True
            user_login.close
        else:
            locked = False
            user_login.close
    if locked == False:
            user_login = open("user.txt", "a")
            user_login.write("\nName: " + name + "\nPasswort: "+ pwd +"\nSecurity Level: " + str(security_lvl))
            user_login.close 
    else:
         print("Nutzername bereits vergeben")
            
    
    
    



#etc

user_create("Test","test",2)