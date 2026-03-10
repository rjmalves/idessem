.. _arquitetura:

Arquitetura do idessem
======================

Esta página descreve a estrutura interna do *idessem*, explicando como o módulo é
organizado, como os arquivos do modelo DESSEM são mapeados para classes Python e
qual é o fluxo típico de leitura e escrita de dados.

Visão Geral da Arquitetura
--------------------------

O *idessem* é uma biblioteca Python que fornece uma interface de alto nível para
leitura e escrita dos arquivos do modelo DESSEM, utilizado pelo Operador Nacional
do Sistema Elétrico (ONS) para o planejamento da operação de curtíssimo prazo do
Sistema Interligado Nacional (SIN). O modelo DESSEM processa dezenas de arquivos
de entrada e produz dezenas de arquivos de saída, todos com formatos textuais
proprietários e bem definidos.

A responsabilidade central do *idessem* é abstrair o formato textual de cada
arquivo em uma classe Python, expondo os dados como propriedades tipadas —
principalmente como :obj:`~pandas.DataFrame` para dados tabulares — e permitindo
que o usuário leia, inspecione, modifique e reescreva esses arquivos sem precisar
conhecer a sintaxe interna de cada formato.

O *idessem* é construído sobre o framework :obj:`cfinterface <cfinterface>`, que
fornece as abstrações de nível mais baixo para leitura e escrita de arquivos
estruturados. A relação entre os dois módulos está descrita em detalhes na seção
:doc:`Como contribuir? <contribuicao>`.

Framework cfinterface
---------------------

O framework `cfinterface <https://github.com/rjmalves/cfi>`_ classifica os arquivos
processados em três categorias, de acordo com a sua estrutura interna:

- :obj:`~cfinterface.files.blockfile.BlockFile`: arquivos compostos por blocos com
  padrão de início bem definido, que podem aparecer múltiplas vezes e em qualquer
  ordem.
- :obj:`~cfinterface.files.sectionfile.SectionFile`: arquivos compostos por seções
  fixas que aparecem sempre na mesma ordem.
- :obj:`~cfinterface.files.registerfile.RegisterFile`: arquivos compostos por
  registros de linha única e formato constante.

.. note::

   No *idessem*, **não são utilizados arquivos do tipo**
   :obj:`~cfinterface.files.sectionfile.SectionFile`. Todos os arquivos do modelo
   DESSEM suportados são implementados como
   :obj:`~cfinterface.files.blockfile.BlockFile` ou
   :obj:`~cfinterface.files.registerfile.RegisterFile`.

.. seealso::

   A seção :doc:`Como contribuir? <contribuicao>` contém uma explicação detalhada das três classes
   de arquivos do *cfinterface*, com exemplos concretos de arquivos do *idessem*
   que seguem cada abordagem.

Estrutura de Módulos
--------------------

O *idessem* expõe duas subpacotes públicas:

**idessem.dessem**

Contém as classes que modelam os arquivos de entrada e de saída do modelo DESSEM.
É o módulo principal da biblioteca, com 46 classes no total.

*Arquivos de entrada* (suportam leitura e escrita):

- :obj:`Areacont <idessem.dessem.areacont.Areacont>`
- :obj:`Dadvaz <idessem.dessem.dadvaz.Dadvaz>`
- :obj:`Deflant <idessem.dessem.deflant.Deflant>`
- :obj:`DessemArq <idessem.dessem.dessemarq.DessemArq>`
- :obj:`Desselet <idessem.dessem.desselet.Desselet>`
- :obj:`Dessopc <idessem.dessem.dessopc.Dessopc>`
- :obj:`Entdados <idessem.dessem.entdados.Entdados>`
- :obj:`Hidr <idessem.dessem.hidr.Hidr>`
- :obj:`Operuh <idessem.dessem.operuh.Operuh>`
- :obj:`Operut <idessem.dessem.operut.Operut>`
- :obj:`Renovaveis <idessem.dessem.renovaveis.Renovaveis>`
- :obj:`Respot <idessem.dessem.respot.Respot>`
- :obj:`Term <idessem.dessem.termdat.Term>`
- :obj:`Uch <idessem.dessem.uch.Uch>`

*Arquivos de saída — avaliação de FPHA* (somente leitura):

- :obj:`AvlAltQueda <idessem.dessem.avl_altqueda.AvlAltQueda>`
- :obj:`AvlDesvFpha <idessem.dessem.avl_desvfpha.AvlDesvFpha>`
- :obj:`AvlEstatFpha <idessem.dessem.avl_estatfpha.AvlEstatFpha>`
- :obj:`AvlFpha1 <idessem.dessem.avl_fpha1.AvlFpha1>`
- :obj:`AvlFpha2 <idessem.dessem.avl_fpha2.AvlFpha2>`
- :obj:`AvlFpha3 <idessem.dessem.avl_fpha3.AvlFpha3>`

*Arquivos de saída — pdo_* (somente leitura):

- :obj:`PdoAvalQmaxUsih <idessem.dessem.pdo_aval_qmaxusih.PdoAvalQmaxUsih>`
- :obj:`PdoCmoBar <idessem.dessem.pdo_cmobar.PdoCmoBar>`
- :obj:`PdoCmosist <idessem.dessem.pdo_cmosist.PdoCmosist>`
- :obj:`PdoEcoFcfCortes <idessem.dessem.pdo_eco_fcfcortes.PdoEcoFcfCortes>`
- :obj:`PdoEcoUsih <idessem.dessem.pdo_eco_usih.PdoEcoUsih>`
- :obj:`PdoEcoUsihConj <idessem.dessem.pdo_eco_usih_conj.PdoEcoUsihConj>`
- :obj:`PdoEcoUsihPolin <idessem.dessem.pdo_eco_usih_polin.PdoEcoUsihPolin>`
- :obj:`PdoElev <idessem.dessem.pdo_elev.PdoElev>`
- :obj:`PdoEolica <idessem.dessem.pdo_eolica.PdoEolica>`
- :obj:`PdoHidr <idessem.dessem.pdo_hidr.PdoHidr>`
- :obj:`PdoInter <idessem.dessem.pdo_inter.PdoInter>`
- :obj:`PdoOperLpp <idessem.dessem.pdo_oper_lpp.PdoOperLpp>`
- :obj:`PdoOperTerm <idessem.dessem.pdo_oper_term.PdoOperTerm>`
- :obj:`PdoOperUsih <idessem.dessem.pdo_oper_usih.PdoOperUsih>`
- :obj:`PdoOperTitulacaoContratos <idessem.dessem.pdo_oper_titulacao_contratos.PdoOperTitulacaoContratos>`
- :obj:`PdoOperTitulacaoUsinas <idessem.dessem.pdo_oper_titulacao_usinas.PdoOperTitulacaoUsinas>`
- :obj:`PdoOperTviagCalha <idessem.dessem.pdo_oper_tviag_calha.PdoOperTviagCalha>`
- :obj:`PdoOperUct <idessem.dessem.pdo_oper_uct.PdoOperUct>`
- :obj:`PdoOperacao <idessem.dessem.pdo_operacao.PdoOperacao>`
- :obj:`PdoReserva <idessem.dessem.pdo_reserva.PdoReserva>`
- :obj:`PdoSist <idessem.dessem.pdo_sist.PdoSist>`
- :obj:`PdoSomFlux <idessem.dessem.pdo_somflux.PdoSomFlux>`
- :obj:`PdoTerm <idessem.dessem.pdo_term.PdoTerm>`

*Arquivos de log — saída de diagnóstico* (somente leitura):

- :obj:`DesLogRelato <idessem.dessem.des_log_relato.DesLogRelato>`
- :obj:`LogInviab <idessem.dessem.log_inviab.LogInviab>`
- :obj:`LogMatriz <idessem.dessem.log_matriz.LogMatriz>`

**idessem.libs**

Contém entidades compartilhadas que podem ser referenciadas por múltiplos arquivos
do modelo. Atualmente possui uma única classe:

- :obj:`UsinasHidreletricas <idessem.libs.usinas_hidreletricas.UsinasHidreletricas>`:
  representação consolidada dos dados de usinas hidrelétricas do SIN.

Convenções de Nomeação
-----------------------

Cada arquivo do modelo DESSEM é mapeado para uma classe Python com nome em
``PascalCase``, derivado do nome de arquivo mais comum encontrado nos decks de
PMO publicados pelo ONS ou nos casos de exemplo distribuídos pelo desenvolvedor
do modelo. A regra geral é:

1. Remover a extensão do arquivo (``*.dat``, ``*.DAT``).
2. Separar as partes do nome pelo delimitador ``_`` (sublinhado).
3. Converter cada parte para ``PascalCase``, ignorando a capitalização original.

.. note::

   Abreviações presentes nos nomes dos arquivos são ignoradas na mudança de
   capitalização. Por exemplo, ``PDO`` se torna ``Pdo`` e não ``PDO``.

Exemplos de mapeamento:

+------------------------+-------------------------------------+
| Nome do arquivo        | Classe Python                       |
+========================+=====================================+
| ``entdados.dat``       | :ref:`Entdados <entdados>`          |
+------------------------+-------------------------------------+
| ``dessemarq.dat``      | :ref:`DessemArq <dessemarq>`        |
+------------------------+-------------------------------------+
| ``DES_LOG_RELATO.DAT`` | :ref:`DesLogRelato <des_log_relato>`|
+------------------------+-------------------------------------+
| ``PDO_SIST.DAT``       | :ref:`PdoSist <pdo_sist>`           |
+------------------------+-------------------------------------+

Fluxo de Dados
--------------

O *idessem* fornece uma interface uniforme para todos os arquivos. O padrão
de uso é sempre o mesmo: o método de classe ``read()`` recebe o caminho do
arquivo e retorna uma instância da classe correspondente, com os dados
já parseados e disponíveis como propriedades.

**Arquivos de entrada** — leitura, modificação e escrita

Os arquivos de entrada do modelo DESSEM (como ``entdados.dat``) suportam tanto
leitura quanto escrita. O fluxo típico é: ler o arquivo original, modificar os
dados desejados através das propriedades da instância e gravar o resultado de
volta com o método ``write()``.

.. code-block:: python

    from idessem.dessem.entdados import Entdados

    # Leitura do arquivo de entrada
    arq = Entdados.read("./entdados.dat")

    # Acesso e modificação de uma propriedade
    arq.uh(codigo_usina=6).volume_inicial
    # 69.51

    arq.uh(codigo_usina=6).volume_inicial *= 1.1
    arq.uh(codigo_usina=6).volume_inicial
    # 76.461

    # Escrita do arquivo modificado
    arq.write("./entdados.dat")

.. seealso::

   O :doc:`Tutorial <tutorial>` contém exemplos adicionais do ciclo de leitura e escrita,
   incluindo o tratamento de versões de arquivo com ``set_version()``.

**Arquivos de saída** — somente leitura

Os arquivos de saída do modelo DESSEM (com prefixo ``pdo_``, ``avl_``, ``log_``
ou ``des_log_``) não implementam o método ``write()``. O fluxo de uso é apenas
de leitura e análise dos resultados:

.. code-block:: python

    from idessem.dessem.pdo_sist import PdoSist

    # Leitura do arquivo de saída
    arq = PdoSist.read("./PDO_SIST.DAT")

    # Acesso à tabela de resultados como DataFrame
    arq.tabela
    #     estagio patamar submercado    cmo   demanda ...
    # 0         1    LEVE         SE  71.48  36935.91 ...
    # ...

.. important::

   Tentar chamar ``write()`` em um arquivo de saída levanta ``NotImplementedError``.
   Arquivos de saída são identificados pelo prefixo do nome da classe:
   ``Pdo*``, ``Avl*``, ``DesLogRelato``, ``LogInviab`` e ``LogMatriz``.

Importações Diretas
-------------------

O submódulo ``idessem.dessem`` utiliza importações diretas (não lazy) em seu
``__init__.py``. Isso significa que ao executar ``import idessem.dessem``,
todas as 46 classes são carregadas imediatamente na memória, incluindo suas
dependências.

.. warning::

   Evite importar o submódulo inteiro em código de produção ou em scripts que
   exigem tempo de inicialização reduzido. Prefira importar diretamente a classe
   que será utilizada:

   .. code-block:: python

      # Recomendado: importa apenas a classe necessária
      from idessem.dessem.entdados import Entdados

      # Evitar em contextos sensíveis a desempenho: carrega todas as 46 classes
      import idessem.dessem

O carregamento completo do módulo pode ser aceitável em sessões interativas
(Jupyter, IPython) ou em aplicações de longa duração onde o custo de
inicialização é pago uma única vez.
