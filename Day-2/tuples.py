tuple1 = ('one','two','three')
# tuples are immutable and faster than lists 

# methods
# count, index, len function, slicing 

# looping of tuples
mixed = (1, 2, 3, 4.0)
for i in mixed:
    print(i)

# tuple having one element
nums = (1,)
print(type(nums))

# tuple without paranthesis
mixed1 = 1,2,3,
print(type(mixed1))

# tuple unpacking
# fruits = ('Mango', 'Banana', 'Apple')
# fruit1, fruit2, fruit3 = (fruits)
# print(fruit3)

# list inside tuple
fruits = ('Mango', ['Banana', 'Apple'])
fruits[1].pop()
fruits[1].append('Cherry')
print(fruits)

# min, max, sum

print(min(mixed1))
print(max(mixed1))
print(sum(mixed1))
