from django.contrib import admin


from .models import AddContact, Message

admin.site.register(AddContact)
admin.site.register(Message)