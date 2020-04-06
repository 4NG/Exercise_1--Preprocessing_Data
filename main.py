from Preprocessing_data import *
from Understand_data import *

data = input("Input your data here: ")
while True:
    try:
        input_data = pd.read_csv(data)
        break
    except:
        print("There is no file name.")
        data = input("Try again! Input your data here: ")


# Understand data
understand = UnderstandData(data)
df_columns = input_data.columns.tolist()
for i in df_columns:
    if input_data[i].dtypes == object:
        print(understand.describe_nominal(input_data[i]))
    else:
        print(understand.describe_numeric(input_data[i]))