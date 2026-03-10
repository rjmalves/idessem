Como contribuir?
=================

Setup de Desenvolvimento
------------------------

O *idessem* é desenvolvido sobre o framework `cfinterface <https://github.com/rjmalves/cfi>`_, que fornece as abstrações para modelagem de arquivos em formato fixo (BlockFile, SectionFile e RegisterFile). Para detalhes sobre a arquitetura interna, consulte a `documentação do cfinterface <https://github.com/rjmalves/cfi>`_.



Instale as dependências de desenvolvimento:

.. code-block:: bash

    git clone https://github.com/rjmalves/idessem.git
    cd idessem
    pip install -e ".[dev]"

Ou com ``uv``:

.. code-block:: bash

    uv sync --extra dev

.. warning::

    Não envie mudanças de documentação para o repositório. A documentação é gerada automaticamente pelos scripts de CI.


Diretrizes de Modelagem
-----------------------

Cada arquivo DESSEM é mapeado para uma classe em `PascalCase`:

- `dessemarq.dat` → :ref:`DessemArq <dessemarq>`
- `entdados.dat` → :ref:`Entdados <entdados>`
- `DES_LOG_RELATO.DAT` → :ref:`DesLogRelato <des_log_relato>`
- `PDO_SIST.DAT` → :ref:`PdoSist <pdo_sist>`

Dados tabulares são representados como :obj:`~pandas.DataFrame` (normalizados quando possível).

Propriedades e colunas em `snake_case`. Nomenclatura padrão para evitar ambiguidades:

- Usinas: `nome_usina`, `codigo_usina`
- Submercados: `nome_submercado`, `codigo_submercado`
- REE: análogo a submercados


Convenções de Código
--------------------

O *idessem* requer conformidade com qualidade de código e testes em CI para releases.

**PEP8 e Formatação**: Siga `PEP8 <https://peps.python.org/pep-0008/>`_ (exceção: `E203 <https://www.flake8rules.com/rules/E203.html>`_). Use `ruff-format <https://docs.astral.sh/ruff/formatter/>`_ para formatação automática.

**Tipagem Estática**: Todas as variáveis devem ter tipos inferíveis. Não use tipos que mudem em tempo de execução.


Testes
------

Execute antes de ``git push``:

.. code-block:: bash

    pytest ./tests
    mypy ./idessem
    ruff check ./idessem

O *idessem* usa:
- `pytest <https://pytest.org>`_ para testes
- `ruff check <https://docs.astral.sh/ruff/linter/>`_ para lint
- `mypy <http://mypy-lang.org/>`_ para tipagem estática (CI)
