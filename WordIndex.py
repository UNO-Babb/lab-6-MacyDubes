#WordIndex.py
#Name:Macy Dubes
#Date: 10/5/2025
#Assignment: Word Index

def main():
  fileName = input("Enter a File Name: ")
  try:
    textFile = open(fileName, 'r')
  except:
    print("Error: Could Not Open File:", fileName)
    return
  
  words = {} #create an empty dictionary
  lineNum = 0
  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace(",",  "")
      w = w.replace(".",  "")
      w = w.replace("!", "")
      w = w.replace("?", "")
      w = w.replace("'", "")
      if w in words: 
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]
  print("Word Index:")
  for word in words:
    print(word, words[word])
  



if __name__ == '__main__':
  main()
