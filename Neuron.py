import random

class Activation:
    @staticmethod
    def IDENTITY(x):
        return x

class Neuron:

    ID = 0

    def __init__(self, f = Activation.IDENTITY):
        self._f = f
        self._conn = []
        self._output = 0
        self._id = Neuron.next_id()
        self._type = ""

    def get_id(self):
        return self._id
    
    def add_connection(self, neuron, weight = random.uniform(-1.0,1.0)):
        self._conn.append((neuron,weight))

    def get_output(self):
        return self._output

    def process(self):
        temp = 0

        for c in self._conn:
            temp += c[0].get_output()*c[1]

        temp = self._f(temp)
        self._output = temp

        return temp

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    @staticmethod
    def next_id():
        i = Neuron.ID
        Neuron.ID += 1
        return i

    def __str__(self):
        s = ""
        s += self.get_type()+" Neuron({}):\n".format(self._id)
        s += "  Activation Function: {}\n".format(self._f)
        s += "  Connections:\n"
        for c in self._conn:
            s += "      "+c[0].get_type()+" Id {} -> Weight {}\n".format(c[0].get_id(), c[1])

        return s

class InputNeuron():

    def __init__(self, f = Activation.IDENTITY):
        self._f = f
        self._value = 0
        self._id = Neuron.next_id()
        self._type = "Input"

    def get_id(self):
        return self._id

    def set_input(self, v):
        self._value = v

    def get_output(self):
        return self._value

    def process(self):
        self._value = self._f(self._value)
        return self._value

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t


class Layer:

    ID = 0

    def __init__(self, f = Activation.IDENTITY, n=0):
        self._f = f
        self._neuron = []
        for _ in range(n):
            self.add_neuron()
        self._id = Layer.next_id()
        self._type = ""

    def get_id(self):
        return self._id

    def add_neuron(self, n = 1):
        neuron = []
        for _ in range(n):
            neuron.append(Neuron(self._f))
            self._neuron.append(neuron[i])
        return neuron

    def process(self):
        for n in self._neuron:
            n.process()

    def get_output(self):
        out = []
        for n in self._neuron:
            out.append(n.get_output())
        return out

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    @staticmethod
    def next_id():
        i = Layer.ID
        Layer.ID += 1
        return i

    def __str__(self):
        s = ""
        s += self.get_type()+" Layer({}):\n".format(self._id)
        s += "  Activation Function: {}\n".format(self._f)
        s += "  Neurons:\n"
        for n in self._neuron:
            s += "      "+n.get_type()+" Neuron({}):\n".format(n._id)

        return s


class InputLayer:

    def __init__(self, f = Activation.IDENTITY, n=0):
        self._f = f
        self._neuron = []
        for _ in range(n):
            self.add_neuron()
        self._id = Layer.next_id()
        self._type = "Input"

    def get_id(self):
        return self._id

    def add_neuron(self, n = 1):
        neuron = []
        for _ in range(n):
            neuron.append(InputNeuron(self._f))
            self._neuron.append(neuron[i])
        return neuron

    def process(self):
        for n in self._neuron:
            n.process()

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    def set_input(self, inp):
        for i in range(self._neuron):
            self._neuron[i].set_input(inp[i])

    def get_output(self):
        out = []
        for n in self._neuron:
            out.append(n.get_output())
        return out

class Net:
    
    def __init__(self, i, o, h = [], f_i = Activation.IDENTITY, f_o = Activation.IDENTITY, f_h = []):
        self._input = InputLayer(f_i, i)
        self._output = Layer(f_o, o)
        self._hidden = []
        for i in range(h):
            self._hidden.append(Layer(f_h[i],h[i]))

inp = []

p = Neuron()

for i in range(3):
    n = InputNeuron()
    n.set_input(i)
    inp.append(n)
    p.add_connection(n,3-i)

print(p.process())