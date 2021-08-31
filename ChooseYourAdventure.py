print("Welcome to the Choose Your Own Adventure Game. Let's begin")
# make sure to convert all string to lower afterwards so "Yes/No" doesn't cause issues #
question_1 = input("You come across a fork in your path. Do you go left or right? ").lower()

if question_1 == "left":
    question_lake = input("You go left. You come across a river. How do you cross - do you use a bridge or a horse? ")
    if question_lake.lower() == "bridge":
        fox = input("You crossed successfully. After the bridge is an injured fox. Do you help it? (yes/no) ").lower()
        if fox.lower() == "yes":
            print("The fox tricked you and bit off your arm. Game Over :/")
        else:
            donkey = input("You cautiously avoided the fox. But you're legs are getting tired. There's a donkey nearby,"
                  "should you try to ride it? (yes/no) ").lower()
            if donkey == "yes":
                princess = input("You were able to ride the donkey and save you're energy. "
                                 "You come across a distressed princess. Do you help her? (yes/no) ").lower()
                if princess == "yes":
                    print("You're kind gesture impressed her. She takes you to her castle and gifts you a treasure "
                          "chest of gold. You win!")
                else:
                    print("Out of spite, the princess kills you for not helping her. Game Over :/")
            else:
                print("You got so tired from walking that you slipped and fell into a ravine. Game Over :/ ")
    else:
        print("You and your horse drowned in the river. Game Over :/")

else:
    question_wizard = input("You go right. A wizard offers you some magic beans. Do you take them? (yes/no) ").lower()
    if question_wizard == "yes":
        fly = input("The beans gave you the power to fly. You see a flock of birds, do you fly with them? (yes/no) ").lower()
        if fly == "yes":
            dinner = input("The birds take you to their hideout and invite you for dinner. "
                           "Do you accept the offer? (yes/no) ").lower()
            if dinner == "yes":
                print("The birds have tricked you into joining them. They cook you for dinner. Game Over :(")
        else:
            castle = input("You decline the offer and fly away. You see a castle nearby. Do you go and explore it?"
                               "(yes/no) ").lower()
            if castle == "yes":
                knight = input("You arrive at the castle and are confronted by a fleet of knights. Do you "
                            "surrender or attack?").lower()
                if knight == "surrender":
                    print("You surrender and are taken hostage. Game Over :(")
                else:
                    print("You try to fight the knights but there are too many. You are killed. Game Over :(")
            else:
                dragon = input("You choose to avoid the castle. While flying, you find a dragon. "
                                   "Do you try to befriend it? (yes/no) ").lower()
                if dragon == "yes":
                    print("You successfully befriend the dragon. The two of you end up taking over the world."
                              "You win! :D")
                else:
                    print("The dragon sees you avoid it and gets angry. It kills you with its fire breath. "
                              "Game Over :/")

    else:
        fairies = input("You declined the beans and continue on your journey. You come across some fairies that need "
                        "your help. Do you help them? (yes/no) ").lower()
        if fairies == "yes":
                print("The fairies stole your belongings. Game Over :(")
        else:
            forest = input("You continue into a forest, but you're starving. There's bushes full of berries, "
                           "do you eat them? (yes/no) ").lower()
            if forest == "no":
                print("You died of hunger. Game Over :(")
            else:
                dog = input("The berries are delicious. As you continue, you see a dog nearby. Do you befriend it?"
                          " (yes/no) ").lower()
                if dog == "yes":
                    box = input("You successfully befriend the dog. You come across a mysterious box. "
                            "Do you open it? (yes/no) ").lower()
                    if box == "yes":
                        print("Congrats! You have discovered a pile of gold. You win!")
                    else:
                        print("Why didn't you open it?! The box contained a box of gold. You lose")
                else:
                    print("The dog becomes agitated that you did not befriend it. "
                          "It attacks you and you die. Game Over :(")