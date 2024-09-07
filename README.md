# My custom wc

This project is `wc` (word count) program exercise. The `wc` program is a command-line utility that counts the number of lines, words, and characters in a given file or input stream.

## Usage

To use this custom `wc` you'll need Python 3, make sure you have it installed on your machine. You can check if Python 3 is installed by running the command `python3 --version` in your terminal.

Once you have Python 3 installed, follow these steps to use the `wc` program:

1. Clone the repository to your local machine.
2. Navigate to the project directory: `/vwc`.
3. Run the `python3 vwc.py` program with the desired file or input stream as an argument using Python 3. For example: `python3 wc.py myfile.txt` or `cat myfile.txt | python3 vwc.py`

## Features

The `wc` program provides the following features:

- Counting the number of lines in a file or input stream.
- Counting the number of words in a file or input stream.
- Counting the number of raw bytes in a file or input stream.
- Counting the number of characters in a file or input stream.

## Examples

Here are some examples of how to use the `wc` program:

- Count the number of lines in a file: `python3 vwc.py myfile.txt -l`
- Count the number of words in a file: `python3 vwc.py myfile.txt -w`
- Count the number of characters in stdin: `echo 'hello world!' | python3 vwc.py -c`

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.