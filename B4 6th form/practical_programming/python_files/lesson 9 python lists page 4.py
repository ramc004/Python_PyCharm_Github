print([1,24,76])
print(['red','yellow','blue'])
print(['red',24,98.6])
print([1,[5,6],7])
print([])

for i in [5, 4, 3, 2, 1] :
    print(i)
print("Blastoff!")

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
 print("Happy New Year:", friend)
print("Done!")

friends = [ 'Joseph', 'Glenn', 'Sally' ]
print (friends[1])
Glenn

fruit = "Banana"
fruit[0] = "b"

x = fruit.lower()
print (x)

lotto = [2, 14, 26, 41, 63]
print(lotto)

lotto[2] = 28
print(lotto)

greet = "Hello Bob"
print(len(greet))

x = [ 1, 2, 'joe', 99]
print (len(x))

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print ("Happy New Year: ", friend)
for i in range(len(friends)) :
    friend = friends[i]
print ("Happy New Year:", friend)
friends = (['Joseph', 'Glenn', 'Sally'])
print(len(friends))
print (range(len(friends)))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

t = [9, 41, 12, 3, 74, 15]
t[1:3]

t[:4]

t[3:]

t[:]

x = list()
dir(x)(['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'])

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

some = [1, 9, 21, 10, 16]
9 in some

15 in some

20 not in some

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends)

print (friends[1])

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

print(sum(nums)/len(nums))

total = 0
count = 0
while True :
 inp = input('Enter a number: ')
 if inp == 'done':
     break
 else:
     value = float(inp)
 total = total + value
 count = count + 1
average = total / count
print("Average:", average)

