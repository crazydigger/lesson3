numbers = '2,3,4,5,5,6,5,3,9'
print(numbers)
l = list(numbers.split(','))
l =sorted(l)
print(set(l))
