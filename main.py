from Preprocessing_data import *

print("                     Welcome!!!                 \n")
print("      Nhom 17 - LAB1 - Preprocessing Data       \n")
print("First, please set up some step: \n")

inputFileString = input("1. Input your file Name Here. This must be a .csv file. For example: test, hello,...  :")
outputFileString = input("2. Name your Output file Name Here. This is a .csv file. For example: output, out,...  :")
logFileString = input("2. Name your Log file Name Here. This is a .txt file. For example: log, log_file,...  :")

def formatParamString(inputFileString, outputFileString, logFileString):
    inputFileString = inputFileString + '.csv'
    outputFileString = outputFileString + '.csv'
    logFileString = logFileString + '.txt'

    return inputFileString, outputFileString, logFileString


inputFileString, outputFileString, logFileString = formatParamString(inputFileString, outputFileString, logFileString)

while True:
    data = ProcessingData(inputFileString, outputFileString, logFileString)
    choice = input("Choose your options: \n"
          "1. Summary \n"
          "2. Replace \n"
          "3. Discretize \n"
          "4. Normalize \n"
          "5. Exit \n")

    if choice == '1':
       data.summary(inputFileString)
       print("This will be wrote down in your {}.".format(logFileString))
       print("Check out {} file later!!!".format(logFileString))
       print('\n')

    elif choice == '2':
        data.replace(inputFileString)
        print("This will be wrote down in your {} and {}.".format(outputFileString, logFileString))
        print("Check out {} and {} files later!!!".format(outputFileString, logFileString))
        print('\n')

    elif choice == '3':
        data.discretize(inputFileString)
        print("This will be wrote down in your {} and {}.".format(outputFileString, logFileString))
        print("Check out {} and {} files later!!!".format(outputFileString, logFileString))
        print('\n')

    elif choice == '4':
        data.normalize(inputFileString)
        print("This will be wrote down in your {} and {}.".format(outputFileString, logFileString))
        print("Check out {} and {} files later!!!".format(outputFileString, logFileString))
        print('\n')

    elif choice == '5':
        print("Thanks for using our program!!! \n")
        print("Remember to check out files. \n")
        print("Good bye!!!")
        break
