import codecs

# Open the input file in read mode and output file in write mode
with codecs.open('input_file.txt', 'r', encoding='utf-8') as input_file, codecs.open('output_file.txt', 'w', encoding='utf-8') as output_file:
  # Read the entire contents of the input file
  text = input_file.read()

  # Use a dictionary to map Cyrillic characters to their Latin counterparts
  cyrillic_to_latin = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E', 'Ж': 'Ž', 'З': 'Z', 'И': 'I',
    'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj', 'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Џ': 'Dž', 'Ш': 'Š'
  }

  # Loop through the text and replace each Cyrillic character with its Latin counterpart
  translated_text = ''
  for char in text:
    if char in cyrillic_to_latin:
      translated_text += cyrillic_to_latin[char]
    else:
      translated_text += char

  # Write the translated text to the output file
  output_file.write(translated_text)