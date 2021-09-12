class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []  #instance variable    
    self.funds = 0.00    
  #

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.funds += amount
  #

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -abs(amount), "description": description})      
      self.funds -= amount
      return True
    else:
      return False
  #

  def get_balance(self):
    return self.funds
  #
  
  def transfer(self, amount, otherCategory):
    if self.check_funds(amount):
      destination = "Transfer to " + otherCategory.category
      self.withdraw(amount, destination)
      source = "Transfer from " + str(self.category)
      otherCategory.deposit(amount, source)
      return True
    else:
      return False    
  #

  def check_funds(self, amount):
    if self.funds - amount >= 0:
      return True
    else:
      return False
  #

  def __str__(self):
    title = self.category.center(30, "*")+"\n"
    ledg = "" 

    for l in self.ledger:
      amount = "{:>7.2f}".format(l["amount"])
      desc = "{:<23}".format(l["description"])
      ledg += "{}{}\n".format(desc[:23], amount[:7])
    #

    total = "Total: {:.2f}".format(self.funds)

    return title+ledg+total
  #
#end class

def create_spend_chart(categories):
  totalSpent = 0
  catsSpent = []
  catsNames = []

  #obtain withrawals per category and total withrawals
  for c in categories:
    catsNames.append(c.category)
    catWithdrawals = 0
    for l in c.ledger:
      if l["amount"] < 0:
        catWithdrawals += abs(l["amount"])
        totalSpent += abs(l["amount"])
      #
    #end for ledger
    catsSpent.append({"withrawals": abs(catWithdrawals)})        
  #end for categories

  #save percentage spent per category and round to nearest 10
  for c in catsSpent:
    p = ((c["withrawals"] / totalSpent * 10) // 1) * 10
    c["withrawals"] = p   
  #end for catsSpent

  barchart = ""
  for n in reversed(range(0, 101, 10)):
    barchart += str(n).rjust(3) + '|'
    for c in catsSpent:
      if c["withrawals"] >= n:
          barchart += " o "
      else:
          barchart += "   "
    barchart += " \n"  
  #end for barchart

  title = "Percentage spent by category\n"

  #example: 10 - for 3 categories
  line = "    " + "-" * (3*len(categories) + 1) + "\n"

  #max category name length
  maxLength = max(map(lambda c: len(c), catsNames))
  catsNames = list(map(lambda c: c.ljust(maxLength), catsNames))

  #arrange vertically
  categ = ""
  for x in zip(*catsNames):
    aux = "".join(map(lambda s: s.center(3), x))
    categ += "    " +  aux + " " + "\n" 
  #end for zip

  return (title + barchart + line + categ).rstrip("\n")
#end create_spend_chart
