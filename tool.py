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
  print("Ayooo! This is a Calculator!")
  time.sleep(1)
  while True:
    print("Type what you would like to do!")
    time.sleep(1)
    print("Type '1': Add")
    time.sleep(.5)
    print("Type '2': Subtract")
    time.sleep(.5)
    print("Type '3': Divide")
    time.sleep(.5)
    print("Type '4': Multiply")
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
    time.sleep(1)
    jk = input("Would like to do another calculation? (Type 'Yes' or 'No'): ").lower()
    time.sleep(1)
    if jk == "yes":
      print("Ok!")
      time.sleep(1)
    else:
      print ("Ok!")
      time.sleep(1)
      break











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



def slc():
  x = input("what sentence/word do you want me to count?: ")
  y = len(x)
  print (f"There are {y} characters in this phrase.")




def ods():
  time.sleep (0.5)
  print ("Hello! This program detects outliers and tells you what it is.")
  time.sleep (1)
  x = input("How many values are in your range?: ")
  time.sleep (0.5)
  x = int(x)
  time.sleep (1)
  print ("Initializing ... ")
  time.sleep (2)
  print ("Thank You.")
  values = []
  time.sleep (1.5)
  for i in range(int(x)):
    y = input("What is your value?:")
    values.append(int(y))
    time.sleep (1)
  time.sleep (1)
  bob = sum(values)
  z = len(values)
  av = bob / z
  while True:
    if av < 10:
      detran = 4
      break
    elif av < 30:
      detran = 8
      break
    elif av < 50:
      detran = 12
      break
    elif av < 100:
      detran = 16
      break
    elif av < 250:
      detran = 25
      break
    elif av < 500:
      detran = 36
      break
    elif av < 1000:
      detran = 52
      break
    else:
      detran = 100
      break
  newx = (x-1)
  values.sort(reverse = False)
  time.sleep (1.5)
  if values[1] - values[0] > detran:
    if values[2] - values[1] > detran:
      if values[newx] - values[newx-1] > detran:
        if values[newx-1] - values[newx - 2] > detran:
          print ("OUTLIERS DETECTED!")
          time.sleep (1)
          print ("Here are the outliers:")
          print (values[0])
          time.sleep (0.5)
          print (values[1])
          time.sleep (0.5)
          print (values[newx])
          time.sleep (0.5)
          print (values[newx-1])
        else:
          print ("OUTLIERS DETECTED!")
          time.sleep (1)
          print ("Here are the outliers:")
          print (values[0])
          time.sleep (0.5)
          print (values[1])
          time.sleep (0.5)
          print (values[newx])
      else:
        print ("OUTLIERS DETECTED!")
        time.sleep (1)
        print ("Here are the outliers:")
        print (values[0])
        time.sleep (0.5)
        print (values[1])
    else:
      print ("OUTLIER DETECTED!")
      time.sleep (1)
      print ("Here is the outlier:")
      time.sleep(0.5)
      print (values[0])
  elif values[newx] - values[newx-1] > detran:
    if values[newx-1] - values[newx-2] > detran:
      if values[1] - values[0] > detran:
        if values[2] - values[1] > detran:
          print ("OUTLIERS DETECTED!")
          time.sleep (1)
          print ("Here are the outliers:")
          print (values[0])
          time.sleep (0.5)
          print (values[1])
          time.sleep (0.5)
          print (values[newx])
          time.sleep (0.5)
          print (values[newx-1])
        else:
          print ("OUTLIERS DETECTED!")
          time.sleep (1)
          print ("Here are the outliers:")
          time.sleep (0.5)
          print (values[0])
          time.sleep (0.5)
          print (values[newx])
          time.sleep (0.5)
          print (values[newx-1])
      else:
        print ("OUTLIERS DETECTED!")
        time.sleep (1)
        print ("Here are the outliers:")
        time.sleep (0.5)
        print (values[newx])
        time.sleep (0.5)
        print (values[newx-1])
    else:
      print ("OUTLIER DETECTED!")
      time.sleep (1)
      print ("Here is the outlier:")
      time.sleep (0.5)
      print (values[newx])
  elif values[2] - values[1] > detran:
    if values[newx-1] - values[newx-2] > detran:
      time.sleep (0.5)
      print ("OUTLIERS DETECTED!") 
      time.sleep (0.8)
      print ("Here are the outliers:")
      time.sleep (1)
      print (values[0])
      time.sleep (0.5)
      print (values[1])
      time.sleep (0.5)
      print (values[newx])
      time.sleep (0.5)
      print (values[newx-1])
    else:
      time.sleep (0.5)
      print ("OUTLIERS DETECTED!")
      time.sleep (1)
      print ("Here are the outliers:")
      time.sleep (1)
      print (values[0])
      time.sleep (0.5)
      print (values[1])
  elif values[newx-1] - values[newx-2] > detran:
    if values[2] - values[1] > detran:
      time.sleep (0.5)
      print ("OUTLIERS DETECTED!") 
      time.sleep (0.8)
      print ("Here are the outliers:")
      time.sleep (1)
      print (values[0])
      time.sleep (0.5)
      print (values[1])
      time.sleep (0.5)
      print (values[newx])
      time.sleep (0.5)
      print (values[newx-1])
    else:
      time.sleep (0.5)
      print ("OUTLIERS DETECTED!")
      time.sleep (1)
      print ("Here are the outliers:")
      time.sleep (1)
      print (values[newx])
      time.sleep (0.5)
      print (values[newx-1])
  else:
    print ("NO OUTLIERS DETECTED.")
    time.sleep (1)
    print (f"Low:{values[0]}")
    print (f"High:{values[newx]}")


def ranpass():
  h = ("")
  print("Hello! This is a Random password generator!")
  time.sleep(1)
  print ("The Password that it generates will have letters, numbers, and special characters!")
  time.sleep(2)
  x = int(input("How many characters would you like your password to be?: "))
  time.sleep(2)
  for d in range(x):
    y = random.choice(['A','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','C','V','B','N','M','a','q','w','e','r','t','y','u','i','o','p','s','d','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0',"!",'@','#','$','%','6','&','*'])
    h = (h + y)

  print("Here is your new password!:",h)
  time.sleep(2)
  print("Stay safe my friend!")
  time.sleep(1.5)
  print("Sending you back to main...")