from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [float(price), date]
        yield company, lista

    def reducer(self, company, values):
        l = list(values)
        menor = 10000000000
        mayor = 0
        date1 = 0
        date2 = 0
        for i in l:
            if i[0]>mayor:
                if mayor != 0 and mayor < menor:
                    date1 = date2
                    menor = mayor
                date2 = i[1]
                mayor = i[0]
            elif i[0]<menor:
                date1 = i[1]
                menor = i[0]
        yield company, (date1, date2)

if __name__ == '__main__':
    MRWordFrequencyCount.run()