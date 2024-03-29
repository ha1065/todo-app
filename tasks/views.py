from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.utils import timezone
from .forms import TaskCreateForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    latest_task_list = Task.objects.for_user(request.user)
    context = {
        'latest_task_list' : latest_task_list
    }
    return render(request, 'tasks/index.html', context)

class TaskCreateView(LoginRequiredMixin, CreateView):

    # another implementation

    # model = Task
    # template_name = 'tasks/task-create.html'
    # fields = ['name', 'description', 'pub_date', 'due_date']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        context = {'form': TaskCreateForm()}
        return render(request, 'tasks/task-create.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return HttpResponseRedirect(reverse_lazy('tasks:index'))
        return render(request, 'tasks/task-create.html', {'form': form})

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    # Alternative way to show detail only for tasks that have been published.
    
    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)

    #     now = timezone.now()
    #     ctx['now'] = now
    #     ctx['today'] = timezone.localtime(now).date()

    #     return ctx

    # def get_queryset(self):
    #     """"
    #     Excludes any questions that aren't published yet
    #     """
    #     return Task.objects.filter(pub_date__lte=timezone.now())

class TaskDeleteView(LoginRequiredMixin, DeleteView):

    model = Task
    template_name = 'tasks/delete.html'
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model=Task
    fields=['name','description','pub_date','due_date' ]
    template_name='tasks/task-edit.html'
   
    

