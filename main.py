wrongcounter = 0
import time
import tool
import games
import message

print("*Log in Screen*")

while True:
  att = int(input("What Is the Passcode? (4 Digit Passcode): "))
  if True:
    # Read passkey from the file


    file = open("sussy.txt", "r+")
    passkey = int((file.read()))

    if att == int(passkey):
      print ("ACCESS GRANTED")
      wrongcounter = 0
      while True:


#Main Menu
        print("")
        print ("--Main Menu--")
        time.sleep (0.5)
        print ("Press '1' to Log Out")
        time.sleep (.5)
        print ("Press '2' to Play Games")
        time.sleep (.5)
        print ("Press '3' to Change Passcode")
        time.sleep (.5)
        print ("Press '4' to Access Tools")
        time.sleep(.5)
        print("Press '5' to Check Messages")
        time.sleep(.5)
        print("Press '6' for Help")
        time.sleep (.5)
        main = int(input("-> "))
        print("")


#logging out

        
        if int(main) == 1:
          z = input("Are you sure? ('Yes' or 'No'): ").lower()
          if  z == "yes":
            print("Logging off...") 
            time.sleep(3)
            print("")
            print("*Log in Screen*")
            time.sleep (1)
            break 
          else:
            print ("Ok. Sending you to Main...")
            time.sleep(1)
          print("")


#changing passcode


        elif int(main) == 3:
          x = input("Are you sure you change the passcode? 'Yes' or 'No': ").lower()
          if  x == "yes":
            passcheck = int(input("Enter Old Passcode: "))
            time.sleep (1)
            print ("Checking ...")
            time.sleep (2)
            if passcheck == passkey:
              print ("Passcode Validated.")
              time.sleep (1.2)
              newpass = input("Enter New Passcode (Has to be 4 Digits): ")
              time.sleep (0.8)
              print ("Running New Passcode ...")
              file.seek(0)
              file.write(newpass)
              time.sleep (2.5)
              print ("Thank You. Password set.")
              time.sleep (1)
            else:
              print("INVALID PASSCODE. ACCOUNT LOCKED.")
              break
          elif x == "No" or x == "no":
            print ("Ok. Sending you back to Main...")
            time.sleep (2)

#games


        elif int(main) == 2:
          print ("--GAMES MENU--")
          time.sleep (.5)
          print ("Type '1' if you want to go back to the Main Menu")
          time.sleep(0.5)
          print ("Type '2' if you want to play Rock Paper Scissors!(Dhaya's Version)")
          time.sleep (.5)
          print ("Type '3' if you want to play Guess the Number!")
          time.sleep(.5)
          print("Type '4' if you want to play Hangman!")
          time.sleep(.5)
          print("Type '5' if you want to play Dice Rolling Simulater!")
          time.sleep(.5)
          print("Type '6' if You want to play TicTacToe!")
          time.sleep(.5)
          print("Type '7' if you want to play Rock Paper Scissors! (Saarth's Version)")
          time.sleep (.5)
          print("Type '8' if you want to use a Custom Number Changer!")
          time.sleep(.5)
          print("Type '9' if you want to play with the Magic 8ball.")
          time.sleep(.5)
          print ("Type '10' if you want to play BlackJack.")
          time.sleep (.6)
          choice = int(input("-> ")) 
          print("")


#actual game codes


          if int(choice) == 1:
            print("Ok, sending you back to main...")
            time.sleep (1.6)
          
          elif int(choice) == 2:
            games.rpsdhaya()
            time.sleep(.5)
            
          elif int(choice) == 3:
            games.g()
            time.sleep(1)

          elif int(choice) == 4:
            games.hm()
            time.sleep(1)

          elif int(choice) == 5:
            games.dice()
            time.sleep(1)

          elif int(choice) == 6:
            games.ttt()
            time.sleep(1)

          elif int(choice) == 7:
            games.rpssaarth()
            time.sleep(1)
          
          elif int(choice) == 8:
            games.nc()
            time.sleep(1)

          elif int(choice) == 9:
            games.bol()
            time.sleep(1)

          elif int(choice) == 10:
            games.bj()
            time.sleep(1)


          
  #Tools Menu



        elif int(main) == 4:
          time.sleep (1)
          print ("--TOOLS MENU--")
          time.sleep (.5)
          print ("Press '1' if you want to go back to Main Menu.")
          time.sleep (0.5)
          print ("Press '2' if you want to use a Calculator.")
          time.sleep (.5)
          print ("Press '3' If you want to use a Mass Converter.")
          time.sleep (.5)
          print ("Press '4' If you want to use a Palindrome Checker.")
          time.sleep (.5)
          print ("Press '5' If you want to use a Sentence/Word Reverser.")
          time.sleep (.5)
          print ("Press '6' If you want to use a MultiInput Average Calculator.")
          time.sleep(.5)
          print("Press '7' If you want to use a Tempurature Converter")
          time.sleep (.5)
          print ("Press '8' if You want to use a Sentence Character Counter.")
          time.sleep (.5)
          print ("Press '9' If you want to use an Outlier Detection System.")
          time.sleep (.5)
          print("Press '10' to use a Random Password Generator")
          time.sleep(.5)
          gangsta = int(input("-> "))
          time.sleep (0.9)
          print("")


#tools function code

          if gangsta == 1:
            print ("Ok. Sending you back to main...")
            time.sleep (1.6)
          elif gangsta == 2:
            tool.calc()
            time.sleep(2)
          elif gangsta == 3:
            tool.pmcc()
            time.sleep (2)
          elif gangsta == 4:
            tool.pal()
            time.sleep (2)
          elif gangsta == 5:
            tool.strrev()
            time.sleep (2)
          elif gangsta == 6:
            tool.mimc()
            time.sleep (2)
          elif gangsta == 7:
            tool.tc()
            time.sleep (2)
          elif gangsta == 8:
            tool.slc()
            time.sleep (2)
          elif gangsta == 9:
            tool.ods()
            time.sleep (2)
          elif gangsta == 10:
            tool.ranpass()
            time.sleep(2)
          



#messages


        elif main == 5:
          time.sleep(1)
          print("--MESSAGES--")
          time.sleep(1)
          print ("Type '1' to return back to main menu.")
          time.sleep(0.5)
          print("Type '2' to be messaged Insults")
          time.sleep(0.5)
          print("Type '3' to be messaged Inspirational quotes")
          time.sleep(0.5)
          print("Type '4' to be messaged Advice")
          time.sleep(0.5)
          print("Type '5' to be messaged things to make you Feel Better")
          time.sleep(0.5)
          print("Type '6' to be messaged Fun Facts")
          time.sleep(1)
          bruh = int(input("-> "))
          time.sleep(1)
          print("")


        
 #Messages Functions


          if bruh == 1:
            time.sleep (1)
            print ("Ok. Sending You back to main ... ")

          elif bruh == 2:
            message.insult()
            time.sleep(1)
            print("Sending you back to main...")
            time.sleep(1.5)

          elif bruh == 3:
            message.inspo()
            time.sleep(1)
            print("Sending you back to main...")
            time.sleep(1.5)

          elif bruh == 4:
            message.advice()
            time.sleep(1)
            print("Sending you back to main...")
            time.sleep(1.5)

          elif bruh == 5:
            message.feelbetter()
            time.sleep(1)
            print("Sending you back to main...")
            time.sleep(1.5)

          elif bruh == 6:
            message.fact()
            time.sleep(1)
            print("Sending you back to main...")
            time.sleep(1.5)

  

#Help menu


        elif int(main) == 6:
          time.sleep (1)
          print ("-- HELP MENU --")
          time.sleep (.6)
          print ("Press '1' to Return to main menu.")
          time.sleep (.6)
          print ("Press '2' to learn how to navigate the program.")
          time.sleep (.6)
          print ("Press '3' to learn what you can do in this program.")
          time.sleep (.6)
          print ("Press '4' for Credits")
          time.sleep (.6)
          verdict = int(input("->"))
          print("")

#Help menu conditions(:)


          if verdict == 1:
            time.sleep (1)
            print ("Ok. Sending you back to main ... ")
            time.sleep (2)

          elif verdict == 2:
            time.sleep (1)
            print ("To Navigate this program, you have to type the number corresponding to the place you want to go to when the prompt '->' appears. Then press enter, and you will arrive at your destination, and so on. ")
            time.sleep(8)
            print ("Returning to Main Menu ...")
            time.sleep (1.6)
          elif verdict == 3:
            time.sleep (1)
            print ("This is a program that consists of many products.")
            time.sleep (2.5)
            print ("The tools menu consists of a variety of tools that could help you such as a calculator, a average calculator, many converters, etc. To find out more, Go back to main menu and go to the 'tools' option. ")
            time.sleep (6)
            print ("The Games menu encompasses a wide variety of games, with more to be added in the future. Some of these include, but are not limited to, Rock Paper Scissors, Hangman, And guess the number, well as  To find out more, Go back to main menu and go to the 'games' option.")
            time.sleep (7)
            print ("The Messages menu is where you can ask an AI bot to message you a random quote/insult/advice in a messaging format. To try this, Go back to main menu and go to the 'messages' option.")
            time.sleep (4.5)
            print ("You can change the passcode by going to the 'change passcode' feature in main menu. You need the old passcode for authorization and the code must be a 4-digit number.")
            time.sleep (4)
            print ("To log out, go back to the main menu and use the log-out option. It will send you back to the login screen.")
            time.sleep (3)
            print ("I am now sending you back to main menu ... ")
            time.sleep (2)
          elif verdict == 4:
            print("The program was made by Dhayashree Ravi and Saarth Desai in 2021")
            time.sleep(3)
            print("We are both 12 years old and made this program for fun!")
            time.sleep(3)
            print ("I am now sending you back to Main Menu ... ")
            time.sleep (2)



#access denied code


    else: 
      wrongcounter = wrongcounter + 1
      if wrongcounter == 3:
        print ("CODE INVALID. ACCESS DENIED, ACCOUNT LOCKED.")
        break
      else:
        print ("CODE INVALID. ACCESS DENIED")
else: 
  print ("internal error")



#The end
