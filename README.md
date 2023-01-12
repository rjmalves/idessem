# idessem


![tests](https://github.com/rjmalves/idessem/workflows/tests/badge.svg)  
[![codecov](https://codecov.io/gh/rjmalves/idessem/branch/main/graph/badge.svg?token=HA31U1FWM4)](https://codecov.io/gh/rjmalves/idessem)

O `idessem` é um pacote Python para manipulação dos arquivos de entrada e saída do programa [DESSEM](https://www.cepel.br/linhas-de-pesquisa/dessem/). O DESSEM é desenvolvido pelo [CEPEL](http://www.cepel.br) e utilizado para a programação da operação do Sistema Interligado Nacional (SIN).

O idessem oferece:

- Meios para leitura dos arquivos de entrada e saída do DESSEM

- Armazenamento e processamento de dados otimizados com o uso de NumPy e Pandas

- Dados estruturados em modelos com o uso do paradigma de orientação a objetos (OOP)

- Utilidades de escritas dos arquivos de entrada do DESSEM para elaboração automatizada de estudos

Com idessem é possível ler os arquivos de texto, característicos do DESSEM, para poupar processamento futuro e reduzir o tempo de execução.

## Instalação

O idessem é compatível com versões de Python >= 3.8 e é construído com base no framework [cfinterface](https://github.com/rjmalves/cfi), que deve sempre ser mantido na versão mais atualizada para a distribuição de Python instalada.

Em posse de uma instalação local de Python, é recomendado que se use um ambiente virtual para instalação de módulos de terceiros, sendo que o idessem não é uma exceção. Para mais detalhes sobre o uso de ambientes virtuais, recomenda-se a leitura do recurso oficial de Python para ambientes virtuais: [venv](https://docs.python.org/3/library/venv.html).

```
python -m pip install idessem
```

## Documentação

Guias, tutoriais e as referências podem ser encontrados no site oficial do pacote: https://rjmalves.github.io/idessem
