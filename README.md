# idessem

[![CI](https://github.com/rjmalves/idessem/actions/workflows/main.yml/badge.svg)](https://github.com/rjmalves/idessem/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/rjmalves/idessem/branch/main/graph/badge.svg?token=HA31U1FWM4)](https://codecov.io/gh/rjmalves/idessem)
[![PyPI](https://img.shields.io/pypi/v/idessem)](https://pypi.org/project/idessem/)
![Python](https://img.shields.io/pypi/pyversions/idessem)
![License](https://img.shields.io/pypi/l/idessem)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://rjmalves.github.io/idessem/)

O `idessem` é um pacote Python para manipulação dos arquivos de entrada e saída do modelo [DESSEM](https://www.cepel.br/linhas-de-pesquisa/dessem/), desenvolvido pelo CEPEL e utilizado para a programação da operação do Sistema Interligado Nacional (SIN).

## Funcionalidades

- Leitura e escrita dos arquivos de entrada e saída do DESSEM, com suporte a mais de 43 classes de arquivos no módulo `dessem` e utilitários no módulo `libs`
- Acesso facilitado aos dados por meio de DataFrames do pandas, permitindo análise e visualização imediatas
- Modelos estruturados com tipagem estática (OOP), compatíveis com ferramentas de análise estática e autocompletar em IDEs
- Construído sobre o framework [cfinterface](https://github.com/rjmalves/cfi), que fornece a infraestrutura de leitura e escrita de arquivos de formato fixo

## Exemplo Rápido

```python
from idessem.dessem.entdados import Entdados

arq = Entdados.read("./entdados.dat")
df_uh = arq.uh(df=True)
```

## Instalação

O `idessem` requer Python >= 3.10 e [cfinterface](https://github.com/rjmalves/cfi).

Via pip:

```bash
pip install idessem
```

Via uv:

```bash
uv add idessem
```

Desenvolvimento:

```bash
pip install -e ".[dev]"
```

## Documentação

Acesse https://rjmalves.github.io/idessem/ para guias, tutoriais e referência da API.

## Contribuição

Contribuições são bem-vindas. Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes de desenvolvimento, configuração do ambiente e fluxo de pull requests.

## Licenca

Distribuido sob a licenca MIT. Autores: Rogerio Alves e Mariana Noel.
