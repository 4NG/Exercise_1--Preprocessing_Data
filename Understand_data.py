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
        di = columns.count()
        uni = columns.unique()
        de = 142193 - di
        de_percent = (de / 142193) * 100
        return di, len(uni.tolist()), de, de_percent


