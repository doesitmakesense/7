string = 'a a a b c a a d c d d'.split()
q = set(string)
list_1 = list(q)

temp = ''

for j in list_1:
    count = 1
    for i in range(len(string)-1):
        if temp == string[i]:
            temp_1 = string.pop(i)
            temp_1 = temp_1,'_', count
            string.insert(i, temp_1)
            count +=1
