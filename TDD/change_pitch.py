import numpy as np
from scipy.io.wavfile import read, write

import numpy as np

def hz_to_midi(frequency_hz):
    return 69 + 12 * np.log2(frequency_hz / 440)

def hz_to_semitone_shift(frequency_hz):
    return 12 * np.log2(frequency_hz / 440)

def change_pitch(input_file, output_file, target_frequency):
    # Read the WAV file
    sample_rate, data = read(input_file)

    # Calculate the current pitch frequency
    current_frequency = 1.0 / (1.0 / sample_rate * len(data))

    # Calculate the pitch ratio
    pitch_ratio = target_frequency / current_frequency

    # Use numpy to change the pitch
    changed_data = np.interp(
        np.arange(0, len(data), pitch_ratio),
        np.arange(0, len(data)),
        data
    ).astype(np.int16)

    # Write the result to a new WAV file
    write(output_file, sample_rate, changed_data)

# Example usage:
input_file = "test.wav"
output_file = "output_pitch_changed.wav"
target_frequency = 453.99822301199464   # Adjust this value to your target frequency


target_frequency = hz_to_semitone_shift(target_frequency)
print(f"MIDI Note: {target_frequency}")

change_pitch(input_file, output_file, target_frequency)