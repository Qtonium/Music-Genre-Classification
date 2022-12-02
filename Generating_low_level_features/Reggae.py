import os
from pydub import AudioSegment
from pathlib import Path
import yt_dlp as youtube_dl
def download_video():
    Reggae="https://www.youtube.com/watch?v=hzqFmXZ8tOE&list=PLp7pAH9am84O9Cd9VlW0W_qVVCL5PC3BI"
    ydl_opts = {
            'ignoreerrors': True,
            'playlistend': 300,
            'format': 'bestaudio/best',
            'outtmpl': 'C:/Users/bahuguns/PycharmProjects/pythonProject/Reggae/%(title)s.%(ext)s',

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',

            }],
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([Reggae])



def cuttera(name, count):

   # importing file from location by giving its path
   sound = AudioSegment.from_mp3(name)
   # Selecting Portion we want to cut
   StrtMin = 0
   StrtSec = 20
   EndMin = 0
   EndSec = 40
   # Time to milliseconds conversion
   StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
   EndTime = StrtMin * 60 * 1000 + EndSec * 1000
   # Opening file and extracting portion of it
   extract = sound[StrtTime:EndTime]
   # Saving file in required location
   extract.export("C:/Users/bahuguns/PycharmProjects/pythonProject/cut/Reggae/portiona"+str(count)+".wav", format="wav")
def cutterb(name, count):

   # importing file from location by giving its path
   sound = AudioSegment.from_mp3(name)
   # Selecting Portion we want to cut
   StrtMin = 0
   StrtSec = 40
   EndMin = 0
   EndSec = 60
   # Time to milliseconds conversion
   StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
   EndTime = StrtMin * 60 * 1000 + EndSec * 1000
   # Opening file and extracting portion of it
   extract = sound[StrtTime:EndTime]
   # Saving file in required location
   extract.export("C:/Users/bahuguns/PycharmProjects/pythonProject/cut/Reggae/portionb"+str(count)+".wav", format="wav")
def cutterc(name, count):

   # importing file from location by giving its path
   sound = AudioSegment.from_mp3(name)
   # Selecting Portion we want to cut
   StrtMin = 0
   StrtSec = 60
   EndMin = 0
   EndSec = 80
   # Time to milliseconds conversion
   StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
   EndTime = StrtMin * 60 * 1000 + EndSec * 1000
   # Opening file and extracting portion of it
   extract = sound[StrtTime:EndTime]
   # Saving file in required location
   extract.export("C:/Users/bahuguns/PycharmProjects/pythonProject/cut/Reggae/portionc"+str(count)+".wav", format="wav")
def cutterd(name, count):

   # importing file from location by giving its path
   sound = AudioSegment.from_mp3(name)
   # Selecting Portion we want to cut
   StrtMin = 0
   StrtSec = 80
   EndMin = 0
   EndSec = 100
   # Time to milliseconds conversion
   StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
   EndTime = StrtMin * 60 * 1000 + EndSec * 1000
   # Opening file and extracting portion of it
   extract = sound[StrtTime:EndTime]
   # Saving file in required location
   extract.export("C:/Users/bahuguns/PycharmProjects/pythonProject/cut/Reggae/portiond"+str(count)+".wav", format="wav")
def cuttere(name, count):

   # importing file from location by giving its path
   sound = AudioSegment.from_mp3(name)
   # Selecting Portion we want to cut
   StrtMin = 0
   StrtSec = 100
   EndMin = 0
   EndSec = 120
   # Time to milliseconds conversion
   StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000
   EndTime = StrtMin * 60 * 1000 + EndSec * 1000
   # Opening file and extracting portion of it
   extract = sound[StrtTime:EndTime]
   # Saving file in required location
   extract.export("C:/Users/bahuguns/PycharmProjects/pythonProject/cut/Reggae/portione"+str(count)+".wav", format="wav")
def main():
   download_video()
   Directory = Path(os.getcwd() + "/Reggae/")
   count=0
   for dp in Directory.glob('*.wav'):
      cuttera(dp,count)
      cutterb(dp, count)
      cutterc(dp, count)
      cutterd(dp, count)
      cuttere(dp, count)

      count=count+1;
      print(dp)
if __name__ == "__main__":
    main()
