from pytube import YouTube
from sys import argv 

link = argv[1]#giving access to the first agrument of the program line, in this case it is the link
yt = YouTube(link)#create a YouTube object from the link

print("Title:", yt.title)#getting title 

print("View:", yt.views)#getting the views

yd = yt.streams.get_highest_resolution()#downloads the highest resolution of the video

yd.download()#put the folder location inside the brackets, downloads video to the folder