from requirements import *

class wavVisualizer:
    def __init__(self, target):
        self.target_file = target
        self.signal = None
        self.time = None

    def visualize_parsed(self, parsed_signal, parsed_time):
        plt.figure(figsize=(10, 4))
        plt.plot(parsed_time, parsed_signal)
        plt.title(f'Visualized WAV File ({self.target_file})')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
     # plt.savefig('Visualized_waveform.png')
        plt.close()
        