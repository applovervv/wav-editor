import wave
import numpy as np
from scipy.interpolate import interp1d

def pitch_shift(input_file, output_file, semitone_shift):
    # Read the WAV file
    with wave.open(input_file, 'rb') as wav_file:
        signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
        framerate = wav_file.getframerate()

    # Calculate the time axis
    time = np.arange(0, len(signal)) / framerate

    # Calculate the pitch-shifted time axis
    shifted_time = time * 2**(semitone_shift / 12.0)

    # Interpolate the signal at the new time points
    shifted_signal = np.interp(shifted_time, time, signal)

    # Write the pitch-shifted signal to a new WAV file
    with wave.open(output_file, 'wb') as output_wav:
        output_wav.setnchannels(1)
        output_wav.setsampwidth(2)
        output_wav.setframerate(framerate)
        output_wav.writeframes(shifted_signal.astype(np.int16).tobytes())

# Example usage:
pitch_shift('test.wav', 'output_pitch_shifted.wav', semitone_shift=0.5421975233413159)
