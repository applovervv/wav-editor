from requirements import *

class wavAnalyzer:
    def __init__(self, target):
        self.target_file = target
        self.analyzed_pitch = None

    def analyze_pitch(self):
        with wave.open(self.target_file, 'rb') as wav_file:
            signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
            framerate = wav_file.getframerate()

        spectrum = np.abs(fft(signal))

        frequencies = np.fft.fftfreq(len(spectrum), d=1/framerate)

        positive_frequencies = frequencies[1:len(frequencies)//2]
        positive_spectrum = spectrum[1:len(spectrum)//2]

        max_amplitude_index = np.argmax(positive_spectrum)

        pitch = positive_frequencies[max_amplitude_index]

        self.analyzed_pitch = pitch