from typing import Any
import importlib

_LAZY_IMPORTS: dict[str, str] = {
    "Areacont": ".areacont",
    "AvlAltQueda": ".avl_altqueda",
    "AvlDesvFpha": ".avl_desvfpha",
    "AvlEstatFpha": ".avl_estatfpha",
    "AvlFpha1": ".avl_fpha1",
    "AvlFpha2": ".avl_fpha2",
    "AvlFpha3": ".avl_fpha3",
    "Dadvaz": ".dadvaz",
    "Deflant": ".deflant",
    "DesLogRelato": ".des_log_relato",
    "Desselet": ".desselet",
    "DessemArq": ".dessemarq",
    "Dessopc": ".dessopc",
    "Entdados": ".entdados",
    "Hidr": ".hidr",
    "LogInviab": ".log_inviab",
    "LogMatriz": ".log_matriz",
    "Operuh": ".operuh",
    "Operut": ".operut",
    "PdoAvalQmaxUsih": ".pdo_aval_qmaxusih",
    "PdoCmoBar": ".pdo_cmobar",
    "PdoEcoFcfCortes": ".pdo_eco_fcfcortes",
    "PdoEcoUsih": ".pdo_eco_usih",
    "PdoEcoUsihConj": ".pdo_eco_usih_conj",
    "PdoEcoUsihPolin": ".pdo_eco_usih_polin",
    "PdoEolica": ".pdo_eolica",
    "PdoHidr": ".pdo_hidr",
    "PdoInter": ".pdo_inter",
    "PdoOperLpp": ".pdo_oper_lpp",
    "PdoOperTerm": ".pdo_oper_term",
    "PdoOperTitulacaoContratos": ".pdo_oper_titulacao_contratos",
    "PdoOperTitulacaoUsinas": ".pdo_oper_titulacao_usinas",
    "PdoOperTviagCalha": ".pdo_oper_tviag_calha",
    "PdoOperUct": ".pdo_oper_uct",
    "PdoOperacao": ".pdo_operacao",
    "PdoReserva": ".pdo_reserva",
    "PdoSist": ".pdo_sist",
    "PdoSomFlux": ".pdo_somflux",
    "PdoTerm": ".pdo_term",
    "Renovaveis": ".renovaveis",
    "Respot": ".respot",
    "Term": ".termdat",
    "Uch": ".uch",
}

__all__ = sorted(_LAZY_IMPORTS.keys())


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module = importlib.import_module(_LAZY_IMPORTS[name], __name__)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return __all__
