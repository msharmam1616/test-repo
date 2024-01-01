print("Welcome to my life quiz")
playing = input("Do you want to play this game? ")

if playing.lower() not in ["yes", "y", "ok"]:
    quit()

print("Okay! Let's play! :) ")

NoOfQuestions = 4
PlayerScore = 0
MaxScore = 5*NoOfQuestions

ans = input("What does CPU stand for? ")
if ans.lower().strip() == "central processing unit":
    print("Correct!")
    PlayerScore += 5
else:
    print("Incorrect!")

ans = input("What does RSVP stand for? ")
if ans.lower().strip() == "reservation":
    print("Correct!")
    PlayerScore += 5
else:
    print("Incorrect!")

ans = input("What does API stand for? ")
if ans.lower().strip() == "application programming interface":
    print("Correct!")
    PlayerScore += 5
else:
    print("Incorrect!")

ans = input("How is work at JP Morgan? ")
if ans.lower().strip() == "sucks":
    print("Correct!")
    PlayerScore += 5
else:
    print("Incorrect!")

percentage = (PlayerScore/MaxScore) * 100

print("Your final score is", PlayerScore, "and percentage is", percentage)
