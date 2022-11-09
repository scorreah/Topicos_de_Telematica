from mrjob.job import MRJob
lista_constantes = []
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, float(price)

    def reducer(self, company, values):
        l = list(values)
        estado = True
        actual = 0
        for i in l:
            if i < actual:
                estado  = False
                break
            actual = i
        if estado:  
            lista_constantes.append(company)      
            yield company, estado

if __name__ == '__main__':
    MRWordFrequencyCount.run()
    print(lista_constantes)