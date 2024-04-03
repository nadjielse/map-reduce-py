# Framework Map Reduce

Este repositório contém uma implementação do framework da Google, o Map Reduce.
Neste projeto foram implementados dois casos de uso para o framework, um cenário
no qual ele é usado para contar palavras em um arquivo dividido em _chunks_, e
outro no qual ele é usado para separar as linhas que combinam com certa busca
também em arquivos divididos em _chunks_.

Este repositório também conta com um programa para gerar arquivos de exemplo
para que o algoritmo principal possa ser executado.

## Execução
As saídas dos programas vão ser armazenadas em um arquivo final chamado
`output.txt` que vai ficar no mesmo diretório desse projeto.

### Word Counter
Para executar o programa de contagem de palavras, você vai precisar usar o
Python digitando no terminal, enquanto neste diretório:

```
python mainWordCounter.py
```

Isso vai automaticamente gerar o arquivo de entrada separado em _chunks_ para
ser processado pelo algoritmo.

### Grep
Para executar o programa de busca de linhas por texto (string ou expressão
regular), você vai precisar executar com o Python esse outro arquivo:

```
python mainGrep.py <search> <is_regex>
```

Para esse programa, você vai precisar passar uns argumentos:

- `search`: O primeiro argumento é a `string` a qual você deseja buscar;
- `is_regex`: O segundo argumento é um booleano (`True` ou `False`) indicando
se você deseja realizar a busca tratando a `string` passada como `string` normal
ou como expressão regular.
