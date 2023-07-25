MockUch = [
    "& Arquivo com os dados de UCH\n",
    "&\n",
    "& Flag para todas as UHEs\n",
    "UCH-OPCAO-PADRAO;1;\n",
    "&\n",
    "& Flag para escolher as UHEs\n",
    "UCH-OPCAO-USINA;1;1;\n",
    "UCH-OPCAO-USINA;1;2;\n",
    "UCH-OPCAO-USINA;1;4;\n",
    "&\n",
    "& Horizonte de estudo\n",
    "&UCH-OPCAO-PADRAO-DATA\n",
    "&\n",
    "& Operação em vazio\n",
    "&UCH-OPCAO-UNIDADE-VAZIO-PADRAO\n",
    "&UCH-OPCAO-CONJUNTO-VAZIO-PADRAO\n",
    "&UCH-OPCAO-USINA-VAZIO-PADRAO\n",
    "&\n",
    "& Ton/Toff; UHE; Ton; Toff\n",
    "UCH-TON-TOFF-USINA; 1; 5; 5;\n",
    "UCH-TON-TOFF-USINA; 2; 5; 5;\n",
    "UCH-TON-TOFF-USINA; 4; 5; 5;\n",
    "&\n",
    "& Custo de partida\n",
    "&UCH-CUSTO-PARTIDA-UNIDADE\n",
    "&UCH-CUSTO-PARTIDA-CONJUNTO\n",
    "&UCH-CUSTO-PARTIDA-USINA\n",
    "&\n",
    "&Custo de partida em vazio\n",
    "&UCH-CUSTO-PARTIDA-VAZIO-UNIDADE\n",
    "&UCH-CUSTO-PARTIDA-VAZIO-CONJUNTO\n",
    "&UCH-CUSTO-PARTIDA-VAZIO-USINA\n",
    "&\n",
    "&Consumo de água em vazio\n",
    "&UCH-CONSUMO-AGUA-VAZIO-UNIDADE\n",
    "&UCH-CONSUMO-AGUA-VAZIO-CONJUNTO\n",
    "&UCH-CONSUMO-AGUA-VAZIO-USINA\n",
    "&\n",
    "&Número máximo de mudanças de status\n",
    "&UCH-LIMITE-MUDANCA-STATUS-VAZIO-UNIDADE\n",
    "&UCH-LIMITE-MUDANCA-STATUS-VAZIO-CONJUNTO\n",
    "&UCH-LIMITE-MUDANCA-STATUS-VAZIO-USINA\n",
    "&\n",
    "&Geração mínima e máxima de cada unidade;UHE;Conj;Uni;Gmin;Gmax;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  1; 3.5;  23;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  2; 3.5;  23;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   1;  1; 3;  12.5;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   1;  2; 3;  12.5;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   2;  1; 3;    14;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   3;  1; 3;    13;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  1; 25;   60;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  2; 25;   60;\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  3; 25;   60;\n",
    "&\n",
    "&Turbinamento mínimo e máximo da unidade\n",
    "&UCH-TURBINAMENTO-MINIMO-MAXIMO-UNIDADE\n",
    "&\n",
    "&Condição inicial da unidade;UHE;Conj;Uni;status;tempo;Gini;Turbini;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  1;   1;  1;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  1;   1;  2;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   1;  1;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   1;  2;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   2;  1;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   3;  1;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  1;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  2;     0;    5;   0;      0;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  3;     0;    5;   0;      0;\n",
    "&\n",
]

MockUchOpcaoPadrao = "UCH-OPCAO-PADRAO;1;\n"
MockUchOpcaoUsina = "UCH-OPCAO-USINA;2;1;\n"
MockUchOpcaoPadraoData = "UCH-OPCAO-PADRAO-DATA;31;0;0;31;23;1;\n"
MockUchTonToffUnidade = "UCH-TON-TOFF-UNIDADE;1;2;1;5;10;\n"
MockUchTonToffConjunto = "UCH-TON-TOFF-CONJUNTO;2;1;5;10;\n"
MockUchTonToffUsina = "UCH-TON-TOFF-USINA; 1; 5; 10;\n"
MockUchGminGmaxUnidade = (
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  1; 3.5;  23;\n",
)
MockUchQturminQturmaxUnidade = (
    "UCH-TURBINAMENTO-MINIMO-MAXIMO-UNIDADE;1;   1;  1; 100;  200;\n"
)
MockUchCondicaoInicialUnidade = (
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   3;  1;     0;    5;   0;      0;\n"
)
