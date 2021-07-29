import time
import random



def pmcc():
  print("kilograms:1, pounds:2, grams:3 ounces:4")
  unit1 = input("what is the unit your value is in?:")
  print()
  invert = input("what is the value that you want to convert?:")
  print()
  unit2 = input("what is the unit you want to convert it to?:")
  print()
  if int(unit1) > 4:
    print ("why must you do this, choose something valid")
  else:
    if int(unit2) > 4:
      print ("stop it. not funny. use a valid number")
    else:
      while True:
        if int(unit1) == 2:
          if int(unit2) == 1:
            exvert = int(invert) * 0.45359237
            break
          else: 
            if int(unit2) == 3:
              exvert = int(invert) * 453.59237
              break
            else:
              if int(unit2) == 2:
                exvert = int(invert) * 1
                print("warning: unit1 = unit2")
                break
              else:
                if int(unit2) == 4:
                  exvert = int(invert) * 16
                  break
                else:
                  print ("internal error")
                  break
        else: 
          if int(unit1) == 1:
            if int(unit2) == 2:
              exvert = int(invert) * 2.2046226218488298442
              break
            else:
              if int(unit2) == 3:
                exvert = int(invert) * 1000
                break
              else:
                  if int(unit2) == 1:
                    exvert = int(invert) * 1
                    print("warning: unit1 = unit2")
                    break
                  else:
                    if int(unit2) == 4:
                      exvert = int(invert) * 35.2739619495871
                      break
                    else:
                      print ("internal error")
                      break
          else:
            if int(unit1) == 3:
              if int(unit2) == 1:
                exvert = int(invert) / 1000
                break
              else:
                  if int(unit2) == 2:
                    exvert = int(invert) * 0.002204622622
                    break
                  else:
                    if int(unit2) == 3:
                      exvert = int(invert) * 1
                      print("warning: unit1 = unit2")
                      break
                    else:
                      if int(unit2) == 4:
                        exvert = int(invert) * 0.03527396194
            else:
              if int(unit1) == 4:
                if int(unit2) == 1:
                  exvert = int(invert) * 0.028349523125
                  break
                else:
                  if int(unit2) == 2:
                    exvert = int(invert) / 16
                    break
                  else:
                    if int(unit2) == 3:
                      exvert = int(invert) * 28.349523125
                      break
                    else:
                      if int(unit2) == 4:
                        exvert = int(invert)
                        print ("warning - unit1 = unit2") 
                        break
                      else:
                        print ("internal error")
                        break
              else:
                print ("internal error")    
      print (f"here is your converted value:{exvert}")







def mimc():
  print ("I will take a certain number of values from you.")
  time.sleep (2)
  print ("I will then calculate the average of these values and tell you.")
  time.sleep (1)
  q = input("are you ready?: ")
  time.sleep (1.5)
  print ("Good. Whatever you just said was saved for future use")
  time.sleep (1)
  x = input("How many values are you going to give me?: ")
  values = []
  for item in range(int(x)):
    value = input("what is your value?:")
    values.append(value)
    time.sleep (0.5)
  print ("please wait as I find your average.")
  time.sleep (3)
  y = len(values)
  sume = 0
  for item in range(y):
    sume = sume + float(values[item])
  finale = sume / y
  print ("here is your calculated average:")
  time.sleep (1)
  print (finale) 
  time.sleep (6)
  phrases = ["lol", "it is then", "lol bruh", "why u bully me", "get some help", "it is the chosen one", "anywho i don't care","why should I care lol", "this is great", "no u", "r u dum"]
  choice = (random.choice(phrases))
  print (f"{q} {choice}")









def calc():
  print("Ayooo! This is a Caluculater!")
  time.sleep(1)
  print("Type what you would like to do!")
  time.sleep(1)
  print("Type 1: Add")
  time.sleep(.5)
  print("Type 2: Subtract")
  time.sleep(.5)
  print("Type 3: Divide")
  time.sleep(.5)
  print("Type 4: Multiply")
  time.sleep(1)
  x = int(input("Your choice: "))
  div = 0
  mul = 0
  sub = 0
  add = 0
  if x == 1:
    y = int(input("How many values would you like to add?: "))
    time.sleep(.5)
    for a in range(y):
      b = int(input("Value: "))
      time.sleep(.5)
      add = add + b
    print("Your total value is",add)
  elif x == 2:
    y = int(input("How many values would you like to subtract?: "))
    time.sleep(.5)
    r = input("Starting value: ")
    time.sleep(.5)
    sub = r
    for a in range(y-1):
      b = int(input("Value: "))
      time.sleep(.5)
      sub = sub - b
    print("Your total value is",sub)
  elif x == 4:
    y = int(input("How many values would you like to multiply?: "))
    time.sleep(.5)
    r = int(input("Starting value: "))
    time.sleep(.5)
    mul = r
    for a in range(y-1):
      b = int(input("Value: "))
      time.sleep(.5)
      mul = mul * b
    print("Your total value is",mul)
  elif x == 3:
    y = int(input("How many values would you like to divide?: "))
    time.sleep(.5)
    r = int(input("Starting value: "))
    time.sleep(.5)
    div = r
    for a in range(y-1):
      b = int(input("Value: "))
      time.sleep(.5)
      div = div//b
    print("Your total value is",div)
  else:
    print("error...")










def pal():
  print("Hello! this is a Palindrome checker!")
  for y in range(1000000):
    x = input("What should I check?: ")
    y = len(x)
    z = []
    a = []
    b = len(x)
    time.sleep(1)
    for i in range(y-1,-1,-1):
      z.append((x[i]))
    for o in range(b):
      a.append((x[o]))
    print ("checking...")
    time.sleep(1)
    if z == a:
      print("This is a palindrome!")
    else:
      print("Nope this is not a palindrome!")
    g = input("Would you like to check another one? ('Yes' or 'No'): ")
    if g == "yes" or g == "Yes":
      print("Ok!")
      time.sleep(1)
    else:
      print("Ok")
      break
  time.sleep (1)
  print("Sending you back to main...")
  time.sleep(1)







def tc():
  print("Hello! This is a calulater to help you convert fahrenheit to celsius!")
  time.sleep(1)
  print("Please enter the temperature you want to convert to celsius.")
  time.sleep(1)
  a = int (input ("Degrees in fahrenheit: "))
  print ("calculating...")
  time.sleep(1)
  b = (a - 32) * 5//9
  print (b,"degrees celsius")






def strrev():
  print ("Hello! This is a sentence/Word reverser!")
  time.sleep (1)
  word = input("what do you want me to reverse?:")
  peice = (word)[::-1]
  print (f"here is it reversed: {peice}")

    



def slc():
  x = input("what sentence/word do you want me to count?: ")
  y = len(x)
  print (f"There are {y} characters in this phrase.")


