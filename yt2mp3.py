#import
from pytube import YouTube
import os

#storage destination
destination = str(input("enter storage path (or none for cwd) \n>>"))

#loop for multiple videos
while True:    
    #url input
    url = str(input("enter video url (q to exit) \n>>"))
    if url == 'q':
        quit()
    url = YouTube(url)

    mins = int(url.length / 60)
    secs = int(url.length % 60)

    #print vid stats
    print("\ntitle: " + url.title + "\n\nlength: " + str(mins) + ':' + str(secs)
          + "\n\ndescription: " + url.description + "\n\nviews: " + str(url.views))

    #save only audio
    audio = url.streams.filter(only_audio=True).first()

    #download and save
    outFile = audio.download(output_path=destination)
    base, ext = os.path.splitext(outFile)
    newFile = base + '.mp3'
    os.rename(outFile, newFile)

    #print result
    print("\n" + url.title + " downloaded.\n")
