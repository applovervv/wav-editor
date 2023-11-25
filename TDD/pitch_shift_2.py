from pydub import AudioSegment

def pitch_shift(audio_path, output_path, target_pitch_hz):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # Calculate the current pitch frequency
    current_pitch_hz = audio.frame_rate

    # Calculate the speedup factor based on the pitch shift
    speedup_factor = target_pitch_hz / current_pitch_hz

    # Apply pitch shift without changing the duration
    shifted_audio = audio.speedup(playback_speed=speedup_factor)

    # Export the result
    shifted_audio.export(output_path, format="wav")

# 예제 사용:
input_file = "voice.wav"
output_file = "output_pitch_shifted.wav"
target_pitch_hz = 453.99822301199464  # 원하는 피치 (예: 440 Hz는 A4 음)

pitch_shift(input_file, output_file, target_pitch_hz)
