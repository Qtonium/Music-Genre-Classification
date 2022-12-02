import librosa
import librosa.display
import numpy
from csv import writer

import pandas as pd
from pydub import AudioSegment
import pandas as pd
import yt_dlp as youtube_dl
import os
from pathlib import Path
list=[]
l2=[]


def Lib(path):

    audio_rec=path
    data,sr = librosa.load(audio_rec)
    list.append(30000)
    l2.append("Length")
    crm_sift=librosa.feature.chroma_stft(y=data,sr=sr)
    list.append(numpy.mean(crm_sift))
    l2.append("chroma_stft_mean")
    list.append(numpy.var(crm_sift))
    l2.append("chroma_stft_var")
    rms = librosa.feature.rms(data)
    list.append(numpy.mean(rms))
    l2.append("rms_mean")
    list.append(numpy.var(rms))
    l2.append("rms_var")
    spectral_centroid=librosa.feature.spectral_centroid(data,sr=sr)
    list.append(numpy.mean(spectral_centroid))
    l2.append("spectral_centroid_mean")
    list.append(numpy.var(spectral_centroid))
    l2.append("spectral_centroid_var")
    spectral_bandwith=librosa.feature.spectral_bandwidth(data,sr=sr)
    list.append(numpy.mean(spectral_bandwith))
    l2.append("spectral_bandwidth_mean")
    list.append(numpy.var(spectral_bandwith))
    l2.append("spectral_bandwidth_var")
    spectral_roll_off=librosa.feature.spectral_rolloff(data,sr=sr)
    list.append(numpy.mean(spectral_roll_off))
    l2.append("rolloff_mean")
    list.append(numpy.var(spectral_roll_off))
    l2.append("rolloff_var")
    # Chirag  -------------
    list.append(numpy.mean(librosa.feature.zero_crossing_rate(data)))
    l2.append("zero_cross_rate_mean")

    list.append(numpy.var(librosa.feature.zero_crossing_rate(data)))
    l2.append("zero_cross_rate_var")
    y_harm, y_perc = librosa.effects.hpss(data)
    list.append(numpy.mean(y_harm))
    l2.append("harmonic_mean")

    list.append(numpy.var(y_harm))
    l2.append("harmonic_var")

    list.append(numpy.mean(y_perc))
    l2.append("perceptr_mean")

    list.append(numpy.var(y_perc))
    l2.append("perceptr_var")

    onset_env = librosa.onset.onset_strength(data, sr=sr)
    list.append(librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0])
    l2.append("tempo")
    mfccs=librosa.feature.mfcc(data,sr= sr)
    ctr = 1

    w,h = mfccs.shape
    for ii in range(w):
        temp = mfccs[ii]
        list.append(numpy.mean(temp))
        l2.append("mfcc" + str(ctr) + "_mean")
        list.append(numpy.var(temp))
        l2.append("mfcc" + str(ctr) + "_var")
        ctr = ctr + 1

    return











    stft=librosa.stft(data)
    stft_db = librosa.amplitude_to_db(abs(stft))
    print(stft_db)
    print(path,data)
def main():
  df = pd.read_csv("data.csv")
  name=['Reggae']
  fg = 0
  for n in name:
    fg=0


    Directory= Path(os.getcwd()+"/cut/"+n+"/")

    for dp in Directory.glob('*.wav'):
         list.clear()
         l2.clear()
         # cutter(dp, count)
         # count=count+1

         x=str(dp).split("\\")
         x=x[-1].split(".")


         list.append(x[0]+n+"."+x[-1])
         print(x[0]+n+"."+x[-1])
         print(fg)
         l2.append("name")
         Lib(dp)
         list.append(n)
         l2.append("Label")

         list3 = pd.DataFrame([list],columns=l2)

         df=df.append([list3],ignore_index=True)
         fg=fg+1


         if fg==1000:
            break
    print("Total=======================================================")
    print(n)
    print(fg)
  df.to_csv("data.csv")
if __name__ == "__main__":
    main()

