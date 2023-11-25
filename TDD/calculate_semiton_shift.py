import librosa
import numpy as np

def calculate_average_semitone_shift_librosa(file_path, hop_length=512, sr=44100):
    # Load the audio file
    y, sr = librosa.load(file_path, sr=sr)

    # Compute the pitch using LibROSA's piptrack
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)

    # Select the pitch with the highest magnitude for each frame
    pitch_indices = np.argmax(magnitudes, axis=0)
    pitch_values = pitches[pitch_indices, range(len(pitch_indices))]

    # Convert Hz to MIDI notes
    midi_notes = librosa.core.hz_to_midi(pitch_values)

    # Calculate the mean pitch deviation in semitones
    mean_semitone_shift = np.mean(midi_notes)

    return mean_semitone_shift

# Example usage:
file_path = "test.wav"
average_semitone_shift = calculate_average_semitone_shift_librosa(file_path)

print(f"Average Semitone Shift: {average_semitone_shift} semitones")
