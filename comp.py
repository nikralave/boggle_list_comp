l = ["A", "B", "C"]

print([n*2 for n in l])


#Long version
# p = []
# for n in l:
#     p.append(n*2)
    

# print(p)

#------------------------------------

print([ i*2 for i in range (7)])

print([ i for i in range (0, 13, 2)])

print([[j for j in range(i)] for i in range(10)])