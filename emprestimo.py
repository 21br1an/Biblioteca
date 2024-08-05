class Emprestimo:
    def __init__(self, pessoa, livro, data_emprestimo, data_devolucao_prevista):
        self.pessoa = pessoa
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao_prevista = data_devolucao_prevista
        self.data_devolucao_real = None

    def devolver(self, data_devolucao_real):
        self.data_devolucao_real = data_devolucao_real