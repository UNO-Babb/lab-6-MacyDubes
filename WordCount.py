#WordCount.py
#Name: Macy Dubes
#Date: 10/5/2025
#Assignment: Word Count

def main():
  fileName = input("Enter a File Name:  ")
  try:
    textFile = open(fileName, 'r')
  except:
    print("Error: Could Not Open File:", fileName)
    return
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    letterCount = letterCount + len(line)
    for w in words:
      wordCount = wordCount + 1
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
  

if __name__ == '__main__':
  main()
