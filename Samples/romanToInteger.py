def roman_to_int(roman_numeral):
  # Create a dictionary with Roman numeral as key and integer as value
  roman_to_int_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  # Convert the input Roman numeral to uppercase
  roman_numeral = roman_numeral.upper()

  # Initialize the result variable to 0
  result = 0

  # Loop through the Roman numeral string
  for i in range(len(roman_numeral)):
    # Get the integer value of the current Roman numeral
    current_value = roman_to_int_dict[roman_numeral[i]]
    # print(roman_to_int_dict[roman_numeral[i]])
    # If the next Roman numeral has a greater integer value, subtract the
    # current value from the result. Otherwise, add the current value to
    # the result.
    if i+1 < len(roman_numeral) and roman_to_int_dict[roman_numeral[i+1]] > current_value:
      result -= current_value
    else:
      result += current_value

  return result

print(roman_to_int("XL"))