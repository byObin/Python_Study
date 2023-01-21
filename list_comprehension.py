array = []
for i in range(0,20,2):
    array.append(i*i)
print(array)

array2 = [j*j for j in range(0,20,2)]
print(array2)

output = [k for k in array2 if k%5==0]
print(output)