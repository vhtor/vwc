def count_lines(file_name):
  try:
    with open(file_name, "rb") as file: # Reads all content as raw bytes
      lines = 0
      buffer_size = 1024 * 1024
      read_file = file.raw.read
      buffer = read_file(buffer_size)
      
      while buffer:
        lines += buffer.count(b'\n')
        buffer = read_file(buffer_size)
        
      return f"Line count: {lines}\n"
  except:
    return ""