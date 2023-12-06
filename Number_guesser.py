import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #ensures input is a digit
    top_of_range = int(top_of_range)

else:
   print("please enter a number next time")
    
if top_of_range <= -1:
        print("Please type a  larger number")
        quit()

###
# else:
# print("type a number next time")

random_number = random.randint(0,top_of_range)
#print(random_number)
guess = 0
while True:
     guess += 1
     user_guess = input("Make a guess")

     if user_guess.isdigit():
       user_guess = int(user_guess)
     
     else:
      print("please enter a number next time")
      continue
     
     if user_guess == random_number:
       print("You got it!")
       break
     elif user_guess>random_number:
        print("Number is way above range!") 

     elif user_guess<random_number:
          print("Number is way below range!")

     else:
        print("Keep trying!")

print("You got it in", guess,"guesses")
    
