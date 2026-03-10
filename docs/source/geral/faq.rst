.. _faq:

Perguntas Frequentes (FAQ)
==========================

Esta página reúne as dúvidas mais comuns dos usuários do *idessem*, organizadas
por tema. Se a sua dúvida não estiver listada aqui, consulte o :doc:`Tutorial <tutorial>`,
a :ref:`Arquitetura <arquitetura>` ou abra uma issue no repositório do projeto.

.. contents:: Índice
   :local:
   :depth: 1


Instalação
----------

**Como instalar o idessem?**

A forma mais simples é instalar via ``pip``::

    $ pip install idessem

Alternativamente, se você utiliza o ``uv`` como gerenciador de ambientes::

    $ uv pip install idessem

Recomenda-se sempre instalar o pacote dentro de um ambiente virtual. Consulte a
:doc:`página de instalação <instalacao>` para instruções detalhadas.

**Qual versão do Python é necessária?**

O *idessem* requer **Python >= 3.10**. As versões 3.10, 3.11 e 3.12 são testadas
continuamente pela integração contínua (CI) do projeto.

.. note::

   Versões anteriores do Python (3.8 e 3.9) não são suportadas. Se você encontrar
   referências a ``>= 3.8`` em documentação mais antiga, considere-as desatualizadas
   — o requisito correto é ``>= 3.10``.

**Como instalar a versão de desenvolvimento (última versão do repositório)?**

Utilize o ``pip`` apontando diretamente para o repositório Git:

.. code-block:: shell

    $ pip install git+https://github.com/rjmalves/idessem

Para selecionar um branch ou tag específico::

    $ pip install git+https://github.com/rjmalves/idessem@v1.0.0

**Como instalar as dependências de desenvolvimento?**

O *idessem* utiliza o ``pyproject.toml`` com extras nomeados. Para instalar as
dependências de desenvolvimento, execute:

.. code-block:: shell

    $ git clone https://github.com/rjmalves/idessem.git
    $ cd idessem
    $ pip install -e ".[dev]"


Uso Geral
---------

**Como ler um arquivo do DESSEM?**

Cada arquivo do DESSEM é representado por uma classe Python. Para ler um arquivo,
utilize o método de classe ``read()``, passando o caminho do arquivo:

.. code-block:: python

    from idessem.dessem.entdados import Entdados

    arq = Entdados.read("./entdados.dat")

O método retorna uma instância da classe com todos os dados já parseados e
disponíveis como propriedades. Consulte o :doc:`Tutorial <tutorial>` para exemplos
adicionais.

**Como acessar os dados em formato DataFrame?**

As propriedades das classes do *idessem* expõem os dados tabulares como objetos
:obj:`~pandas.DataFrame`. Basta acessar a propriedade correspondente na instância
retornada pelo ``read()``:

.. code-block:: python

    from idessem.dessem.pdo_sist import PdoSist

    arq = PdoSist.read("./PDO_SIST.DAT")
    df = arq.tabela
    print(df.head())

Cada classe documenta as propriedades disponíveis e o significado de cada coluna.

**Quais arquivos suportam escrita?**

Apenas os **arquivos de entrada** do modelo DESSEM implementam o método ``write()``.
Os arquivos de saída são somente leitura.

- **Arquivos de entrada** (suportam ``read()`` e ``write()``): ``entdados.dat``,
  ``dessemarq.dat``, ``hidr.dat``, ``operuh.dat``, entre outros — são as classes
  sem prefixo ``Pdo``, ``Avl``, ``Log`` ou ``Des``.
- **Arquivos de saída** (apenas ``read()``): todos os arquivos com prefixo ``pdo_``,
  ``avl_``, ``log_`` ou ``des_log_`` — como ``PDO_SIST.DAT``, ``AVL_FPHA1.DAT``,
  ``DES_LOG_RELATO.DAT``.

.. warning::

   Tentar chamar ``write()`` em um arquivo de saída levanta ``NotImplementedError``.
   Consulte a :ref:`Arquitetura <arquitetura>` para a lista completa de classes por
   categoria.

**Como usar o versionamento com ``set_version()``?**

Alguns arquivos do DESSEM tiveram alterações de sintaxe entre versões do modelo.
O método de classe ``set_version()`` informa ao *idessem* qual versão do formato
deve ser usada na leitura:

.. code-block:: python

    from idessem.dessem.avl_fpha1 import AvlFpha1

    # Especifica a versão antes de ler o arquivo
    AvlFpha1.set_version("19.3")
    arq = AvlFpha1.read("./AVL_FPHA1.DAT")

Quando ``set_version()`` não é chamado, o *idessem* assume a versão mais recente
do arquivo. Isso pode causar erros de parsing se o arquivo foi gerado por uma
versão mais antiga do modelo DESSEM.


Compatibilidade com Versões do DESSEM
--------------------------------------

**Quais versões do DESSEM são suportadas?**

O *idessem* suporta as versões do modelo DESSEM para as quais as classes foram
implementadas e testadas. O versionamento é tratado individualmente por arquivo:
quando um arquivo possui variações de formato entre versões do modelo, o
*idessem* disponibiliza suporte às versões mais comuns por meio do método
``set_version()``.

Se você precisar ler um arquivo gerado por uma versão específica do DESSEM,
verifique a documentação da classe correspondente na :doc:`Referência da API <../referencia/dessem/index>`
para consultar quais versões são aceitas pelo ``set_version()``.

**O que acontece se eu não especificar a versão com ``set_version()``?**

Se ``set_version()`` não for chamado, será utilizada a versão mais recente
disponível para aquele arquivo. Isso é adequado para a maioria dos casos, mas
pode resultar em erros de parsing quando o arquivo foi produzido por uma versão
antiga do DESSEM cujo formato é diferente do atual.

.. code-block:: python

    from idessem.dessem.avl_fpha1 import AvlFpha1

    # Versão padrão (mais recente) — use quando o arquivo for recente
    arq_recente = AvlFpha1.read("./AVL_FPHA1.DAT")

    # Versão explícita — necessária para arquivos de versões antigas do DESSEM
    AvlFpha1.set_version("19.3")
    arq_antigo = AvlFpha1.read("./AVL_FPHA1_v19_3.DAT")


Resolução de Problemas
-----------------------

**Erro de importação do ``cfinterface`` — o que fazer?**

O *idessem* depende do framework ``cfinterface`` na faixa de versão
``>=1.8.0,<=1.8.3``. Esta faixa é fixada intencionalmente porque versões
posteriores introduziram mudanças de API incompatíveis com o *idessem*.

Se você encontrar um erro como:

.. code-block:: text

    ImportError: cannot import name 'X' from 'cfinterface'

ou mensagens de incompatibilidade de versão durante a instalação, verifique
se a versão instalada do ``cfinterface`` está dentro da faixa suportada:

.. code-block:: shell

    $ pip show cfinterface

Se necessário, force a reinstalação dentro da faixa correta:

.. code-block:: shell

    $ pip install "cfinterface>=1.8.0,<=1.8.3"

.. note::

   O ``pip install idessem`` instala automaticamente o ``cfinterface`` dentro
   da faixa compatível. O problema costuma ocorrer quando outras bibliotecas
   do ambiente atualizam o ``cfinterface`` para uma versão incompatível.
   Nesses casos, considere usar um ambiente virtual isolado.

**O pip não consegue resolver as dependências — o que fazer?**

Se o ``pip`` apresentar conflito de dependências envolvendo o ``cfinterface``,
a causa mais comum é que outro pacote no ambiente exige uma versão incompatível.
A solução recomendada é criar um ambiente virtual isolado para o *idessem*:

.. code-block:: shell

    $ python -m venv .venv
    $ source .venv/bin/activate   # Linux/macOS
    $ .venv\Scripts\activate      # Windows
    $ pip install idessem

**Erro de codificação ao ler arquivos — como resolver?**

Alguns arquivos do modelo DESSEM são gerados com codificações diferentes de
UTF-8 (por exemplo, Latin-1 / ISO-8859-1), especialmente quando contêm
caracteres especiais do português (ã, ç, é, etc.).

Se você encontrar um ``UnicodeDecodeError`` ao ler um arquivo, verifique a
documentação da classe para saber qual codificação ela espera. Em geral, os
arquivos de texto do DESSEM utilizam Latin-1.

Se o problema persistir, inspecione o arquivo com um editor hexadecimal ou
utilize o Python para detectar a codificação:

.. code-block:: python

    import chardet

    with open("./arquivo.dat", "rb") as f:
        resultado = chardet.detect(f.read())
    print(resultado)

**``AttributeError`` ao acessar uma propriedade — por quê?**

Um ``AttributeError`` ao acessar uma propriedade normalmente indica uma de
duas situações:

1. **A propriedade não existe para a versão especificada do arquivo.** Algumas
   propriedades foram adicionadas em versões mais recentes do formato. Verifique
   se você está usando a versão correta com ``set_version()``.

2. **O arquivo não foi lido com sucesso.** Se o parsing falhou silenciosamente,
   a instância pode estar em estado inconsistente. Verifique se não há erros
   ou avisos no console durante o ``read()``.

.. code-block:: python

    from idessem.dessem.entdados import Entdados

    arq = Entdados.read("./entdados.dat")

    # Se arq.uh(...) retornar None, a usina não existe no arquivo
    resultado = arq.uh(codigo_usina=999)
    if resultado is None:
        print("Usina não encontrada no arquivo.")
    else:
        print(resultado.volume_inicial)


Desempenho
-----------

**Por que ``import idessem.dessem`` é lento?**

O submódulo ``idessem.dessem`` utiliza importações diretas (eager) em seu
``__init__.py``. Isso significa que ao executar ``import idessem.dessem``,
todas as 43 classes do módulo são carregadas imediatamente na memória,
juntamente com todas as suas dependências transitivas.

O custo de inicialização pode ser perceptível em scripts de curta duração ou
em ambientes com recursos limitados.

**Como otimizar importações para scripts de alto desempenho?**

Importe diretamente a classe que você precisa, em vez de importar o submódulo
inteiro:

.. code-block:: python

    # Recomendado: carrega apenas a classe necessária
    from idessem.dessem.entdados import Entdados
    from idessem.dessem.pdo_sist import PdoSist

    # Evitar em scripts sensíveis a tempo de inicialização:
    import idessem.dessem  # carrega todas as 43 classes

Ao importar apenas as classes necessárias, o tempo de inicialização é
reduzido significativamente, pois apenas os módulos envolvidos na cadeia
de dependências daquela classe específica serão carregados.

.. note::

   O custo de importação é pago uma única vez por processo. Em aplicações
   de longa duração (como servidores ou sessões interativas Jupyter/IPython),
   o impacto é mínimo e o ``import idessem.dessem`` pode ser conveniente.
