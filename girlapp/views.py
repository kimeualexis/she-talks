from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Issue, Comment
from .forms import CommentForm, IssueForm


class IssueListView(LoginRequiredMixin, ListView):
	model = Issue
	template_name = 'girlapp/index.html'
	context_object_name = 'issues'
	ordering = ['-created']
	paginate_by = 2


class UserIssueListView(ListView):
	model = Issue
	template_name = 'girlapp/user_questions.html'
	context_object_name = 'issues'
	paginate_by = 7

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Issue.objects.filter(author=user).order_by('-created')


class IssueDetailView(DetailView):
	model = Issue


class IssueCreateView(LoginRequiredMixin, CreateView):
	model = Issue
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Issue

	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		issue = self.get_object()
		if self.request.user == issue.user:
			return True
		return False


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Issue
	success_url = '/home'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def detail(request, issue_id):
	form = CommentForm(request.POST or None, request.FILES or None)
	issue = get_object_or_404(Issue, pk=issue_id)
	if form.is_valid():
		comm = form.save(commit=False)
		comm.user = request.user
		comm.issue = issue
		comm.save()
	form = CommentForm()
	return render(request, 'girlapp/issue_detail.html', {'form': form, 'issue': issue})


def delete(request, issue_id):
	issue = get_object_or_404(Issue, pk=issue_id)
	issue.delete()
	return redirect('quiz:quiz-index')


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment

	fields = ['comment']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.user:
			return True
		return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment

	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.user:
			return True
		return False


def index(request):
	return render(request, 'girlapp/home.html')
