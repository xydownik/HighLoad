from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


# Create your views here.
def hello_blog(request):
    return HttpResponse("Hello, Blog!")

@api_view(['GET', 'POST'])
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        serializer = PostSerializer(post)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'City deleted successfully'}, status=204)
def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Associate the post with the logged-in user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/delete_post.html', {'post': post})
