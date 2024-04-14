import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 오디오 파일 로드
audio_path = "../../pianosound/Can't_Help_Falling_In_Love.wav"
y, sr = librosa.load(audio_path)

# Short-Time Fourier Transform (STFT)
D = np.abs(librosa.stft(y))

# 스펙트로그램을 데시벨 단위로 변환
S_db = librosa.amplitude_to_db(D, ref=np.max)

# 스펙트로그램 시각화
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_db, sr=sr, x_axis="time", y_axis="hz")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram")
plt.show()
