# v1.0.0
 
- Primeira major release
- Suporte à leitura da maioria dos arquivos de entrada do modelo DESSEM
- Inclusão de suporte aos arquivos de entrada: `respot.dat` [#77](https://github.com/rjmalves/idessem/issues/77), `deflant.dat` [#76](https://github.com/rjmalves/idessem/issues/76), `areacont.dat` [#75](https://github.com/rjmalves/idessem/issues/75), `dadvaz.dat` [#44](https://github.com/rjmalves/idessem/issues/44) e `desselet.dat` [#41](https://github.com/rjmalves/idessem/issues/41)
- Inclusão de suporte aos arquivos de saída: `log_inviab.dat` [#79](https://github.com/rjmalves/idessem/issues/79), `pdo_cmobar.dat` [#78](https://github.com/rjmalves/idessem/issues/78), `pdo_oper_titulacao_contratos` e `pdo_oper_titulacao_usinas` [#80](https://github.com/rjmalves/idessem/issues/80), `pdo_somflux.dat` [#81](https://github.com/rjmalves/idessem/issues/81)
- Correção na leitura do arquivo de entrada `renovaveis.dat` [#73](https://github.com/rjmalves/idessem/issues/73)
- Inclusão de suporte aos novos campos do arquivo de entrada `operuh.dat`
- Métodos le_arquivo e escreve_arquivo deprecados
- Gestão do projeto através de arquivo `pyproject.toml` em substituição ao par `setup.py` + `requirements.txt`
- Requisito de versão de Python atualizado para `>=3.10`
- Dependência da cfinterface atualizada para [v1.8.0](https://github.com/rjmalves/cfi/releases/tag/v1.8.0)
- Refactor da modelagem utilizada para dados provenientes das LIBS: criado o submódulo `libs`, de forma que o usuário possa realizar a importação com `from idessem.libs import ...`.
- Modelagem de entidades das LIBS não é feita baseada nos arquivos fornecidos nos casos de exemplo das versões do modelo, mas sim baseado nas entidades envolvidas na informação, semelhante à divisão feita no site da documentação oficial [LIBS](https://see.cepel.br/manual/libs/latest/index.html)
