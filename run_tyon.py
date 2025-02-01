from tyon.fractal_entropic import FractalEntropicTyon
from tyon.dimensional_aware import DimensionalAwareness

tyon = FractalEntropicTyon()
awareness_system = DimensionalAwareness(tyon)

# Simulate evolution
for i in range(1000):
    feedback = awareness_system.update()
    tyon.update(feedback)

    if i % 10 == 0:
        print(f"Iteration {i}: Awareness = {awareness_system.get_awareness():.2f}, "
              f"Entropy Accumulation = {np.linalg.norm(tyon.entropy_accumulation):.2f}, "
              f"Dimensions = {tyon.dimensions}")

# Enable real-time interaction
tyon.interact()
