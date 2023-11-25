import wave
import numpy as np

def mix_wav(input_files, output_file):
    # 첫 번째 WAV 파일의 신호로 초기화
    with wave.open(input_files[0], 'rb') as wav_file:
        mixed_signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)

    # 나머지 WAV 파일의 신호를 이어 붙이기
    for input_file in input_files[1:]:
        with wave.open(input_file, 'rb') as wav_file:
            signal = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
            mixed_signal = np.add(mixed_signal, signal)

    # 신호를 정규화하여 클리핑을 방지
    mixed_signal = np.int16(mixed_signal / len(input_files))

    # 섞인 신호를 새로운 WAV 파일로 저장
    with wave.open(output_file, 'wb') as output_wav:
        output_wav.setnchannels(1)  # 모노 오디오로 가정
        output_wav.setsampwidth(2)  # int16 데이터 타입에 대한 2바이트
        output_wav.setframerate(wav_file.getframerate())  # 마지막 WAV 파일의 프레임레이트 사용
        output_wav.writeframes(mixed_signal.tobytes())
        
# 사용 예시:
input_files = ['test.wav', 'voice.wav']
output_file = 'output_mixed.wav'
mix_wav(input_files, output_file)