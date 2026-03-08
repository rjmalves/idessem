Tutorial
============

O *idessem* provê uma interface semelhante para todos os arquivos do modelo DESSEM. Para os arquivos de entrada, 
são implementadas as capacidades de leitura e escrita, permitindo uma geração automática de arquivos. Para os arquivos 
de saída, é implementada somente a capacidade de leitura, de modo a permitir análise facilitada de resultados.

A leitura dos arquivos é sempre implementada a partir do método `read` da respectiva classe, enquanto que a escrita
dos arquivos é implementada pelo método `write` da instância em questão, quando for suportada.

Um exemplo é o processamento do arquivo que contém a entrada de dados gerais :ref:`entdados.dat <entdados>`. Sendo um arquivo de entrada,
é permitido realizar a leitura e a escrita deste arquivo, modificando alguma informação de entrada caso
seja desejado pelo usuário. Por exemplo, pode-se fazer uma sensibilidade de alterar o volume inicial de um reservatório:


.. code-block:: python

    from idessem.dessem.entdados import Entdados
    arq_entdados = Entdados.read("./entdados.dat")
    arq_entdados.uh(codigo_usina=6).volume_inicial
    69.51
    
    arq_entdados.uh(codigo_usina=6).volume_inicial*= 1.1
    arq_entdados.uh(codigo_usina=6).volume_inicial
    76.46100000000001

    arq_entdados.write("./entdados.dat")


Se tratando dos arquivos de saída, não existe implementação para o método `write`, mas é possível realizar
a leitura normalmente, e acessar todas as propriedades encontradas. Para o :ref:`PDO_SIST.DAT <pdo_sist>`, por exemplo:

.. code-block:: python

    from idessem.dessem.pdo_sist import PdoSist
    arq_pdo_sist = PdoSist.read("./PDO_SIST.DAT")
    arq_pdo_sist.tabela

        estagio patamar submercado    cmo   demanda perdas  ...  corte_carga    saldo  recebimento  geracao_termica_minima  geracao_termica_maxima  energia_armazenada
    0          1    LEVE         SE  71.48  36935.91      -  ...          0.0 -3461.61      3461.61                 2555.95                 9489.79           122020.78
    1          1    LEVE          S  71.44   9974.79      -  ...          0.0  3009.85     -3009.85                  246.00                 1348.57            14792.56
    2          1    LEVE         NE  71.46  11465.14      -  ...          0.0  3317.36     -3317.36                    4.00                 5997.78            39932.58
    3          1    LEVE          N  73.57   7341.98      -  ...          0.0 -2865.60      2865.60                 1153.00                 3134.21            14434.54
    4          1    LEVE         FC   0.00      0.00      -  ...          0.0     0.00         0.00                    0.00                    0.00                0.00
    ..       ...     ...        ...    ...       ...    ...  ...          ...      ...          ...                     ...                     ...                 ...
    255       52   MEDIA         SE  71.99  39910.00      -  ...          0.0 -6271.76      6271.76                 2544.95                 9478.79           121052.53
    256       52   MEDIA          S  71.95  12148.00      -  ...          0.0  2704.38     -2704.38                  246.00                 1348.57            15032.88
    257       52   MEDIA         NE  71.97  12032.00      -  ...          0.0  6032.64     -6032.64                    4.00                 5997.78            40053.92
    258       52   MEDIA          N  75.27   7053.00      -  ...          0.0 -2465.27      2465.27                 1153.00                 3134.21            14365.11
    259       52   MEDIA         FC  71.99      0.00      -  ...          0.0     0.00         0.00                    0.00                    0.00                0.00

    [260 rows x 20 columns]    


Alguns arquivos do modelo DESSEM podem sofrer alterações de sintaxe conforme são feitas atualizações no modelo.
Desta forma, poderia ser necessário criar mais de uma classe para dar suporte ao mesmo arquivo. Todavia, o framework
`cfinterface <https://github.com/rjmalves/cfi>`_ possui uma modelagem para dar suporte a mais de uma
versão do mesmo arquivo fazendo uso do método `set_version` de cada uma das classes. Caso não seja especificada a versão 
por meio do método `set_version`, será considerada a versão mais recente do arquivo. Por exemplo, o arquivo 
:ref:`AVL_FPHA1.DAT <avl_fpha1>` possui diferentes formatos dependendo da versão do modelo DESSEM:  


.. code-block:: text

    *  MODELO DESSEM     - VERSAO 19.3 - Janeiro de 2023 (CPLEX)                         *

    -----;--------------;-------;---------;------------;-------------;-------------;-------------;
    USIH ;    Nome      ;SegFPHA; Fcorrec ;    Rhs     ;    Varm     ;    Qtur     ;    Qlat     ;
    -----;--------------;-------;---------;------------;-------------;-------------;-------------;
     001 ; CAMARGOS     ;    1  ; 1.00000 ;   -11.8461 ;    0.020604 ;    0.224440 ;    0.000000 ;
     001 ; CAMARGOS     ;    2  ; 1.00000 ;    -5.7558 ;    0.020604 ;    0.186494 ;    0.000000 ;
     001 ; CAMARGOS     ;    3  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.225931 ;    0.000000 ;
     001 ; CAMARGOS     ;    4  ; 1.00000 ;     7.0475 ;    0.000000 ;    0.182021 ;    0.000000 ;




.. code-block:: text

    *  MODELO DESSEM     - VERSAO 19.3.1 - Fevereiro de 2023 (CPLEX)                     *

    -----;--------------;-------;---------;--------;------------;-------------;-------------;-------------;
    USIH ;    Nome      ;SegFPHA; Fcorrec ; QlatpM ;    Rhs     ;    Varm     ;    Qtur     ;    Qlat     ;
    -----;--------------;-------;---------;--------;------------;-------------;-------------;-------------;
     001 ; CAMARGOS     ;    1  ; 1.00000 ;   0.00 ;   -11.4690 ;    0.020604 ;    0.223018 ;    0.000000 ;
     001 ; CAMARGOS     ;    2  ; 1.00000 ;   0.00 ;    -7.8204 ;    0.013736 ;    0.225763 ;    0.000000 ;
     001 ; CAMARGOS     ;    3  ; 1.00000 ;   0.00 ;    -7.7113 ;    0.013736 ;    0.224743 ;    0.000000 ;
     001 ; CAMARGOS     ;    4  ; 1.00000 ;   0.00 ;    -5.2177 ;    0.020604 ;    0.184069 ;    0.000000 ;


Para a leitura deste arquivo gerado em uma versão inferior do modelo DESSEM, deve ser especificada a versão 
desejada antes de efetuar a leitura do arquivo. 

.. code-block:: python

    from idessem.dessem.avlfpha1 import AvlFpha1
    AvlFpha1.set_version("19.3")
    arq_avfpha1 = AvlFpha1.read("./AVL_FPHA1.DAT")


