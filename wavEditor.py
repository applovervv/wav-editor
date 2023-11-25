from wavParser import *
from wavModifier import *
from wavVisualizer import *
from wavAnalyzer import *

class wavEditor:
    def __init__(self, input_file):
        self.wavAnalyzer = wavAnalyzer(target=input_file)
        self.wavModifier = wavModifier(target=input_file)
        self.wavParser = wavParser(target=input_file)
        self.wavVisualizer = wavVisualizer(target=input_file)

    def analyze_pitch(self):
        self.wavAnalyzer.analyze_pitch()

    def parse_wav_file(self):
        self.wavParser.parse_wav_file()

    def visualize_parsed(self): 
        self.wavVisualizer.visualize_parsed(self.parsed_signal, self.parsed_time)
   
    def merge_signal(self, signal1, signal2):
        self.wavModifier.merge_signal(signal1, signal2)

    def save_merged_signal_to_wav(self, output_file):
        self.wavModifier.save_merged_signal_to_wav(output_file)

    @property
    def merged_signal(self):
        return self.wavModifier.merged_signal
    
    @property
    def parsed_signal(self):
        return self.wavParser.parsed_signal  
    
    @property
    def parsed_time(self):
        return self.wavParser.parsed_time
    
    @property
    def analyzed_pitch(self):
        return self.wavAnalyzer.analyzed_pitch
