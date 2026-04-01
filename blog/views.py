from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from messaging.models import Notification

# FBVs simples
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# CBVs del blog
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'resumen', 'contenido', 'imagen']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'resumen', 'contenido', 'imagen']
    success_url = reverse_lazy('post_list')
    raise_exception = False

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

    def handle_no_permission(self):
        messages.error(self.request, 'No tenés permiso para editar este post.')
        return redirect('post_list')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    raise_exception = False

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

    def handle_no_permission(self):
        messages.error(self.request, 'No tenés permiso para borrar este post.')
        return redirect('post_list')

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        if post.autor != request.user:
            Notification.objects.create(
                user=post.autor,
                message=f"{request.user.username} le dio ❤️ a tu post '{post.titulo}'"
            )
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})