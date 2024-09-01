import argparse

from char_parsing import count_characters

# Defining the Argument parser
parser = argparse.ArgumentParser(description = "vwc: Custom command-line word count")

# Defining available Arguments
parser.add_argument("-c", "--chars", action = "store_true", help = "Count characters")
parser.add_argument("filename", type = str, help = "File to process")

# Parsing Arguments
args = parser.parse_args()
filename = args.filename

# The string with the all info about the file to be displayed to the user
final_result = ""

# File processing
if args.chars:
  char_count = count_characters(filename)
  final_result += char_count if char_count != "" else ""


# Display the final result
print(final_result)