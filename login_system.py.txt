#Correct username/password stored already.
username="Xyz123"
password="123@24"
u_name=input("Enter the user name:")
p_word=input("Enter the password:")
attempts=3
while attempts>0:
 if u_name!=username or p_word!=password:
   attempts=attempts-1
   if attempts==0:
     break
   print("Attempts left",attempts)
   u_name=input("Enter the correct user name:")
   p_word=input("Enter the correct password:")
 else:
   print("Welcome Xyz123")
   break
if attempts==0:
  print("Account blocked")