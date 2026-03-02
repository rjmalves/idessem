# Guia de Migração

## v1.1.0 para v1.2.0

### Sem alterações na API pública

A atualização de v1.1.0 para v1.2.0 não introduz alterações na API pública. Todas as classes, métodos e propriedades existentes continuam funcionando da mesma forma. As mudanças são internas e transparentes para o usuário.

### Requisito de cfinterface

A dependência `cfinterface` foi atualizada para `>= 1.9.0`. Usuários que instalam o `idessem` via `pip` ou `uv` receberão esta versão automaticamente pela restrição no `pyproject.toml`. Se a cfinterface for gerenciada manualmente, é necessário atualizá-la para a versão 1.9.0 ou superior.

### Melhorias de desempenho

- A leitura do arquivo `pdo_operacao` foi otimizada com a substituição do padrão de concatenação incremental de DataFrames por concatenação única (`pd.concat`), resultando em ganho significativo para arquivos com muitos blocos.
- O tempo de importação do módulo `idessem.dessem` foi reduzido com a implementação de lazy imports (PEP 562). As classes são carregadas sob demanda no primeiro acesso.

### Qualidade de código

- Modo strict do mypy habilitado para todos os módulos (`idessem.dessem.*`, `idessem.libs.*`, `idessem.config`), com anotações de tipo em todos os arquivos de produção.
- Todos os comentários `# type: ignore` foram substituídos por códigos de erro específicos (ex: `# type: ignore[override]`).
- Suite de benchmarks criada com `pytest-benchmark` para monitoramento de desempenho de leitura.
