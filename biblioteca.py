from pessoa import Pessoa
from livro import Livro
from emprestimo import Emprestimo
from datetime import datetime


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.pessoas = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def emprestar_livro(self, livro, pessoa, data_emprestimo, data_devolucao_prevista):
        if not livro.emprestado:
            livro.emprestado = True
            emprestimo = Emprestimo(pessoa, livro, data_emprestimo, data_devolucao_prevista)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            return None

    def devolver_livro(self, livro, pessoa, data_devolucao_real):
        for emprestimo in self.emprestimos:
            if emprestimo.livro == livro and emprestimo.pessoa == pessoa and emprestimo.data_devolucao_real is None:
                emprestimo.devolver(data_devolucao_real)
                livro.emprestado = False
                break

    def relatorio_mensal(self, mes):
        print(f"Relatório de Empréstimos para o Mês {mes}:")
        for emprestimo in self.emprestimos:
            if emprestimo.data_emprestimo.month == mes:
                print(f"Livro: {emprestimo.livro.titulo}, "
                      f"Pessoa: {emprestimo.pessoa.nome}, "
                      f"Data Empréstimo: {emprestimo.data_emprestimo}, "
                      f"Data Devolução Prevista: {emprestimo.data_devolucao_prevista}, "
                      f"Data Devolução Real: {emprestimo.data_devolucao_real}")


# Exemplo
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando pessoas
    pessoa1 = Pessoa("Brayan", "123", "Rua A, 123")
    pessoa2 = Pessoa("Diogo", "456", "Rua B, 456")
    biblioteca.adicionar_pessoa(pessoa1)
    biblioteca.adicionar_pessoa(pessoa2)

    # Adicionando livros
    livro1 = Livro("Livro A", "Autor A", "111-111", 300)
    livro2 = Livro("Livro B", "Autor B", "222-222", 150)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Empréstimos
    data_emprestimo = datetime(2024, 8, 1)
    data_devolucao_prevista = datetime(2024, 8, 15)
    biblioteca.emprestar_livro(livro1, pessoa1, data_emprestimo, data_devolucao_prevista)

    data_devolucao_real = datetime(2024, 8, 10)
    biblioteca.devolver_livro(livro1, pessoa1, data_devolucao_real)

    # Relatório mensal
    biblioteca.relatorio_mensal(8)