from .models import Message

def unread_messages(request):
    if request.user.is_authenticated:
        # Count messages sent to the user that haven't been read yet
        count = Message.objects.filter(receiver=request.user, is_read=False).count()
        return {'unread_count': count}
    return {'unread_count': 0}