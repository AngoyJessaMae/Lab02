class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output  # Output is associated with the state itself
        self.transitions = {}  # transitions[input] = next_state

    def add_transition(self, input_symbol, next_state):
        """Add a transition for the given input symbol."""
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        """Get the next state for the given input symbol."""
        return self.transitions.get(input_symbol)


class MooreMachine:
    def __init__(self):
        self.states = {}
        self.start_state = None

    def add_state(self, name, output, is_start=False):
        """Add a new state to the machine with its associated output."""
        state = MooreState(name, output)
        self.states[name] = state
        if is_start:
            self.start_state = state
        return state

    def process_input(self, input_string):
        current_state = self.start_state
        output = current_state.output  # Output from initial state

        for symbol in input_string:
            current_state = current_state.get_next_state(symbol)
            if current_state:
                output += current_state.output

        return output



print("=" * 60)
print("CONVERTED MOORE MACHINE")
print("=" * 60)

moore = MooreMachine()

# Create Moore states with their associated outputs
# Based on the original Mealy machine transition table
A = moore.add_state("A", "A", is_start=True)
B = moore.add_state("B", "B")
C = moore.add_state("C", "C")
D = moore.add_state("D", "B")
E = moore.add_state("E", "C")

# Define transitions for the Moore machine based on Mealy table:
# State A: 0→A, 1→B
A.add_transition('0', A)
A.add_transition('1', B)

# State B: 0→C, 1→D
B.add_transition('0', C)
B.add_transition('1', D)

# State C: 0→D, 1→B
C.add_transition('0', D)
C.add_transition('1', B)

# State D: 0→B, 1→C
D.add_transition('0', B)
D.add_transition('1', C)

# State E: 0→D, 1→E
E.add_transition('0', D)
E.add_transition('1', E)


# --- Test inputs ---
print("\nMoore Machine Test Results:")
print("-" * 60)
inputs = ["00110", "11001", "1010110", "101111"]

for s in inputs:
    output = moore.process_input(s)
    print(f"Input:  {s}")
    print(f"Output: {output}\n")
