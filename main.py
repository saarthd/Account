wrongcounter = 0
import time
import tool
import games
import message
import fun
import money
import random

class spectrum:
  red = ("\033[91m")
  yellow = ("\033[93m")
  green = ("\033[92m")
  blue = ("\033[94m")
  cyan = ("\033[96m")
  magenta = ("\033[95m")
  black = ("\033[90m")
  white = ("\033[97m")
  

print(spectrum.white + "*Log in Screen*")

while True:
  att = str(input(spectrum.white + "What Is the Password?: "))
  if True:

    # Read passkey from the file

    file = open("sussy.txt", "r+")
    passkey = str((file.read()))

    if att == passkey:
      print (spectrum.green + "ACCESS GRANTED")
      time.sleep(1)
      mono = random.choice([5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,15,15,20])
      str(money.add_money(mono))
      print("+",mono,"neows was added to your wallet! (login money)")
      time.sleep(1)
      wrongcounter = 0
      while True:


#Main Menu
        print("")
        print (spectrum.cyan + "--Main Menu--")
        time.sleep (0.5)
        print ("Press '1' to Log Out")
        time.sleep (.5)
        print ("Press '2' to Play Games")
        time.sleep (.5)
        print ("Press '3' to Change Password")
        time.sleep (.5)
        print ("Press '4' to the 'Fun' Menu ")
        time.sleep (.5)
        print ("Press '5' to Access Tools")
        time.sleep(.5)
        print("Press '6' to Check Messages")
        time.sleep(.5)
        print("Press '7' for Help")
        time.sleep (.5)
        main = str(input("-> "))
        print("")


#logging out

        
        if main == 1:
          while True:
            z = input(spectrum.red + "Are you sure?: ").lower()
            if  z[0] == "y":
              print(spectrum.white + "Logging off...") 
              time.sleep(3)
              print("")
              print(spectrum.white + "*Log in Screen*")
              time.sleep (1)
              break 
            elif z[0] == "n":
              print (spectrum.white + "Ok. Sending you to Main...")
              time.sleep(1)
              break
            else:
              print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
              time.sleep(1)

          if z[0] == "y":
            break
          else:
            pass

#changing passcode


        elif main == 3:
          x = input(spectrum.red + "Are you sure you want to change the Password?: ").lower()
          if  x[0] == "y":
            passcheck = str(input(spectrum.yellow + "Enter Old Password: "))
            time.sleep (1)
            print ("Checking ...")
            time.sleep (2)
            if passcheck == passkey:
              print ("Password Validated.")
              time.sleep (1.2)
              newpass = input("Enter New Password (Has to be 4 Digits): ")
              time.sleep (0.8)
              print ("Running New Password ...")
              file.seek(0)
              file.truncate()
              file.write(newpass)
              file.close()
              time.sleep (2.5)
              print ("Thank You. Password set.")
              time.sleep (1)
            else:
              print(spectrum.red + "INVALID PASSWORD. ACCOUNT LOCKED.")
              break
          elif x[0] == "n":
            print (spectrum.cyan + "Ok. Sending you back to Main...")
            time.sleep (2)

#games


        elif main == 2:
          print (spectrum.green)
          print("--GAMES MENU--")
          time.sleep (.5)
          print ("Type '1' if you want to go back to the Main Menu")
          time.sleep(0.5)
          print ("Type '2' if you want to play Rock Paper Scissors!(Dhaya's Version)")
          time.sleep (.5)
          print ("Type '3' if you want to play Guess the Number!")
          time.sleep(.5)
          print("Type '4' if you want to play Hangman!")
          time.sleep(.5)
          print("Type '5' if you want to play Dice Rolling Simulator!")
          time.sleep(.5)
          print("Type '6' if You want to play TicTacToe!")
          time.sleep(.5)
          print("Type '7' if you want to play Rock Paper Scissors! (Saarth's Version)")
          time.sleep (.5)
          print ("Type '8' if you want to play BlackJack.")
          time.sleep (.6)
          while True:
            choice = int(input("-> ")) 
            print("")


  #actual game codes


            if choice == 1:
              print(spectrum.cyan + "Ok, sending you back to main...")
              time.sleep (1.6)
              break
            
            elif choice == 2:
              games.rpsdhaya()
              time.sleep(.5)
              break
              
            elif choice == 3:
              games.g()
              time.sleep(1)
              break

            elif choice == 4:
              games.hm()
              time.sleep(1)
              break

            elif choice == 5:
              games.dice()
              time.sleep(1)
              break

            elif choice == 6:
              games.ttt()
              time.sleep(1)
              break

            elif choice == 7:
              games.rpssaarth()
              time.sleep(1)
              break

            elif choice == 8:
              games.bj()
              time.sleep(1)
              break

            else:
              print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
              time.sleep(1)


          
  #Tools Menu



        elif main == 5:
          time.sleep (1)
          print (spectrum.blue + "--TOOLS MENU--")
          time.sleep (.5)
          print ("Press '1' to go back to Main Menu.")
          time.sleep (0.5)
          print ("Press '2' to use a Calculator.")
          time.sleep (.5)
          print ("Press '3' to use a Mass Converter.")
          time.sleep (.5)
          print ("Press '4' to use a Palindrome Checker.")
          time.sleep (.5)
          print ("Press '5' to use a Sentence/Word Reverser.")
          time.sleep (.5)
          print ("Press '6' to use a MultiInput Average Calculator.")
          time.sleep(.5)
          print("Press '7' to use a Tempurature Converter")
          time.sleep (.5)
          print ("Press '8' to use a Sentence Character Counter.")
          time.sleep (.5)
          print ("Press '9' to use an Outlier Detection System.")
          time.sleep (.5)
          print("Press '10' to use a Random Password Generator")
          time.sleep(.5)
          while True:
            gangsta = int(input("-> "))
            time.sleep (0.9)
            print("")


  #tools function code

            if gangsta == 1:
              print (spectrum.cyan + "Ok. Sending you back to main...")
              time.sleep (1.6)
              break
            elif gangsta == 2:
              tool.calc()
              time.sleep(2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet!")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 3:
              tool.pmcc()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet!  ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 4:
              tool.pal()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 5:
              tool.strrev()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 6:
              tool.mimc()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 7:
              tool.tc()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 8:
              tool.slc()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 9:
              tool.ods()
              time.sleep (2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            elif gangsta == 10:
              tool.ranpass()
              time.sleep(2)
              life = random.choice([0,0,0,0,0,0,1,1,1,1,1,2])
              if life == 0:
                time.sleep (1)
                pass
              elif life == 1:
                time.sleep(1)
                tool_mon = random.choice([40,40,40,50,50,50,50,75,75,75,100,100,100,100,100,125,125,125,150,150,150,150,200,200])
                str(money.add_money(tool_mon))
                print(f"+{tool_mon} neows was added to your wallet! ")
                time.sleep(2)
              elif life == 2:
                time.sleep(1)
                str(money.add_money(800))
                print ("You won the Jackpot for using a tool! +800 neows!")
                time.sleep (2)
              break
            else:
              print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
              time.sleep(1)
          



#messages


        elif main == 6:
          time.sleep(1)
          print(spectrum.magenta + " --MESSAGES-- ")
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
          while True:
            bruh = int(input("-> "))
            time.sleep(1)
            print("")


          
  #Messages Functions


            if bruh == 1:
              time.sleep (1)
              print (spectrum.cyan + "Ok. Sending You back to main ... ")
              break

            elif bruh == 2:
              message.insult()
              time.sleep(1)
              print(spectrum.cyan + "Sending you back to main...")
              time.sleep(1.5)
              break

            elif bruh == 3:
              message.inspo()
              time.sleep(1)
              print(spectrum.cyan + "Sending you back to main...")
              time.sleep(1.5)
              break

            elif bruh == 4:
              message.advice()
              time.sleep(1)
              print(spectrum.cyan + "Sending you back to main...")
              time.sleep(1.5)
              break

            elif bruh == 5:
              message.feelbetter()
              time.sleep(1)
              print(spectrum.cyan + "Sending you back to main...")
              time.sleep(1.5)
              break

            elif bruh == 6:
              message.fact()
              time.sleep(1)
              print(spectrum.cyan + "Sending you back to main...")
              time.sleep(1.5)
              break

            else:
              print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
              time.sleep(1)
  

#Help menu


        elif main == 7:
          time.sleep (1)
          print (spectrum.red + "-- HELP MENU --")
          time.sleep (.6)
          print ("Press '1' to Return to main menu.")
          time.sleep (.6)
          print ("Press '2' to learn how to navigate the program.")
          time.sleep (.6)
          print ("Press '3' to learn what you can do in this program.")
          time.sleep (.6)
          print ("Press '4' for Credits")
          time.sleep (.6)
          while True:
            verdict = int(input("-> "))
            print("")

#Help menu conditions(:)


            if verdict == 1:
              time.sleep (1)
              print (spectrum.yellow + "Ok. Sending you back to main ... ")
              time.sleep (2)
              break

            elif verdict == 2:
              time.sleep (1)
              print ("To Navigate this program, you have to type the number corresponding to the place you want to go to when the prompt '->' appears. Then press enter, and you will arrive at your destination, and so on. ")
              time.sleep(8)
              print (spectrum.cyan + "Returning to Main Menu ...")
              time.sleep (1.6)
              break
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
              print (spectrum.cyan + "I am now sending you back to main menu ... ")
              time.sleep (2)
              break
            elif verdict == 4:
              time.sleep (1)
              print (spectrum.magenta + " -- CREDITS -- ")
              time.sleep (2)
              print ("Designers & Software Engineers:")
              time.sleep (1)
              print ("Saarth Desai (12)")
              time.sleep (1)
              print ("Dhayashree Ravi (12)")
              time.sleep (1)
              print ("Message from creators: Thank you for using our software!")
              time.sleep (2)
              cred_mon = random.choice([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,100,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
              str(money.add_money(cred_mon))
              print(spectrum.green + "+",cred_mon,"neows was added to your wallet! (Little Easter Egg)")
              time.sleep(1)
              print (spectrum.cyan + "Sending you back to main ... ")
              time.sleep (2)
              break
            else:
              print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
              time.sleep(1)


        
        elif main == 4:
          print (spectrum.yellow + "--FUN MENU--")
          time.sleep (.5)
          print ("Type '1' to go back to the Main Menu")
          time.sleep(.5)
          print ("Type '2' to use the Magic 8ball!")
          time.sleep(.5)
          print("Type '3' to use a Custom Number Changer!")
          time.sleep (.5)
          print ("Press '4' to use a Sentence/Word Reverser!")
          time.sleep(.5)
          print("Type '5' for a Random Story Line Generator!")
          time.sleep(.5)
          print("Type '6' to play Mad Libs!")
          time.sleep (.5)
          print("Type '7' to Fight Against a Bot")
          time.sleep(.6)


          while True:
            fchoice = int(input("-> ")) 
            print("")

            if fchoice == 1:
              print(spectrum.cyan + "Ok, sending you back to main...")
              time.sleep (1.6)
              break

            elif fchoice == 2:
              fun.bol()
              time.sleep(.5)
              break

            elif fchoice == 3:
              fun.nc()
              time.sleep(.5)
              break

            elif fchoice == 4:
              fun.strrev()
              time.sleep(.5)
              break

            elif fchoice == 5:
              fun.slg()
              time.sleep(.5)
              break

            elif fchoice == 6:
              fun.ml()
              time.sleep(.5)
              break

            elif fchoice == 7:
              fun.fight()
              time.sleep(.5)
              break
            
            else:
              print("Sorry, I do not understand. Please try again.")
              time.sleep(1)








#access  denied code


        else:
          print(spectrum.yellow + "Sorry, I do not understand. Please try again.")
          time.sleep(1)

    else: 
      wrongcounter = wrongcounter + 1
      if wrongcounter == 3:
        print (spectrum.red + "CODE INVALID. ACCESS DENIED, ACCOUNT LOCKED.")
        break
      else:
        print (spectrum.red + "CODE INVALID. ACCESS DENIED")
  else:
    print (spectrum.red + "Internal Error.")
else: 
  print (spectrum.red + "internal error.")
