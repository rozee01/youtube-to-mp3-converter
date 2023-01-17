import PySimpleGUI as sg
from pytube import YouTube
import os
def fn(ch):
    yt=YouTube(ch)
    ad=yt.streams.filter(only_audio=True).first()
    destination=r"C:\Users\Arij\Desktop"
    telecharg=ad.download(output_path=destination)
    base, ext = os.path.splitext(telecharg)
    file=base+'.mp3'
    os.rename(telecharg,file)
layout=[[sg.Text("Enter the link you want to convert to mp3")],
[sg.InputText(key="link")],
[sg.Button("convert",key="convert", button_color="#311432")]]
window=sg.Window("Youtube to MP3 Convertor", layout, margins=(216,131), background_color='#E6E6FA')
while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED:
        break
    if event=="convert":
        ch=values["link"]
        fn(ch)
        break
window.close()
