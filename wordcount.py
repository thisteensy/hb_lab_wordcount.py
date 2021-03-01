# put your code here.

word_count_dict = {}
def word_count(file):
  word_count_data = open(file)

  for line in word_count_data:
    line = line.rstrip()
    file_data = line.split()

  

    for word in file_data:
      word_count_dict[word] = word_count_dict.get(word, 0) +1
  
  for word, count in word_count_dict.items():
    print(word, count)
  
  word_count_data.close()
  
word_count("./test.txt")