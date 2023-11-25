import numpy as np


"""

test.wav 453.99822301199464 Hz
voice.wav 250.24509803921566 Hz
"""
def hz_to_semitone_shift(frequency_hz):
    return 12 * np.log2(frequency_hz / 440)

# Example usage:
frequency_hz = 453.99822301199464  # Replace this with your frequency
semitone_shift = hz_to_semitone_shift(frequency_hz)
print(f"Semitone Shift: {semitone_shift} semitones")