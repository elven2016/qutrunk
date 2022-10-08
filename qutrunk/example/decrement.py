"""Self-increment operation and Self-decrement operation example."""
from qutrunk.circuit import QCircuit
from qutrunk.circuit.gates import Measure, All
from qutrunk.circuit.ops import QSP
from qutrunk.circuit.ops import DEC


def decrement(num_qubits, init_value):
    circuit = QCircuit()
    qr = circuit.allocate(num_qubits)

    QSP(init_value) * qr

    DEC * qr

    All(Measure) * qr
    res = circuit.run()
    print(res.get_outcome())

    return circuit


if __name__ == "__main__":
    circuit = decrement(4, 0)
    # circuit.print(unroll=False)

