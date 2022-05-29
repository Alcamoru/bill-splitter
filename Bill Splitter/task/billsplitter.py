# write your code here
import random

print("Enter the number of friends joining (including you):")
n_friends = int(input())

if n_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = dict()
    for friend in range(n_friends):
        friends[input()] = 0

    print("Enter the total bill value:")
    bill = int(input())
    bill_per_person = round(bill / n_friends, 2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    who_is_lucky = input()
    if who_is_lucky == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        # bill_per_person = round(bill / n_friends, 2)
        friends = {x: bill_per_person for x in friends}
        for friend in friends:
            if friend != lucky:
                friends[friend] += round(friends[lucky] / n_friends + 1, 2)
        friends[lucky] = 0
    else:
        print("No one is going to be lucky")
        lucky = ""
        friends = {x: bill_per_person for x in friends}

    print(friends)
