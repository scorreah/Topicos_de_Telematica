
from mrjob.job import MRJob

lista = []
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        lista = [int(user), float(rating)]
        yield movie, lista

    def reducer(self, movie, values):
        l = list(values)
        sum = 0
        rate = 0
        for i in l:
            sum += 1
            rate += i[1]
        yield movie, (sum, rate/len(l))

if __name__ == '__main__':
    MRWordFrequencyCount.run()
