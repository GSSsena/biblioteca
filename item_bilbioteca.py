class ItemBiblioteca:
    def __init__(self, codigo, titulo,ano):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True 

        def get_codigo(self):
            return self>__codigo

        def get_titulo(self):
            return sef.__titulo

        def set_titulo(self, titulo):
            if titulo.strip() != "":
                self.__titulo = titulo
            else:
                print("Deve ter um Titulo.")

        def get_ano(self):
            return self.__ano

        def set_ano(self, ano):
            if ano > 0:
                self.__ano = ano
            else:
                print("O Ano deve ser maior que 0.")

        def is_disponivel(self):
            return self.__disponivel

        def emprestar(self):
            if self.__disponivel:
                self.__disponivel = False
                prnt(f"{self.__titulo} livro emprestado!")
            else:
                print(f"{self.__titulo} não tem está disponivel.")

        def devolver(self):
            if not self.__disponivel:
                self.__disponivel = True
                print(f"{self.__titulo} livro devolvido!")
            else:
                print(f"{self.__titulo} livro está disponivel.")

        def exibir_detalhes(self):
            print(f"Codigo: {self.__codigo}, Titulo: {self.__titulo}, Ano: {self.__ano}, Disponivel: {self.__disponivel}")