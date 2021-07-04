from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings

from PIL import Image
import numpy as np
import os, cv2
from uuid import uuid4

from .admin import FaceApi


def home_view(request):
    return render(request, 'faceapi/home.html', {})


def plot_boxes(I, resp):
    for re in resp:
        x1, y1, w, h = re['box']
        cv2.rectangle(I, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)
    return I


def detect_view(request):
    if request.method == "POST":
        json_response = {}
        f = request.FILES['img']
        pth, f_name = save_file(f)
        I = np.asarray(Image.open(str(pth)))
        resp = FaceApi.detector.detect_faces(I)
        I = plot_boxes(I, resp)
        I = Image.fromarray(I)
        I.save(settings.BASE_DIR / "static/imgs/{}".format(f_name))
        json_response['n_faces'] = len(resp)
        json_response['data'] = resp
        json_response['resp_imgurl'] = "/static/imgs/{}".format(f_name)
        return JsonResponse(json_response, status=200)
    else:
        return HttpResponse("<h5 style='color: red;'>Bad request type for this URL.</h5>", status=400)


def save_file(file):
    f_name = str(uuid4()) + os.path.splitext(file.name)[1]
    path = settings.MEDIA_ROOT / f_name
    with open(path, "wb") as f:
        f.write(file.read())
    return path, f_name

