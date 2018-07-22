fw = open('sample.txt', 'w')
fw.write('have a nice day !\n')
fw.write('I have come again.\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
