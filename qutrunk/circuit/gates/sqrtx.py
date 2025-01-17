import numpy as np

from .basicgate import BasicGate
from qutrunk.circuit import Command
from qutrunk.circuit.qubit import QuBit


class SqrtXGate(BasicGate):
    """Square-root X gate class.

    Example:
        .. code-block:: python

            SqrtX * qr[0]
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "SqrtX"

    def __or__(self, qubit):
        """Quantum logic gate operation.

        Args:
            qubit: The quantum bit to apply SqrtX gate.

        Example:
            .. code-block:: python

                SqrtX * qr[0]

        Raises:
            NotImplementedError: If the argument is not a Qubit object.
        """
        if not isinstance(qubit, QuBit):
            raise TypeError("The argument must be Qubit object.")

        targets = [qubit.index]
        cmd = Command(self, targets, inverse=self.is_inverse)
        self.commit(qubit.circuit, cmd)

    def __mul__(self, qubit):
        """Overwrite * operator to achieve quantum logic gate operation, \
            reuse __or__ operator implement."""
        self.__or__(qubit)

    @property
    def matrix(self):
        """Access to the matrix property of this gate."""
        return 0.5 * np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]])

    def inv(self):
        """Apply inverse gate."""
        gate = SqrtXGate()
        gate.is_inverse = not self.is_inverse
        return gate

    def ctrl(self, ctrl_cnt=1):
        """Apply controlled gate.
        
        Args:
            ctrl_cnt: The number of control qubits, default: 1.
        """
        if ctrl_cnt > 1:
            raise ValueError("SqrtX gate do not support multiple control bits.")
        gate = CSqrtXGate()
        gate.is_inverse = self.is_inverse
        return gate


SqrtX = SqrtXGate()


class CSqrtXGate(BasicGate):
    """Controlled-√X gate.

    Example:
        .. code-block:: python

            CSqrtX * (qr[0], qr[1])
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "CSqrtX"

    def __or__(self, qubits):
        """Quantum logic gate operation.

        Args:
            qubits: qubits[0] is control qubit, qubits[1] is target qubit.

        Example:
            .. code-block:: python

                CSqrtX * (qr[0], qr[1])

        Raises:
            TypeError: If the argument is not a Qubit object.
            AttributeError: If the qubits should not be two.
        """
        if not all(isinstance(qubit, QuBit) for qubit in qubits):
            raise TypeError("The argument must be Qubit object.")

        if len(qubits) != 2:
            raise ValueError(
                "Parameter error: One controlled and one target qubit are required."
            )

        self.qubits = qubits
        controls = [qubits[0].index]
        targets = [qubits[1].index]
        cmd = Command(self, targets, controls, inverse=self.is_inverse)
        self.commit(qubits[0].circuit, cmd)

    def __mul__(self, qubits):
        """Overwrite * operator to achieve quantum logic gate operation, reuse __or__ operator implement."""
        self.__or__(qubits)

    @property
    def matrix(self):
        """Access to the matrix property of this gate."""
        return np.array(
            [(1 + 1j) / 2, 0, (1 - 1j) / 2, 0],
            [0, 1, 0, 0],
            [(1 - 1j) / 2, 0, (1 + 1j) / 2, 0],
            [0, 0, 0, 1],
        )

    def inv(self):
        """Apply inverse gate"""
        gate = CSqrtXGate()
        gate.is_inverse = not self.is_inverse
        return gate


CSqrtX = CSqrtXGate()
