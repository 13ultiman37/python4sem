class C32:
    def __init__(self):
        self.state = 'A'
        self.states = {
            'A': {
                'chip': ('B', 0),
                'click': ('H', 1)
            },
            'B': {
                'chain': ('C', 2),
                'chip': ('D', 4),
                'click': ('H', 3)
            },
            'C': {'chain': ('D', 5)},
            'D': {
                'chain': ('E', 6),
                'click': ('G', 7)
            },
            'E': {
                'chip': ('F', 8),
                'chain': ('G', 9)
            },
            'F': {'chip': ('G', 10)},
            'G': {'chain': ('H', 11)}
        }

    def set_state(self, method):
        try:
            new_state = self.states.get(self.state).get(method)
            if new_state is None:
                raise RuntimeError
            self.state = new_state[0]
            return new_state[1]
        except RuntimeError:
            return None

    def chip(self):
        return self.set_state('chip')

    def chain(self):
        return self.set_state('chain')

    def click(self):
        return self.set_state('click')


o = C32()
print(o.chain())
print(o.chip())
print(o.chain())
