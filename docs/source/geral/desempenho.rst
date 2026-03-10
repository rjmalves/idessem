.. _desempenho:

Guia de Desempenho
==================

Esta página apresenta orientações qualitativas para uso eficiente do *idessem*,
cobrindo otimização de importações, leitura em lote de arquivos, considerações
de memória e um resumo das boas práticas.

Otimizacao de Importacoes
--------------------------

Ao executar ``import idessem.dessem``, o interpretador Python carrega
imediatamente todas as 43 classes de arquivos definidas em
``idessem/dessem/__init__.py``. Em scripts rápidos ou em ambientes com
restrição de tempo de inicialização — como funções AWS Lambda — esse carregamento
completo pode introduzir latência desnecessária.

.. code-block:: python
   :caption: Anti-padrão: importação completa do módulo

   import idessem.dessem  # carrega todas as 43 classes

O padrão recomendado é importar apenas a classe necessária diretamente do módulo
que a define:

.. code-block:: python
   :caption: Recomendado: importação específica

   from idessem.dessem.entdados import Entdados

.. note::

   As importações diretas em ``idessem/dessem/__init__.py`` são intencionais e
   fazem parte do design da biblioteca. Esta orientação aplica-se ao código do
   *usuário*, não à estrutura interna do *idessem*.

Ao importar apenas as classes utilizadas, o tempo de inicialização do script é
reduzido proporcionalmente ao número de módulos não carregados. Para scripts que
utilizam apenas um ou dois arquivos DESSEM, a diferença pode ser perceptível em
ambientes com restrições de CPU ou disco.

Leitura de Arquivos em Lote
----------------------------

Ao processar múltiplos arquivos de saída do DESSEM (arquivos ``PDO_*``) de forma
independente, é possível explorar paralelismo para reduzir o tempo total de
processamento. Como a leitura de arquivos é predominantemente limitada pela
entrada/saída (I/O-bound), o uso de processos separados evita a contenção do GIL
do CPython.

.. code-block:: python

   from concurrent.futures import ProcessPoolExecutor
   from idessem.dessem.pdo_sist import PdoSist
   from idessem.dessem.pdo_hidr import PdoHidr

   arquivos = {"pdo_sist": PdoSist, "pdo_hidr": PdoHidr}

   def ler_arquivo(nome, classe):
       return classe.read(f"./{nome.upper()}.DAT")

   with ProcessPoolExecutor() as executor:
       resultados = {
           nome: executor.submit(ler_arquivo, nome, cls)
           for nome, cls in arquivos.items()
       }

.. warning::

   Cada arquivo deve ser lido em um processo ou thread separado. O estado
   interno das classes de arquivo do *idessem* não é compartilhado entre
   processos, o que torna o ``ProcessPoolExecutor`` mais adequado do que o
   ``ThreadPoolExecutor`` para operações de leitura intensiva.

A abordagem com ``ProcessPoolExecutor`` é indicada para cenários em que vários
arquivos ``PDO_*`` independentes precisam ser lidos antes de análises
combinadas. Para um único arquivo ou para fluxos sequenciais simples, a leitura
direta com ``Classe.read(caminho)`` é suficiente e mais simples.

Consideracoes de Memoria
-------------------------

Arquivos de saída como ``PDO_HIDR.DAT`` e ``PDO_OPERACAO.DAT`` podem conter
grandes volumes de dados tabulares, especialmente em simulações DESSEM de
múltiplas semanas com muitos estágios e patamares. As propriedades dessas classes
retornam :obj:`~pandas.DataFrame` que residem inteiramente em memória após a
leitura.

.. tip::

   Após extrair as informações necessárias de um objeto de arquivo, libere a
   referência com ``del`` para que o coletor de lixo do Python possa recuperar
   a memória:

   .. code-block:: python

      from idessem.dessem.pdo_hidr import PdoHidr

      arq_pdo_hidr = PdoHidr.read("./PDO_HIDR.DAT")
      tabela_hidr = arq_pdo_hidr.tabela  # extrai o DataFrame necessário

      del arq_pdo_hidr  # libera a memória do objeto de arquivo

Recomenda-se carregar apenas os arquivos estritamente necessários para a análise
em andamento, evitando manter múltiplos objetos de arquivo grandes em memória
simultaneamente quando não são mais utilizados.

Boas Praticas
--------------

A seguir, um resumo das recomendações desta página:

**Recomendado:**

- Importar apenas as classes utilizadas com ``from idessem.dessem.<modulo> import <Classe>``
- Usar ``ProcessPoolExecutor`` para leitura paralela de múltiplos arquivos ``PDO_*`` independentes
- Extrair os dados necessários para variáveis locais e liberar o objeto de arquivo com ``del`` após o uso
- Carregar apenas os arquivos necessários para a análise em andamento

**Evitar:**

- ``import idessem.dessem`` em scripts sensíveis à latência de inicialização quando apenas uma ou duas classes são necessárias
- Manter múltiplos objetos de arquivo grandes (como ``PDO_HIDR`` e ``PDO_OPERACAO``) carregados simultaneamente sem necessidade
- Compartilhar instâncias de classes de arquivo entre threads sem sincronização adequada
