import librosa
import matplotlib.pyplot as plt
import numpy as np

# 오디오 파일 로드
audio_path = "../../pianosound/Can't_Help_Falling_In_Love.wav"
y, sr = librosa.load(audio_path)

# 시간 배열 생성
time = np.arange(0, len(y)) / sr

# 파형 시각화
plt.figure(figsize=(14, 5))
plt.plot(time, y)  # x축에 시간 배열 사용
plt.title("Audio Waveform")
plt.xlabel("Time (seconds)")  # x축 레이블을 초 단위로 변경
plt.ylabel("Amplitude")
plt.show()
