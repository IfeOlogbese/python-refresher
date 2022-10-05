name = 'Bob'
greeting = f'Hello, {name}'

# print(greeting)

# Using format syntax
greeting = 'Hello, {}'
with_name = greeting.format(name)
print(with_name)

# Longer, multiple substitues
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
