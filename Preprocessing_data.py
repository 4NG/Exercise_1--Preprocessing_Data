import pandas as pd
import numpy as np
import statistics
import math


class ProcessingData:
    """
    :type input_file: csv
    :type output_file: csv
    :type log_file: txt
    """
    def __init__(self, input_file, output_file, log_file):
        self.input_file = input_file
        self.output_file = output_file
        self.log_file = log_file

    def summary(self, data):
        """
        Tom tat du lieu

        :param data: du lieu nhap vao
        :return: file txt luu lai cac thong tin cua du lieu
        """

        log = open(self.log_file, 'w')
        log.writelines("1.     Tom tat du lieu:     ")
        log.writelines('\n')

        """
        data : du lieu nhap vao duoc chuyen thanh pandas dataframe
        data_columns : danh sach cac thuoc tinh 
        """
        data = pd.read_csv(data)
        data_columns = data.columns.tolist()

        """
        log file: 
            so mau: 
            so thuoc tinh: 
        """
        print("    Tom tat du lieu:     \n")
        print("So mau: {}".format(len(data.index)))

        log_line = "so mau: {}".format(len(data.index))
        log.writelines(log_line)
        log.writelines('\n')

        print("So thuoc tinh: {}".format(len(data_columns)))

        log_line = "so thuoc tinh: {}".format(len(data_columns))
        log.writelines(log_line)
        log.writelines('\n')

        """
        log file: 
            thuoc tinh 1: <ten> <kieu du lieu>
            ...
            thuoc tinh n: <ten> <kieu du lieu>
        """
        for col in data_columns:
            if data[col].dtypes == object:
                log_line = "thuoc tinh {}: {} - nominal".format(str(data_columns.index(col) + 1), col)
                print(log_line)

            else:
                log_line = "thuoc tinh {}: {} - numeric".format(str(data_columns.index(col) + 1), col)
                print(log_line)

            log.writelines(log_line)
            log.writelines('\n')

        log.close()

    def replace(self, data):
        """
        Thay the thuoc tinh bi thieu

        :param data: du lieu nhap vao
        :return:
            file txt: luu lai cac gia tri thieu va gia tri moi cua thuoc tinh
            file csv: du lieu dau ra da duoc xu li
        """
        print("     Dien gia tri bi thieu    \n")

        log = open(self.log_file, 'a')
        log.writelines("2.     Dien gia tri bi thieu     ")
        log.writelines('\n')

        data = pd.read_csv(data)
        data_columns = data.columns.tolist()

        """
        log file:
            thuoc tinh: <ten thuoc tinh>, <so gia tri thieu>, <gia tri moi>
        """
        for col in data_columns:
            count_missing_value = data[col].isnull().sum()  # tinh so gia tri thieu

            if data[col].dtypes == object:
                popular_str = data[col].mode()[0]  # tim ra chuoi pho bien nhat cua thuoc tinh nominal
                data[col].replace(to_replace=np.nan, value=popular_str, inplace=True)  # thay the gia tri thieu NaN
                log_line = "thuoc tinh: {}, {}, {}".format(col, count_missing_value, popular_str)
                print(log_line)

            else:
                mean_value = data[col].mean()  # tim gia tri trung binh cua thuoc tinh numeric
                data[col].replace(to_replace=np.nan, value=mean_value, inplace=True) # thay the gia tri thieu NaN
                log_line = "thuoc tinh: {}, {}, {}".format(col, count_missing_value, mean_value)
                print(log_line)

            log.writelines(log_line)
            log.writelines('\n')

        log.close()
        data.to_csv(self.output_file, index=False, header=True)

    def discretize(self, data):
        """
        Chia gio mot hay nhieu thuoc tinh numeric

        :param data: du lieu nhap vao
        :return:
            file txt: luu lai cac thuoc tinh duoc chia gio, mien gia tri va so mau
            file csv: du lieu dau ra da duoc xu li
        """

        print("     Chia gio mot hoac nhieu thuoc tinh numeric     \n")

        n = input('Please enter how many bag do you want: ')
        n = int(n)
        dis_type = input('What kind of binding you want?\n'
                        '1. for Equal-Width-Binding \n'
                        '2. for Equal-Depth-Binding \n')

        data = pd.read_csv(data)
        output = data

        log = open(self.log_file, 'a')
        log.writelines("3.     Chia gio mot hoac nhieu thuoc tinh numeric     ")
        log.writelines('\n')

        if dis_type == '1':
            for col in data.columns:
                if data[col].dtype == 'float' or data[col].dtype == 'int':
                    process = data[col].tolist()
                    M = max(process)
                    m = min(process)
                    width = int((M - m) / n)
                    binArray = []
                    countLog = [0] * n

                    for i in range(0, n + 1):
                        binArray = binArray + [m + width * i]

                    for i in range(0, n):
                        for j in range(len(process)):
                            if (process[j] > binArray[i]) and (process[j] < binArray[i + 1]):
                                process[j] = round(binArray[i], 2)
                                countLog[i] += 1

                    output[col] = process
                    log_line = 'thuoc tinh: ' + col + ' '

                    """
                    log file : 
                        thuoc tinh: <ten thuoc tinh> <mien gia tri gio 1>:<so mau>...<mien gia tri gio k>:<so mau>
                    """
                    for i in range(n):
                        log_line = log_line + '[' + str(binArray[i]) + ';' + str(binArray[i + 1]) + '] ' \
                                         + str(countLog[i]) + ' '
                        print(log_line)

                    log.writelines(log_line)
                    log.writelines('\n')

            log.close()
            output.to_csv(self.output_file, index=False, header=True)

        elif dis_type == '2':
            for col in data.columns:
                if data[col].dtype == 'float' or data[col].dtype == 'int':
                    process = data[col].tolist()
                    length = len(process)
                    depth = int(length / n)

                    for i in range(0, n):
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

                    output[col] = process
                    log_line = 'thuoc tinh: ' + col + ' '

                    for i in range(n + 1):
                        if i * depth < length - depth:
                            log_line = log_line + '[' + str(depth * i) + ';' + str(depth * (i + 1)) + '] ' \
                                             + str(depth) + ' '
                            print(log_line)

                        else:
                            log_line = log_line + '[' + str(depth * i) + ';' + str(length) + '] ' \
                                             + str(length - depth * n) + ' '
                            print(log_line)

                    log.writelines(log_line)
                    log.writelines('\n')

            log.close()
            output.to_csv(self.output_file, index=False, header=True)

    def normalize(self, data):
        """
        Chuan hoa du lieu theo min-max, z-score

        :param data: du lieu nhap vao
        :return:
            file txt: luu lai cac thuoc tinh da chuan hoa va mien du lieu moi
            file csv: du lieu dau ra da duoc xu li
        """
        print("     Chuan hoa du lieu     \n")

        dis_type = input('What kind of normalize you want?\n'
                        '1. Min-Max\n'
                        '2. Z-Score\n')

        data = pd.read_csv(data)
        output = data

        log = open(self.log_file, "a")
        log.writelines("4.     Chuan hoa du lieu     ")
        log.writelines('\n')

        if dis_type == '1':

            log.writelines("Chuan hoa theo Min-Max \n")

            new_min = input('Please enter new min: ')
            new_max = input('Please enter new max: ')

            new_min = int(new_min)
            new_max = int(new_max)

            for col in data.columns:
                if data[col].dtype != object:
                    max1 = max(data[col])
                    min1 = min(data[col])
                    process = data[col].tolist()
                    for i in range(len(data[col])):
                        process[i] = ((data[col][i] - min1) * (new_max - new_min) / (max1 - min1)) + new_min

                    """
                    log file:
                        thuoc tinh: <ten thuoc tinh> <mien gia tri chuan hoa>
                    """
                    log_line = "thuoc tinh: {} [{}, {}]".format(col, new_min, new_max)
                    print(log_line)
                    log.writelines(log_line)
                    log.writelines('\n')

                    output[col] = process

        elif dis_type == '2':
            log.writelines("Chuan hoa theo Z-Score \n")

            for col in data.columns:
                maxn = 0
                minn = 0
                if data[col].dtype != object:
                    process = data[col].tolist()
                    for i in range(len(process)):
                        if math.isnan(process[i]):
                            process[i] = 0

                    x = statistics.mean(process)
                    variance = sum([(point - x) ** 2 for point in process]) / len(data[col])
                    dlc = math.sqrt(variance)

                    for i in range(len(data[col])):
                        process[i] = (data[col][i] - x) / dlc
                    maxn = max(process)
                    minn = min(process)
                    output[col] = process

                    log_line = "thuoc tinh: {} [{} {}]".format(col, str(int(minn) - 1), str(int(maxn) + 1))
                    print(log_line)
                    log.writelines(log_line)
                    log.writelines('\n')

        log.close()
        output.to_csv(self.output_file, index=False, header=True)

