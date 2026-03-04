from item_bilbioteca import ItemBiblioteca

class Revista(ItemBilioteca):
    def __init__(self, codigo, titulo, ano, edição, mes):
        super().__init__(codigo, titulo, ano)
        self.__edição = edição
        se.__mes = mes

    def exibir_detalhes(self):
        status = "Disponivel" if self.get_disponivel() else "Emprestado"
        print(f"[Revista] codigo: {self.get_codigo()} | "
        f"titulo: {self.get_titulo()} | "
        f"Edição: {self.__edicao} | "
        f"Mês: {self.__mes} | "
        f"Ano: {self.get_ano()} | "
        f"Status: {status}")
        
commit()