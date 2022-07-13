from visual_automata.fa.nfa import VisualNFA

class Main:
    nfa = VisualNFA(
        states={"q0", "q1", "q2",  "q3", "q4"},
        input_symbols={"a", "b", "c"},
        transitions= {
            "q0": {"a": {"q0"}, "": {"q1"}},
            "q1": {"a": {"q1"}, "b": {"q1"}, "": {"q2", "q3"}},
            "q2": {"c": {"q2"}},
            "q3": {"a": {"q3"}, "": {"q4"}},
            "q4": {"b": {"q4"}},
        },
        initial_state="q0",
        final_states={"q2", "q3", "q4"},
    )
    nfaEliminated = VisualNFA.eliminate_lambda(nfa)

    def isAcceptedNFA(self, myString):
        if self.nfa.accepts_input(myString):
            return True
        else: 
            print("Not Accepted")
            return False

    def isAcceptedNFAEliminated(self, myString):
        if self.nfaEliminated.accepts_input(myString):
            return True
        else:
            return False