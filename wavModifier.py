from requirements import *

class wavModifier():
    def __init__(self, target):
        self.target_file = target
        self.merged_signal = None
        self.time = None

    def merge_signal(self, signal1, signal2):
        len_signal1 = len(signal1)
        len_signal2 = len(signal2)
        
        if len_signal1 >= len_signal2:
            # array1이 더 크거나 같은 경우
            self.merged_signal = signal1 + np.pad(signal2, (0, len_signal1 - len_signal2))
        else:
            # array2가 더 큰 경우
            self.merged_signal  = np.pad(signal1, (0, len_signal2 - len_signal1)) + signal2

    def save_merged_signal_to_wav(self,output_file):
            with wave.open(output_file, 'wb') as output_wav:
                with wave.open(self.target_file, 'rb') as input_wav:
                    output_wav.setnchannels(input_wav.getnchannels())
                    output_wav.setsampwidth(input_wav.getsampwidth())
                    output_wav.setframerate(input_wav.getframerate())
                    output_wav.writeframes(self.merged_signal.tobytes())

