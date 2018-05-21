numbers = input("Enter numbers separated by a comma: ")
numbers = [int(n) for n in numbers.split(',')]
end = len(numbers) - 1
while end != 0:

      for i in range(end):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
          end = end - 1
