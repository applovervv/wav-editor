from requirements import *


class wavParser:
    def __init__(self, target):
        self.target_file = target
        self.parsed_signal = None
        self.parsed_time = None

    def parse_wav_file(self):
        with wave.open(self.target_file, 'rb') as wav_file:
            self.parsed_signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
            self.parsed_time = np.arange(0, len(self.parsed_signal)) / wav_file.getframerate()


   