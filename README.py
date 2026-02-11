arr = [1,4,3,5,8,6]

min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]

print([min, max])
