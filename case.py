'''
    uso do with na Orientação a Objetos em Python
    para abertura e fechamento de sessões
'''


class AlgumaCoisa:
    def __enter__(self):
        print('Estou entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo", {exc_type, exc_val, exc_tb})


with AlgumaCoisa() as something:
    print("estou no meio")
    # raise Exception("Erro teste")
