from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts is our query set
    #getting all Post models with publish date, and sorting them by date.
    #We can also reverse the ordering by adding - at the beginning:
    return render(request, 'blog/post_list.html', {'posts':posts}) # function
    #takes request and fill return the value produced by render (will put together template blog/post_list.html)
    # {'posts':posts} allows to send it as the answer to users request
