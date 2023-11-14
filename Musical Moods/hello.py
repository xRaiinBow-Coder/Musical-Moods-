import time
import os
import webbrowser

print(f"welcome would you like to acces your music account today?")
time.sleep(1)
user = input("Yes or No: ")

attempts = 3


if user == "No":
    username = input("what is your username?:")
    password = input("what is your password?:")
    password1 = input("please enter your password again for validation: ")
    if password == password1:
        file = open("login.txt", "w")
        file.writelines(username + ":" + password)
        file.close()
        os.system("cls")
        user = "Yes"   

elif user == "Yes":
    while attempts > 0:
        LoginUsername = input("username: ")
        LoginPassword = input("what is your password: ")
        file = open("login.txt", "r")
        data = file.readline()
        file.close()
        if data == LoginUsername + ":" + LoginPassword:
            os.system("cls")
            break
        else:
            print("please enter valid details")
            attempts -= 1
            print("Attempts  left", attempts)
        if attempts == 0:
            print("you no longer have any attempts left")
            exit()

        
name = input("please enter your name: ")
file = open("name.txt", "w")
file.writelines(name)
file.close()
os.system("cls")   

print(name)


print("What type of mood are we feeling today?: ")
time.sleep(0.5)
mood = input("Happy, Sad, Angry or Chilled: ")
os.system("cls")

if mood == "Happy":
    print(f"Great {name}, here is your happy playlist")
    textFile = open("h.txt", "r")
    happy = textFile.read().splitlines()
    textFile.close()
    url = "https://www.youtube.com/playlist?list=PL9NPhEnsdchlEulHhCUSuEy8H1yrcGNBT"
    webbrowser.open(url)
    for i in happy:
        print(i)
        time.sleep(0.4)
        
        
elif mood == "Sad":
    print(f"Thats unfortunate! {name}, here is your sad playlist")
    textFile = open("s.txt", "r")
    sad = textFile.read().splitlines()
    textFile.close()
    url = "https://www.youtube.com/playlist?list=PL9NPhEnsdchmb7q9Z_0pgaXjzW49PDz0L"
    webbrowser.open(url)
    for i in sad:
        print(i)
        time.sleep(0.4)
        

elif mood == "Angry":
    print(f"Get your anger out! {name}")
    textFile = open("m.txt", "r")
    mad = textFile.read().splitlines()
    textFile.close()
    url = "https://www.youtube.com/playlist?list=PL9NPhEnsdchm6xchjAnvkWUsJUjhXq9jt"
    webbrowser.open(url)
    for i in mad:
        print(i)
        time.sleep(0.4)
        

elif mood == "Chilled":
    print(f"Here is some beats {name} to relax too")
    textFile = open("c.txt", "r")
    chilled = textFile.read().splitlines()
    textFile.close()
    url = "https://www.youtube.com/playlist?list=PL9NPhEnsdchkUks2n6b5llJnzLkxOmC5_"
    webbrowser.open(url)
    for i in chilled:
        print(i)
        time.sleep(0.4)
        
else:
    print("please pick one of the moods above.")
    exit()
 

print("do you want to add more songs to a playlist?")
A = input("Yes or No: ")

if A == "Yes":
    print("Which playlist?")
elif A == "No":
    exit()

playlist = input("Happy, Sad, Angry or Chilled: ")
os.system("cls")

while True:
    if playlist == "Happy":
        song = input(f"what is you happy songs, {name},: ")
        Artist = input(f"Who is the Artist?: ")
        file = open("h.txt", "a")
        file.writelines("\n" + song + ": " + Artist)
        file.close()

        choice = input("Enter another? Yes or No: ")
        if choice == "No":
            break

    elif playlist == "Sad":
        song = input(f"What is your sad song, {name}: ")
        Artist = input(f"Who is the Artist?: ")
        file =open("s.txt", "a")
        file.writelines("\n" + song + ": " + Artist)
        file.close()

        choice = input("Enter another? Yes or No: ")
        if choice == "No":
            break

    elif playlist == "Angry":
        song = input(f"What is your sad Angry songs? {name},: ")
        Artist = input(f"Who is the Artist?: ")
        file =open("m.txt", "a")
        file.writelines("\n" + song + ": " + Artist)
        file.close()

        choice = input("Enter another? Yes or No: ")
        if choice == "No":
            break

    elif playlist == "Chilled":
        song = input(f"What is your chilling out songs? {name},: ")
        Artist = input(f"Who is the Artist?: ")
        file =open("c.txt", "a")
        file.writelines("\n" + song + ": " + Artist)
        file.close()

        choice = input("Enter another? Yes or No: ")
        if choice == "No":
            break


print("Add your songs to their respected playlists from text file into youtube.")
url = "youtube.com"
webbrowser.open(url)