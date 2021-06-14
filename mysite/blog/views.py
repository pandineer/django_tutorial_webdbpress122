from django.http import HttpResponse
from django.template.loader import render_to_string
from blog.models import Post

def post_list(request):
  body = render_to_string(
    "post_list.html",
    {"posts": Post.objects.all()}
  )

  return HttpResponse(body)
