#data-structures - way to structure data in a meaningful way. Store multiple values in some type of order or category.
#tuples are immutable (do not change) lists of data...lists of constants

name = "Alex"
print(name)
name = "Tim"
print(name)
#strings are immutable and cannot change waht's inside...just replace the whole thing.
name[1] = "a"
print(name)
#tuples
states = ('IL', 'IN', 'KY')

print(states[1])

#display multiple items in a tuple
for state in states:
    print(state)
    