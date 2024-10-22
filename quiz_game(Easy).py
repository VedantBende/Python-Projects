print("Welcome to my Quiz Game!")

playing = input("Would you like to play? (yes/no): ").lower()
if playing == "yes":
    print("Okay! Let's Play :)")
    print("")
    print("(Note: If you want to quit in mid-game just type 'quit' in the answer!)")
    print("")
else:
    print("Okay Bye! See You Around...")
    quit()

input("Press Enter To Start... ")

correct_answers = 0
total_questions = 50

# Question 1
answer = input("What does CPU stand for? = ").lower()
if answer == "central processing unit":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 2
answer = input("What does RAM stand for? = ").lower()
if answer == "random access memory":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 3
answer = input("What does OS stands for? = ").lower()
if answer == "operating system":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 4
answer = input("Who is considered the father of the computer? = ").lower()
if answer == "charles babbage":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 5
answer = input("What does URL stand for? = ").lower()
if answer == "uniform resource locator":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 6
answer = input("What does SSD stand for in computer? = ").lower()
if answer == "solid state drive":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 7
answer = input("What does HDD stand for in computer? = ").lower()
if answer == "hard disk drive":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 8
answer = input("Which company developed the Windows operating system? = ").lower()
if answer == "microsoft":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 9
answer = input("What does GPU stands for? = ").lower()
if answer == "graphics processing unit":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 10
answer = input("What is the primary use of web browsers? = ").lower()
if answer == "browsing":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 11
answer = input("What is the capital of France? = ").lower()
if answer == "paris":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 12
answer = input("Which country is known as the Land of the Rising Sun? = ").lower()
if answer == "japan":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 13
answer = input("What is the largest continent by land area? = ").lower()
if answer == "asia":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 14
answer = input("What is the capital city of Australia? = ").lower()
if answer == "canberra":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 15
answer = input("What is the longest river in the world? = ").lower()
if answer == "nile river" or "neil":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 16
answer = input("Which country has the most islands? = ").lower()
if answer == "sweden":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 17
answer = input("What is the largest desert in the world? = ").lower()
if answer == "sahara desert":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 18
answer = input("What is the capital of Canada? = ").lower()
if answer == "ottawa":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 19
answer = input("In which country would you find the city of Istanbul? = ").lower()
if answer == "turkey":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 20
answer = input("What is the smallest country in the world by land area? = ").lower()
if answer == "vatican city":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 21
answer = input("What gas do plants absorb from the atmosphere for photosynthesis? = ").lower()
if answer == "carbon dioxide":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 22
answer = input("Who was the first man to walk on the Moon? = ").lower()
if answer == "neil armstrong":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 23
answer = input("What is the largest ocean on Earth? = ").lower()
if answer == "pacific ocean" or "pacific":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 24
answer = input("What is the chemical symbol for gold? = ").lower()
if answer == "au":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 25
answer = input("What is the name of the ship that sank in 1912? = ").lower()
if answer == "titanic":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 26
answer = input("Who wrote 'Harry Potter and the Sorcerer's Stone'? = ").lower()
if answer == "j.k. rowling":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 27
answer = input("What is the capital city of Germany? = ").lower()
if answer == "berlin":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 28
answer = input("How many continents are there on Earth? = ").lower()
if answer == "seven" or "7":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 29
answer = input("What is the largest organ in the human body? = ").lower()
if answer == "skin":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 30
answer = input("What is the main ingredient in guacamole? = ").lower()
if answer == "avocado":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 31
answer = input("What is the name of the famous clock tower in London? = ").lower()
if answer == "big ben":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 32
answer = input("What is the currency used in the United Kingdom? = ").lower()
if answer == "pound sterling" or "pound":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 33
answer = input("Who discovered America in 1492? = ").lower()
if answer == "christopher columbus":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 34
answer = input("What is the smallest planet in our solar system? = ").lower()
if answer == "mercury":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 35
answer = input("What is the name of the galaxy we live in? = ").lower()
if answer == "milky way":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 36
answer = input("What is the capital of Italy? = ").lower()
if answer == "rome":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 37
answer = input("What is the primary component of Jupiter's atmosphere? = ").lower()
if answer == "hydrogen":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 38
answer = input("What is the name of the first manned mission to the Moon? = ").lower()
if answer == "apollo 11":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 39
answer = input("What is the chemical symbol for sodium? = ").lower()
if answer == "na":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 40
answer = input("What is the name of the river that runs through Egypt? = ").lower()
if answer == "nile":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 41
answer = input("What is the largest country by land area? = ").lower()
if answer == "russia":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 42
answer = input("Who was the first President of the India? = ").lower()
if answer == "dr. rajendra prasad" or "dr rajendra prasad" or "rajendra prasad":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 43
answer = input("What is the smallest bone in the human body? = ").lower()
if answer == "stapes":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 44
answer = input("What is the capital of Brazil? = ").lower()
if answer == "brasilia":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 45
answer = input("Who was the first woman to win a Nobel Prize? = ").lower()
if answer == "marie curie":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 46
answer = input("What is the capital of England? = ").lower()
if answer == "london":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 47
answer = input("What is the largest volcano in the world? = ").lower()
if answer == "mauna loa":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 48
answer = input("Which Indian city is known as the 'City of Joy'? = ").lower()
if answer == "kolkata":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 49
answer = input("What is the symbol for the element oxygen? = ").lower()
if answer == "o":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")

# Question 50
answer = input("What is the capital of Japan? = ").lower()
if answer == "tokyo":
    correct_answers += 1
    print("Correct!")
elif answer == "quit":
    print("Okay Bye! See You Around...")
    quit()
else:
    print("Oh! That's Incorrect!")


print("")
print("Your score is " + str(correct_answers) + "/" + str(total_questions) + ".")

print("")
print("Thanks for playing!")
