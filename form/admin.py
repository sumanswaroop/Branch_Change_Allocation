from django.contrib import admin

# Register your models here.
from form.models import userpost,program

class userpostAdmin(admin.ModelAdmin):
	class Meta:
		model = userpost

class programAdmin(admin.ModelAdmin):
	class Meta:
		model=program

admin.site.register(program,programAdmin)
admin.site.register(userpost, userpostAdmin)
