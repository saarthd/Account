def add_money(money=100):
  file = open("wallet.txt","r+")
  x = int(file.readline()) + money
  file.seek(0)
  file.write(str(x))
  file.truncate()
  file.close()
  return x

