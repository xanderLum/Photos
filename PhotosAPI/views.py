from django.http import Http404
from django.shortcuts import render
from django.views import generic
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Photo

from rest_framework import status
from .serializer import FileSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

#without using generic view
def index(request):
    all_photos = Photo.objects.all()
    context = {'all_photos' : all_photos}
    return render(request, 'PhotosAPI/index.html', context)

#without using generic view
def detail(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")
    return render(request, 'PhotosAPI/detail.html', {'object': photo})

#w/ generic view
class IndexView(generic.ListView):
    template_name = 'PhotosAPI/index.html'
    context_object_name = "all_photos"

    def get_queryset(self):
        return Photo.objects.all()

#w/ generic view
class DetailView(generic.DetailView):
    template_name = 'PhotosAPI/detail.html'
    model = Photo

#w/ generic view
#status { D = Draft, P = Post}
class PostPhotoView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#w/ generic view
class ListPhotoView(generic.ListView):
    template_name = 'PhotosAPI/index.html'
    context_object_name = "all_photos"

    def get_queryset(self):
        return Photo.objects.all()