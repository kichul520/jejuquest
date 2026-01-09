import uuid
from django.db import models


class PreRegistration(models.Model):
    """사전 예약자 모델"""
    email = models.EmailField(unique=True, verbose_name='이메일')
    referral_code = models.CharField(
        max_length=8,
        unique=True,
        verbose_name='추천 코드'
    )
    referred_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='referrals',
        verbose_name='추천인'
    )
    
    # 추가 개인정보 필드 (선택)
    phone = models.CharField(max_length=20, blank=True, verbose_name='전화번호')
    region = models.CharField(max_length=20, blank=True, verbose_name='거주 지역')
    age_group = models.CharField(max_length=10, blank=True, verbose_name='연령대')
    
    # 동의 필드
    privacy_agreed = models.BooleanField(default=False, verbose_name='개인정보 수집 동의')
    marketing_agreed = models.BooleanField(default=False, verbose_name='마케팅 수신 동의')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일시')

    class Meta:
        verbose_name = '사전 예약'
        verbose_name_plural = '사전 예약 목록'

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class TeaserQuestLog(models.Model):
    """티저 퀴즈 기록 모델"""
    quiz_name = models.CharField(max_length=100, verbose_name='퀴즈명')
    user_answer = models.CharField(max_length=200, verbose_name='사용자 답변')
    is_correct = models.BooleanField(verbose_name='정답 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='참여일시')

    class Meta:
        verbose_name = '퀴즈 기록'
        verbose_name_plural = '퀴즈 기록 목록'


    def __str__(self):
        return f"{self.quiz_name} - {'정답' if self.is_correct else '오답'}"


class Quest(models.Model):
    """퀘스트 모델"""
    title = models.CharField(max_length=100, verbose_name='퀘스트명')
    description = models.TextField(verbose_name='설명')
    icon = models.CharField(max_length=50, verbose_name='아이콘', help_text='이모지 또는 아이콘 클래스')
    is_starter_pack = models.BooleanField(default=False, verbose_name='스타터팩 포함 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')

    class Meta:
        verbose_name = '퀘스트'
        verbose_name_plural = '퀘스트 목록'

    def __str__(self):
        return self.title
