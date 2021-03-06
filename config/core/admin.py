from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from django.db.models import Count

from .forms import AreaAdminForm, VacancyAdminForm, ProfileAdminForm, MessageAdminForm, SearchQueryAdminForm
from .models import Vacancy, Area, Profile, Message, SearchQuery


class AreaListFilter(SimpleListFilter):
    title = 'Области'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return Area.objects.annotate(one=Count('vacancies')).filter(one__gt=0).values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset.all()
        else:
            return queryset.filter(area__id__exact=self.value())


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    form = VacancyAdminForm
    save_as = True
    save_on_top = True
    list_display = (
        'vacancy_id', 'area', 'status', 'name', 'employer_name', 'alternate_url', 'created_at', 'updated_at', 'salary'
    )
    list_filter = (
        'status', AreaListFilter, 'employer_name'
    )
    list_editable = ('status',)
    ordering = ('created_at',)
    search_fields = ('vacancy_id', 'name')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('area_id', 'in_search', 'parent_id', 'name',)
    list_editable = ('in_search',)
    search_fields = ('name',)
    form = AreaAdminForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('external_id', 'name',)
    search_fields = ('name',)
    form = ProfileAdminForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('profile', 'text', 'created_at',)
    search_fields = ('name',)
    form = MessageAdminForm


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('search_text', 'in_search')
    search_fields = ('search_text',)
    list_editable = ('in_search',)
    form = SearchQueryAdminForm
