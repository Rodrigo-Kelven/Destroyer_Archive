# Destroyer_Archive

Um script construido para fins educacionais.
A construção deste script se deve a curiosidade de como os dados podem ser "apagados/sobre-escritos" ou se tornar inutilizável.

## Uma breve explicação
### O que é um Byte?

Um byte é uma unidade básica de armazenamento de dados em computação e telecomunicações. 
Ele é composto por 8 bits, onde cada bit pode ter um valor de 0 ou 1. Portanto, um byte pode representar 256 valores diferentes (de 0 a 255). Os bytes são usados para codificar informações, como caracteres em texto, números, imagens e outros tipos de dados.

Por exemplo, na codificação ASCII, o caractere 'A' é representado pelo byte 65, enquanto o caractere 'B' é representado pelo byte 66. Em sistemas de arquivos, os dados são armazenados em bytes, e a manipulação de arquivos geralmente envolve a leitura e escrita de bytes.

## Como os Dados são Sobrescritos Neste Script

### No script, a função alterar_todos_os_bytes realiza a sobrescrita de todos os bytes de um arquivo da seguinte maneira:

  - Leitura do Arquivo: O arquivo é aberto em modo de leitura e escrita binária ("r+b"). O conteúdo do arquivo é lido completamente em uma variável.
  - Criação de Novo Conteúdo: Um novo bytearray é criado para armazenar os bytes alterados. Para cada byte no conteúdo original, um novo byte aleatório é gerado usando random.randint(0, 255), que produz um valor entre 0 e 255.
  - Substituição de Bytes: Cada byte original é substituído por um byte aleatório. Isso é feito em um loop que percorre todos os bytes do conteúdo original.
  - Escrita do Novo Conteúdo: Após a modificação, o ponteiro do arquivo é movido de volta para o início (f.seek(0)), e o novo conteúdo (que agora contém apenas bytes aleatórios) é escrito de volta ao arquivo.
  - Corte do Arquivo: Se o novo conteúdo for menor que o original (o que não deve acontecer neste caso, já que estamos substituindo todos os bytes), o arquivo é cortado para garantir que não haja dados antigos restantes.


## Funcionalidades

- Sobrescreve todos os bytes de um arquivo com bytes aleatórios.
- Garante que os dados originais não possam ser recuperados.
- Implementação simples e fácil de usar.

## Melhorias

- Usar a [entropia](https://www.google.com/search?q=entropia+da+maquina&client=ubuntu-sn&hs=LBt&sca_esv=78bc5112cdd6277c&channel=fs&ei=OmuEZ5DRGoj35OUPz8rqiAs&ved=0ahUKEwiQ1rHpxPGKAxWIO7kGHU-lGrEQ4dUDCA8&uact=5&oq=entropia+da+maquina&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2VudHJvcGlhIGRhIG1hcXVpbmEyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCBAAGIAEGKIEMggQABiABBiiBEjcIFD9BVi2H3AAeAKQAQGYAZ4FoAG5FqoBCTItMi4yLjEuMrgBA8gBAPgBAZgCB6AC2hPCAgQQABhHwgIFEAAYgATCAgoQABiABBhDGIoFmAMAiAYBkAYIkgcLMS4wLjIuMS4yLjGgB8Mh&sclient=gws-wiz-serp)
  da máquina para gerar uma sequência de Bytes aleatorios, transformalos em hexadecimal, e converte-los aleatoriamente, cada hexadecimal para cada "palavra/string" do arquivo.
- Ao ser instalado ou executado, de forma automática, percorra todo o sistema, liste todos os arquivos em todas as pastas, ***não deixe o usuário interagir com a máquina*** (cortando contato com: teclado, mouse) e encrypt todo o sistema

  ## Instalação e Execução

## Clone o repositório

```bash
  git clone https://github.com/Rodrigo-Kelven/Destroyer_Archive
```
    
## Entre no diretório do projeto e de permissão

```bash
  cd Destroyer_Archive
  chmod +x Create_archive.py
  chmod +x script_destroyer.py
```

## Inicie o script criando um arqivo para ser modificado

```bash
  pyhton Create_archive.py
```

## Inicie o script para corromper os dados

```bash
  pyhton script_destroyer.py
```


# Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.

## Autores

- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
