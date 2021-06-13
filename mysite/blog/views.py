from django.http import HttpResponse
from blog.models import Post

def post_list(request):
  body = ""
  for post in Post.objects.all():
    body += post.title + "<br>"
  return HttpResponse(body)
