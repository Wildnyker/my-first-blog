from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm # to add froms to view
from django.shortcuts import redirect # allows to redirect user from one page to other

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts is our query set
    #getting all Post models with publish date, and sorting them by date.
    #We can also reverse the ordering by adding - at the beginning:
    return render(request, 'blog/post_list.html', {'posts':posts}) # function
    #takes request and fill return the value produced by render (will put together template blog/post_list.html)
    # {'posts':posts} allows to send it as the answer to users request

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # will get a page with id of this page
    #which is geiven to object automaticly, or 404 error page
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)# wont commit ir before save method() as we
            # will provide author.
            post.author = request.user # the author will be a logged user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # from django.shortcuts import redirect
            # will redirect us to the detailed view of this page
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # gets in an instance of the previously filled model
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


