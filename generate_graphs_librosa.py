import librosa
import librosa.display
import matplotlib.pyplot as plt
import sklearn
from sklearn.preprocessing import normalize

audio_recording = "portiona55.wav"
data,sr=librosa.load(audio_recording)
print(type(data),type(sr)) #Loads and decodes the audio as time series

#
# plt.figure(figsize=(18,6))
# librosa.display.waveshow(data,color='#2B4F72')
# plt.show()


# stft=librosa.stft(data)
# stft_amp_to_db=librosa.amplitude_to_db(abs(stft))
# plt.figure(figsize=(14,6))
# librosa.display.specshow(stft_amp_to_db,sr=sr,x_axis="time",y_axis="hz")
# plt.colorbar()
# plt.show()

# spectral_rolloff=librosa.feature.spectral_rolloff(data+0.01, sr=sr)[0]
# plt.figure(figsize=(18,6))
# librosa.display.waveshow(data,sr=sr, alpha=0.6)
# plt.show()
#
# chroma_features = librosa.feature.chroma_stft(data, sr=sr)
# plt.figure(figsize=(18,6))
# librosa.display.specshow(chroma_features,sr=sr,x_axis='time',y_axis='chroma',cmap='coolwarm')
# plt.colorbar()
# plt.title("Chroma Feature")
# plt.show()

#
# start=1000
# end=1500
# plt.figure(figsize=(18,6))
# plt.plot(data[start:end])
# plt.grid()
# plt.show()
#
# spectral_centroids = librosa.feature.spectral_centroid(data, sr=sr)[0]
# spectral_centroids.shape
# (775,)
# # Computing the time variable for visualization
# frames = range(len(spectral_centroids))
# t = librosa.frames_to_time(frames)
# # Normalising the spectral centroid for visualisation
# def normalize(x, axis=0):
#     return sklearn.preprocessing.minmax_scale(x, axis=axis)
# #Plotting the Spectral Centroid along the waveform
# librosa.display.waveshow(data, sr=sr, alpha=0.4)
# plt.plot(t, normalize(spectral_centroids), color='r')
# plt.show()
plt.figure(figsize=(18,6))
mfccs = librosa.feature.mfcc(data, sr=sr)
print(mfccs.shape)
(20, 97)
#Displaying  the MFCCs:
librosa.display.specshow(mfccs, sr=sr, x_axis='time')
plt.show()