# idessem

> Pacote Python para leitura e escrita dos arquivos de entrada e saída do modelo DESSEM.

[![CI](https://github.com/rjmalves/idessem/actions/workflows/main.yml/badge.svg)](https://github.com/rjmalves/idessem/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/rjmalves/idessem/branch/main/graph/badge.svg?token=HA31U1FWM4)](https://codecov.io/gh/rjmalves/idessem)
[![PyPI version](https://img.shields.io/pypi/v/idessem)](https://pypi.org/project/idessem/)
[![Python versions](https://img.shields.io/pypi/pyversions/idessem)](https://pypi.org/project/idessem/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentacao](https://img.shields.io/badge/docs-online-blue)](https://rjmalves.github.io/idessem/)

O `idessem` é um pacote Python para manipulação dos arquivos de entrada e saída do modelo [DESSEM](https://www.cepel.br/linhas-de-pesquisa/dessem/), desenvolvido pelo [CEPEL](http://www.cepel.br) e utilizado para a programação da operação do Sistema Interligado Nacional (SIN).

## Funcionalidades

- Leitura e escrita dos arquivos de entrada e saída do DESSEM, com suporte a mais de 43 classes de arquivos no módulo `dessem` e utilitários no módulo `libs`
- Dados tabulares expostos como `DataFrame` do [pandas](https://pandas.pydata.org/), prontos para análise e visualização
- Interface orientada a objetos consistente: cada arquivo corresponde a uma classe com método `read` e, quando aplicável, método `write`
- Modelos estruturados com tipagem estática, compatíveis com ferramentas de análise estática e autocompletar em IDEs

## Exemplo Rapido

Leitura do arquivo de entrada `entdados.dat` e acesso aos dados de usinas hidráulicas como DataFrame:

```python
from idessem.dessem.entdados import Entdados

arq = Entdados.read("./entdados.dat")
df_uh = arq.uh(df=True)
```

Leitura de um arquivo de saída e acesso aos dados de operação:

```python
from idessem.dessem.pdo_sist import PdoSist

arq_sist = PdoSist.read("./PDO_SIST.DAT")
arq_sist.tabela
```

## Instalacao

O `idessem` é compatível com Python 3.11, 3.12, 3.13 e 3.14.

Instalação a partir do PyPI:

```
pip install idessem
```

Instalação da versão de desenvolvimento diretamente do repositório:

```
pip install git+https://github.com/rjmalves/idessem
```

## Documentacao

A documentação completa do pacote está disponível em [rjmalves.github.io/idessem](https://rjmalves.github.io/idessem/) e inclui:

- [Tutorial](https://rjmalves.github.io/idessem/geral/tutorial.html) — exemplos de leitura, escrita e modificação de arquivos
- [Arquitetura](https://rjmalves.github.io/idessem/geral/arquitetura.html) — estrutura interna do pacote e do framework cfinterface
- [Perguntas Frequentes](https://rjmalves.github.io/idessem/geral/faq.html) — dúvidas comuns dos usuários
- [Guia de Desempenho](https://rjmalves.github.io/idessem/geral/desempenho.html) — características de performance e resultados de benchmarks
- [Referencia da API](https://rjmalves.github.io/idessem/referencia) — documentação de todas as classes e propriedades públicas

## Contribuindo

Contribuições são bem-vindas. Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para instruções sobre como configurar o ambiente de desenvolvimento, executar os testes e enviar pull requests.

## Licenca

Distribuído sob a licença [MIT](LICENSE.md).
