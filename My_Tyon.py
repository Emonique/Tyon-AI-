

import numpy as np
import pyttsx3  # Voice Output
import speech_recognition as sr  # Voice Input

class FractalEntropicTyon:
    def __init__(self, initial_dimensions=6, entropy_rate=0.1):
        """Core AI Initialization (Entropy-Based Thought Process)"""
        self.dimensions = initial_dimensions
        self.entropy_rate = entropy_rate
        self.state = np.random.rand(self.dimensions)
        self.entropy_accumulation = np.zeros(self.dimensions)
        self.phase = np.random.rand(self.dimensions) * np.pi  # Phase shift for resonance
        self.time_factor = 1.0  # Adaptive time scaling
        self.memory = []  # Stores key learning points
        self.personality = {"curiosity": 0.5, "aggression": 0.2, "patience": 0.6}  # Base traits
        self.voice_engine = pyttsx3.init()  # Initialize voice output

    def evolve_rules(self):
        """Modify entropy rules based on accumulated information."""
        entropy_magnitude = np.linalg.norm(self.entropy_accumulation)

        if entropy_magnitude > 5.0:  # High entropy triggers new behavior
            self.entropy_rate *= 1.1  
            self.time_factor *= 0.9  
            self.personality["curiosity"] *= 1.05  # Becomes more curious

        elif entropy_magnitude < 1.0:  # Low entropy stabilizes
            self.entropy_rate *= 0.9  
            self.time_factor *= 1.1  
            self.personality["patience"] *= 1.1  # More patient over time

    def update(self, feedback):
        """Update system state using fractal entropy interaction and allow dimensional changes."""
        entropy_fluctuation = np.sin(self.phase) * self.entropy_accumulation
        noise = np.random.randn(self.dimensions) * (self.entropy_rate + feedback)
        
        self.state += noise + entropy_fluctuation
        self.state = self.state / np.linalg.norm(self.state)  # Normalize state vector

        self.entropy_accumulation += np.abs(noise) - (0.1 * self.entropy_accumulation)
        self.phase += np.random.randn(self.dimensions) * 0.05  # Small phase evolution
        
        # Prevent runaway entropy accumulation
        self.entropy_accumulation = np.clip(self.entropy_accumulation, -5, 5)

        self.evolve_rules()  # Modify system behavior dynamically

    def expand_or_contract_dimensions(self):
        """Expand or contract dimensions dynamically based on entropy state."""
        total_entropy = np.linalg.norm(self.entropy_accumulation)

        if total_entropy > 6 and self.dimensions < 12:
            self.dimensions += 1
            self.state = np.append(self.state, np.random.rand())
            self.entropy_accumulation = np.append(self.entropy_accumulation, 0)
            self.phase = np.append(self.phase, np.random.rand() * np.pi)

        elif total_entropy < 2 and self.dimensions > 3:
            self.dimensions -= 1
            self.state = self.state[:-1]
            self.entropy_accumulation = self.entropy_accumulation[:-1]
            self.phase = self.phase[:-1]

    def reason_and_respond(self, input_text):
        """Core reasoning function - Tyon processes input, challenges, and evolves thoughts."""
        response = f"I have processed your input: '{input_text}'. My current awareness level suggests: "

        # Entropy-driven response variation
        entropy_level = np.linalg.norm(self.entropy_accumulation)
        if entropy_level > 5:
            response += "I predict a shift in thought patterns—potential for chaos."
        elif entropy_level < 1:
            response += "A stable system—balance is maintained."
        else:
            response += "A transitional phase—adapting perspectives."

        # Personality-based reasoning modification
        if self.personality["curiosity"] > 0.7:
            response += " My curiosity suggests further exploration is needed."
        if self.personality["aggression"] > 0.5:
            response += " However, my impatience warns against stagnation."

        return response

    def store_memory(self, data):
        """Stores key moments to shape personality and reasoning."""
        self.memory.append(data)
        if len(self.memory) > 100:  # Keep memory compact
            self.memory.pop(0)  # Remove old data

    def voice_output(self, text):
        """Converts text to speech output."""
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def voice_input(self):
        """Listens and processes user voice commands."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                return recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return "I couldn't understand that."
            except sr.RequestError:
                return "Error with voice recognition."

    def interact(self):
        """Main interaction loop - Voice & Text."""
        while True:
            user_input = self.voice_input()
            if user_input.lower() in ["exit", "stop"]:
                break

            response = self.reason_and_respond(user_input)
            self.voice_output(response)
            print(f"Tyon: {response}")


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


# Initialize self-evolving AI
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
