Como contribuir?
=================

.. note::

   O guia completo para contribuidores — incluindo configuração do ambiente, ferramentas de qualidade de código, execução de testes e fluxo de pull request — está disponível no arquivo `CONTRIBUTING.md <https://github.com/rjmalves/idessem/blob/main/CONTRIBUTING.md>`_ na raiz do repositório.

   Esta página descreve as convenções de modelagem específicas do *idessem* e as referências ao framework *cfinterface*, que utilizam recursos de marcação próprios do Sphinx.


O framework `cfinterface` e a modelagem de arquivos
----------------------------------------------------

O módulo *idessem* é desenvolvido considerando o framework proposto no módulo `cfinterface <https://github.com/rjmalves/cfi>`_.

A abordagem proposta no framework consiste em classificar os arquivos processados com relação à sua construção. São definidas três classes de arquivos:

- :obj:`~cfinterface.files.blockfile.BlockFile`
- :obj:`~cfinterface.files.sectionfile.SectionFile`
- :obj:`~cfinterface.files.registerfile.RegisterFile`

Esta classificação independe do arquivo ser constituído de armazenamento no formato texto ou binário, sendo que
esta informação é fornecida na declaração da classe que modela o arquivo em questão. Também é possível fornecer
informações sobre a codificação padrão utilizada em casos de arquivos gerados com caracteres especiais.

A modelagem de arquivos como :obj:`~cfinterface.files.blockfile.BlockFile` se baseia na definição de blocos do arquivo que
possuem um padrão específico, binário ou textual, que indica o início de um conjunto de informações que seja
autocontido e bem definido. Opcionalmente, também pode haver um padrão de terminação, ou o bloco pode determinar
a sua terminação seguindo outros critérios. Um bloco é definido como um elemento da classe :obj:`~cfinterface.components.block.Block`.
Exemplos de arquivos do módulo *idessem* que são implementados através deste modelo são o :ref:`entdados.dat <entdados>` e :ref:`desselet.dat <desselet>`.

O uso dos modelos da :obj:`~cfinterface.files.sectionfile.SectionFile` se baseia na definição de seções do arquivo que
sempre aparecem em uma mesma ordem e são obrigatórias. Da mesma forma, o arquivo pode ser binário ou textual. Diferentemente da modelagem
por :obj:`~cfinterface.files.blockfile.BlockFile`, que permite que um mesmo bloco apareça diversas vezes no arquivo, a abordagem
por seções não permite flexibilidade na definição de quais conteúdos aparecem e na ordem que aparecem. Podem, cada objeto
:obj:`~cfinterface.components.section.Section` pode definir o seu critério de fim, permitindo uma certa flexibilidade dentro de cada
seção. Exemplos de arquivos do módulo *idessem* que são implementados através deste modelo são o :ref:`dessopc.dat <dessopc>` e :ref:`operuh.dat <operuh>`.

Por fim, a abordagem por :obj:`~cfinterface.files.registerfile.RegisterFile` se baseia na definição de unidades mínimas de conteúdo
que ocupam sempre uma única linha e tem formato constante, que são chamadas de registros. Da mesma forma, o arquivo pode ser binário ou textual.
Registros podem ser vistos como blocos de uma só linha mas, devido à sua simplicidade, são de mais fácil definição, através da classe
:obj:`~cfinterface.components.register.Register`. A implementação de um registro consiste apenas na sua definição, visto que
a leitura e a escrita deste são inteiramente obtidas do formato dos seus campos. No *idessem*, o arquivo :ref:`dessemarq.dat <dessemarq>` é modelado
seguindo esta abordagem.


Diretrizes de modelagem para o módulo `idessem`
------------------------------------------------

A principal diretriz para o desenvolvimento do *idessem* é a relação entre arquivos do modelo DESSEM e as classes
disponíveis para uso. Cada arquivo de entrada do modelo é mapeado para uma classe do módulo, que segue
o nome geralmente utilizado para o arquivo nos casos de exemplo que são fornecidos junto com o modelo pelo desenvolvedor
ou pelo ONS para publicação dos decks de PMO. É utilizado sempre `PascalCase` para determinação dos nomes
das classes, sendo que abreviações que possivelmente se encontram nos nomes dos arquivos são ignoradas na mudança de caso. Por exemplo:

- `entdados.dat` é modelado na classe :ref:`Entdados <entdados>`
- `dessemarq.dat` é modelado na classe :ref:`DessemArq <dessemarq>`
- `DES_LOG_RELATO.DAT` é modelado na classe :ref:`DesLogRelato <des_log_relato>`
- `PDO_SIST.DAT` é modelado na classe :ref:`PdoSist <pdo_sist>`

É convencionado, sempre que possível, que as propriedades das classes que contém os dados processados dos arquivos
lidem com objetos do tipo :obj:`~pandas.DataFrame` para a representação de dados tabulares. Além disso, se possível,
é recomendado processar a informação contida nos arquivos para que esteja na seguindo as formas normais
para dados tabulares, mesmo quando há divergência na representação textual nos arquivos de entrada do DESSEM.

As propriedades das classes e também as colunas dos :obj:`~pandas.DataFrame` que são produzidos são convencionados de
serem nomeados em `snake_case`. Além disso, deve-se evitar ao máximo ambiguidades na escolha dos nomes das propriedades e
das colunas. Alguns pontos recorrentes onde são encontradas ambiguidades e deve-se adotar um termo único são:

- Propriedade ou :obj:`~pandas.DataFrame` que contenha informações de usinas (hidrelétricas, termelétricas, etc.) e venham e conter atributos
  como código (`int`) e nome (`str`) convenciona-se chamar de *nome_usina* e *codigo_usina*, para garantir o único sentido possível.
- Propriedade ou :obj:`~pandas.DataFrame` que contenha informações relativas aos submercados de energia, que ora são
  mencionados como subsistemas de energia, adota-se o termo único *submercado*. De modo semelhante, locais onde apareçam
  informações desta entendidade são denominados *codigo_submercado* e *nome_submercado*. O mesmo raciocínio se aplica
  ao se referir a REE.


Configuracao do ambiente e procedimentos de qualidade
------------------------------------------------------

Para instalar as dependências de desenvolvimento::

    $ git clone https://github.com/rjmalves/idessem.git
    $ cd idessem
    $ uv sync --extra dev
    $ uv run pre-commit install

.. warning::

   O conteúdo da documentação gerada (HTML em ``docs/build/``) não deve ser enviado para o repositório. Isto é feito
   automaticamente pelos scripts de CI no caso de qualquer modificação no branch ``main``.

Antes de realizar um ``git push`` é recomendado executar os procedimentos de qualidade que serão novamente executados pelo ambiente de CI::

    $ uv run ruff check ./idessem
    $ uv run ruff format ./idessem
    $ uv run mypy ./idessem
    $ uv run pytest ./tests
