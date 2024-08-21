from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def index(request):
    '''Pagina inicial'''
    return render(request, 'register/index.html')

@login_required
def topics(request):
    '''Todos os assuntos'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'register/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Um assunto e suas entradas'''
    topic = Topic.objects.get(id= topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'register/topic.html', context)

@login_required
def new_topic(request):
    '''Adiciona um novo assunto'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner =request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form':form}
    return render(request, 'register/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Cria uma anotação para um tópico'''
    topic =  Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    
    context = {'topic':topic, 'form': form}
    return render(request, 'register/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''Edita uma entrada'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'register/edit_entry.html', context)

@login_required
def delete_topic(request, topic_id):
    '''Remove um tópico'''
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return HttpResponseRedirect(reverse('topics'))
    
    context = {'topic': topic}
    return render(request, 'register/delete_topic.html', context)

@login_required
def delete_entry(request, entry_id):
    '''Remove uma entrada'''
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        entry.delete()
        return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic}
    return render(request, 'register/delete_entry.html', context)

def descubra(request):
    
    return render(request, 'register/descubra.html')

def chat_view(request):
    return render(request, 'chat/chat.html')