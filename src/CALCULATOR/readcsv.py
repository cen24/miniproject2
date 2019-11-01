import pandas as pd


class read:


    def read_csv(obj):
        data = pd.read_csv(obj)
        data = data.values

        a = []
        b = []
        c = []
        for var in range(len(data)):
            a.append(data[var][0])
            b.append(data[var][1])
            c.append(data[var][2])
        z = [a, b, c]

        return z
    def read_array(obj):
        data = pd.read_csv(obj)
        data = data.values

        return data