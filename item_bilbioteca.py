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

