def add_money(money=100):
  file = open("mon_stor.txt","r+")
  x = int(file.readline()) + money
  file.seek(0)
  file.write(str(x))
  file.truncate()
  file.close()
  return x

# y = str(money.add_money(int(random.choice([5,10,15])))
# print ("+5 neows was added to your wallet! (login money)")
# time.sleep(1)