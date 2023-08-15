def main():
  TITLE = 'frankenstein.txt'
  PATH_TO_BOOK = f'books/{TITLE}'
  text = extractText(PATH_TO_BOOK)
  words = getWordList(text)
  word_count = getWordCount(words)
  char_counts = countChars(text)
  char_list = list(char_counts.items())
  char_list.sort()
  output(PATH_TO_BOOK, char_list, word_count)
  
def output(book_path, char_list, word_count):
    print('\n', f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document', '\n')
    
    for pair in char_list:
       if pair[0].isalpha():
          print(f"The '{pair[0]}' character was found {pair[1]} times")
          
    print('--- End report ---')


def extractText(path):
    with open(path) as f:
      return f.read()

def getWordList(text):
   words = text.split()
   return words

def getWordCount(list):
   return len(list)

def countChars(text):
  chars = {}
  for c in text:
    low_c = c.lower()
    if low_c in chars:
       chars[low_c] += 1
    else:
       chars[low_c] = 1
  return chars

main()