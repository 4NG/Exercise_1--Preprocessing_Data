from Preprocessing_data import *
from Understand_data import *

# optionString = input("Type Option Here: ")
inputFileString = input("Type Input File Name Here: ")
outputFileString = input("Output File Name Here: ")
logFileString = input("Output File Name Here: ")

# while True:
#     try:
#         input_data = pd.read_csv(inputFileString)
#         break
#     except:
#         print("There is no file name.")
#         data = input("Try again! Input your data here: ")

# Understand data
# understand = UnderstandData(data)
# df_columns = input_data.columns.tolist()
# for i in df_columns:
#     if input_data[i].dtypes == object:
#         print(understand.describe_nominal(input_data[i]))
#     else:
#         print(understand.describe_numeric(input_data[i]))
def formatParamString(inputFileString, outputFileString, logFileString):
    inputFileString = inputFileString + '.csv'
    outputFileString = outputFileString + '.csv'
    logFileString = logFileString + '.txt'

    return inputFileString, outputFileString, logFileString


inputFileString, outputFileString, logFileString = formatParamString(inputFileString, outputFileString, logFileString)

discretize = Preprocessing_data(inputFileString, outputFileString, logFileString)
discretize.discretize()
