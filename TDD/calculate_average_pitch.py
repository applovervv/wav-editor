import wave
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

def calculate_pitch(input_file):
    # Read the WAV file
    with wave.open(input_file, 'rb') as wav_file:
        signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
        framerate = wav_file.getframerate()

    # Calculate the power spectrum using FFT
    spectrum = np.abs(fft(signal))

    # Calculate the corresponding frequencies
    frequencies = np.fft.fftfreq(len(spectrum), d=1/framerate)

    # Exclude negative frequencies and their corresponding amplitudes
    positive_frequencies = frequencies[1:len(frequencies)//2]
    positive_spectrum = spectrum[1:len(spectrum)//2]

    # Find the index of the maximum amplitude
    max_amplitude_index = np.argmax(positive_spectrum)

    # Calculate the corresponding pitch
    pitch = positive_frequencies[max_amplitude_index]

    return pitch

# Example usage:
input_file = 'voice.wav'
average_pitch = calculate_pitch(input_file)
print(f"Average pitch of the WAV file: {average_pitch} Hz")
