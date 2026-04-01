def notifications_count(request):
    if request.user.is_authenticated:
        count = request.user.notifications.filter(read=False).count()
        return {'unread_notifications': count}
    return {'unread_notifications': 0}