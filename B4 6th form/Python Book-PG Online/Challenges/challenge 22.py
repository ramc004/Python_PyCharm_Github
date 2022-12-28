sequence = [1, 1]
current = 2
length = 0
while length < 3:
    try:
        length = int(input("How many numbers would you like in the sequence?\nIt must be at least three: "))
    except:
        print("That's not a number.")
        length = 0
while len(sequence) < length:
    sequence.append(sequence[current - 2] + sequence[current - 1])
    current += 1
print("The sequence is", sequence)
sequence.reverse()
print("Reversed it would be", sequence)
print("The sum of the numbers in the sequence is", sum(sequence))
