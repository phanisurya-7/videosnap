from django.contrib import admin
from .models import Profile, Projects, Education, Experience, Certifications, Contact, Achievements


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'user', 'city', 'state')
    search_fields = ('username', 'user__username', 'city')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certifications)
admin.site.register(Contact)
admin.site.register(Achievements)
