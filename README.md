# python_data_structures_and_algorithms

## Overview

This project consists of Python functions to solve three different problems related to data structures and algorithms. It includes functions for working with stacks, sequences (lists/tuples), and dictionaries.

### Problem 1: is_balanced(expression)

- This function checks whether a given expression containing parentheses, curly braces, and square brackets is balanced.
- An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.

- Example usage:
  expression1 = "([]{})"
  expression2 = "([)]"
  print(is_balanced(expression1)) # Output: True
  print(is_balanced(expression2)) # Output: False
  Problem 2: remove_duplicates(sequence)
  This function takes a sequence (list or tuple) and returns a new sequence with duplicates removed while maintaining the original order of elements.

  Example usage:
  input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
  result = remove_duplicates(input_sequence)
  print(result) # Output: [2, 3, 4, 5, 6, 7]

  Problem 3: word_frequency(sentence)
  This function takes a sentence and returns a dictionary containing the frequency of each word in the sentence.
  It ignores punctuation and considers words in a case-insensitive manner.

  Example usage:
  sentence = "This is a test sentence. This sentence is a test."
  result = word_frequency(sentence)
  print(result)
  Project Structure
  stacks.py: Contains the implementation of the is_balanced function.
  sequences.py: Contains the implementation of the remove_duplicates function.
  dictionaries.py: Contains the implementation of the word_frequency function.

  README.md: This file, providing project information and instructions.
  Other files: You may include additional files or scripts as needed for your project.
  Clone the Project

  To clone this project to your local machine, use the following command in your terminal:

git clone https://github.com/your-username/your-repo-name.git

Install Dependencies
This project does not have any external dependencies. You can simply run the Python scripts without the need for additional installations.

Contributing
Feel free to contribute to this project by adding more functions or improving existing ones. Submit a pull request with your changes, and they will be reviewed.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Make sure to replace `"your-username"` and `"your-repo-name"` in the cloning instructions with your actual GitHub username and repository name.
