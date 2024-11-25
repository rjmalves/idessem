MockPdoEcoFcfCortes = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 20.2 - Dezembro  de 2023 (CPLEX)                       *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    " TE  PMO - SETEMBRO/22 - OUTUBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPE - Data do Caso: 03/09/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "--------------------------------\n",
    "Cortes da Funcao de Custo Futuro                                                \n",
    "--------------------------------\n",
    "------------------------------------------------------------------------------\n",
    "ICUT:      Indice do corte                                                                                                                                                                              \n",
    "TP.ENTID:  Tipo de entidade:                                                                                                                                                                            \n",
    "           SIST:   Subsistema                                                                                                                                                                           \n",
    "           USIH:   Usina hidroeletrica                                                                                                                                                                  \n",
    "           USIHTV: Usina hidroeletrica com tempo de viagem                                                                                                                                              \n",
    "           USIT:   Usina termoeletrica                                                                                                                                                                  \n",
    "           USIE:   Usina elevatoria                                                                                                                                                                     \n",
    "           CONTR:  Contrato de Importacao/Exportacao                                                                                                                                                    \n",
    "           INTERC: Intercambio entre subsistemas                                                                                                                                                        \n",
    "ID.ENTID:  Numero da entidade                                                                                                                                                                           \n",
    "NomeEntid: Nome da entidade                                                                                                                                                                             \n",
    "TP.COEF:   Tipo de coeficiente na FCF                                                                                                                                                                   \n",
    "           RHS:   Termo independente                                                                                                                                                                    \n",
    "           VUTIL:   Volume armazenado util                                                                                                                                                              \n",
    "           QDEFP:   Vazao defluente passada (para tempo de viagem)                                                                                                                                      \n",
    "           GTERF: Geracao termica futura (usinas com antecipacao de despacho)                                                                                                                           \n",
    "ILAG:      Indice do lag (quantidade de periodos passados (<0) ou futuros (>0)                                                                                                                          \n",
    "IPAT:      Patamar de Carga                                                                                                                                                                             \n",
    "Val.Coef:  Valor do coeficiente.                                                                                                                                                                        \n",
    "Unid:      Unidade correspondente                                                                                                                                                                       \n",
    "------------------------------------------------------------------------------\n",
    "\n",
    "------;--------;------;---------------;-------;-----;-----;------------------------------;----------------;\n",
    " ICUT ;TP.ENTID;ID.ENT;   NomeEntid   ;TP.COEF;ILAG ;IPAT ;           Val.Coef           ;      Unid      ;\n",
    "  -   ;   -    ;  -   ;       -       ;   -   ;  -  ;  -  ;              -               ;       -        ;\n",
    "------;--------;------;---------------;-------;-----;-----;------------------------------;----------------;\n",
    " 0001 ; -      ;     0;      -        ;  RHS  ;   0 ;   0 ;          58927591.16372437   ;  1000$         ;\n",
    " 0001 ; USIH   ;     1; CAMARGOS      ; VARM  ;   0 ;   0 ;               -62.93312916   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     2; ITUTINGA      ; VARM  ;   0 ;   0 ;               -60.68463680   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     4; FUNIL-GRANDE  ; VARM  ;   0 ;   0 ;               -58.16677726   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     6; FURNAS        ; VARM  ;   0 ;   0 ;               -54.40857050   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     7; M. DE MORAES  ; VARM  ;   0 ;   0 ;               -46.38860599   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     8; ESTREITO      ; VARM  ;   0 ;   0 ;               -44.45318384   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     9; JAGUARA       ; VARM  ;   0 ;   0 ;               -38.72104126   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    10; IGARAPAVA     ; VARM  ;   0 ;   0 ;               -34.76226993   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    11; VOLTA GRANDE  ; VARM  ;   0 ;   0 ;               -33.39363480   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    12; P. COLOMBIA   ; VARM  ;   0 ;   0 ;               -30.79648480   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    14; CACONDE       ; VARM  ;   0 ;   0 ;               -46.52960740   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    15; E. DA CUNHA   ; VARM  ;   0 ;   0 ;               -38.51159480   ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    16; A.S.OLIVEIRA  ; VARM  ;   0 ;   0 ;               -30.93232024   ; (1000$/hm3)    ;\n",
]


MockPdoEcoFcfCortes19 = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 19.4.1 -   Maio  de 2023 (CPLEX)                       *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - JUNHO/23 - JULHO/23 - REV 2 - FCF COM CVAR - 12 REE - VALOR ESPERADO - Data do Caso: 13/06/2023                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "--------------------------------\n",
    "Cortes da Funcao de Custo Futuro                                                \n",
    "--------------------------------\n",
    "------------------------------------------------------------------------------\n",
    "ICUT:      Indice do corte                                                                                                                                                                              \n",
    "TP.ENTID:  Tipo de entidade:                                                                                                                                                                            \n",
    "           SIST:   Subsistema                                                                                                                                                                           \n",
    "           USIH:   Usina hidroeletrica                                                                                                                                                                  \n",
    "           USIHTV: Usina hidroeletrica com tempo de viagem                                                                                                                                              \n",
    "           USIT:   Usina termoeletrica                                                                                                                                                                  \n",
    "           USIE:   Usina elevatoria                                                                                                                                                                     \n",
    "           CONTR:  Contrato de Importacao/Exportacao                                                                                                                                                    \n",
    "           INTERC: Intercambio entre subsistemas                                                                                                                                                        \n",
    "ID.ENTID:  Numero da entidade                                                                                                                                                                           \n",
    "NomeEntid: Nome da entidade                                                                                                                                                                             \n",
    "TP.COEF:   Tipo de coeficiente na FCF                                                                                                                                                                   \n",
    "           RHS:   Termo independente                                                                                                                                                                    \n",
    "           VUTIL:   Volume armazenado util                                                                                                                                                              \n",
    "           QDEFP:   Vazao defluente passada (para tempo de viagem)                                                                                                                                      \n",
    "           GTERF: Geracao termica futura (usinas com antecipacao de despacho)                                                                                                                           \n",
    "ILAG:      Indice do lag (quantidade de periodos passados (<0) ou futuros (>0)                                                                                                                          \n",
    "IPAT:      Patamar de Carga                                                                                                                                                                             \n",
    "Val.Coef:  Valor do coeficiente.                                                                                                                                                                        \n",
    "Unid:      Unidade correspondente                                                                                                                                                                       \n",
    "------------------------------------------------------------------------------\n",
    "\n",
    "------;--------;------;---------------;-------;-----;-----;------------------------;----------------;\n",
    " ICUT ;TP.ENTID;ID.ENT;   NomeEntid   ;TP.COEF;ILAG ;IPAT ;        Val.Coef        ;      Unid      ;\n",
    "  -   ;   -    ;  -   ;       -       ;   -   ;  -  ;  -  ;           -            ;       -        ;\n",
    "------;--------;------;---------------;-------;-----;-----;------------------------;----------------;\n",
    " 0001 ; RHS    ;     0;      -        ;  RHS  ;   0 ;   0 ;     237331555.0724059  ;  1000$         ;\n",
    " 0001 ; USIH   ;     1; CAMARGOS      ; VARM  ;   0 ;   0 ;             0.0005367  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     2; ITUTINGA      ; VARM  ;   0 ;   0 ;             0.0004674  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     4; FUNIL-GRANDE  ; VARM  ;   0 ;   0 ;             0.0003980  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     6; FURNAS        ; VARM  ;   0 ;   0 ;             0.0003465  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     7; M. DE MORAES  ; VARM  ;   0 ;   0 ;             0.0003820  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     8; ESTREITO      ; VARM  ;   0 ;   0 ;             0.0003377  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;     9; JAGUARA       ; VARM  ;   0 ;   0 ;             0.0003213  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    10; IGARAPAVA     ; VARM  ;   0 ;   0 ;             0.0002783  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    11; VOLTA GRANDE  ; VARM  ;   0 ;   0 ;             0.0001941  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    12; P. COLOMBIA   ; VARM  ;   0 ;   0 ;             0.0001268  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    14; CACONDE       ; VARM  ;   0 ;   0 ;            -0.0000078  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    15; E. DA CUNHA   ; VARM  ;   0 ;   0 ;             0.0001052  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    16; A.S.OLIVEIRA  ; VARM  ;   0 ;   0 ;             0.0001222  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    17; MARIMBONDO    ; VARM  ;   0 ;   0 ;             0.0000488  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    18; A. VERMELHA   ; VARM  ;   0 ;   0 ;             0.0000330  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    20; BATALHA       ; VARM  ;   0 ;   0 ;             0.0000000  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    21; SERRA FACAO   ; VARM  ;   0 ;   0 ;            -0.0000060  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    24; EMBORCACAO    ; VARM  ;   0 ;   0 ;            -0.0000099  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    25; NOVA PONTE    ; VARM  ;   0 ;   0 ;            -0.0000030  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    26; MIRANDA       ; VARM  ;   0 ;   0 ;             0.0000623  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    27; CAPIM BRANC1  ; VARM  ;   0 ;   0 ;             0.0001209  ; (1000$/hm3)    ;\n",
    " 0001 ; USIH   ;    28; CAPIM BRANC2  ; VARM  ;   0 ;   0 ;             0.0000999  ; (1000$/hm3)    ;\n",
]
