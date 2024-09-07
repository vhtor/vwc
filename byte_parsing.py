def count_bytes(file_name):
  try:
    with open(file_name, "rb") as file: # Reads all content as raw bytes
      content = file.read()
      byte_count = len(content)
      return f"Byte count: {byte_count}\n"
  except:
    return ""