import time
import random


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




def strrev():
  print ("Hello! This is a sentence/Word reverser!")
  time.sleep (1)
  word = input("what do you want me to reverse?:")
  peice = (word)[::-1]
  print (f"here is it reversed: {peice}")

    
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
    print ("Press '4' to go back to main menu.")
    time.sleep (.5)
    ml = int(input("->"))
    time.sleep (1)
    if ml == 4:
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
        ad3 = ("Adjective:")
        time.sleep (1)
        as1 = ("Wierd Name:")
        time.sleep (1)
        vi3 = ("verb-(ing):")
        time.sleep (1)
        pn2 = ("Plural Noun:")
        time.sleep (1)
        c2 = input("Color:")
        time.sleep (1)
        wn = ("2nd Wierd Name:")
        time.sleep (1)
        g = ("Gibberish:")
        time.sleep (1)
        nu3 = ("Number:")
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




