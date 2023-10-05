from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
	{
		'author' : 'EunikeHP',
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'October 2, 2023'
	},
	{
		'author' : 'CoreyMS',
		'title' : 'Blog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'October 3, 2023'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})