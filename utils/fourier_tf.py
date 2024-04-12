import numpy as np
import matplotlib.pyplot as plt
import librosa

# 오디오 파일 로드
audio_path = "../../pianosound/Can't_Help_Falling_In_Love.wav"
y, sr = librosa.load(audio_path)

# 푸리에 변환 수행
fft_result = np.fft.fft(y)
magnitude = np.abs(fft_result)  # 진폭 스펙트럼 계산
frequency = np.linspace(0, sr, len(magnitude))  # 주파수 축 생성

# 주파수 축을 절반으로 줄이기 (나이퀴스트 주파수 이상은 의미 없음)
half_frequency = frequency[: len(frequency) // 2]
half_magnitude = magnitude[: len(magnitude) // 2]

# 주파수 스펙트럼 시각화
plt.figure(figsize=(10, 5))
plt.plot(half_frequency, half_magnitude)
plt.title("Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
