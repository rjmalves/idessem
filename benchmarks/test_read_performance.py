"""Benchmark suite for idessem read performance.

Run with: uv run pytest benchmarks/ --benchmark-only -n 0
"""

from unittest.mock import patch

from idessem.dessem.hidr import Hidr
from idessem.dessem.entdados import Entdados
from idessem.dessem.pdo_eco_usih import PdoEcoUsih
from idessem.dessem.pdo_operacao import PdoOperacao
from tests.mocks.mock_open import mock_open
from tests.mocks.arquivos.entdados import MockEntDados
from tests.mocks.arquivos.pdo_eco_usih import MockPdoEcoUsih
from tests.mocks.arquivos.pdo_operacao import MockPdoOperacao


HIDR_PATH = "./tests/mocks/arquivos/hidr.dat"
DUMMY_PATH = "./tests/__init__.py"


def test_read_hidr(benchmark):
    """Benchmark binary RegisterFile read (Hidr)."""
    benchmark(Hidr.read, HIDR_PATH)


def test_read_entdados(benchmark):
    """Benchmark text RegisterFile read (Entdados)."""
    with patch("builtins.open", mock_open(read_data="".join(MockEntDados))):
        benchmark(Entdados.read, DUMMY_PATH)


def test_read_pdo_eco_usih(benchmark):
    """Benchmark ArquivoCSV read (PdoEcoUsih)."""
    with patch("builtins.open", mock_open(read_data="".join(MockPdoEcoUsih))):
        benchmark(PdoEcoUsih.read, DUMMY_PATH)


def test_read_pdo_operacao(benchmark):
    """Benchmark BlockFile read (PdoOperacao)."""
    with patch("builtins.open", mock_open(read_data="".join(MockPdoOperacao))):
        benchmark(PdoOperacao.read, DUMMY_PATH)
