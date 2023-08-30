# Build a random number generator using quantum random number generator

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer


# Generate a random number between 0 and 1 use oop
class RandomNumberGenerator:
    def __init__(self, length):
        self.length = length
        self.qr = QuantumRegister(length)
        self.cr = ClassicalRegister(length)
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def generate(self):
        for i in range(self.length):
            self.circuit.h(self.qr[i])
            self.circuit.measure(self.qr[i], self.cr[i])
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return list(counts.keys())[0]

    def plot(self):
        self.circuit.draw(output='mpl')
        plt.show()

    def get_circuit(self):
        return self.circuit

    def get_qr(self):
        return self.qr

    def get_cr(self):
        return self.cr

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length
        self.qr = QuantumRegister(length)
        self.cr = ClassicalRegister(length)
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def get_result(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return list(counts.keys())[0]

    def get_result_list(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return list(counts.keys())

    def get_result_dict(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def get_result_prob(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return list(counts.values())[0] / 1000

    def get_result_prob_list(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return int(counts.values()) / 1000


# Generate a random number between 0 and 1 use function
def generate_random_number(length):
    qr = QuantumRegister(length)
    cr = ClassicalRegister(length)
    circuit = QuantumCircuit(qr, cr)
    for i in range(length):
        circuit.h(qr[i])
        circuit.measure(qr[i], cr[i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    return list(counts.keys())[0]


# Generate a random number between 0 and 1 use function
def generate_random_number_list(length, num):
    qr = QuantumRegister(length)
    cr = ClassicalRegister(length)
    circuit = QuantumCircuit(qr, cr)
    for i in range(length):
        circuit.h(qr[i])
        circuit.measure(qr[i], cr[i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=num)
    result = job.result()
    counts = result.get_counts(circuit)
    return list(counts.keys())


# Generate a random number between 0 and 1 use function
def generate_random_number_dict(length, num):
    qr = QuantumRegister(length)
    cr = ClassicalRegister(length)
    circuit = QuantumCircuit(qr, cr)
    for i in range(length):
        circuit.h(qr[i])
        circuit.measure(qr[i], cr[i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=num)
    result = job.result()
    counts = result.get_counts(circuit)
    return counts


# Generate a random number between 0 and 1 use function
def generate_random_number_prob(length, num):
    qr = QuantumRegister(length)
    cr = ClassicalRegister(length)
    circuit = QuantumCircuit(qr, cr)
    for i in range(length):
        circuit.h(qr[i])
        circuit.measure(qr[i], cr[i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=num)
    result = job.result()
    counts = result.get_counts(circuit)
    return list(counts.values())[0] / num


# def main():
def main():
    length = 5
    qr = QuantumRegister(length)
    cr = ClassicalRegister(length)
    circuit = QuantumCircuit(qr, cr)
    for i in range(length):
        circuit.h(qr[i])
        circuit.measure(qr[i], cr[i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    print(list(counts.keys())[0])
    circuit.draw(output='mpl')
    plt.show()
    print(generate_random_number(5))
    print(generate_random_number_list(5, 1000))
    print(generate_random_number_dict(5, 1000))
    print(generate_random_number_prob(5, 1000))
    print(RandomNumberGenerator(5).generate())
    print(RandomNumberGenerator(5).get_result())
    print(RandomNumberGenerator(5).get_result_list())
    print(RandomNumberGenerator(5).get_result_dict())
    print(RandomNumberGenerator(5).get_result_prob())
    print(RandomNumberGenerator(5).get_result_prob_list())
    RandomNumberGenerator(5).plot()
    print(RandomNumberGenerator(5).get_circuit())
    print(RandomNumberGenerator(5).get_qr())
    print(RandomNumberGenerator(5).get_cr())
    print(RandomNumberGenerator(5).get_length())
    RandomNumberGenerator(5).set_length(6)
    print(RandomNumberGenerator(5).get_length())
    RandomNumberGenerator(5).plot()
    print(RandomNumberGenerator(5).get_result())
    print(RandomNumberGenerator(5).get_result_list())
    print(RandomNumberGenerator(5).get_result_dict())
    print(RandomNumberGenerator(5).get_result_prob())
    print(RandomNumberGenerator(5).get_result_prob_list())
    RandomNumberGenerator(5).plot()
    print(RandomNumberGenerator(5).get_circuit())
    print(RandomNumberGenerator(5).get_qr())
    print(RandomNumberGenerator(5).get_cr())
    print(RandomNumberGenerator(5).get_length())
    RandomNumberGenerator(5).set_length(6)
    print(RandomNumberGenerator(5).get_length())
    RandomNumberGenerator(5).plot()


if __name__ == '__main__':
    main()
