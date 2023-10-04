# Input string from the treasure hunter
input_string = input("Masukkan string perjalanan treasure hunter: ")

# Define the evaluate_treasure lambda function
evaluate_treasure = lambda input_string: eval(''.join([char if char == '$' else '0' if char == 'x' and eval(''.join([c for c in input_string[input_string.index(char)::-1] if c == '$'])) < 10 else '/2' if char == '#' and eval(''.join([c for c in input_string[input_string.index(char)::-1] if c == '$'])) > 0 else '' for char in input_string]))

# Calculate the treasure value using the lambda function
result = evaluate_treasure(input_string)

# Display the result
print(f"Nilai harta karun yang ditemukan: {result}")
