# put your code here.


def word_count(file):
  word_count_data = open(file)

  for line in word_count_data:
    file_data = line.split(" ")

  word_count_dict = {}

  for word in file_data:
    word_count_dict[word] = +1
  print(f"{word_count_dict.keys()}, {word_count_dict.values()}")
  
  word_count_data.close()
  
word_count("test.txt")