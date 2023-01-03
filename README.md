# Jogos com Python

### Tecnologias utilizadas
Python e PyCharm.

### Desafio
https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

### Descrição
Projeto realizado nos cursos de Python (prof. Nico Steppat) da Formação: Iniciando com Engenharia de Dados da Alura com modificações feitas por mim.

Temos três scripts:
1) jogos.py onde há toda a lógica do menu inicial e da escolha do jogo pelo usuário;
2) adivinhacao.py é um jogo onde o usuário deve acertar um número secreto gerado pelo programa, a cada chute, o sistema informa se o número secreto é maior ou menor do que aquele foi digitado. O usuário inicia o jogo com 1000 pontos e vai perdendo pontos de acordo com a distância do valor que chutou até o número secreto;
3) forca.py simula um jogo em que é necessário adivinhar as letras que formam uma palavra secreta, o número de tentativas é definido de acordo com o tamanho dessa palavra.

Modificações gerais:
- Melhoria no menu dos jogos: com opção de sair, de jogar novamente, etc;
- Tratamento de erros em todos os menus para valores inválidos digitados pelo usuário.

Modificação no Jogo da Adivinhação:
- Aceitar apenas números digitados pelo usuário no chute.

Modificação no Jogo da Forca:
- Aceitar acentos ou cedilhas digitados pelo usuário no chute da letra;
- Ajuste para o jogo funcionar com palavras compostas;
- Permitir apenas letras no chute da letra;
- Definir a quantidade máxima de chute de letras de acordo com a quantidade de caracteres da palavra secreta;
- Adição de outras categorias no jogo;
- Exibição de dica da palavra secreta.
