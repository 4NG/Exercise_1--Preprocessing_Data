import pandas as pd
import numpy as np
import statistics


class Preprocessing_data:
    """
    :type input_data: pandas dataframe
    """
    def __init__(self, inputFileString,outputFileString,logFileString):
        self.inputFileString = inputFileString
        self.outputFileString = outputFileString
        self.logFileString = logFileString

    def summary(self):
        pass

    def replace(self):
        pass

    def discretize(self):
        N = input('Please enter how many bag do you want: ')
        N = int(N)
        disType = input('What kind of binding you want?\n'
                      '1 for Equal-Width-Binding\n'
                      '2 for Equal-Depth-Binding\n')

        data = pd.read_csv('test.csv')
        outputDataFrame = data
        logFile = open(self.logFileString, 'a')
        if disType == '1':
            for col in data.columns:
                if data[col].dtype == 'float' or data[col].dtype == 'int':
                    process = data[col].tolist()
                    M = max(process)
                    m = min(process)
                    width = int((M - m) / N)
                    binArray = []
                    countLog = [0]*N
                    for i in range(0, N + 1):
                        binArray = binArray + [m + width * i]
                    for i in range(0, N):
                        for j in range(len(process)):
                            if process[j] > binArray[i] and process[j] < binArray[i+1]:
                                process[j] = round(binArray[i], 2)
                                countLog[i] += 1
                    outputDataFrame[col] = process
                    logLineContent = 'thuoc tinh: ' + col + ' '
                    for i in range(N):
                        logLineContent = logLineContent + '[' + str(binArray[i]) + ';' + str(binArray[i+1]) + '] ' \
                                         + str(countLog[i]) + ' '
                    logFile.writelines(logLineContent)
                    logFile.writelines('\n')
            logFile.close()
            outputDataFrame.to_csv('output.csv')
        elif disType == '2':
            for col in data.columns:
                if data[col].dtype == 'float' or data[col].dtype == 'int':
                    process = data[col].tolist()
                    length = len(process)
                    depth = int(length / N)
                    for i in range(0, N):
                        arr = []
                        for j in range(i * depth, (i + 1) * depth):
                            if j >= length:
                                break
                            arr = arr + [process[j]]
                        AssignValue = statistics.mean(arr)
                        for j in range(i * depth, (i + 1) * depth):
                            if j >= length:
                                break
                            process[j] = AssignValue
                    outputDataFrame[col] = process
                    logLineContent = 'thuoc tinh: ' + col + ' '
                    for i in range(N + 1):
                        if(i*depth < length - depth):
                            logLineContent = logLineContent + '[' + str(depth*i) + ';' + str(depth*(i+1)) + '] ' \
                                             + str(depth) + ' '
                        else:
                            logLineContent = logLineContent + '[' + str(depth * i) + ';' + str(length) + '] ' \
                                             + str(length - depth*(N)) + ' '
                    logFile.writelines(logLineContent)
                    logFile.writelines('\n')
            logFile.close()
            outputDataFrame.to_csv(self.outputFileString)
def normalize(self):
        pass


    

