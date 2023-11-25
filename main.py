from wavEditor import *

test_audio_signal = None
voice_audio_signal = None

wav_editor = wavEditor(input_file='test.wav')
wav_editor.parse_wav_file()
wav_editor.analyze_pitch()
test_audio_signal = wav_editor.parsed_signal
test_audio_pitch = wav_editor.analyzed_pitch

wav_editor = wavEditor(input_file='voice.wav')
wav_editor.parse_wav_file()
wav_editor.analyze_pitch()
voice_audio_signal = wav_editor.parsed_signal
voice_audio_pitch = wav_editor.analyzed_pitch

print("test.wav",test_audio_pitch,"Hz")
print("voice.wav",voice_audio_pitch,"Hz")

# wav_editor.merge_signal(test_audio_signal,voice_audio_signal)
# wav_editor.save_merged_signal_to_wav('merged_out.wav')

# wav_editor.calculate_pitch
