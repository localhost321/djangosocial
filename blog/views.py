from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Like, Post,Comment
from .forms import ContactForm,NewCommentForm
# for testing
from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponseRedirect

from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect


from django.urls import reverse
from decouple import config

def index(request):
    return render(request,'blog/index.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

#ediiteed
@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	user = request.user
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.post = post
			data.username = user
			data.save()
			return redirect('post-detail', pk=pk)
	else:
		form = NewCommentForm()
	return render(request, 'blog/post_detail.html', {'post':post, 'form':form})



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # ediittted
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #eddittted
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False






def about(request):
    # context={}
    # context['form']=About()
    return render(request, 'blog/about.html')
       
# testing
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:

                send_mail(
                    subject,
                    message,
                    'email',
                    ['config.[EMAIL_HOST_USER]'],
                    fail_silently=False,
                )
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('blog-home')
      
    form = ContactForm()
    return render(request, "blog/contact.html", {'form':form})    


# ediitted
@login_required
def like(request):
	post_id = request.GET.get("likeId", "")
	user = request.user
	post = Post.objects.get(pk=post_id)
	liked= False
	like = Like.objects.filter(user=user, post=post)
	if like:
		like.delete()
	else:
		liked = True
		Like.objects.create(user=user, post=post)
	resp = {
        'liked':liked
    }
	response = JsonResponse.dumps(resp)
	return HttpResponse(response, content_type = "application/json")

# editted
# def LikeView(request,pk):
#     user = request.user
#     post=get_object_or_404(Post,id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))