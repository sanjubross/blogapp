from django.contrib import messages
from django.core.files.base import File
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

# Create your views here.


class BlogIndex(View):

    def get(self, request):
        form = BlogForm()
        comment = CommentForm()
        blogs = Blog.objects.all()
        comments = Comment.objects.all()

        context = {
            'blogs':blogs,
            'form':form,
            'comment':comment,
            'comments':comments
        }

        return render(request, "index.html", context)

    def post(self, request):


        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratualtion! Your Post has been added.")
            return redirect("/")

        comment = CommentForm(request.POST)

        if comment.is_valid():
            comment.save()
            messages.success(request, "Congratualtion! Your comment has been added.")
            return redirect("/")

class BlogView(View):

    def get(self, request, id):
        try:
            blcn = Blog.objects.get(id=id)
            return render(request, "blogview.html", {'blcn':blcn})
        except Blog.DoesNotExist:
            return render(request, "blogview.html", {'error': 'No data found.'})