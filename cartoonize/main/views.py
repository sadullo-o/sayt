from threading import Timer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from guest_user.decorators import allow_guest_user
from .forms import RasmForm
from .models import Video, Cartoon
import cv2
import numpy as np

from threading import Thread
# Create your views here.

def cartoonize(video_url, username):
    cap = cv2.VideoCapture(video_url)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'media/{username}.avi', fourcc, 20.0, size)


    def color_quantization(img, k):
    # Transform the image
      data = np.float32(img).reshape((-1, 3))

    # Determine criteria
      criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
      ret, label, center = cv2.kmeans(data, k, None, criteria, -1000, cv2.KMEANS_RANDOM_CENTERS)
      center = np.uint8(center)
      result = center[label.flatten()]
      result = result.reshape(img.shape)
      return result


    while cap.isOpened():
        try:
            _, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 200, cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY, 15, 11)

                # Cartoonization

            total_color = 5
            img = color_quantization(frame, total_color)

            color = cv2.bilateralFilter(img, d=1, sigmaColor=200,sigmaSpace=200)
            cartoon = cv2.bitwise_and(color, color, mask=edges)

            cv2.imshow('Recording...', cartoon)

            out.write(cartoon)
        except:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    print('OK')
    cap.release()
    out.release()
    cv2.destroyAllWindows()




@allow_guest_user
def home(request):
    user = request.user.username
    if request.method == "POST":
        form = RasmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
        else:
            print(form)

    return render(request, 'main/index.html', {'user': user})


@allow_guest_user
def result(request):
    user = request.user.username

    video = Video.objects.all().filter(username=user).last()
    video_url = 'http://127.0.0.1:8000' + video.file.url
    result_url = 'http://127.0.0.1:8000/media/' + user + '.avi'
    if request.method == "POST":
        cartoonize(video_url, user)
        return redirect(result_url)
        # result_url = 'http://127.0.0.1:8000/media/' + user + '.avi'
        # car = Cartoon(username=user, file=result_url)
        # car.save()

        # print(video.file.url)
        # print(video_url)


    return render(request, 'main/result.html', {'user': result_url, 'video': video})









