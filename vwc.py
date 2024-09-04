import argparse

from char_parsing import count_characters
from line_parsing import count_lines
from word_parsing import count_words

# Defining the Argument parser
parser = argparse.ArgumentParser(description = "vwc: Custom command-line word count")

# Defining available Arguments
parser.add_argument("-c", "--chars", action = "store_true", help = "Count characters")
parser.add_argument("-l", "--lines", action = "store_true", help = "Count lines")
parser.add_argument("-w", "--words", action = "store_true", help = "Count words")
parser.add_argument("filename", type = str, help = "File to process")

# Parsing Arguments
args = parser.parse_args()
file_name = args.filename

# The string with the all info about the file to be displayed to the user
final_result = ""

# File processing
if args.chars:
  char_count = count_characters(file_name)
  final_result += char_count if char_count != "" else ""
if args.lines:
  line_count = count_lines(file_name)
  final_result += line_count if line_count != "" else ""
if args.words:
  word_count = count_words(file_name)
  final_result += word_count if word_count != "" else ""
  


# Display the final result
print(final_result)