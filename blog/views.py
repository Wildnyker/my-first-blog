from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {}) # function
#takes request and fill return the value produced by render (will put together template blog/post_list.html)
