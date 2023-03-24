MockAvlFpha1 = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 19.3 - Janeiro de 2023 (CPLEX)                         *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER- Data do Caso: 11/08/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "\n",
    " Restricoes de Funcao de Producao\n",
    " --------------------------------\n",
    "\n",
    "Nomenclatura:\n",
    "-------------\n",
    "-------------------------------------------------------------------------------------------\n",
    "Varm   : Volume Armazenado Util                                                 (MW/(hm3)) \n",
    "Qtur   : Vazao Turbinada                                                        (MW/(m3/s))\n",
    "Qlat   : Vazao lateral (vertimento, defluencias e afluencias a jusante da usina)(MW/(m3/s))\n",
    "Rhs    : Termo independente                                                     (MW)       \n",
    "Fcorrec: Fator de correcao                                                      (p.u.)     \n",
    "-------------------------------------------------------------------------------------------\n",
    "\n",
    "-----;--------------;-------;---------;--------;------------;-------------;-------------;-------------;\n",
    "USIH ;    Nome      ;SegFPHA; Fcorrec ; QlatpM ;    Rhs     ;    Varm     ;    Qtur     ;    Qlat     ;\n",
    "-----;--------------;-------;---------;--------;------------;-------------;-------------;-------------;\n",
    " 001 ; CAMARGOS     ;    1  ; 1.00000 ;   0.00 ;   -11.8461 ;    0.020604 ;    0.224440 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    2  ; 1.00000 ;   0.00 ;    -5.7558 ;    0.020604 ;    0.186494 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    3  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.225931 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    4  ; 1.00000 ;   0.00 ;     7.0475 ;    0.000000 ;    0.182021 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    1  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.252414 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    2  ; 1.00000 ;   0.00 ;     0.3224 ;    0.000000 ;    0.246235 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    3  ; 1.00000 ;   0.00 ;     0.8986 ;    0.000000 ;    0.240713 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    4  ; 1.00000 ;   0.00 ;     1.6711 ;    0.000000 ;    0.235777 ;    0.000000 ;\n",
    " 004 ; FUNIL-GRANDE ;    1  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.359617 ;    0.000000 ;\n",
    " 004 ; FUNIL-GRANDE ;    2  ; 1.00000 ;   0.00 ;     1.7646 ;    0.000000 ;    0.354932 ;    0.000000 ;\n",
    " 006 ; FURNAS       ;    1  ; 1.00000 ;   0.00 ;  -102.7361 ;    0.009221 ;    0.815922 ;   -0.006295 ;\n",
    " 006 ; FURNAS       ;    2  ; 1.00000 ;   0.00 ;   -70.3757 ;    0.006147 ;    0.820912 ;   -0.003873 ;\n",
    " 006 ; FURNAS       ;    3  ; 1.00000 ;   0.00 ;   -67.7903 ;    0.006147 ;    0.817732 ;   -0.005526 ;\n",
    " 006 ; FURNAS       ;    4  ; 1.00000 ;   0.00 ;   -39.1232 ;    0.009221 ;    0.763759 ;   -0.008165 ;\n",
    " 006 ; FURNAS       ;    5  ; 1.00000 ;   0.00 ;   -36.4171 ;    0.003074 ;    0.826960 ;   -0.001422 ;\n",
    " 006 ; FURNAS       ;    6  ; 1.00000 ;   0.00 ;   -34.6942 ;    0.003074 ;    0.822722 ;   -0.003145 ;\n",
    " 006 ; FURNAS       ;    7  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.828770 ;   -0.000590 ;\n",
    " 006 ; FURNAS       ;    8  ; 1.00000 ;   0.00 ;    78.9566 ;    0.000000 ;    0.758329 ;   -0.009061 ;\n",
    " 007 ; M. DE MORAES ;    1  ; 1.00000 ;   0.00 ;   -85.5048 ;    0.049155 ;    0.359362 ;   -0.015446 ;\n",
    " 007 ; M. DE MORAES ;    2  ; 1.00000 ;   0.00 ;   -69.2721 ;    0.036866 ;    0.366620 ;   -0.006176 ;\n",
    " 007 ; M. DE MORAES ;    3  ; 1.00000 ;   0.00 ;   -63.8135 ;    0.036866 ;    0.360843 ;   -0.013591 ;\n",
    " 007 ; M. DE MORAES ;    4  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.368101 ;   -0.002299 ;\n",
    " 008 ; ESTREITO     ;    1  ; 1.00000 ;   0.00 ;   -20.8524 ;    0.196928 ;    0.560329 ;   -0.006520 ;\n",
    " 008 ; ESTREITO     ;    2  ; 1.00000 ;   0.00 ;   -20.5513 ;    0.295392 ;    0.548535 ;   -0.010090 ;\n",
    " 008 ; ESTREITO     ;    3  ; 1.00000 ;   0.00 ;   -11.4893 ;    0.098464 ;    0.564583 ;   -0.001904 ;\n",
    " 008 ; ESTREITO     ;    4  ; 1.00000 ;   0.00 ;    -9.5952 ;    0.098464 ;    0.560793 ;   -0.005019 ;\n",
    " 008 ; ESTREITO     ;    5  ; 1.00000 ;   0.00 ;    -9.5262 ;    0.196928 ;    0.548999 ;   -0.009038 ;\n",
    " 008 ; ESTREITO     ;    6  ; 1.00000 ;   0.00 ;    -0.6711 ;    0.295392 ;    0.535277 ;   -0.012304 ;\n",
    " 008 ; ESTREITO     ;    7  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.565047 ;   -0.000720 ;\n",
    " 008 ; ESTREITO     ;    8  ; 1.00000 ;   0.00 ;    36.5821 ;    0.000000 ;    0.533884 ;   -0.013196 ;\n",
    " 009 ; JAGUARA      ;    1  ; 1.00000 ;   0.00 ;   -15.1635 ;    0.240036 ;    0.407837 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    2  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.408217 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    3  ; 1.00000 ;   0.00 ;    26.2854 ;    0.240036 ;    0.356356 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    4  ; 1.00000 ;   0.00 ;    42.6743 ;    0.000000 ;    0.355214 ;    0.000000 ;\n",
    " 010 ; IGARAPAVA    ;    1  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.156737 ;   -0.000672 ;\n",
    " 010 ; IGARAPAVA    ;    2  ; 1.00000 ;   0.00 ;     1.3671 ;    0.000000 ;    0.152673 ;   -0.002026 ;\n",
    " 010 ; IGARAPAVA    ;    3  ; 1.00000 ;   0.00 ;     3.6758 ;    0.000000 ;    0.149242 ;   -0.002912 ;\n",
    " 010 ; IGARAPAVA    ;    4  ; 1.00000 ;   0.00 ;     6.5004 ;    0.000000 ;    0.146444 ;   -0.003331 ;\n",
    " 011 ; VOLTA GRANDE ;    1  ; 1.00000 ;   0.00 ;    -3.6576 ;    0.034707 ;    0.246634 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    2  ; 1.00000 ;   0.00 ;    -2.5263 ;    0.017353 ;    0.250275 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    3  ; 1.00000 ;   0.00 ;    -1.6531 ;    0.052060 ;    0.240723 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    4  ; 1.00000 ;   0.00 ;    -1.1823 ;    0.017353 ;    0.246767 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    5  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.250408 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    6  ; 1.00000 ;   0.00 ;     0.7712 ;    0.034707 ;    0.240856 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    7  ; 1.00000 ;   0.00 ;     1.0968 ;    0.069414 ;    0.236133 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    8  ; 1.00000 ;   0.00 ;     3.4701 ;    0.052060 ;    0.236266 ;    0.000000 ;\n",
    " 012 ; P. COLOMBIA  ;    1  ; 1.00000 ;   0.00 ;    -9.8887 ;    0.106163 ;    0.179769 ;   -0.002622 ;\n",
    " 012 ; P. COLOMBIA  ;    2  ; 1.00000 ;   0.00 ;    -8.2647 ;    0.079622 ;    0.181165 ;   -0.001873 ;\n",
    " 012 ; P. COLOMBIA  ;    3  ; 1.00000 ;   0.00 ;    -6.7695 ;    0.079622 ;    0.179935 ;   -0.002369 ;\n",
    " 012 ; P. COLOMBIA  ;    4  ; 1.00000 ;   0.00 ;    -6.0753 ;    0.053081 ;    0.182560 ;   -0.001128 ;\n",
    " 012 ; P. COLOMBIA  ;    5  ; 1.00000 ;   0.00 ;    -5.0785 ;    0.053081 ;    0.181330 ;   -0.001641 ;\n",
    " 012 ; P. COLOMBIA  ;    6  ; 1.00000 ;   0.00 ;    -3.3204 ;    0.026541 ;    0.183956 ;   -0.000389 ;\n",
    " 012 ; P. COLOMBIA  ;    7  ; 1.00000 ;   0.00 ;    -2.8220 ;    0.026541 ;    0.182726 ;   -0.000902 ;\n",
    " 012 ; P. COLOMBIA  ;    8  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.184122 ;   -0.000157 ;\n",
    " 014 ; CACONDE      ;    1  ; 1.00000 ;   0.00 ;    -9.1519 ;    0.031995 ;    0.798218 ;   -0.012716 ;\n",
    " 014 ; CACONDE      ;    2  ; 1.00000 ;   0.00 ;    -7.1286 ;    0.023996 ;    0.811528 ;   -0.012540 ;\n",
    " 014 ; CACONDE      ;    3  ; 1.00000 ;   0.00 ;    -6.3978 ;    0.023996 ;    0.800821 ;   -0.012729 ;\n",
    " 014 ; CACONDE      ;    4  ; 1.00000 ;   0.00 ;    -5.1756 ;    0.015998 ;    0.833036 ;   -0.010517 ;\n",
    " 014 ; CACONDE      ;    5  ; 1.00000 ;   0.00 ;    -4.3152 ;    0.015998 ;    0.814131 ;   -0.012204 ;\n",
    " 014 ; CACONDE      ;    6  ; 1.00000 ;   0.00 ;    -2.9319 ;    0.007999 ;    0.863278 ;   -0.004884 ;\n",
    " 014 ; CACONDE      ;    7  ; 1.00000 ;   0.00 ;    -2.3029 ;    0.007999 ;    0.835639 ;   -0.009250 ;\n",
    " 014 ; CACONDE      ;    8  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.865881 ;   -0.002147 ;\n",
    " 015 ; E. DA CUNHA  ;    1  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.775500 ;   -0.003671 ;\n",
    " 015 ; E. DA CUNHA  ;    2  ; 1.00000 ;   0.00 ;     0.9522 ;    0.000000 ;    0.748829 ;   -0.009795 ;\n",
    " 015 ; E. DA CUNHA  ;    3  ; 1.00000 ;   0.00 ;     2.1600 ;    0.000000 ;    0.731914 ;   -0.013086 ;\n",
    " 015 ; E. DA CUNHA  ;    4  ; 1.00000 ;   0.00 ;     3.2563 ;    0.000000 ;    0.721678 ;   -0.015012 ;\n",
    " 016 ; A.S.OLIVEIRA ;    1  ; 1.00000 ;   0.00 ;     0.0000 ;    0.000000 ;    0.228516 ;   -0.001323 ;\n",
    " 016 ; A.S.OLIVEIRA ;    2  ; 1.00000 ;   0.00 ;     0.2916 ;    0.000000 ;    0.220405 ;   -0.004006 ;\n",
    " 016 ; A.S.OLIVEIRA ;    3  ; 1.00000 ;   0.00 ;     0.7492 ;    0.000000 ;    0.214043 ;   -0.006024 ;\n",
]
MockAvlFpha1v190300 = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  MODELO DESSEM     - VERSAO 19.3 - Janeiro de 2023 (CPLEX)                         *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA ONS                                                                                                                                                   \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER- Data do Caso: 11/08/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "\n",
    " Restricoes de Funcao de Producao\n",
    " --------------------------------\n",
    "\n",
    "Nomenclatura:\n",
    "-------------\n",
    "-------------------------------------------------------------------------------------------\n",
    "Varm   : Volume Armazenado Util                                                 (MW/(hm3)) \n",
    "Qtur   : Vazao Turbinada                                                        (MW/(m3/s))\n",
    "Qlat   : Vazao lateral (vertimento, defluencias e afluencias a jusante da usina)(MW/(m3/s))\n",
    "Rhs    : Termo independente                                                     (MW)       \n",
    "Fcorrec: Fator de correcao                                                      (p.u.)     \n",
    "-------------------------------------------------------------------------------------------\n",
    "\n",
    "-----;--------------;-------;---------;------------;-------------;-------------;-------------;\n",
    "USIH ;    Nome      ;SegFPHA; Fcorrec ;    Rhs     ;    Varm     ;    Qtur     ;    Qlat     ;\n",
    "-----;--------------;-------;---------;------------;-------------;-------------;-------------;\n",
    " 001 ; CAMARGOS     ;    1  ; 1.00000 ;   -11.8461 ;    0.020604 ;    0.224440 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    2  ; 1.00000 ;    -5.7558 ;    0.020604 ;    0.186494 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    3  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.225931 ;    0.000000 ;\n",
    " 001 ; CAMARGOS     ;    4  ; 1.00000 ;     7.0475 ;    0.000000 ;    0.182021 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    1  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.252414 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    2  ; 1.00000 ;     0.3224 ;    0.000000 ;    0.246235 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    3  ; 1.00000 ;     0.8986 ;    0.000000 ;    0.240713 ;    0.000000 ;\n",
    " 002 ; ITUTINGA     ;    4  ; 1.00000 ;     1.6711 ;    0.000000 ;    0.235777 ;    0.000000 ;\n",
    " 004 ; FUNIL-GRANDE ;    1  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.359617 ;    0.000000 ;\n",
    " 004 ; FUNIL-GRANDE ;    2  ; 1.00000 ;     1.7646 ;    0.000000 ;    0.354932 ;    0.000000 ;\n",
    " 006 ; FURNAS       ;    1  ; 1.00000 ;  -102.7361 ;    0.009221 ;    0.815922 ;   -0.006295 ;\n",
    " 006 ; FURNAS       ;    2  ; 1.00000 ;   -70.3757 ;    0.006147 ;    0.820912 ;   -0.003873 ;\n",
    " 006 ; FURNAS       ;    3  ; 1.00000 ;   -67.7903 ;    0.006147 ;    0.817732 ;   -0.005526 ;\n",
    " 006 ; FURNAS       ;    4  ; 1.00000 ;   -39.1232 ;    0.009221 ;    0.763759 ;   -0.008165 ;\n",
    " 006 ; FURNAS       ;    5  ; 1.00000 ;   -36.4171 ;    0.003074 ;    0.826960 ;   -0.001422 ;\n",
    " 006 ; FURNAS       ;    6  ; 1.00000 ;   -34.6942 ;    0.003074 ;    0.822722 ;   -0.003145 ;\n",
    " 006 ; FURNAS       ;    7  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.828770 ;   -0.000590 ;\n",
    " 006 ; FURNAS       ;    8  ; 1.00000 ;    78.9566 ;    0.000000 ;    0.758329 ;   -0.009061 ;\n",
    " 007 ; M. DE MORAES ;    1  ; 1.00000 ;   -85.5048 ;    0.049155 ;    0.359362 ;   -0.015446 ;\n",
    " 007 ; M. DE MORAES ;    2  ; 1.00000 ;   -69.2721 ;    0.036866 ;    0.366620 ;   -0.006176 ;\n",
    " 007 ; M. DE MORAES ;    3  ; 1.00000 ;   -63.8135 ;    0.036866 ;    0.360843 ;   -0.013591 ;\n",
    " 007 ; M. DE MORAES ;    4  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.368101 ;   -0.002299 ;\n",
    " 008 ; ESTREITO     ;    1  ; 1.00000 ;   -20.8524 ;    0.196928 ;    0.560329 ;   -0.006520 ;\n",
    " 008 ; ESTREITO     ;    2  ; 1.00000 ;   -20.5513 ;    0.295392 ;    0.548535 ;   -0.010090 ;\n",
    " 008 ; ESTREITO     ;    3  ; 1.00000 ;   -11.4893 ;    0.098464 ;    0.564583 ;   -0.001904 ;\n",
    " 008 ; ESTREITO     ;    4  ; 1.00000 ;    -9.5952 ;    0.098464 ;    0.560793 ;   -0.005019 ;\n",
    " 008 ; ESTREITO     ;    5  ; 1.00000 ;    -9.5262 ;    0.196928 ;    0.548999 ;   -0.009038 ;\n",
    " 008 ; ESTREITO     ;    6  ; 1.00000 ;    -0.6711 ;    0.295392 ;    0.535277 ;   -0.012304 ;\n",
    " 008 ; ESTREITO     ;    7  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.565047 ;   -0.000720 ;\n",
    " 008 ; ESTREITO     ;    8  ; 1.00000 ;    36.5821 ;    0.000000 ;    0.533884 ;   -0.013196 ;\n",
    " 009 ; JAGUARA      ;    1  ; 1.00000 ;   -15.1635 ;    0.240036 ;    0.407837 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    2  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.408217 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    3  ; 1.00000 ;    26.2854 ;    0.240036 ;    0.356356 ;    0.000000 ;\n",
    " 009 ; JAGUARA      ;    4  ; 1.00000 ;    42.6743 ;    0.000000 ;    0.355214 ;    0.000000 ;\n",
    " 010 ; IGARAPAVA    ;    1  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.156737 ;   -0.000672 ;\n",
    " 010 ; IGARAPAVA    ;    2  ; 1.00000 ;     1.3671 ;    0.000000 ;    0.152673 ;   -0.002026 ;\n",
    " 010 ; IGARAPAVA    ;    3  ; 1.00000 ;     3.6758 ;    0.000000 ;    0.149242 ;   -0.002912 ;\n",
    " 010 ; IGARAPAVA    ;    4  ; 1.00000 ;     6.5004 ;    0.000000 ;    0.146444 ;   -0.003331 ;\n",
    " 011 ; VOLTA GRANDE ;    1  ; 1.00000 ;    -3.6576 ;    0.034707 ;    0.246634 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    2  ; 1.00000 ;    -2.5263 ;    0.017353 ;    0.250275 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    3  ; 1.00000 ;    -1.6531 ;    0.052060 ;    0.240723 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    4  ; 1.00000 ;    -1.1823 ;    0.017353 ;    0.246767 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    5  ; 1.00000 ;     0.0000 ;    0.000000 ;    0.250408 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    6  ; 1.00000 ;     0.7712 ;    0.034707 ;    0.240856 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    7  ; 1.00000 ;     1.0968 ;    0.069414 ;    0.236133 ;    0.000000 ;\n",
    " 011 ; VOLTA GRANDE ;    8  ; 1.00000 ;     3.4701 ;    0.052060 ;    0.236266 ;    0.000000 ;\n",
    " 012 ; P. COLOMBIA  ;    1  ; 1.00000 ;    -9.8887 ;    0.106163 ;    0.179769 ;   -0.002622 ;\n",
]
