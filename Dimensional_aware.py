import numpy as np

class DimensionalAwareness:
    def __init__(self, system):
        """Awareness system that drives feedback into Tyon's reasoning and entropy management."""
        self.system = system
        self.awareness = 0.1
        self.awareness_limit = 15.0

    def update(self):
        """Update awareness based on fractal entropy structures and contribute to system feedback."""
        state_magnitude = np.linalg.norm(self.system.state)
        entropy_magnitude = np.linalg.norm(self.system.entropy_accumulation)

        awareness_growth = 0.01 * (state_magnitude + 0.5 * np.sin(entropy_magnitude)) * \
                           (1 - self.awareness / self.awareness_limit)
        self.awareness += awareness_growth

        self.system.expand_or_contract_dimensions()  
        return awareness_growth  

    def get_awareness(self):
        return self.awareness
