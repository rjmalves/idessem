# Changelog

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Nao Publicado]

## [1.4.0] - 2026-09-17

### Adicionado

- Suporte aos registros de geração mínima e máxima por conjunto e por usina do arquivo `uch.csv` (`UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO` e `UCH-GERACAO-MINIMA-MAXIMA-USINA`) e ao campo de tipo de agregação (`tipo_agregacao`) do registro `UCH-OPCAO-PADRAO-USINA` (@carlosribeiro06)

### Modificado

- Compatibilização da leitura do arquivo `uch.csv` com o novo padrão de dados de Unit Commitment Hidráulico (UCH) do DESSEM. Diversos registros e métodos da classe `Uch` foram renomeados para refletir os novos identificadores — por exemplo, `UchOpcaoUsina` para `UchOpcaoPadraoUsina`, `UchOpcaoPadraoData` para `UchPadraoData` e `UchOpcaoUnidadeVazioPadrao` para `UchOpcaoVazioUnidade` — e foram removidos os registros e métodos que deixaram de existir no novo padrão, incluindo o turbinamento mínimo/máximo por unidade e as variantes por conjunto e por usina de operação em vazio, Ton/Toff, consumo de água em vazio, limite de mudança de status em vazio e custo de partida

## [1.3.0] - 2026-06-09

### Adicionado

- Suporte ao formato estendido do arquivo `hidr.dat`, com os coeficientes dos polinômios volume-cota e cota-área em precisão dupla (registros de 832 bytes), através do novo registro `RegistroUHEHidrF64`. A classe `Hidr` detecta o formato automaticamente pelo tamanho do arquivo, reconhecendo cadastros de 320 ou 600 usinas em registros de 792 ou 832 bytes, com possibilidade de forçar via `version="f32"` ou `version="f64"`.
- Propriedade `tamanho_registro` e método `converte_tamanho_registro` na classe `Hidr`, permitindo inspecionar e converter entre os formatos de precisão simples e dupla.

### Modificado

- Montagem vetorizada do DataFrame `cadastro` da classe `Hidr` (construção em lote em vez de linha a linha), reduzindo significativamente o tempo de leitura de arquivos `hidr.dat`. As colunas inteiras passam a usar o tipo nullable `Int64`.

## [1.2.1] - 2026-03-17

### Corrigido

- Garantia de que as colunas `codigo_ree` e `nome_ree` estejam sempre presentes no DataFrame retornado por `PdoEcoUsih.tabela`, independente da versão do DESSEM utilizada [#92](https://github.com/rjmalves/idessem/issues/92)

## [1.2.0] - 2026-03-10

### Modificado

- Modernização da infraestrutura de CI/CD: migração para release com OIDC trusted publishing e deploy de documentação via GitHub Pages
- Adoção de ruff como linter e formatador, mypy em modo strict para todos os módulos
- Adoção de pre-commit hooks para verificação automática de qualidade
- Requisito de versão de Python atualizado para `>=3.11`, com suporte a 3.11, 3.12, 3.13 e 3.14
- Dependências atualizadas: cfinterface `>=1.9.0`, pandas `>=3.0.0`, numpy `>=2.2.1`
- Documentação expandida com guias de arquitetura, desempenho, FAQ e tutorial
- README e metadados do projeto alinhados com convenções do inewave

## [1.1.0] - 2026-02-02

### Adicionado

- Inclusão de suporte aos arquivos `PDO_CMOSIST`, `PDO_ELEV` e `PDO_OPER_USIH` (@rdlobato)

### Modificado

- Ajustes de testes e documentação para suporte a pandas `>= 3.0.0`

## [1.0.0] - 2025-02-21

### Adicionado

- Primeira major release
- Suporte à leitura da maioria dos arquivos de entrada do modelo DESSEM
- Inclusão de suporte aos arquivos de entrada: `respot.dat` [#77](https://github.com/rjmalves/idessem/issues/77), `deflant.dat` [#76](https://github.com/rjmalves/idessem/issues/76), `areacont.dat` [#75](https://github.com/rjmalves/idessem/issues/75), `dadvaz.dat` [#44](https://github.com/rjmalves/idessem/issues/44) e `desselet.dat` [#41](https://github.com/rjmalves/idessem/issues/41)
- Inclusão de suporte aos arquivos de saída: `log_inviab.dat` [#79](https://github.com/rjmalves/idessem/issues/79), `pdo_cmobar.dat` [#78](https://github.com/rjmalves/idessem/issues/78), `pdo_oper_titulacao_contratos` e `pdo_oper_titulacao_usinas` [#80](https://github.com/rjmalves/idessem/issues/80), `pdo_somflux.dat` [#81](https://github.com/rjmalves/idessem/issues/81)
- Inclusão de suporte aos novos campos do arquivo de entrada `operuh.dat`

### Modificado

- Métodos le_arquivo e escreve_arquivo deprecados
- Gestão do projeto através de arquivo `pyproject.toml` em substituição ao par `setup.py` + `requirements.txt`
- Requisito de versão de Python atualizado para `>=3.10`
- Dependência da cfinterface atualizada para [v1.8.0](https://github.com/rjmalves/cfi/releases/tag/v1.8.0)
- Refactor da modelagem utilizada para dados provenientes das LIBS: criado o submódulo `libs`, de forma que o usuário possa realizar a importação com `from idessem.libs import ...`.
- Modelagem de entidades das LIBS não é feita baseada nos arquivos fornecidos nos casos de exemplo das versões do modelo, mas sim baseado nas entidades envolvidas na informação, semelhante à divisão feita no site da documentação oficial [LIBS](https://see.cepel.br/manual/libs/latest/index.html)

### Corrigido

- Correção na leitura do arquivo de entrada `renovaveis.dat` [#73](https://github.com/rjmalves/idessem/issues/73)

[Nao Publicado]: https://github.com/rjmalves/idessem/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/rjmalves/idessem/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/rjmalves/idessem/compare/v1.1.1...v1.2.0
[1.1.0]: https://github.com/rjmalves/idessem/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/rjmalves/idessem/releases/tag/v1.0.0
