from pytube import YouTube
import os
yt=YouTube(input("donner l'adresse url "))
ad=yt.streams.filter(only_audio=True).first()
destination=r"C:\Users\Arij\Desktop"
telecharg=ad.download(output_path=destination)
base, ext = os.path.splitext(telecharg)
file=base+'.mp3'
os.rename(telecharg,file)
print(yt.title+"a été téléchargé")