import time
import random
import money


def bol():
  print("Hello! This is the *Magic 8ball*!!!")
  time.sleep(1.5)
  print("Just ask me a question and I'll respond with how likely is is to happen!")
  time.sleep(2)
  while True:
    input("What is your question?: ")
    time.sleep(1)
    print (random.choice(["No.","Maybe.","Definetly not.","Without a doubt.","You may rely on it.","It is certain.","It is decidedly so.","Without a doubt.","Yes, definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]))
    time.sleep(1)
    print("Thank you for using the *Magic 8ball*!")
    time.sleep(1)
    bob = input("Would you like to ask another question? (Type 'Yes' or 'No'): ").lower()
    if bob == "yes":
      print("Ok!")
      time.sleep(1)
    else: 
      print("Ok!")
      break
  time.sleep(1)
  print("Sending you back to main...")


def nc():
  x = input("what number do you want me to change?")
  maximum = input("what is the maximum amount I can change it by?")
  y = int(x)
  z = (random.randint(1,int(maximum)))
  signs = ["+", "-"]
  sign = (random.choice(signs))
  if sign == "+" :
    newx = y + z
  elif sign == "-":
    newx = y - z
  time.sleep (2)
  print (f"here is your changed number:{newx}")
  time.sleep (2.5)
  print (f"here is the amount by which I changed your number: {z}")
  time.sleep(1)
  print("Sending you back to main...")




def strrev():
  print ("Hello! This is a Sentence/Word reverser!")
  time.sleep (1)
  while True:
    word = input("what do you want me to reverse?:")
    peice = (word)[::-1]
    print (f"here is it reversed: {peice}")
    time.sleep(1)
    while True:
      x = input("Would you like to do another one?: ").lower()
      time.sleep(1)
      if x[0] == "y":
        print("Ok!")
        break
        time.sleep(1)
      elif x[0] == "n":
        print("")
        print("Ok!")
        time.sleep(1)
        break
      else:
        print("Sorry, I could do not understand. Please try again.")
        time.sleep(1)
    if x[0] == "n":
      break
    else:
      pass
  time.sleep(1)
  print("Sending you back to main...")

    
def slg():
  print("Hello! This is a Random Story Line Generator!")
  time.sleep(1)
  while True:
    print("Generating Story Line...")
    time.sleep(1)
    print("")
    when = random.choice(["A few years ago","A long time ago","Once upon a time","Yesterday","Last night","In the morning","Last month","One day in the 1900's"])
    who = random.choice(["an Old Man","a Rabbit","an Elephant","an Old Lady","a Child","a Snake","a Mouse","a Moose","a Funny Kid","a Duck"])
    name = random.choice(["George","Eve","Ava","John","Josh","Bob","Steve","Mary","Andrew","Charles","Eric","Macey","Jack","Jasckson","Mike","Mia","Eliana","Lucas","Skyler","Zoe","Judy","Olivia","Jasmine","Leo","Alessia","Noah"])
    place = random.choice(["India","New York","New York City","California","Florida","Orlando","Chicago","LA","Tokyo","China","Russia","Egypt"])
    place2 = random.choice(["the movies","a friends house","School","a Pizza Place","a trampoline park","Disneyland","a haunted house","the park"])
    happened = random.choice(["wrote a book.","found a secret key.","fought a dragon.","made a LOT of friends.","became a celebrity.","won a dream vacation.","won the lottery.","peed themselves.","jumped in a nearby pool."])
    print (when + ", " + who + " who's name was " + name + ", " + "lived in " + place + "." + " Then " + name + " went to " + place2 + " and unexpectedly " + happened)
    print(" ")
    time.sleep(5)
    while True:
      x = input("Would you like to have another one?: ").lower()
      time.sleep(1)
      if x[0] == "y":
        print("Ok!")
        break
        time.sleep(1)
      elif x[0] == "n":
        print("")
        print("Ok! Thanks for using the Random Story Line Generator")
        time.sleep(1)
        break
      else:
        print("Sorry, I could do not understand. Please try again.")
        time.sleep(1)
    if x[0] == "n":
      break
    else:
      pass
  time.sleep(1)
  print("Sending you back to main...")




def ml():
  print ("Welcome to Madlibs!")
  time.sleep (1)
  while True:
    #Madlib Options
    print ("Press '1' For A 'cat' madlib.")
    time.sleep (.5)
    print ("Press '2' for a 'dog' madlib.")
    time.sleep (.5)
    print ("Press '3' if you want a 'baby yoda' madlib.")
    time.sleep (.5)
    print ("Press '4' for a beach madlib!")
    time.sleep(.5)
    print ("Press '5' to go back to main menu.")
    time.sleep (.5)
    ml = int(input("->"))
    time.sleep (1)
    if ml == 5:
      print("Ok! Sending you back to main . . . ")
      break
      time.sleep (1)
    else:
      print ("Ok! Let's Start!")
      time.sleep (1)
      if ml == 1:
        vi = input("verb-(ing):")
        time.sleep (1)
        ad1 = input("adjective:")
        time.sleep (1)
        pn = input("Plural Noun:")
        time.sleep (1)
        nu = input("Number:")
        time.sleep (1)
        v1 = input("verb:")
        time.sleep (1)
        pn2 = input ("2nd Plural Noun: ")
        time.sleep (1)
        nu2 = input ("2nd Number: ")
        time.sleep(1)
        td = input("Type Of Dinosuar:")
        time.sleep (1)
        b = input("Type of Bug:")
        time.sleep (1)
        ad2 = input("2nd Adjective:")
        time.sleep (1)
        c = input ("Color:")
        time.sleep (1)
        ffr = input("Fast Food Restaurant: ")
        time.sleep (1)
        print ("Creating Madlib . . . ")
        time.sleep (2)
        print ("Initializing Madlib . . .")
        time.sleep (2)
        print (" -- Cat Breeds -- ")
        time.sleep (1)
        print (f"Have you ever heard of a {vi} cat? Well now you have! These little guys are {ad1}, and strong! They can climb {pn} up to {nu} feet high, and can {v1} over {pn2} at {nu2} miles per hour! They eat {td} eggs for breakfast, and love slurping {b} juice. They're {ad2}, too. You won't find them here, though. They live deep within the {c} jungles of {ffr} island.")
        time.sleep (10)
        print ("Sending You back to the Madlibs Options . . .")
        time.sleep (2)
      elif ml == 2:
        fm = input("Family Member:")
        time.sleep (1)
        t = input("Teacher:")
        time.sleep (1)
        n1 = input("Noun:")
        time.sleep (1)
        cl = input("Clothing:")
        time.sleep (1)
        d = input("Drink:")
        time.sleep (1)
        s = input("Sport:")
        time.sleep (1)
        vi2 = input("Verb-(ing):")
        time.sleep (1)
        f = input("Food:")
        time.sleep (1)
        n2 = input("2nd Noun:")
        time.sleep (1)
        print ("Creating Madlib . . . ")
        time.sleep (2)
        print ("Initializing Madlib . . .")
        time.sleep (2)
        print("-- All about Dogs! -- ")
        time.sleep (1)
        print(f"Dogs are Incredible. Dogs can be your best friend, your {fm}, your {t}, and a million other things! They love to wag their {n1}, and eat your {cl}, and drink up all the {d}. They can be great at {s}, too. In fact, your dog is probably better than you at {vi2}, and slam-dunking {f}! Be sure your dog get plenty of water, pets, and {n2}!")
        time.sleep (8)
        print ("Sending you back to the Madlibs Options . . .")
        time.sleep (2)
      elif ml == 3:
        mn = input("Made-up Name:")
        time.sleep (1)
        ad3 = input("Adjective:")
        time.sleep (1)
        as1 = input("Wierd Name:")
        time.sleep (1)
        vi3 = input("verb-(ing):")
        time.sleep (1)
        pn2 = input("Plural Noun:")
        time.sleep (1)
        c2 = input("Color:")
        time.sleep (1)
        wn = input("2nd Wierd Name:")
        time.sleep (1)
        g = input("Gibberish:")
        time.sleep (1)
        nu3 = input("Number:")
        time.sleep (1)
        v = input("Verb:")
        time.sleep (1)
        o = input("Object(s):")
        time.sleep (1)
        nu4 = input("Second number:")
        time.sleep (1)
        pr = input("Profession:")
        time.sleep (1)
        en = input("Evil name:")
        time.sleep (1)
        print ("Creating Madlib . . . ")
        time.sleep (2)
        print ("Initializing Madlib . . .")
        time.sleep (2)
        print (" -- Baby Yoda -- ")
        time.sleep (1.6)
        print (f"A long time ago, in a galaxy far far away called the {mn} Galaxy, a {ad3} child was born. His Origins are mysterious, but after you read this, you'll know all the secrets! He's actually from the {as1} species of alien who are famously good at {vi3} {pn2} with their mind. The most famous {as1} was a small {c2} one named {wn}, who was the leader of the {g} Order for a very long time. In fact, they can live up to {nu3} years old! I bet you didn't know they like to {v} {o}! Even though Baby Yoda is {nu4} years old, he is still considered a child, so it's a good thing he met a mandalorian {pr}. Together, they've visited tons of planets, And even escaped the evil Imperial Officer {en}.")
        time.sleep (10)
        print ("Sending You back to Madlibs Options ... ")
        time.sleep (2)
      elif ml == 4:
        ad4 = input("Adjective:")
        time.sleep (1)
        n3 = input("Noun:")
        time.sleep (1)
        n4 = input("2nd Noun:")
        time.sleep (1)
        n5 = input("3rd Noun:")
        time.sleep (1)
        n6 = input("4th Noun:")
        time.sleep (1)
        v2 = input("Verb:")
        time.sleep (1)
        edn = input("Edible Noun:")
        time.sleep (1)
        edn2 = input("2nd Edible Noun:")
        time.sleep (1)
        d2 = input("Drink:")
        time.sleep (1)
        v3 = input ("2nd Verb:")
        time.sleep (1)
        pn3 = input("Plural Noun:")
        time.sleep (1)
        print ("Creating Madlib . . . ")
        time.sleep (2)
        print ("Initializing Madlib . . .")
        time.sleep (2)
        print(" -- A Trip to the Beach! -- ")
        time.sleep (1.6)
        print(f"Summer trips to the beach are so {ad4}! Pack your {n3}, a {n4} to dry yourself off, and {n5} to prevent sunburns. Be sure to bring a {n6} to {v2} with in the water. You can bring a beach picnic, with {edn}, {edn2}, and {d2} to drink. It's fun to {v3} for hours in the water, and to see {pn3} sail across in the distance.")
        time.sleep (9)
        print ("Sending you back to the Mad-Libs options ... ")
        time.sleep (2)
  time.sleep(1)
  print("Sending you back to main...")

    






def fight():
  bh = 100
  mh = 100

  print("Hello! This is 'Fight'!")
  time.sleep(2)
  print("The object of the game is to defeat the Bot!")
  time.sleep(2)
  print("You both start with 100 health and whoever reaches 0 health first loses!")
  time.sleep(2)
  print("Ready!")
  time.sleep(1)
  print("Set!")
  time.sleep(1)
  print("Fight!")

  while True:

    punch_m = int(random.choice(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]))

    heal_m = int(random.choice(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]))

    kick_m = int(random.choice(["10","11","12","13","14","15","16","17","18","19","20","50","51","52","53","54","55","56"]))

    time.sleep(1)
    print("Your turn!")
    while True:
      time.sleep(1)
      x = input("Would you like to 'Punch', 'Kick' or 'Heal up'?: ").lower()
      time.sleep(1)
      if x[0] == "p":
        print("You chose to Punch the Bot! The Bot lost",punch_m, "health")
        bh = bh - punch_m
        break
      elif x[0] == "h":
        print("You chose to Heal up! You healed",heal_m,"health")
        mh = mh + heal_m
        break
      elif x[0] == "k":
        print("You chose to Kick! The Bot lost",kick_m,"health")     
        bh = bh - kick_m
        break
      else:
        print("Sorry, I did not understand. Please try again.")

    time.sleep(2)

    if mh <= 0:
      print("Sorry, you Lost. The Bot wins!")
      time.sleep(2)
      print("Thanks for playing!")
      time.sleep(1)
      str(money.add_money(50))
      print("+50 neows was added to your wallet! (Money for winning)")
      time.sleep(1)
      break
    else:
      pass

    if bh <= 0:
      print("The Bot Lost! You win!")
      time.sleep(2)
      print("Thanks for playing!")
      time.sleep(1)
      str(money.add_money(250))
      print("+250 neows was added to your wallet! (Money for winning)")
      time.sleep(1)
      break
    else:
      pass

    punch_b = int(random.choice(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]))

    heal_b = int(random.choice(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]))

    kick_b = int(random.choice(["10","11","12","13","14","15","16","17","18","19","20","50","51","52","53","54","55","56"]))

    time.sleep(3)
    print("Bots turn!")
    time.sleep(1)
    choice = random.choice(["p","h","k"])
    if choice == "p":
      print("The Bot chose to Punch You! You lost",punch_b, "health")
      mh = mh - punch_b
    elif choice == "h":
      print("The Bot chose to Heal up! The Bot Healed",heal_b,"health")
      bh = bh + heal_b
    elif choice == "k":
      print("The Bot chose to Kick! You lost",kick_b,"health")     
      mh = mh - kick_b
      break
    else:
      pass

    time.sleep(3)
    print("")
    print ("Stats:")
    time.sleep(1)
    print("You:", mh, "health left")
    print("Bot:", bh, "health left")
    time.sleep(3)
    print("")

    if mh <= 0:
      print("Sorry, you Lost. The Bot wins!")
      time.sleep(2)
      print("Thanks for playing!")
      time.sleep(1)
      str(money.add_money(50))
      print("+50 neows was added to your wallet! (Money for winning)")
      time.sleep(1)
      break
    else:
      pass

    if bh <= 0:
      print("The Bot Lost! You win!")
      time.sleep(2)
      print("Thanks for playing!")
      time.sleep(1)
      str(money.add_money(250))
      print("+250 neows was added to your wallet! (Money for winning)")
      time.sleep(1)
      break
    else:
      pass
  time.sleep(1)
  print("Sending you back to main...")