import time
import random

def rpsdhaya():
  time.sleep(1)
  print("*Hello! This is Rock, Paper, Scissors!*")
  time.sleep(1)
  print ("*The computer will determine the winner!*") 
  time.sleep(1)
  print("*Ready, set, start!*")
  time.sleep(1)
  print("*Type either 'Rock', 'Paper', 'Scissors'*")
  time.sleep(1)
  while True:
    x = input("Write what you will play: ").lower()
    y = random.choice(["rock", "paper", "scissors"])
    time.sleep(1)
    print(f"I choose {y}")
    time.sleep(1)
    r = x[0]
    f = y[0]

    if r == f:
      print("Its a tie!")
      break
    elif r == "p" and f == "r":
      print("Paper covers rock! You win!")
      break
    elif r == "p" and f == "s":
      print("Scissors cuts paper! You lose!")
      break
    elif r == "s" and f == "p":
      print("Scissors cuts paper! You win!")
      break
    elif r == "s" and f == "r":
      print("Rock smashes scissors! You lose!")
      break
    elif r == "r" and f == "p":
      print("Paper covers rock! You lose!")
      break
    elif r == "r" and f == "s":
      print("Rock smashes scissors! You win!")
      break

    else:
      print("Sorry, I do not understand. Please try again.")
      time.sleep(1)

def g():
  time.sleep(1)
  print("Hello! This is a number guessing game!")
  time.sleep(1)
  print ("So basically I think of a number and you have 10 guesses to guess guess it!") 
  time.sleep(2)
  print("Ready, set, start!")
  time.sleep(1)
  a = int(input("What is the maximum number I can choose?: "))
  time.sleep(1)
  print ("caculating number...")
  time.sleep(2)
  print ("I have chosen my number.")
  time.sleep(1.5)
  x = random.randint(1,a)
  def guess(x):
    y = int(input(f"Enter an number from 1 to {a}: "))
    if y < x:
      print ("guess is too low")
      return 0
    elif y > x:
      print ("guess is too high")
      return 0
    else:
      print ("You guessed it! Good Job!")
      time.sleep(1)
      return 1
  guessed = False
  for i in range(0,10):
    if 1 == guess(x):
      guessed = True
      break
  if guessed == False: 
    print("Sorry, you lost!")
  else:
    print ("Ok. Sending you back to main...")
    time.sleep (1)

def hm():
  print("Hello! This is Hangman!")
  time.sleep(1)
  print("I will choose a random word, and you have to try to guess it by guessing one letter at a time. ")
  time.sleep(1)
  print("Ready? Lets start!")
  time.sleep(1)
  print("Generating random word...")



  words = ["cost","cry","shorter","extra","fifteen","stronger","appearance","exchange","old","hung","twice","charge","mighty","famous","name","been","finally","grade","table","off","finest","army","entire","thousand","list","myself","attack","beauty","action","plan","most","desert","sent","gate","clearly","past","mental","nature","sheep","or","mad","treated","person","section","personal","arrive","neck","jet","water","stranger","visit","consider","sing","place","some","train","rubber","later","show","care","tears","cross","lost","process","nodded","orange","shelter","nobody","further","calm","silk","snake","handle","without","shoot","shaking","biggest","worse","birthday","struck","street","grow","smell","three","carry","forest","spider","suppose","tightly","sell","source","pressure","control","blow","burn","fast","understanding","mixture","eat","learn","lady","round","quite","so","danger","planned","news","reason","law","apple","write","strong","equal","organized","distance","has","weight","highest","customs","our","question","meet","count","everybody","wish","shop","ocean","ill","tomorrow","park","south","usual","line","dig","spoken","particles","outer","worry","go","leaf","huge","service","arrow","proud","your","nails","sugar","loud","him","faster","speed","reach","knowledge","strange","grabbed","composition","aloud","physical","depend","report","hand","another","opportunity","highway","drew","beat","rich","please","say","warm","pole","powerful","sand","dry","smile","doctor","mirror","atom","mud","test","man","nation","up","ear","trade","court","together","what","buried","measure","eventually","collect","rest","darkness","diagram","ready","beautiful","yesterday","wave","building","health","bow","saw","judge","lift","parts","major","differ","alike","deeply","roar","success","using","wrote","organization","cattle","sum","how","variety","able","climb","low","brick","thought","explore","constantly","tell","yes","fighting","copper","promised","limited","phrase","clothing","failed","market","forgotten","face","repeat","wild","lead","camp","road","why","quiet","label","industry","stomach","importance","everything","matter","supper","become","giant","nearby","also","previous","bear","wherever","pile","too","corner","rod","adventure","friendly","stream","hay","hardly","attempt","managed","six","stretch","help","given","busy","clean","split","party","slipped","correctly","threw","toy","public","cabin","sense","hollow","remain","attached","form","take","snow","mood","applied","printed","ball","forth","eaten","slave","character","standard","luck","closely","invented","row","uncle","frog","noted","follow","feed","clear","upper","do","enough","neighbor","coach","distant","itself","mistake","substance","size","realize","image","satisfied","ants","coast","these","fourth","roll","bit","ancient","pencil","world","storm","spin","general","trick","summer","folks","plain","hearing","seen","ship","settlers","birth","whatever","men","needs","art","although","swimming","whole","third","walk","natural","father","putting","torn","seed","whose","tongue","till","word","firm","castle","you","slow","appropriate","aid","yet","native","frame","bank","relationship","machine","while","life","cap","caught","sail","however","fierce","seldom","afraid","eleven","complex","continued","wet","certainly","fully","special","stopped","voyage","make","seeing","prepare","ten","late","partly","within","wooden","numeral","sold","goose","built","fifty","current","present","tip","individual","story","hurried","island","becoming","properly","pictured","dog","furniture","battle","massage","dark","mass","noun","heavy","seat","television","dream","vowel","strip","himself","gently","tax","sat","captured","beyond","suggest","giving","almost","studied","twelve","surface","its","ride","factory","tea","union","could","tried","disappear","land","laugh","son","idea","hunter","replace","capital","trace","curious","teeth","thing","chose","chair","night","similar","especially","music","greater","shoulder","directly","get","creature","condition","rather","result","official","perfectly","than","gold","disease","day","finger","silver","due","sink","see","transportation","gain","verb","example","beneath","division","ordinary","drop","shelf","hat","shallow","forty","date","anything","guard","bend","halfway","poem","top","beside","sentence","spell","unless","made","important","clothes","order","thin","mouth","tree","strength","brief","wing","hurt","location","open","hot","share","reader","metal","muscle","swept","ahead","dangerous","former","courage","political","gray","nuts","mail","women","friend","board","listen","potatoes","baseball","film","more","wait","cell","valley","steel","blind","wagon","build","jack","is","replied","teacher","brown","parallel","ice","winter","white","opposite","information","congress","arm","shake","milk","area","whispered","noon","recall","acres","right","map","fix","species","visitor","gravity","cool","owner","hang","bottom","thread","believed","crop","plane","pitch","not","his","might","bean","theory","act","rice","continent","got","last","fat","pair","fellow","far","whenever","route","motor","nearest","century","straw","region","my","dropped","indeed","engineer","thank","topic","riding","gulf","coming","sang","cloud","interest","nervous","longer","rear","porch","death","column","dinner","will","develop","several","smoke","pony","wealth","sweet","fire","mission","thou","yourself","base","once","wide","everyone","dozen","height","sun","knew","direction","below","wonder","we","every","swam","point","recent","note","solid","small","garage","port","doll","practical","sick","lamp","automobile","simply","against"]



  word = random.choice(words)
  print("Each '-' reresents 1 character in the word")
  time.sleep(1)
  guesses = ''
  turns = 12
  


  while turns > 0:
      failed = 0
      for char in word:
          if char in guesses:
              print(char)
          else:
              print("-")
              failed += 1  
  
      if failed == 0:
          print("You Won! Good job!")
          break
      
      guess = input("What is your guess?: ")
      
      guesses += guess
      
      if guess not in word:
          
          turns -= 1
        
          print("No letters match")
          time.sleep(0.5)
          print("You have", + turns, 'more guesses')
          time.sleep(0.5)
          
          if turns == 0:
            time.sleep(0.5)
            print("Sorry you lost")
  print("The word was: ",word)

def dice():
  print ("Hello! This is a Dice Rolling Simulator!")
  time.sleep(1)
  print ("Type 'Roll' to Roll the Dice or 'Done' once your Done")
  time.sleep(1)
  for x in range(1000000):
    d = random.choice([1,2,3,4,5,6])
    y = input("Type 'Roll' or 'Done': ")
    time.sleep(0.5)
    if y == "roll" or y == "Roll":
      print ("You rolled a",d)
      time.sleep(0.5)
    else:
      print("Ok! Thanks for playing!")
      break


def ttt():
  blank = "|_|"
  gameboard = [[blank,blank,blank],[blank,blank,blank],[blank,blank,blank]]
  print ("Hello! Welcome to TicTacToe!")
  time.sleep (2)
  t=""
  ot=""

  while True:
    print ("Which side do you want to be on?('X' or 'O')")
    time.sleep (0.7)
    t = input("->")
    time.sleep (0.5)
    print ("Please Wait. Integrizing ... ")
    time.sleep (2.5)
    if t == "O" or t == "o":
      t = " O "
      ot = " X "
      break
    elif t == "X" or t == "x":
      t = " X "
      ot = " O "
      break
    else:
      print ("Please Give me either a 'X' or an 'O'.")
      time.sleep (1)
  while True:
    if gameboard [0][0] == gameboard [0][1] == gameboard [0][2] == t or gameboard [1][0] == gameboard [1][1] == gameboard [1][2] == t or gameboard [2][0] == gameboard [2][1] == gameboard [2][2] == t or gameboard [0][0] == gameboard [0][1] == gameboard [0][2] == t or gameboard [1][0] == gameboard [1][1] == gameboard [1][2] == t or gameboard [2][0] == gameboard [2][1] == gameboard [2][2] == t or gameboard [0][0] == gameboard [1][1] == gameboard [2][2] == t or gameboard [0][2] == gameboard [1][1] == gameboard [2][0] == t :
      print ("You win!. Press 'Run' to play again!")
      break
    elif gameboard [0][0] == gameboard [0][1] == gameboard [0][2] == ot or gameboard [1][0] == gameboard [1][1] == gameboard [1][2] == ot or gameboard [2][0] == gameboard [2][1] == gameboard [2][2] == ot or gameboard [0][0] == gameboard [0][1] == gameboard [0][2] == ot or gameboard [1][0] == gameboard [1][1] == gameboard [1][2] == ot or gameboard [2][0] == gameboard [2][1] == gameboard [2][2] == ot or gameboard [0][0] == gameboard [1][1] == gameboard [2][2] == ot or gameboard [0][2] == gameboard [1][1] == gameboard [2][0] == ot :
      print ("I Win! Press run to play again!")
      break
    elif gameboard [0][0] != blank and gameboard [0][1] != blank and gameboard [0][2] != blank and  gameboard [1][0] != blank and gameboard [1][1] != blank and gameboard [1][2] != blank and gameboard [2][0] != blank and gameboard [2][1] != blank and gameboard [2][2] != blank:
      print ("Draw! Press 'run' to play again.")
      break
    else:
      print (f"Choose the Row and Column of where you want to put your {t}.(Row - 0,1,2) (Column - 0,1,2)")
      time.sleep (1)
      x = int(input("Row ->"))
      time.sleep (0.8)
      y = int(input("Collumn ->"))
      if not gameboard [x][y] == blank:
        print("Sorry. This spot is taken. Try Again.")
        time.sleep (1)
      else:
        gameboard [x][y] = t 
        while True:
          if gameboard [0][0] == ot and gameboard [0][1] == ot and gameboard [0][2] == blank:
            r = 0
            c = 2
          elif gameboard [0][0] == ot and gameboard [0][1] == blank and gameboard [0][2] == ot:
            r = 0
            c = 1
          elif gameboard [0][0] == blank and gameboard [0][1] == ot and gameboard [0][2] == ot:
            r = 0
            c = 0
          elif gameboard [1][0] == ot and gameboard [1][1] == ot and gameboard [1][2] == blank:
            r = 1
            c = 2
          elif gameboard [1][0] == ot and gameboard [1][1] == blank and gameboard [1][2] == ot:
            r = 1
            c = 1
          elif gameboard [1][0] == blank and gameboard [1][1] == ot and gameboard [1][2] == ot:
            r = 1
            c = 0
          elif gameboard [2][0] == ot and gameboard [2][1] == ot and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [2][0] == ot and gameboard [2][1] == blank and gameboard [2][2] == ot:
            r = 2
            c = 1
          elif gameboard [2][0] == blank and gameboard [2][1] == ot and gameboard [2][2] == ot:
            r = 2
            c = 0
          elif gameboard [0][0] == ot and gameboard [1][0] == ot and gameboard [2][0] == blank:
            r = 2
            c = 0
          elif gameboard [0][0] == ot and gameboard [1][0] == blank and gameboard [2][0] == ot:
            r = 1
            c = 0
          elif gameboard [0][0] == blank and gameboard [1][0] == ot and gameboard [2][0] == ot:
            r = 0
            c = 0
          elif gameboard [0][1] == ot and gameboard [1][1] == ot and gameboard [2][1] == blank:
            r = 2
            c = 1
          elif gameboard [0][1] == ot and gameboard [1][1] == blank and gameboard [2][1] == ot:
            r = 1
            c = 1
          elif gameboard [0][1] == blank and gameboard [1][1] == ot and gameboard [2][1] == ot:
            r = 0
            c = 1
          elif gameboard [0][2] == ot and gameboard [1][2] == ot and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [0][2] == ot and gameboard [1][2] == blank and gameboard [2][2] == ot:
            r = 1
            c = 2
          elif gameboard [0][2] == blank and gameboard [1][2] == ot and gameboard [2][2] == ot:
            r = 0
            c = 2
          elif gameboard [0][0] == ot and gameboard [1][1] == ot and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [0][0] == ot and gameboard [1][1] == blank and gameboard [2][2] == ot:
            r = 1
            c = 1
          elif gameboard [0][0] == blank and gameboard [1][1] == ot and gameboard [2][2] == ot:
            r = 0
            c = 0
          elif gameboard [2][0] == ot and gameboard [1][1] == ot and gameboard [0][2] == blank:
            r = 0
            c = 2
          elif gameboard [2][0] == ot and gameboard [1][1] == blank and gameboard [0][2] == ot:
            r = 1
            c = 1
          elif gameboard [2][0] == blank and gameboard [1][1] == ot and gameboard [0][2] == ot:
            r = 2
            c = 0
          elif gameboard [0][0] == t and gameboard [0][1] == t and gameboard [0][2] == blank:
            r = 0
            c = 2
          elif gameboard [0][0] == t and gameboard [0][1] == blank and gameboard [0][2] == t:
            r = 0
            c = 1
          elif gameboard [0][0] == blank and gameboard [0][1] == t and gameboard [0][2] == t:
            r = 0
            c = 0
          elif gameboard [1][0] == t and gameboard [1][1] == t and gameboard [1][2] == blank:
            r = 1
            c = 2
          elif gameboard [1][0] == t and gameboard [1][1] == blank and gameboard [1][2] == t:
            r = 1
            c = 1
          elif gameboard [1][0] == blank and gameboard [1][1] == t and gameboard [1][2] == t:
            r = 1
            c = 0
          elif gameboard [2][0] == t and gameboard [2][1] == t and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [2][0] == t and gameboard [2][1] == blank and gameboard [2][2] == t:
            r = 2
            c = 1
          elif gameboard [2][0] == blank and gameboard [2][1] == t and gameboard [2][2] == t:
            r = 2
            c = 0
          elif gameboard [0][0] == t and gameboard [1][0] == t and gameboard [2][0] == blank:
            r = 2
            c = 0
          elif gameboard [0][0] == t and gameboard [1][0] == blank and gameboard [2][0] == t:
            r = 1
            c = 0
          elif gameboard [0][0] == blank and gameboard [1][0] == t and gameboard [2][0] == t:
            r = 0
            c = 0
          elif gameboard [0][1] == t and gameboard [1][1] == t and gameboard [2][1] == blank:
            r = 2
            c = 1
          elif gameboard [0][1] == t and gameboard [1][1] == blank and gameboard [2][1] == t:
            r = 1
            c = 1
          elif gameboard [0][1] == blank and gameboard [1][1] == t and gameboard [2][1] == t:
            r = 0
            c = 1
          elif gameboard [0][2] == t and gameboard [1][2] == t and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [0][2] == t and gameboard [1][2] == blank and gameboard [2][2] == t:
            r = 1
            c = 2
          elif gameboard [0][2] == blank and gameboard [1][2] == t and gameboard [2][2] == t:
            r = 0
            c = 2
          elif gameboard [0][0] == t and gameboard [1][1] == t and gameboard [2][2] == blank:
            r = 2
            c = 2
          elif gameboard [0][0] == t and gameboard [1][1] == blank and gameboard [2][2] == t:
            r = 1
            c = 1
          elif gameboard [0][0] == blank and gameboard [1][1] == t and gameboard [2][2] == t:
            r = 0
            c = 0
          elif gameboard [2][0] == t and gameboard [1][1] == t and gameboard [0][2] == blank:
            r = 0
            c = 2
          elif gameboard [2][0] == t and gameboard [1][1] == blank and gameboard [0][2] == t:
            r = 1
            c = 1
          elif gameboard [2][0] == blank and gameboard [1][1] == t and gameboard [0][2] == t:
            r = 2
            c = 0
          else:
            r = random.randint(0,2)
            c = random.randint(0,2)
          if not gameboard [r][c] == blank:
            print()
          else:
            gameboard [r][c] = ot
            break
        time.sleep (1)
        print ("Good Choice!")
        time.sleep (1.3)
        print (f"I chose row {r},collumn {c}.")
        time.sleep (1)
        print ("Here is the Board:")
        time.sleep (0.7)
        for i in range(3):
          for j in range(3):
            print (gameboard[i][j],end='',sep="\t")
          print ("")
        time.sleep (2.5)




def rpssaarth():
  print ("I am going to play Rock Paper Scissors with you!")
  time.sleep (3)
  while True:
    print ("3!")
    time.sleep (1)
    print ("2!")
    time.sleep (1)
    print ("1!")
    time.sleep (1)
    print ("Go!")
    time.sleep (1)
    print ("I have chosen my sign.")
    our = random.choice([1,2,3])
    time.sleep (0.8)
    print ("choose Your Sign:")

    time.sleep (0.5)
    print ("Rock = 1, Paper = 2, Scissors = 3")
    while True:
      their = input("What did you choose?:")
      if int(their) > 3 or int(their) < 0:
        print ("Give me a valid number.")
        print ("Rock = 1, Paper = 2, Scissors = 3")
      elif int(their) == 1 or int(their) == 2 or int(their) == 3:
        break
    time.sleep (0.5)
    their = int(their)
    if our == 1:
      print ("I chose Rock!")
      if int(their) == 1:
        print ("Tie! We have to redo it!! ")
        time.sleep (1)
      elif int(their) == 2:
        print ("Paper Covers Rock! You win.")
        time.sleep (1)
        print ("Press Run to Play Again!")
        break
      elif their == 3:
        print ("Rock Smashes Scissors! You lose!!!")  
        time.sleep (1)
        print ("Press Run to play again!")
        break
    elif our == 2:
      print ("I chose Paper!")
      if their == 1:
        print ("Paper Covers Rock! You lose!!!!!!")
        time.sleep (1)
        break
      elif their == 2:
        print ("Tie! We have to redo it! ")
        time.sleep (1)
      elif their == 3:
        print ("Scissor cuts Paper. You win.")
        time.sleep (1)
        print ("Press run to play again!")
        break
    elif our == 3:
      print ("I chose Scissors!")
      if their == 1:
        print ("Rock Demolishes Scissor. You Win.")
        time.sleep (1)
        print ("Press run to play again !")
        break
      elif their == 2:
        print ("Scissor cuts Paper! You lose!!!")
        time.sleep (1)
        break
      elif their == 3:
        print ("Tie! We have to redo it! ")
        time.sleep (1)
    else:
      print ("Internal error")


def bj():
  userstand = 0
  botstand = 0
  double = 0
  rod = 1
  stand1 = 0
  stand2 = 0
  print("Hello! This is Blackjack!")
  time.sleep(1)
  J = 10
  Q = 10
  K = 10
  time.sleep(1)
  A = random.choice([1,11])
  card_options =[A,2,3,4,5,6,7,8,9,10,J,Q,K,A,2,3,4,5,6,7,8,9,10,J,Q,K,A,2,3,4,5,6,7,8,9,10,J,Q,K,A,2,3,4,5,6,7,8,9,10,J,Q,K,A,2,3,4,5,6,7,8,9,10,J,Q,K,A,2,3,4,5,6,7,8,9,10,J,Q,K]
  deck = (random.sample(card_options, 30))
  print("1 player or 2 player? (1/2) ")
  time.sleep (0.5)
  opt = int(input("->"))
  time.sleep (1)
  if opt == 1:
    username = input("What is your name:")
    x = random.choice(deck)
    usercards = [x]
    y = random.choice(deck)
    botcards = [y]
    print ("Ok! Lets the Games Begin!")
    time.sleep (1.5)
    while True:
      time.sleep (1)
      print ("Bot's Cards:")
      time.sleep (.5)
      print (botcards)
      time.sleep (.5)
      print (f"{username}'s Cards:")
      time.sleep(.5)
      print (usercards)
      time.sleep (1.5)
      print ("Would you like to hit or stand?(h/s)")
      hs = input("->").lower()
      time.sleep (1)
      if hs == "h":
        print ("Sure!")
        card = random.choice(deck)
        time.sleep (1)
        print (" You got a . . . ")
        time.sleep(1.6)
        print (card)
        usercards.append(card)
        if sum(usercards) > 21:
          time.sleep (1)
          print ("You Busted!")
          time.sleep(.5)
          print (f"Here were your cards: {usercards}")
          time.sleep (1)
          print ("Press 'run' to play again!")
          break
        else:
          time.sleep (1)
          print ("It is the bot's turn.")
          time.sleep (2)
          if sum(botcards) > 16 and sum(botcards) < 21:
            print ("The bot has decided to stand.")
            time.sleep(1)
            print ("It is now your turn.")
          else:
            print ("The bot has decided to hit!")
            time.sleep(1)
            botcard = (random.choice(deck))
            print (f"the bot got a {botcard}.")
            botcards.append(botcard)
            if sum(botcards) > 21:
              print ("The Bot Busted! You win!")
              time.sleep (1)
              print ("Press 'run' to play again!")
              break
            else:
              time.sleep (1)
              print ("It is now your turn.")
      elif hs == "s":
        time.sleep (1)
        print ("Ok.")
        time.sleep (1)
        print ("You stand. It is now the bot's turn.")
        userstand = 1
        time.sleep (2)
        if sum(botcards) > 16 and sum(botcards) < 21:
          print ("The bot has decided to stand.")
          botstand = 1
          time.sleep(1)
          if sum(botcards) > sum(usercards):
            double = 1
            print("Bot Wins! You Lose!")
            break
          elif sum(botcards) < sum(usercards):
            double = 1
            print ("You win! Bot loses! Press 'Run' to play again!")
            break
          else:
            print ("Tie! Press 'Run' to play again!")
            break
        else:
          print ("The bot has decided to hit!")
          time.sleep(1)
          while True:
            botcard = (random.choice(deck))
            print (f"the bot got a {botcard}.")
            botcards.append(botcard)
            if userstand == 1:
              time.sleep(1)
              print ("It is now the bot's turn.")
              if sum(botcards) > 16:
                if sum(botcards) > 21:
                  time.sleep(1)
                  break
                else:
                  print ("The bot decided to stand.")
                  time.sleep (1)
                  if sum(botcards) > sum(usercards):
                    double = 1
                    print("Bot Wins! You Lose! Press 'Run' to play again!")
                    break
                  elif sum(botcards) < sum(usercards):
                    double = 1
                    print ("You win! Bot loses! Press 'Run' to play again!")
                    break
                  else:
                    print("Tie! Press 'Run' To play again!")
                    break
              else:
                print ("The bot decided to hit!")
          if double == 1:
            break
          else:    
            if sum(botcards) > 21:
              print ("The Bot Busted! You win!")
              time.sleep (1)
              print ("Press 'run' to play again!")
              break
            else:
              time.sleep (1)
              print ("It is now your turn.")
  else:
    player1 = input("Player 1: What is your Name: ")
    time.sleep (1.6)
    player2 = input("Player 2: What is your Name: ")
    time.sleep (1)
    print ("Initializing Game . . . ")
    time.sleep (2)
    print ("Ok! Ready?")
    time.sleep (1)  
    print ("3!")
    time.sleep (1)
    print ("2!")
    time.sleep (1)
    print ("1!")
    time.sleep (1)
    print ("Let the Games Begin!!!")
    time.sleep (1)
    x = random.choice(deck)
    cards1 = [x]
    y = random.choice(deck)
    cards2 = [y]
    while True:
      time.sleep (1)
      print (f" {player1}'s Cards:")
      time.sleep (0.5)
      print (cards1)
      time.sleep (0.5)
      print (f"{player2}'s Cards:")
      time.sleep (0.5)
      print (cards2)
      time.sleep (2)
      if stand1 == 0:
        print (f"{player1}: Would You like to Hit or Stand? (h/s)")
        time.sleep (0.6)
        z1 = input("->").lower()
        time.sleep (1)
        if z1[0] == "h":  
          print ("Sure!")
          card1 = random.choice(deck)
          time.sleep (1)
          print ("You got a . . . ")
          time.sleep (2)
          print (f"    {card1}    ")
          cards1.append(card1)
          time.sleep (1)
          if sum(cards1) > 21:
            print (f"{player1} busts! {player2} Wins!!! ")
            time.sleep (2)
            break
          else:
            if stand2 == 0:
              print (f"It is now {player2}'s turn.")
              time.sleep (1)
              print (f"{player2}: Would You like to Hit or Stand? (h/s)")
              time.sleep (0.6)
              z2 = input("->").lower()
              time.sleep (1)
              if z2[0] == "h":
                print ("Sure!")
                card2 = random.choice(deck)
                time.sleep (1)
                print ("You got a . . . ")
                time.sleep (1)
                print (f"   {card2}   ")
                cards2.append(card2)
                time.sleep (2)
                if sum(cards2) > 21:
                  print (f"{player2} busts! {player1} Wins!!!")
                  time.sleep (2)
                  break
                else:
                  rod = rod + 1
                  print (f" -- ROUND {rod} -- ")
                  time.sleep (1)
              elif z2[0] == "s":
                print ("Ok.")
                stand2 = 1
                time.sleep (1.6)
                rod = rod + 1
                print (f" -- ROUND {rod} -- ")
                time.sleep (1)
            else:
              time.sleep (1)
              rod = rod + 1
              print (f" -- ROUND {rod} -- ")
              time.sleep (1)
        elif z1[0] == "s":
          print ("Sure!")
          stand1 = 1
          time.sleep (2)
          if stand2 == 0:
            print (f"It is now {player2}'s turn.")
            time.sleep (1)
            print (f"{player2}: Would You like to Hit or Stand? (h/s)")
            time.sleep (0.5)
            z2 = input("->").lower()
            time.sleep (1)
            if z2[0] == "h":
              print ("Sure!")
              time.sleep (1)
              card2 = random.choice(deck)
              print ("You got a . . . ")
              time.sleep (2)
              print (f"   {card2}   ")
              cards2.append(card2)
              time.sleep (2)
              if sum(cards2) > 21:
                print (f"{player1} busts! {player2} Wins!!!")
                time.sleep (2)
                break
              else:
                rod = rod + 1
                print (f" -- ROUND {rod} -- ")
                time.sleep (1)
            elif z2[0] == "s":
              print ("Ok.")
              time.sleep (2)
              print ("The winner is . . . ")
              time.sleep (2)
              if sum(cards2) < sum(cards1):
                print (f"{player1}!!! Congratulations!!!")
                time.sleep (3)
                break
              elif sum(cards1) < sum(cards2):
                print (f"{player2}!!! Congratulations!!!")
                time.sleep (3)
                break
              else:
                print (f"Tie!!! Congratulations to {player1} and {player2}!!!")
                time.sleep (3)
                break
          else:
            time.sleep (1)
            print ("The winner is . . . ")
            time.sleep (2)
            if sum(cards2) < sum(cards1):
              print (f"{player1}!!! Congratulations!!!")
              time.sleep (3)
              break
            elif sum(cards1) < sum(cards2):
              print (f"{player2}!!! Congratulations!!!")
              time.sleep (3)
              break
            else:
              print (f"Tie!!! Congratulations to {player1} and {player2}!!!")
              time.sleep (3)
              break
      else:
        print (f"{player2}: Would You like to Hit or Stand? (h/s)")
        time.sleep (0.6)
        z2 = input("->").lower()
        time.sleep (1)
        if z2[0] == "h":
          print ("Sure!")
          card2 = random.choice(deck)
          time.sleep (1)
          print ("You got a . . . ")
          time.sleep (1)
          print (f"   {card2}   ")
          cards2.append(card2)
          time.sleep (2)
          if sum(cards2) > 21:
            print (f"{player1} busts! {player2} Wins!!!")
            time.sleep (2)
            break
          else:
            rod = rod + 1
            stand1 = 1
            print (f" -- ROUND {rod} -- ")
            time.sleep (1)
        elif z2[0] == "s":
          print ("Ok.")
          time.sleep (2)
          print ("The winner is . . . ")
          time.sleep (2)
          if sum(cards2) < sum(cards1):
            print (f"{player1}!!! Congratulations!!!")
            time.sleep (3)
            break
          elif sum(cards1) < sum(cards2):
            print (f"{player2}!!! Congratulations!!!")
            time.sleep (3)
            break
          else:
            print (f"Tie!!! Congratulations to {player1} and {player2}!!!")
            time.sleep (3)
            break