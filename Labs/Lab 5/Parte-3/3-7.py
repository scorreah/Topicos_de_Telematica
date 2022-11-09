
from mrjob.job import MRJob

lista = []
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        lista1 = [int(movie), float(rating)]
        yield genre, lista1

    def reducer(self, genre, values):
        l = list(values)
        mejor = 0
        peor = 10000000000000000
        mejor_pel = 0
        peor_pel = 0
        for i in l:
            if i[1]>mejor:
                if mejor != 0 and mejor < peor:
                    peor_pel = mejor_pel
                    peor = mejor
                mejor_pel = i[0]
                mejor = i[1]
            elif i[1]<peor:
                peor_pel = i[0]
                peor = i[1]
        yield genre, (mejor_pel, peor_pel)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
    
