def count_words(file_name):
  try:
    with open(file_name, "rb") as file: # Reads all content as raw bytes
      word_count = 0
      buffer_size = 1024 * 1024
      read_file = file.raw.read
      buffer = read_file(buffer_size)
      
      while buffer:
        words = buffer.split()
        word_count += len(words)
        buffer = read_file(buffer_size)
        
      return f"Word count: {word_count}\n"
  except:
    return ""