array= [15,29,9,40,3]
sw = True
print("This is the not ordered list: ", array)
while sw:
    sw = False
    for i in range (len(array) -1):
        if array[i] > array[i+1]:
            sw=True
            array[i], array[i+1] = array[i+1], array[i]

print("Now, this is the list ordered: ", array)