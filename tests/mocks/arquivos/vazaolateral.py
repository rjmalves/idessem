MockVazaoLateral = [
    " &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n",
    " & Influências laterais \n",
    " &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n",
    "& ============== Belo Monte e Pimental\n",
    " &;UsinaInfluenciada;FatorTurbinamento;FatorVertimento\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA;288;1;1\n",
    " &\n",
    " &;UsinaInfluenciada;CodigoPosto;FatorVazIncremental\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-POSTO;288;314;0.07\n",
    " &\n",
    " &;UsinaInfluenciada;CodigoUsina;Fator\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA;288;314;1\n",
    " &\n",
    "& ============== Itaipu e Baixo Iguacu\n",
    " &;UsinaInfluenciada;FatorTurbinamento;FatorVertimento\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA;66;1.03;1.03\n",
    " &\n",
    " &;UsinaInfluenciada;CodigoUsina;Fator\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA;66;83;1.17\n",
    " &\n",
    "& ============== Fontes AB e Fontes C\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA;147;1;1\n",
    " &\n",
    " &;UsinaInfluenciada;CodigoUsina;Fator\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA;147;146;1\n",
    "\t&\n",
    "& ============== Fontes C e Fontes AB\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA;146;1;1\n",
    " &\n",
    " &;UsinaInfluenciada;CodigoUsina;Fator\n",
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA;146;147;1",
]

MockHidreletricaVazaoJusanteInfluenciaDefluencia = (
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-DEFLUENCIA;288;1;1\n"
)
MockHidreletricaVazaoJusanteInfluenciaUsina = (
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-USINA;288;314;1\n"
)
MockHidreletricaVazaoJusanteInfluenciaPosto = (
    "HIDRELETRICA-VAZAO-JUSANTE-INFLUENCIA-POSTO;288;314;0.07\n"
)
