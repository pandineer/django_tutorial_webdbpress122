from django.template.response import TemplateResponse
from blog.models import Post

def post_list(request):
  return TemplateResponse(
    request,
    "post_list.html",
    {"posts": Post.objects.all()}
  )
