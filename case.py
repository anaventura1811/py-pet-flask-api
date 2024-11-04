'''
    Uso do with na Orientação a Objetos em Python
    para abertura e fechamento de sessões

    exc_type: O tipo de exception que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None.

    exc_val: O value correspondente à exception que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None.

    exc_tb: O traceback (rastreamento de pilha) associado à exception ocorrida.
    Se não ocorreu nenhuma exceção, este parâmetro também será None.
'''


class AlgumaCoisa:
    def __enter__(self):
        print('Estou entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo", {exc_type, exc_val, exc_tb})


with AlgumaCoisa() as something:
    print("estou no meio")
    # raise Exception("Erro teste")
