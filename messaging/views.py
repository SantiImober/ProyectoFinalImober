from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .models import Message, Notification

@login_required
def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user)
    messages_sent = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/inbox.html', {
        'messages_received': messages_received,
        'messages_sent': messages_sent,
    })

@login_required
def send_message(request):
    users = User.objects.exclude(id=request.user.id)
    receiver_id = request.GET.get('receiver')
    if request.method == 'POST':
        receiver_id = request.POST['receiver']
        content = request.POST['content']
        receiver = get_object_or_404(User, id=receiver_id)
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        Notification.objects.create(
            user=receiver,
            message=f"{request.user.username} te envió un mensaje"
        )
        return redirect('inbox')
    return render(request, 'messaging/message_form.html', {
        'users': users,
        'receiver_id': receiver_id,
    })

@login_required
def notifications(request):
    notifs = Notification.objects.filter(user=request.user)
    notifs.update(read=True)
    return render(request, 'messaging/notifications.html', {'notifs': notifs})