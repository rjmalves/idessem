.. _instalacao:

Instalação
==========

O *idessem* requer Python >= 3.10. Use um `ambiente virtual <https://docs.python.org/3/library/venv.html>`_.

.. note::

    O *idessem* depende de ``cfinterface>=1.8.0,<=1.8.3`` para compatibilidade com a API interna.

Versão Oficial
--------------

.. code-block:: bash

    pip install idessem
    pip install --upgrade idessem  # atualizar
    pip install --upgrade idessem==x.y.z  # versão específica

Com uv:

.. code-block:: bash

    uv add idessem

Desenvolvimento
---------------

Clone e instale dependências:

.. code-block:: bash

    git clone https://github.com/rjmalves/idessem.git
    cd idessem
    pip install -e ".[dev]"

Ou com ``uv``:

.. code-block:: bash

    uv sync --extra dev

Consulte `CONTRIBUTING.md <https://github.com/rjmalves/idessem/blob/main/CONTRIBUTING.md>`_ para setup completo e fluxo de contribuição.

Verificar Instalação
--------------------

.. code-block:: bash

    python -c "import idessem; print(idessem.__version__)"
