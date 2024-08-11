import time

escape_the_mansion = input("You are now inside a mysterious, abandoned mansion, where darkness surrounds you on all sidesand strange sounds fill the air. No one knows how you got here, but you quickly realize that you must find a way out before something terrible happens. You must be cautious with every step you take, as danger lurks around every corner. Gather your courage and prepare to face the challenges that await you. Your survival depends on your wit and your ability to make the right decisions. Will you escape this mansion, or will the mystery consume you forever? \nto deal with this situation you gotta choose a way \n1-Look in the library\n2-hide in the closet\n3-try unlock the closed doors\nprint the number")

while True:
    if escape_the_mansion.lower() == "1":
        print("you find the map\nyou gotta find that gold")
        the_new_way =input("know you have to choose you're new way to cache you're tresor\n1-the best way ever seen\n2-dealing with the weird villigers\n3-the deasrt that gonna kill you slowly\nprint the number")
        while True:
            if the_new_way.lower() == "2":
                print("the oeon poped out you took a boat")
                time.sleep(3)
                print("every thing is black")
                time.sleep(3)
                print("I am dying")
                time.sleep(3)
                print("you see someone coming")
                time.sleep(3)
                print("wait it's you're old friend")
                time.sleep(3)
                print("It's 11am it's get up bro you were dreaming")
                time.sleep(3)
                print("you gotta restart")
                break
            elif the_new_way.lower() == "3":
                print("the oeon poped out you took a boat")
                time.sleep(3)
                print("every thing is black")
                time.sleep(3)
                print("I am dying")
                time.sleep(3)
                print("you see someone coming")
                time.sleep(3)
                print("wait it's you're old friend")
                time.sleep(3)
                print("It's 11am it's get up bro you were dreaming")
                time.sleep(3)
                print("you gotta restart")
                break
            elif the_new_way.lower() == "1" or "the best way ever seen" or "1-the best way ever seen":
                print("its a bush you really thought it's that easy")
                time.sleep(3)
                print("you gotta restart")
                break
            else:
                print("it does not work like that,restart")
                time.sleep(3)
                print("you gotta restart")
                break
    elif escape_the_mansion.lower() == "3" or "try unlock the doors" or "3-try unlock the doors":
        print("its closed")
        time.sleep(3)
        print("you gotta restart")
        break
    elif escape_the_mansion.lower() == "2" or "hide the closet" or "2-hide the closet":
        print("you are going to keep waiting")
        time.sleep(3)
        print("you gotta restart")
        break
    else:
        print("error")
        time.sleep(3)
        print("you gotta restart")
        break

                
            
