#coding:utf-8

from django.contrib import admin
from polls.models import Poll,Choice


class ChoiceAdmin(admin.StackedInline):
    model=Choice
    extra=3


#admin.site.register(Poll)#将Poll函数注册到管理界面
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]#"collapse" 样式类用于显示初始时是收缩的 fieldset cf

    inlines = [ChoiceAdmin]#Choice 对象在 Poll 管理页面中被编辑。 默认情况下，提供 3 个 choices 的字段空间。



admin.site.register(Poll, PollAdmin)