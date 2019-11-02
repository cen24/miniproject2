import pandas as pd
import csv


class read:


    def read_csv(obj):
        # data = pd.read_csv(obj)
        # data = data.values

        with open(obj, 'r') as f:

            reader = csv.reader(f)
            next(f)
            data = list(reader)

        a = []
        b = []
        c = []
        for var in range(len(data)):
            a.append(float(data[var][0]))
            b.append(float(data[var][1]))
            c.append(float(data[var][2]))
        z = [a, b, c]

        return z
    def read_array(obj):
        data = pd.read_csv(obj)
        data = data.values

        return data

    def read_csv2(obj):


        with open(obj, 'r') as f:

            reader = csv.reader(f)
            next(f)
            data = list(reader)

        a = []
        b = []

        for var in range(len(data)):
            a.append(float(data[var][0]))
            b.append(float(data[var][1]))

        z = [a, b]
        return z