def count_characters(file_name):
  try:
    with open(file_name, "rb") as file: # Reads all content as raw bytes
      content = file.read()
      char_count = len(content)
      return f"Char count: {char_count}\n"
  except:
    return ""