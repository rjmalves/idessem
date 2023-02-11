MockPdoSist = [
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
    "\n",
    "____________________________________________________________________\n",
    "\n",
    "  TE  PMO - AGOSTO/22 - SETEMBRO/22 - REV 1 - FCF COM CVAR - 12 REE - VALOR ESPER- Data do Caso: 11/08/2022                                                       \n",
    "____________________________________________________________________\n",
    "\n",
    "\n",
    " \n",
    "Relatorio dos subsistemas \n",
    " \n",
    "  \n",
    "OBS.:\n",
    "1) A geracao de Itaipu injetada, no subsistema Sudeste (SE), inclui a geracao para atender a carga da ANDE.\n",
    "2) Intercambio IV-SE nao corresponde a recebimento do SE pois Itaipu(60hz) ja se encontra no SE.\n",
    "  \n",
    "------;--------;------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;\n",
    "      ;        ;      ;    Cmo     ;   Demanda  ;   Perdas   ;   GpQusi   ;  GfixBar   ;  Grenova   ;  SomatGH   ;  SomatGT   ; ConsEleva  ;  Import.   ;  Export.   ; CortCarg.  ;   Saldo    ;Recebimento ; SomaGTMin  ; SomatGTMax ;   Earm     ;\n",
    " IPER ;  Pat   ; Sist ;   $/MWH    ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;     MW     ;    MWH     ;\n",
    "------;--------;------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;\n",
    "   1  ;   LEVE ; SE   ;      71.48 ;   36935.91 ;     -      ;       0.00 ;       0.00 ;    5006.00 ;   27152.97 ;    2555.95 ;     108.62 ;    6479.64 ;    6079.64 ;       0.00 ;   -3461.61 ;    3461.61 ;    2555.95 ;    9489.79 ;  122020.78 ;\n",
    "   1  ;   LEVE ; S    ;      71.44 ;    9974.79 ;     -      ;       0.00 ;       0.00 ;    1287.00 ;   11451.64 ;     246.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3009.85 ;   -3009.85 ;     246.00 ;    1348.57 ;   14792.56 ;\n",
    "   1  ;   LEVE ; NE   ;      71.46 ;   11465.14 ;     -      ;       0.00 ;       0.00 ;    8948.00 ;    5830.50 ;       4.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3317.36 ;   -3317.36 ;       4.00 ;    5997.78 ;   39932.58 ;\n",
    "   1  ;   LEVE ; N    ;      73.57 ;    7341.98 ;     -      ;       0.00 ;       0.00 ;     524.00 ;    3199.37 ;    1153.00 ;       0.00 ;       0.00 ;     400.00 ;       0.00 ;   -2865.60 ;    2865.60 ;    1153.00 ;    3134.21 ;   14434.54 ;\n",
    "   1  ;   LEVE ; FC   ;       0.00 ;       0.00 ;     -      ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;\n",
    "   2  ;   LEVE ; SE   ;      70.96 ;   35792.39 ;     -      ;       0.00 ;       0.00 ;    5001.00 ;   25565.27 ;    2555.95 ;     108.62 ;    5199.00 ;    4799.00 ;       0.00 ;   -3910.78 ;    3910.78 ;    2555.95 ;    9489.79 ;  122019.92 ;\n",
    "   2  ;   LEVE ; S    ;      70.92 ;    9612.77 ;     -      ;       0.00 ;       0.00 ;    1274.00 ;   11166.29 ;     276.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3103.52 ;   -3103.52 ;     246.00 ;    1348.57 ;   14795.27 ;\n",
    "   2  ;   LEVE ; NE   ;      70.94 ;   11269.00 ;     -      ;       0.00 ;       0.00 ;    8928.00 ;    5670.92 ;       4.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3333.92 ;   -3333.92 ;       4.00 ;    5997.78 ;   39933.80 ;\n",
    "   2  ;   LEVE ; N    ;      73.12 ;    7252.19 ;     -      ;       0.00 ;       0.00 ;     540.00 ;    3432.54 ;    1153.00 ;       0.00 ;       0.00 ;     400.00 ;       0.00 ;   -2526.66 ;    2526.66 ;    1153.00 ;    3134.21 ;   14434.10 ;\n",
    "   2  ;   LEVE ; FC   ;       0.00 ;       0.00 ;     -      ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;\n",
    "   3  ;   LEVE ; SE   ;      70.48 ;   34704.04 ;     -      ;       0.00 ;       0.00 ;    4992.00 ;   25075.66 ;    2555.95 ;     238.37 ;    5743.21 ;    5343.21 ;       0.00 ;   -3450.80 ;    3450.80 ;    2555.95 ;    9489.79 ;  122024.51 ;\n",
    "   3  ;   LEVE ; S    ;      70.44 ;    9332.79 ;     -      ;       0.00 ;       0.00 ;    1259.00 ;   10112.10 ;     306.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    2344.31 ;   -2344.31 ;     306.00 ;    1348.57 ;   14801.55 ;\n",
    "   3  ;   LEVE ; NE   ;      70.46 ;   11106.87 ;     -      ;       0.00 ;       0.00 ;    8875.00 ;    5511.47 ;       4.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3283.60 ;   -3283.60 ;       4.00 ;    5997.78 ;   39935.46 ;\n",
    "   3  ;   LEVE ; N    ;      72.57 ;    7153.21 ;     -      ;       0.00 ;       0.00 ;     554.00 ;    3669.11 ;    1153.00 ;       0.00 ;       0.00 ;     400.00 ;       0.00 ;   -2177.10 ;    2177.10 ;    1153.00 ;    3134.21 ;   14433.60 ;\n",
    "   3  ;   LEVE ; FC   ;       0.00 ;       0.00 ;     -      ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;\n",
    "   4  ;   LEVE ; SE   ;      70.47 ;   34021.72 ;     -      ;       0.00 ;       0.00 ;    4989.00 ;   25248.82 ;    2555.95 ;     288.37 ;    5904.55 ;    5504.55 ;       0.00 ;   -2648.32 ;    2648.32 ;    2555.95 ;    9489.79 ;  122029.14 ;\n",
    "   4  ;   LEVE ; S    ;      70.43 ;    9053.78 ;     -      ;       0.00 ;       0.00 ;    1246.00 ;    9260.31 ;     306.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    1758.54 ;   -1758.54 ;     306.00 ;    1348.57 ;   14809.41 ;\n",
    "   4  ;   LEVE ; NE   ;      70.45 ;   10952.88 ;     -      ;       0.00 ;       0.00 ;    8806.00 ;    5325.69 ;       4.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    3182.82 ;   -3182.82 ;       4.00 ;    5997.78 ;   39937.57 ;\n",
    "   4  ;   LEVE ; N    ;      71.35 ;    7054.39 ;     -      ;       0.00 ;       0.00 ;     567.00 ;    3441.36 ;    1153.00 ;       0.00 ;       0.00 ;     400.00 ;       0.00 ;   -2293.03 ;    2293.03 ;    1153.00 ;    3134.21 ;   14433.08 ;\n",
    "   4  ;   LEVE ; FC   ;       0.00 ;       0.00 ;     -      ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;\n",
    "   5  ;   LEVE ; SE   ;      70.47 ;   33444.94 ;     -      ;       0.00 ;       0.00 ;    4998.00 ;   24724.69 ;    2555.95 ;     288.37 ;    5600.41 ;    5200.41 ;       0.00 ;   -2586.67 ;    2586.67 ;    2555.95 ;    9489.79 ;  122035.61 ;\n",
    "   5  ;   LEVE ; S    ;      70.43 ;    8829.00 ;     -      ;       0.00 ;       0.00 ;    1245.00 ;    9331.38 ;     306.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    2053.38 ;   -2053.38 ;     306.00 ;    1348.57 ;   14815.95 ;\n",
    "   5  ;   LEVE ; NE   ;      70.45 ;   10842.99 ;     -      ;       0.00 ;       0.00 ;    8700.00 ;    5102.51 ;       4.00 ;       0.00 ;       0.00 ;       0.00 ;       0.00 ;    2963.52 ;   -2963.52 ;       4.00 ;    5997.78 ;   39940.16 ;\n",
    "\n",
]
