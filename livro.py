class Livro:
    def __init__(self, titulo, autor, isbn, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.numero_paginas = numero_paginas
        self.emprestado = False