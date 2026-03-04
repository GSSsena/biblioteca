estrutura inicial do projeto

Criou pasta biblioteca-poo e arquivos vazios (main.py, item_biblioteca.py, livro.py, revista.py, biblioteca.py, README.md)

cria classe ItemBiblioteca com encapsulamento

Implementou atributos privados (__codigo, __titulo, __ano, __disponivel)

Criou getters e setters com validação

adiciona emprestar e devolver no ItemBiblioteca

Implementou métodos emprestar(), devolver()

Criou método polimórfico exibir_detalhes() como NotImplementedError

cria classe Livro herdando ItemBiblioteca

Implementou atributos __autor e __num_paginas

Sobrescreveu exibir_detalhes() usando f-strings


cria classe Revista herdando ItemBiblioteca

Implementou atributos __edicao e __mes

Sobrescreveu exibir_detalhes() usando f-strings
