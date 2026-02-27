from item_biblioteca import item_biblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def get_autor(self):
        returnself.__autor

    def set_autor(self, autor):
        if autor:
            self.__autor = autor
        else:
            print("Autor deve ter um nome.")

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, num_paginas):
        if num_paginas > 0:
            self.__num_paginas = num_paginas
        else:
            print("O numero da pagina do livro deve ser acima de 0.")

    def exibir_detalhes(self):
        status = "Disponivel"  if self.__disponivel()else "Emprestado"
        print(f"[Livro] Codigo: {self.get_codigo()}, Titulo: {self.get_titulo()}. "
        f"Autor: {self.__autor}, paginas:{self.__num_pagimas}, Ano: {self.get_ano()}, status: {self}")