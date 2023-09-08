# list has no limit. can include any data type, different from array.
# index is the spot in the list.

test_scores = [90,70,75,54,90]
print(test_scores[3])

# for in loop - for items in list

for score in test_scores:
    score = score -2
    print(score)

#append can add new data to a list

    new_score = 95
    test_scores.append(new_score)


#extend combines data from one list to another
test_scores_2 = [100,55]
test_scores.extend(test_scores_2)
print(test_scores)

# remove data from a list using remove function/method
test_scores.remove(55)
print

#find something in a list to remove
looking_for = int(input("Give me a number you want to remove from the list"))
found = looking_for in test_scores
if(found==True):
    test_scores.remove(looking_for)
    print("FOUND")
    print(test_scores)
else:
    print("Value was not on the list.")

#count instances of something
print(test_scores.count(90))

#sorting list
test_scores.sort()
print(test_scores)

#finding length of a list
print(len(test_scores))