"""self decrement example."""

from qutrunk.circuit import QCircuit
from qutrunk.circuit.gates import CNOT, Measure, Toffoli, X, All, MCX
from qutrunk.circuit.ops import QSP


def decrement(num_qubits, init_value):
    circuit = QCircuit()
    qr = circuit.allocate(num_qubits)

    QSP(init_value) * qr

    X * qr[0]
    CNOT * (qr[0], qr[1])
    Toffoli * (qr[0], qr[1], qr[2])
    MCX(3) * (qr[0], qr[1], qr[2], qr[3])

    All(Measure) * qr
    res = circuit.run()
    print(res.get_outcome())
    return circuit


if __name__ == "__main__":
    circuit = decrement(4, 0)
    circuit.draw()
