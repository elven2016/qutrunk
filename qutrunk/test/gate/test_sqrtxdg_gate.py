import numpy as np

from qutrunk.circuit.gates import SqrtXdg
from qutrunk.circuit import QCircuit
from qutrunk.test.global_parameters import ZERO_STATE


def test_sqrtx_gate():
    """Test SqrtXdg gate."""
    # local backend
    circuit = QCircuit()
    qr = circuit.allocate(1)
    SqrtXdg * qr[0]
    result = circuit.get_statevector()
    result_backend = np.array(result).reshape(-1, 1)

    # math
    result_math = np.dot(SqrtXdg.matrix, ZERO_STATE)

    assert np.allclose(result_backend, result_math)


def test_sqrtx_inverse_gate():
    """Test the inverse of SqrtXdg gate."""
    # local backend
    circuit = QCircuit()
    qr = circuit.allocate(1)
    SqrtXdg.inv() * qr[0]
    result = circuit.get_statevector()
    result_backend = np.array(result).reshape(-1, 1)

    # math
    m = 0.5 * np.array([
        [[1 + 1j, 1 - 1j],
         [1 - 1j, 1 + 1j]]
    ])
    result_math = np.dot(m, ZERO_STATE)

    assert np.allclose(result_backend, result_math)
