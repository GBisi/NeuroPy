class Perceptron:
    
    def __init__(self, f):
        ''' 
        Initialize new Perceptron
        params f: activation function
        '''
    
        self.f = f
        self.weight = [] #list of weights
        self.input = [] #list of input
        self.output = 0
        
    def add_link(self, w):
        ''' 
        Add a link in the perceptron
        params w: the weight of the link
        '''
        self.weight.append(w)
        self.input.append(0)
        
    def set_input(self, inp):
        ''' 
        Set new input 
        params inp: array of input
        '''
        if len(inp) == len(self.weight):
            self.input = inp

    def process(self):
        ''' 
        Process the input 
        '''
        res = 0

        print("PROCESS")

        #step 1
        for i in range(len(self.weight)): 
            print("{} * {} -> {}".format(self.input[i], self.weight[i], self.input[i]*self.weight[i]))
            res += self.input[i]*self.weight[i]

        #step 2
        self.output = self.f(res)
        print("----\n{} -> {}".format(res,self.output))

        return self.output

    def get_output(self):
        ''' 
        return the output
        '''
        return self.output

    def __str__(self):
        return "INPUT: {}\nWEIGHT: {}\nOUTPUT: {}".format(self.input,self.weight,self.output)

def Identity(x):
    return x

def Heaviside(x):
    if x > 0:
        return 1
    else:
        return 0

p = Perceptron(Heaviside)

p.add_link(1)
p.add_link(-1)
p.add_link(0)

p.set_input([5,2])

print(p)
p.process()