import random
answers = ["yes","no","perhaps","impossible","yes but only for a while","you will die tomorrow","absoulutly not","definetly", "look behind you"]
while True:
    question = input("question (type quit to leave) : ")
    if question == "quit":
        break
    print(random.choice(answers))