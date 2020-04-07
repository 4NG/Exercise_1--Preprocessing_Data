class UnderstandData:

    def __init__(self, input_data):
        self.input_data = input_data

    @staticmethod
    def describe_numeric(columns):
        me = columns.mean()
        va = columns.var()
        a = columns.count()
        de = 142193 - a
        de_percent = (de / 142193) * 100
        return me, va, de, de_percent

    @staticmethod
    def describe_nominal(columns):
        uni = columns.unique()
        only = columns.value_counts()   # count value appear only one time
        only = only[only == 1].index
        di = columns.count()
        de = 142193 - di
        de_percent = (de / 142193) * 100
        return len(uni.tolist()), len(only), de, de_percent

    """
    def mean(data):
        return sum(data) / len(data)

    def var(data):
        mu = mean(data)
        return sum([(point - mu) ** 2 for point in data]) / len(data)
    """


