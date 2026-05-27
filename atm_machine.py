#Assignment: ATM Machine Program
print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")
amount=1000
try:
  choice=int(input("Enter the choice:"))
  while choice!=4:
    if choice==1:
      print("Balance=",amount)
      choice=int(input("Enter the choice:"))
    elif choice==2:
      money=int(input("Enter the amount you want to deposit:"))
      if money>0:
        amount=amount+money
        print("updated Balance=",amount)
      else:
        print("Amount should be greater then 0")
      choice=int(input("Enter the choice:"))
    elif choice==3:
      withdraw=int(input("Enter the amount to be withdrawn:"))
      if withdraw<amount:
        amount=amount-withdraw
        print("Remaining amount after withdrawl=",amount)
      elif withdraw<0:
        print("withdrawl amount cannot be zero")
      else:
        print("Available Balance is low for this withdrawl")
        print("Curent available Balance=",amount)
      choice=int(input("Enter the choice:"))
  print("Thank you")
except:
  print("Enter the correct choice")
  
