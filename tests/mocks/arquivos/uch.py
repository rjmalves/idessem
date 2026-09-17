MockUch = [
    "& Arquivo com os dados de UCH\n",
    "&\n",
    "& Flag para todas as UHEs\n",
    "UCH-OPCAO-PADRAO;1\n",
    "&\n",
    "& Flag para escolher as UHEs\n",
    "UCH-OPCAO-PADRAO-USINA;1;1;1\n",
    "UCH-OPCAO-PADRAO-USINA;1;2;2\n",
    "UCH-OPCAO-PADRAO-USINA;1;4;3\n",
    "&\n",
    "& Horizonte de estudo\n",
    "&UCH-PADRAO-DATA\n",
    "&\n",
    "& Operação em vazio\n",
    "&UCH-OPCAO-VAZIO-UNIDADE\n",
    "&\n",
    "& Ton e Toff de cada unidade;UHE;Conj;Uni;Ton;Toff\n",
    "&Ton e Toff da unidade; UHE;Conj;Uni;Ton;Toff\n",
    "UCH-TON-TOFF-UNIDADE;     1;   1;  1;  5;  5\n",
    "UCH-TON-TOFF-UNIDADE;     1;   1;  2;  5;  5\n",
    "UCH-TON-TOFF-UNIDADE;     2;   1;  1;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     2;   1;  2;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     2;   2;  1;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     2;   3;  1;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     4;   1;  1;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     4;   1;  2;   5; 5\n",
    "UCH-TON-TOFF-UNIDADE;     4;   1;  3;   5; 5\n",
    "&\n",
    "& Custo de partida\n",
    "&UCH-CUSTO-PARTIDA-UNIDADE\n",
    "&\n",
    "&Custo de partida em vazio\n",
    "&UCH-CUSTO-PARTIDA-VAZIO-UNIDADE\n",
    "&\n",
    "&Consumo de água em vazio\n",
    "&UCH-CONSUMO-AGUA-VAZIO-UNIDADE\n",
    "&\n",
    "&Número máximo de mudanças de status\n",
    "&UCH-LIMITE-MUDANCA-STATUS-VAZIO-UNIDADE\n",
    "&\n",
    "&Geração mínima e máxima de cada unidade;UHE;Conj;Uni;Gmin;Gmax\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  1; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  2; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   1;  1; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   1;  2; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   2;  1; 3;    14\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         2;   3;  1; 3;    13\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  1; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  2; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         4;   1;  3; 25;   60\n",
    "&\n",
    "&Geração mínima e máxima de cada conjunto;UHE;Conj;Gmin;Gmax\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         1;   1; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         1;   1; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         2;   1; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         2;   1; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         2;   2; 3;    14\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         2;   3; 3;    13\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         4;   1; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         4;   1; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         4;   1; 25;   60\n",
    "&\n",
    "&Geração mínima e máxima de cada usina;UHE;Gmin;Gmax\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         1; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         1; 3.5;  23\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         2; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         2; 3;  12.5\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         2; 3;    14\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         2; 3;    13\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         4; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         4; 25;   60\n",
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         4; 25;   60\n",
    "&\n",
    "&Condição inicial da unidade;UHE;Conj;Uni;status;tempo;Gini;Turbini;\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  1;   1;  1;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  1;   1;  2;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   1;  1;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   1;  2;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   2;  1;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   3;  1;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  1;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  2;     0;    5;   0;      0\n",
    "UCH-CONDICAO-INICIAL-UNIDADE;  4;   1;  3;     0;    5;   0;      0\n",
    "&\n",
]

MockUchOpcaoPadrao = "UCH-OPCAO-PADRAO;1\n"
MockUchOpcaoPadraoUsina = "UCH-OPCAO-PADRAO-USINA;2;1;3\n"
MockUchPadraoData = "UCH-PADRAO-DATA;1;23;1\n"
MockUchOpcaoVazioUnidade = "UCH-OPCAO-VAZIO-UNIDADE;1;1;1;1"
MockUchTonToffUnidade = "UCH-TON-TOFF-UNIDADE;1;2;1;5;10\n"
MockUchGminGmaxUnidade = (
    "UCH-GERACAO-MINIMA-MAXIMA-UNIDADE;         1;   1;  1; 3.5;  23\n",
)
MockUchGminGmaxConjunto = (
    "UCH-GERACAO-MINIMA-MAXIMA-CONJUNTO;         4;   1; 25;   60\n",
)
MockUchGminGmaxUsina = (
    "UCH-GERACAO-MINIMA-MAXIMA-USINA;         1;  3.5;  23\n",
)
MockUchCondicaoInicialUnidade = (
    "UCH-CONDICAO-INICIAL-UNIDADE;  2;   3;  1;     0;    5;   0;      0\n"
)
MockUchConsumoAguaVazioUnidade = "UCH-CONSUMO-AGUA-VAZIO-UNIDADE;1;2;2;10.0"
MockUchLimiteMudancaStatusVazioUnidade = (
    "UCH-LIMITE-MUDANCA-STATUS-VAZIO-UNIDADE;1;2;2;5"
)
MockUchCustoPartidaUnidade = "UCH-CUSTO-PARTIDA-UNIDADE;1;2;2;300.50"
MockUchCustoPartidaVazioUnidade = "UCH-CUSTO-PARTIDA-VAZIO-UNIDADE;1;2;2;100.50"
