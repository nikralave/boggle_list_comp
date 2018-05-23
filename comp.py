# l = ["A", "B", "C"]

# print([n*2 for n in l])


#Long version
# p = []
# for n in l:
#     p.append(n*2)
    

# print(p)

#------------------------------------

# print([ i*2 for i in range (7)])

# print([ i for i in range (0, 13, 2)])

# print( [i*2 for i in range (10)])

#Cheallenge 1
# print(["*" for i in range(5)])

#Challenge 2

l = ["Hi", "There", "Everyone"] 
 
print([len(i) for i in l ])

#Challenge 3

print([(i**2) for i in range(8)])

#Challenge 4

print([(i, i+1) for i in range(5)])

#Challenge 5

word = 'woohoo'

print([ i for i in word])

#Challenge 6

things = ['car', 'cat', 'maps', 'if', 'level']
 
print ([(i, len(i)) for i in things])

#Challenge 7

booland = [(False, False), (False, True), (True, False), (True, True)]

print([(i[0] and i[1]) for i in booland])
print([(i and j) for i,j in booland])

#Challenge 8

boolor = [(False, False), (False, True), (True, False), (True, True)]

print([(i[0] or i[1]) for i in boolor])
print([(i or j) for i,j in boolor])

#------------------------------------------------------
l = [(i, j) for i in range(3) for j in range(3)]
print(l)


#[(0, 0, 0), (0, 0, 1)]


#------------------------------------------------------

# Dictionary Comprehension Challenge

words = ['Hi', 'There', 'Everyone']

print({ i:len(i) for i in words})

word = 'code'
print({i:ord(i) for i in word})

['car', 'cat', 'maps', 'if', 'level'] 