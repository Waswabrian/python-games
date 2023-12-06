print("welcome to my kenyan-knowledge quiz game!!")
playing = input("Do you want to play?? ")
if playing.lower() != "yes":
    quit()
print("let's play :)")
score = 0
print(playing)

first_quest = input("What's your name?")
print("Welcome " + first_quest)

independence = input("when did Kenya gain independence?")
if independence == "1963":
  print("Correct!")
  score += 1
else:
   print("Incorrect!")

print(independence)

president = input("Who was the first president of the republic of Kenya?")
if president == "Jomo Kenyatta":
   print("Correct!")
   score += 1
else:
   print("Incorrect!")

print(president)

republic = input("When did Kenya proclaimed a republic??")

if republic == "1964":
   print("Correct!")
   score += 1
else :
   print("Incorrect!")

print(republic)

death_one = input("When did the first president die?")

if death_one == "1978":
   print("Correct!")
   score += 1
else:
   print("Incorrect!")
print(death_one)

president_two = input("Who became the second president?")
 
if president_two == "Daniel Arap Moi":
   print("Correct!")
   score += 1
else:
   print("Incorrect!")

print(president_two)

print("Thank you for playing")
print("You got" + str(score) + "questions correct")
print("You got" + str((score/4)*100) + "^%")

