def count_chars(file_name):
  try:
    with open(file_name, "r", encoding="utf-8") as file: # Reads all content as raw bytes
      char_count = 0
      buffer_size = 1024 * 1024
      buffer = file.read(buffer_size)
      
      while buffer:
        char_count += len(buffer)
        buffer = file.read(buffer_size)
        
      return f"Char count: {char_count}\n"
  except:
    return ""