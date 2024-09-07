import sys

def count_chars(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            buffer_size = 1024 * 1024
            char_count = 0
            buffer = file.read(buffer_size)
            
            while buffer:
                char_count += len(buffer)
                buffer = file.read(buffer_size)
            
            return f"Char count: {char_count}\n"
    except Exception as e:
        print(f"Error reading file: {e}", file = sys.stderr)
        return ""