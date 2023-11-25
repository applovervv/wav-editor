import wave
import array
import math

def generate_sine_wave(frequency, duration, amplitude=0.5, sample_rate=44100):
    t = [i / sample_rate for i in range(int(duration * sample_rate))]
    samples = array.array('h', [int(amplitude * 32767.0 * math.sin(2.0 * math.pi * frequency * ti)) for ti in t])
    return samples

def text_to_speech(text, output_file='output.wav'):
    char_frequencies = {
        'ㄱ': 392.0, 'ㄴ': 440.0, 'ㄷ': 493.88, 'ㄹ': 523.25, 'ㅁ': 587.33,
        'ㅂ': 659.26, 'ㅅ': 698.46, 'ㅇ': 783.99, 'ㅈ': 880.0, 'ㅊ': 987.77,
        'ㅋ': 1046.5, 'ㅌ': 1174.66, 'ㅍ': 1318.51, 'ㅎ': 1396.91, 'ㅏ': 1567.98,
        'ㅑ': 1760.0, 'ㅓ': 1975.53, 'ㅕ': 2093.0, 'ㅗ': 2349.32, 'ㅛ': 2637.02,
        'ㅜ': 2793.83, 'ㅠ': 3135.96, 'ㅡ': 3520.0, 'ㅣ': 3951.07, ' ': 0  # 공백은 일시 정지를 나타냅니다.
    }

    samples = array.array('h')

    for char in text:
        if char in char_frequencies:
            frequency = char_frequencies[char]
            samples.extend(generate_sine_wave(frequency, 0.3))  # 각 글자에 대해 0.3초 동안의 사인 파형을 생성합니다.
        else:
            samples.extend(generate_sine_wave(0, 0.3))  # 알 수 없는 글자에 대해 일시 정지합니다.

    with wave.open(output_file, 'w') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(44100)
        wave_file.writeframes(samples.tobytes())

# 예제 사용:
text_to_speech("안녕하세요, 이것은 매우 기본적인 텍스트 음성 합성 예제입니다.")
