#Mohib Ibrahim
#Assignment 10

def Translate(string,dictionary):
    words = string.split()
    output = [ ]
    space = ' '
    for word in words:
        word = word.lower()
        if word in dictionary:
            output.append(dictionary[word])
        else:
            return 'UNABLE TO TRANSLATE'
    output = space.join(output)
    return output

def FileDictionary(file_name,dictionary):
    file = open(file_name,encoding = 'utf8')
    count = 0
    for line in file:
        line = line.rstrip('\n')
        line_words= line.split(':')
        dictionary[line_words[0]]=line_words[1]
    file.close       
    


################################################################################

spanish_dict = { }

FileDictionary('english_spanish.txt',spanish_dict)

print('Welcome to XU Translatr, to exit please enter \'quit\'')

while True:
    sentence = input('\nPlease enter a sentence to translate: ')
    if sentence == 'quit':
      break
    else:    
        translation = Translate(sentence,spanish_dict)
        print('Your translation is:\n' + translation)
print('Thank you for using XU Translator')

   
