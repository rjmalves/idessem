# Como Contribuir

## Setup

1. Fork e clone:

```bash
git clone https://github.com/<seu-usuario>/idessem.git
cd idessem
```

2. Instale dependências (com `uv` ou `pip`):

```bash
uv sync --extra dev
# ou: pip install -e ".[dev]"
```

3. Instale pre-commit hooks:

```bash
pre-commit install
```

## Ferramentas de Qualidade de Código

- **ruff**: Lint e formatação automática (executados via pre-commit hooks)
- **mypy**: Verificação de tipagem (configurado como hook manual; execute com `uv run mypy ./idessem`)
- **pre-commit**: Orquestra ruff antes de cada commit

Executar todos os hooks manualmente:

```bash
pre-commit run --all-files
```

## Testes

Execute testes com:

```bash
pytest ./tests
# ou com uv: uv run pytest ./tests
# paralelo: pytest ./tests -n auto
```

## Convenções de Modelagem

- Arquivos DESSEM são mapeados para classes `PascalCase` (ex: `entdados.dat` → `Entdados`)
- Propriedades em `snake_case`
- Dados tabulares como `pandas.DataFrame`, normalizados conforme normas relacionais
- Coluna padrão para usinas: `nome_usina`, `codigo_usina`; submercados: `nome_submercado`, `codigo_submercado`

Consulte a [página de arquitetura](https://rjmalves.github.io/idessem/geral/arquitetura.html) para detalhes completos.

## Pull Requests

1. Crie um branch descritivo:

```bash
git checkout -b feat/nome-da-funcionalidade
```

2. Teste e verifique qualidade:

```bash
pytest ./tests
pre-commit run --all-files
```

3. Push e abra PR contra `main`:

```bash
git push origin feat/nome-da-funcionalidade
```

## Convenções de Commits

Siga [commits convencionais](https://www.conventionalcommits.org/):

- `feat:` — nova funcionalidade
- `fix:` — correção de bug
- `refactor:` — refatoração sem mudança de comportamento
- `test:` — adição ou correção de testes
- `docs:` — alterações na documentação
- `chore:` — manutenção (dependências, CI, configurações)
