import argparse

from byte_parsing import count_bytes
from line_parsing import count_lines
from word_parsing import count_words
from char_parsing import count_chars

# Defining the Argument parser
parser = argparse.ArgumentParser(description = "vwc: Custom command-line word count")

# Defining available Arguments
parser.add_argument("-c", "--bytes", action = "store_true", help = "Count bytes")
parser.add_argument("-l", "--lines", action = "store_true", help = "Count lines")
parser.add_argument("-w", "--words", action = "store_true", help = "Count words")
parser.add_argument("-m", "--chars", action = "store_true", help = "Count characters")
parser.add_argument("filename", type = str, help = "File to process")

# Parsing Arguments
args = parser.parse_args()
is_default_parsing = not (args.bytes or args.lines or args.words or args.chars)

# Parsing file
file_name = args.filename

# The string with the all info about the file to be displayed to the user
final_result = ""

# File processing
if args.lines or is_default_parsing:
  line_count = count_lines(file_name)
  final_result += line_count if line_count != "" else ""
if args.words or is_default_parsing:
  word_count = count_words(file_name)
  final_result += word_count if word_count != "" else ""
if args.bytes or is_default_parsing:
  byte_count = count_bytes(file_name)
  final_result += byte_count if byte_count != "" else ""
if args.chars:
  char_count = count_chars(file_name)
  final_result += char_count if char_count != "" else ""


# Display the final result
print(final_result)