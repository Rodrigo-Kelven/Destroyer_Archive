import os
import random

def alterar_todos_os_bytes():
    # Lê o conteúdo do arquivo
    with open("exemplo.txt", "r+b") as f:
        # Lê todo o conteúdo do arquivo
        conteudo = f.read()
        
        # Cria uma nova lista de bytes alterados
        novo_conteudo = bytearray()
        
        for byte in conteudo:
            # Substitui cada byte por um byte aleatório
            novo_byte = random.randint(0, 255)  # Gera um byte aleatório
            novo_conteudo.append(novo_byte)  # Adiciona o novo byte à nova lista
        
        # Volta ao início do arquivo e escreve o novo conteúdo
        f.seek(0)
        f.write(novo_conteudo)
        
        # Se o novo conteúdo for menor que o original, corta o arquivo
        f.truncate()

alterar_todos_os_bytes()
