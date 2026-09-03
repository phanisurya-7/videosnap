from django.shortcuts import render, redirect
from .models import Post, PostImage


# Display all posts
def posts_view(request):
    if request.method == "POST":
        title_variable = request.POST.get("title")
        content_variable = request.POST.get("content")

        # Create the post
        post = Post.objects.create(
            title_column=title_variable,
            content_column=content_variable
        )

        # Get all uploaded images
        images = request.FILES.getlist("images")

        # Save each image
        for image in images:
            PostImage.objects.create(
                post=post,
                image=image
            )

        return redirect("posts")

    posts = Post.objects.all().order_by("-created_at")
    return render(request, "posts/posts.html", {"posts": posts})




# Create a new post
def create_post_view(request):

    if request.method == "POST":
        title_variable = request.POST.get("title")
        content_variable = request.POST.get("content")

        # Create the post
        post = Post.objects.create(
            title_column=title_variable,
            content_column=content_variable
        )

        # Get all uploaded images
        images = request.FILES.getlist("images")

        # Save each image
        for image in images:
            PostImage.objects.create(
                post=post,
                image=image
            )

        return redirect("posts")
    return render(request,"posts/posts.html")
        