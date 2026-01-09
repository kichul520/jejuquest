from django.contrib import admin
from .models import PreRegistration, TeaserQuestLog, Quest


@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'region', 'age_group', 'privacy_agreed', 'marketing_agreed', 'referral_code', 'referred_by', 'created_at')
    search_fields = ('email', 'phone', 'referral_code')
    list_filter = ('region', 'age_group', 'privacy_agreed', 'marketing_agreed', 'created_at')
    readonly_fields = ('referral_code', 'created_at')


@admin.register(TeaserQuestLog)
class TeaserQuestLogAdmin(admin.ModelAdmin):
    list_display = ('quiz_name', 'user_answer', 'is_correct', 'created_at')
    list_filter = ('quiz_name', 'is_correct', 'created_at')


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_starter_pack', 'created_at')
    list_filter = ('is_starter_pack', 'created_at')
    search_fields = ('title', 'description')
