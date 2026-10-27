def generate_sequence(start, end, step):
    sequenz = []
    for num in range(start, end, step):
        sequenz.append(num)
    return sequenz

def sum_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

def count_multiples(numbers, divisor):
    count = 0
    for num in numbers:
        if num%divisor == 0:
            count += 1
    return count

def analyze_sequence(start, end, step, divisor):
    sequenz = generate_sequence(start, end, step)
    sum = sum_numbers(sequenz)
    multiples = count_multiples(sequenz, divisor)
    return sequenz, sum, multiples

start = int(input('Where do you wanna start: '))
end = int(input('Where do you wanna stop: '))
step = int(input('In wich steps do you wanna go through the loop: '))
divisor = int(input('Input the divisor: '))

sequenz, sum, multiples = analyze_sequence(start, end, step, divisor)
print()
print(f'Sequenz: {sequenz}')
print(f'Sum: {sum}')
print(f'Multiples of {divisor}: {multiples}')