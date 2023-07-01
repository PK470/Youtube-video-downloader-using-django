from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from pytube import YouTube
import os
from django.shortcuts import redirect
from django.urls import reverse

from django.shortcuts import get_object_or_404

# Create your views here.





def yt_down(request):
    return render(request,'yt.html')

def wrong(request):
    return render(request,'wrong.html')

def aboutus(request):
    return render(request,'aboutus.html')

def yt_download(request):
    message = "Please Enter Valid Url"
    global url 
    url = request.GET.get('url')
    print('url:-',url)
    url1 = url
    
    if url1 is not None and len(url1) == 0 :
        return render(request,'yt.html',{'msg':message})
    if url1 is not None and "https://www.youtube.com/" not in url1:
        message = "Invalid Url"
        return render(request,'yt.html',{'msg':message})
        
    yt = YouTube(url)
    resolution= []
    rsl = yt.streams.all()
    for i in rsl:
        resolution.append(i.resolution)
    resolution = list(dict.fromkeys(resolution))
    elink = url.replace("watch?v=","embed/")
    return render(request,'yt1.html',{'rsl': resolution,'embd': elink})

def dw(request):
    path ="C:/Users/91844/OneDrive/Desktop/myapp/ytdownload/video/"
    rsl = request.GET.get('u')
    print("quality : ",rsl )
    try:
        yt = YouTube(url)
        filename = yt.streams.first().default_filename
        #ctime = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')+".mp4"
        
        filename = os.path.splitext(filename)[0]
        filename = filename + ".mp4"
        stream = yt.streams.get_by_resolution(rsl)
        stream.download(path)
        
        #os.rename(original_filepath, new_filepath)

        
        #file = open(file_path, 'rb')

        # Create the FileResponse object
        

        with open(os.path.join(path,filename), 'rb') as f:
            data = f.read()   


        
            ##download file by response      
        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return response
    except:
        message ="Something wents wrong , try again..!"
        #return HttpResponseRedirect('home',{'msg':message})
        #return redirect(reverse('home'))
        return render(request,'wrong.html')