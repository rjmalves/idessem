.. _dessem:

DESSEM
=======


A estrutura do *idessem* padroniza os objetos de interface existentes. 
A interface com o DESSEM segue o padrão de implementar modelos para armazenar cada uma das informações existentes
nos arquivos de entrada e saída, além de classes utilitárias para gerenciar com a leitura e interpretação das informações
dos arquivos, bem como na geração de novos arquivos.

Classes são nomeadas em ``CamelCase``, enquanto funções, métodos e variáveis recebem seus nomes em ``snake_case``.


Básico da interface DESSEM
----------------------------

É recomendado que a importação seja feita sempre de forma a utilizar somente os objetos que serão de fato necessários para 
o estudo em questão. Desta forma, não é recomendado importar todo o módulo ``idessem.dessem`` ou utilizar o `wildcard` ``*``.

A importação recomendada é, por exemplo::

    >>> from idessem.dessem.pdo_sist import PdoSist

Para a leitura do arquivo `PDO_SIST.DAT`::

    >>> from idessem.dessem.pdo_sist import PdoSist
    >>>
    >>> diretorio = "/home/usuario/..."
    >>> rel = PdoSist.le_arquivo(diretorio, "PDO_SIST.DAT")
    >>> rel
    <idessem.dessem.PdoSist object at 0x000001BC7663B340>

Arquivos
---------

.. toctree::
   :maxdepth: 2

   arquivos/avl_altqueda
   arquivos/avl_desvfpha
   arquivos/avl_estatfpha
   arquivos/avl_fpha1
   arquivos/des_log_relato
   arquivos/log_matriz
   arquivos/pdo_hidr
   arquivos/pdo_oper_uct
   arquivos/pdo_sist
   arquivos/polinjus
   arquivos/hidr
   arquivos/pdo_eco_usih
