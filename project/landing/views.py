import random
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.conf import settings
from .models import PreRegistration, TeaserQuestLog

# 10개의 제주 관찰형 퀴즈
QUIZZES = [
    {
        'id': 'dolhareubang_hands',
        'question': '🗿 돌하르방의 손 위치에 담긴 의미는?',
        'description': '제주도의 수호신 돌하르방! 손의 위치에 따라 다른 의미를 가지고 있습니다. 왼손이 위에 있는 돌하르방은 어떤 의미일까요?',
        'hint': '조선시대 관리들의 복장을 떠올려보세요! 🤔',
        'options': [
            {'value': '문관', 'label': '📚 문관 (文官) - 학문과 지혜를 상징'},
            {'value': '무관', 'label': '⚔️ 무관 (武官) - 무예와 힘을 상징'},
            {'value': '풍요', 'label': '🌾 풍요 - 농사의 풍년을 기원'},
            {'value': '수호', 'label': '🛡️ 수호 - 마을을 지키는 수문장'},
        ],
        'answer': '문관',
        'explanation': '왼손이 위에 있는 돌하르방은 문관을 나타냅니다. 오른손이 위에 있으면 무관이에요. 손의 위치로 신분을 구별했답니다!'
    },
    {
        'id': 'jeju_black_pig',
        'question': '🐷 제주 흑돼지의 특징은?',
        'description': '제주 흑돼지는 일반 돼지와 다른 특별한 특징이 있어요. 진짜 제주 흑돼지를 구별하는 방법은?',
        'hint': '털 색깔만으로는 부족해요! 🐽',
        'options': [
            {'value': '털색', 'label': '🖤 털이 검은색이다'},
            {'value': '코끝', 'label': '👃 코끝까지 검은색이다'},
            {'value': '크기', 'label': '📏 일반 돼지보다 작다'},
            {'value': '꼬리', 'label': '🌀 꼬리가 곱슬곱슬하다'},
        ],
        'answer': '코끝',
        'explanation': '진짜 제주 흑돼지는 코끝(주둥이)까지 검은색이에요! 털만 검은 돼지는 그냥 검은 돼지랍니다.'
    },
    {
        'id': 'haenyeo_suit',
        'question': '🤿 해녀의 물질 복장 색깔은?',
        'description': '제주 해녀들이 바다에서 물질할 때 입는 잠수복의 전통적인 색깔은 무엇일까요?',
        'hint': '바다에서 눈에 잘 띄어야 해요! 🌊',
        'options': [
            {'value': '검정', 'label': '⬛ 검정색'},
            {'value': '주황', 'label': '🟧 주황색'},
            {'value': '파랑', 'label': '🟦 파란색'},
            {'value': '흰색', 'label': '⬜ 흰색'},
        ],
        'answer': '검정',
        'explanation': '해녀들의 잠수복은 전통적으로 검정색이에요. 하지만 테왁(부력 도구)은 주황색으로 바다에서 위치를 알 수 있게 해줍니다!'
    },
    {
        'id': 'jeju_wind',
        'question': '💨 제주의 삼다(三多) 중 하나인 "바람"의 방향은?',
        'description': '제주도는 바람이 많기로 유명해요. 겨울철 제주에 부는 대표적인 바람의 방향은?',
        'hint': '시베리아에서 불어오는 바람이에요! ❄️',
        'options': [
            {'value': '북서풍', 'label': '🧭 북서풍'},
            {'value': '남동풍', 'label': '🧭 남동풍'},
            {'value': '동풍', 'label': '🧭 동풍'},
            {'value': '남풍', 'label': '🧭 남풍'},
        ],
        'answer': '북서풍',
        'explanation': '겨울철 제주에는 시베리아에서 불어오는 차가운 북서풍이 불어요. 이 바람을 "하늬바람"이라고도 부릅니다!'
    },
    {
        'id': 'hallasan_lake',
        'question': '🏔️ 한라산 정상의 호수 이름은?',
        'description': '한라산 정상에는 아름다운 화구호가 있어요. 이 호수의 이름은 무엇일까요?',
        'hint': '흰 사슴이 물을 마시던 곳이라는 전설이 있어요! 🦌',
        'options': [
            {'value': '백록담', 'label': '🦌 백록담'},
            {'value': '천지연', 'label': '💧 천지연'},
            {'value': '정방폭포', 'label': '🌊 정방폭포'},
            {'value': '산굼부리', 'label': '🕳️ 산굼부리'},
        ],
        'answer': '백록담',
        'explanation': '한라산 정상의 호수는 백록담이에요. "흰 사슴이 물을 마시는 연못"이라는 뜻으로, 신선이 흰 사슴을 타고 내려와 물을 마셨다는 전설이 있어요!'
    },
    {
        'id': 'jeju_stone_wall',
        'question': '🪨 제주 돌담의 특징은?',
        'description': '제주도 곳곳에서 볼 수 있는 검은 돌담! 이 돌담의 독특한 특징은 무엇일까요?',
        'hint': '제주의 강한 바람과 관련이 있어요! 💨',
        'options': [
            {'value': '구멍', 'label': '🕳️ 구멍이 숭숭 뚫려있다'},
            {'value': '높이', 'label': '📏 2m 이상으로 높다'},
            {'value': '시멘트', 'label': '🧱 시멘트로 붙여져 있다'},
            {'value': '색깔', 'label': '🎨 여러 색 돌이 섞여있다'},
        ],
        'answer': '구멍',
        'explanation': '제주 돌담은 구멍이 숭숭 뚫려있어요! 이건 일부러 그렇게 쌓은 거예요. 바람이 통과하게 해서 강풍에도 무너지지 않게 한 선조들의 지혜랍니다!'
    },
    {
        'id': 'jeju_horse',
        'question': '🐴 제주 조랑말의 특징은?',
        'description': '제주 조랑말은 천연기념물로 지정된 토종말이에요. 가장 큰 특징은?',
        'hint': '제주의 환경에 적응한 결과예요! 🏝️',
        'options': [
            {'value': '작은키', 'label': '📐 키가 작다 (120cm 내외)'},
            {'value': '긴다리', 'label': '🦵 다리가 길다'},
            {'value': '흰색', 'label': '🤍 털이 흰색이다'},
            {'value': '빠름', 'label': '💨 매우 빠르다'},
        ],
        'answer': '작은키',
        'explanation': '제주 조랑말은 키가 120cm 내외로 작아요! 제주의 거친 환경에서 작은 체구가 유리했기 때문이에요. 작지만 강인한 생명력을 가졌답니다!'
    },
    {
        'id': 'jeju_citrus',
        'question': '🍊 제주 감귤의 원래 이름은?',
        'description': '제주하면 떠오르는 감귤! 제주에서 가장 오래된 전통 감귤 품종의 이름은?',
        'hint': '조선시대 임금님께 진상했던 귀한 과일이에요! 👑',
        'options': [
            {'value': '진귤', 'label': '🏛️ 진귤 (진상귤)'},
            {'value': '한라봉', 'label': '🏔️ 한라봉'},
            {'value': '천혜향', 'label': '🌸 천혜향'},
            {'value': '레드향', 'label': '❤️ 레드향'},
        ],
        'answer': '진귤',
        'explanation': '진귤은 조선시대부터 임금님께 진상하던 제주 토종 감귤이에요. 한라봉, 천혜향은 현대에 개발된 품종이랍니다!'
    },
    {
        'id': 'jeju_gate',
        'question': '🚪 제주 전통가옥 대문의 이름은?',
        'description': '제주 전통가옥에는 특이한 대문이 있어요. 나무 막대기 3개로 된 이 대문의 이름은?',
        'hint': '집주인이 어디 있는지 알려주는 역할을 해요! 📍',
        'options': [
            {'value': '정낭', 'label': '🪵 정낭'},
            {'value': '솟대', 'label': '🪶 솟대'},
            {'value': '장승', 'label': '🗿 장승'},
            {'value': '서낭당', 'label': '⛩️ 서낭당'},
        ],
        'answer': '정낭',
        'explanation': '정낭은 제주 전통 대문이에요! 나무 막대기의 개수로 주인의 외출 상태를 알려줬어요. 3개 다 걸려있으면 "멀리 갔다", 없으면 "집에 있다"는 뜻이에요!'
    },
    {
        'id': 'jeju_olle',
        'question': '🚶 제주 올레길의 "올레" 뜻은?',
        'description': '제주 올레길은 유명한 트레킹 코스예요. "올레"는 제주 방언으로 무슨 뜻일까요?',
        'hint': '집과 관련된 단어예요! 🏠',
        'options': [
            {'value': '골목', 'label': '🏘️ 집으로 가는 좁은 골목'},
            {'value': '바다', 'label': '🌊 바닷가 길'},
            {'value': '오름', 'label': '⛰️ 오름으로 가는 길'},
            {'value': '걷다', 'label': '👣 천천히 걷다'},
        ],
        'answer': '골목',
        'explanation': '"올레"는 제주 방언으로 "집 대문에서 마을길까지 이어지는 좁은 골목"을 뜻해요. 집으로 들어가는 정겨운 길이라는 의미가 담겨있답니다!'
    },
    {
        'id': 'jeju_basalt',
        'question': '🪨 제주 현무암에 구멍이 많은 이유는?',
        'description': '제주도 곳곳에서 볼 수 있는 검은 현무암! 이 돌에 구멍이 숭숭 뚫려있는 이유는 무엇일까요?',
        'hint': '화산 폭발과 관련이 있어요! 🌋',
        'options': [
            {'value': '가스', 'label': '💨 용암 속 가스가 빠져나간 자리'},
            {'value': '바람', 'label': '🌀 강한 바람에 깎여서'},
            {'value': '파도', 'label': '🌊 파도에 침식되어서'},
            {'value': '벌레', 'label': '🐛 벌레가 파먹어서'},
        ],
        'answer': '가스',
        'explanation': '현무암의 구멍은 뜨거운 용암이 식을 때 가스가 빠져나간 자리예요! 이런 구멍 덕분에 제주 돌담이 바람을 통과시켜 무너지지 않는 거랍니다.'
    },
    {
        'id': 'jeju_yongduam',
        'question': '🐉 용두암 전설 속 용은 무엇을 훔쳤나요?',
        'description': '제주 용두암에는 용이 돌로 변한 전설이 있어요. 이 용이 하늘에서 훔친 것은?',
        'hint': '용궁의 보물이에요! 💎',
        'options': [
            {'value': '구슬', 'label': '🔮 한라산 신령의 구슬'},
            {'value': '금', 'label': '🥇 황금 덩어리'},
            {'value': '공주', 'label': '👸 용왕의 공주'},
            {'value': '검', 'label': '⚔️ 신비한 보검'},
        ],
        'answer': '구슬',
        'explanation': '전설에 따르면 용이 한라산 신령의 구슬을 훔쳐 달아나다가 신령의 화살에 맞아 돌로 변했대요. 그래서 바다를 향해 고개를 든 용의 모습이 되었답니다!'
    },
    {
        'id': 'hallasan_height',
        'question': '🏔️ 한라산의 높이는 얼마일까요?',
        'description': '한라산은 남한에서 가장 높은 산이에요. 정확한 높이는?',
        'hint': '숫자가 연속으로 이어져요! 📏',
        'options': [
            {'value': '1950', 'label': '📐 1,950m'},
            {'value': '1947', 'label': '📐 1,947m'},
            {'value': '2000', 'label': '📐 2,000m'},
            {'value': '1850', 'label': '📐 1,850m'},
        ],
        'answer': '1947',
        'explanation': '한라산의 높이는 1,947m로, 남한에서 가장 높은 산이에요! 1, 9, 4, 7... 숫자가 연속으로 이어지는 것이 특징이랍니다.'
    },
    {
        'id': 'jeju_sammu',
        'question': '🚫 제주도 "삼무도(三無島)"에서 없는 것이 아닌 것은?',
        'description': '제주도는 예로부터 세 가지가 없는 섬이라고 불렸어요. 다음 중 삼무에 포함되지 않는 것은?',
        'hint': '도둑, 거지, 그리고... 🤔',
        'options': [
            {'value': '뱀', 'label': '🐍 뱀'},
            {'value': '대문', 'label': '🚪 대문'},
            {'value': '도둑', 'label': '🦹 도둑'},
            {'value': '거지', 'label': '🙏 거지'},
        ],
        'answer': '뱀',
        'explanation': '삼무도는 도둑, 거지, 대문이 없다는 뜻이에요! 서로 돕고 사는 제주 사람들의 정을 보여주는 말이죠. 뱀은 삼무에 포함되지 않아요.'
    },
    {
        'id': 'seongsan_ilchulbong',
        'question': '🌅 성산일출봉이 유네스코에 등재된 이유는?',
        'description': '성산일출봉은 유네스코 세계자연유산이에요. 특별한 이유는 무엇일까요?',
        'hint': '화산 지형과 관련있어요! 🌋',
        'options': [
            {'value': '수성화산', 'label': '🌊 세계적으로 희귀한 수성화산'},
            {'value': '높이', 'label': '📏 엄청난 높이'},
            {'value': '일출', 'label': '☀️ 아름다운 일출'},
            {'value': '해녀', 'label': '🤿 해녀 문화'},
        ],
        'answer': '수성화산',
        'explanation': '성산일출봉은 바닷속에서 화산이 폭발해 만들어진 수성화산이에요! 분화구가 원형 그대로 보존된 세계적으로 희귀한 지형이랍니다.'
    },
    {
        'id': 'jeju_gotjawal',
        'question': '🌲 제주 곶자왈의 특별한 점은?',
        'description': '곶자왈은 제주에만 있는 독특한 숲이에요. 이 숲의 특별한 기능은?',
        'hint': '제주의 생명수와 관련있어요! 💧',
        'options': [
            {'value': '지하수', 'label': '💧 빗물을 지하수로 저장'},
            {'value': '약초', 'label': '🌿 희귀 약초가 자람'},
            {'value': '새', 'label': '🐦 철새 도래지'},
            {'value': '온천', 'label': '♨️ 온천수가 솟음'},
        ],
        'answer': '지하수',
        'explanation': '곶자왈은 빗물을 걸러 지하수로 저장하는 "제주의 허파"예요! 제주 식수의 대부분이 이 곶자왈 덕분에 만들어진답니다.'
    },
    {
        'id': 'jeju_camellia',
        'question': '🌺 제주 동백꽃이 특별한 이유는?',
        'description': '제주도는 동백꽃으로 유명해요. 제주 동백꽃의 특징은 무엇일까요?',
        'hint': '꽃이 지는 방식이 달라요! 🌸',
        'options': [
            {'value': '통째로', 'label': '🔴 꽃이 통째로 떨어짐'},
            {'value': '향기', 'label': '👃 향기가 매우 강함'},
            {'value': '크기', 'label': '📏 다른 지역보다 큼'},
            {'value': '색깔', 'label': '🎨 여러 색이 섞임'},
        ],
        'answer': '통째로',
        'explanation': '동백꽃은 꽃잎이 하나씩 지지 않고 통째로 뚝 떨어져요! 그래서 "머리가 떨어진다"고 해서 무사들이 꺼렸다는 이야기도 있답니다.'
    },
    {
        'id': 'haenyeo_signal',
        'question': '🤿 해녀가 물 위로 올라올 때 내는 소리는?',
        'description': '제주 해녀들은 물질 후 특유의 소리를 내요. 이 소리의 이름은?',
        'hint': '숨을 내쉬며 내는 휘파람 같은 소리예요! 🎵',
        'options': [
            {'value': '숨비소리', 'label': '🎵 숨비소리'},
            {'value': '바람소리', 'label': '💨 바람소리'},
            {'value': '파도소리', 'label': '🌊 파도소리'},
            {'value': '호루라기', 'label': '📯 호루라기소리'},
        ],
        'answer': '숨비소리',
        'explanation': '"숨비소리"는 해녀가 깊은 바다에서 올라와 숨을 내쉴 때 나는 "호오이~" 소리예요! 유네스코 인류무형문화유산으로 등재된 소중한 문화랍니다.'
    },
    {
        'id': 'jeju_tamna',
        'question': '👑 제주도의 옛 이름 "탐라"의 뜻은?',
        'description': '제주도는 옛날에 탐라국이라는 독립된 나라였어요. "탐라"의 뜻은?',
        'hint': '섬의 특징을 담은 이름이에요! 🏝️',
        'options': [
            {'value': '섬나라', 'label': '🏝️ 섬나라 (바다를 건넌 나라)'},
            {'value': '신선', 'label': '🧙 신선이 사는 곳'},
            {'value': '감귤', 'label': '🍊 감귤의 나라'},
            {'value': '바람', 'label': '💨 바람의 나라'},
        ],
        'answer': '섬나라',
        'explanation': '"탐라(耽羅)"는 "바다를 건너야 하는 섬나라"라는 뜻이에요! 고려 시대까지 약 1,000년간 독립된 왕국이었답니다.'
    },
    {
        'id': 'jeju_udo',
        'question': '🐄 우도(牛島)는 왜 "소섬"이라고 불릴까요?',
        'description': '제주 동쪽에 있는 우도는 "소섬"이라는 뜻이에요. 그 이유는?',
        'hint': '섬의 모양을 잘 살펴보세요! 👀',
        'options': [
            {'value': '모양', 'label': '🐄 섬 모양이 소가 누운 형상'},
            {'value': '방목', 'label': '🌾 소를 방목했던 섬'},
            {'value': '전설', 'label': '📖 소가 변한 전설'},
            {'value': '풀', 'label': '🌿 소가 좋아하는 풀이 많음'},
        ],
        'answer': '모양',
        'explanation': '우도는 하늘에서 보면 소가 누워있는 모양이에요! 머리, 뿔, 등, 꼬리까지 소의 형상을 닮아서 "소섬"이라고 불린답니다.'
    },
]


def index(request: HttpRequest):
    """메인 랜딩 페이지"""
    return render(request, 'landing/index.html')


def quiz(request: HttpRequest):
    """티저 퀴즈 페이지"""
    # 특정 퀴즈 선택 또는 랜덤
    quiz_id = request.GET.get('q', None)

    if quiz_id:
        quiz_data = next((q for q in QUIZZES if q['id'] == quiz_id), None)

    if not quiz_id or not quiz_data:
        quiz_data = random.choice(QUIZZES)

    return render(request, 'landing/quiz.html', {
        'quiz': quiz_data,
        'total_quizzes': len(QUIZZES)
    })


def quiz_result(request: HttpRequest):
    """퀴즈 결과 페이지"""
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id', '')
        answer = request.POST.get('answer', '')

        # 퀴즈 찾기
        quiz_data = next((q for q in QUIZZES if q['id'] == quiz_id), None)

        if quiz_data:
            is_correct = answer == quiz_data['answer']

            # 퀴즈 기록 저장
            TeaserQuestLog.objects.create(
                quiz_name=quiz_id,
                user_answer=answer,
                is_correct=is_correct
            )

            return render(request, 'landing/quiz_result.html', {
                'is_correct': is_correct,
                'user_answer': answer,
                'quiz': quiz_data,
                'total_quizzes': len(QUIZZES)
            })

    return redirect('landing:quiz')


def pre_register(request: HttpRequest):
    """사전 예약 페이지"""
    referred_by_code = request.GET.get('ref', '')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        referred_by_code = request.POST.get('referred_by', '')
        
        # 추가 필드 수집
        phone = request.POST.get('phone', '').strip()
        region = request.POST.get('region', '')
        age_group = request.POST.get('age_group', '')
        privacy_agreed = request.POST.get('privacy_agreed') == 'on'
        marketing_agreed = request.POST.get('marketing_agreed') == 'on'
        
        # 개인정보 동의 필수 체크
        if not privacy_agreed:
            return render(request, 'landing/pre_register.html', {
                'error': '개인정보 수집·이용에 동의해 주세요.',
                'referred_by': referred_by_code,
                'form_data': {
                    'email': email,
                    'phone': phone,
                    'region': region,
                    'age_group': age_group,
                }
            })

        # 이메일 중복 체크
        if PreRegistration.objects.filter(email=email).exists():
            return render(request, 'landing/pre_register.html', {
                'error': '이미 등록된 이메일입니다.',
                'referred_by': referred_by_code
            })

        # 추천인 찾기
        referred_by = None
        if referred_by_code:
            referred_by = PreRegistration.objects.filter(
                referral_code=referred_by_code
            ).first()

        # 새 등록 생성
        registration = PreRegistration.objects.create(
            email=email,
            referred_by=referred_by,
            phone=phone,
            region=region,
            age_group=age_group,
            privacy_agreed=privacy_agreed,
            marketing_agreed=marketing_agreed
        )

        # 공유 링크 생성 (SITE_URL 설정 시 해당 URL 사용, 없으면 현재 요청 기준)
        if settings.SITE_URL:
            share_url = f'{settings.SITE_URL}/pre-register/?ref={registration.referral_code}'
        else:
            share_url = request.build_absolute_uri(
                f'/pre-register/?ref={registration.referral_code}'
            )

        return render(request, 'landing/pre_register.html', {
            'success': True,
            'referral_code': registration.referral_code,
            'share_url': share_url
        })

    return render(request, 'landing/pre_register.html', {
        'referred_by': referred_by_code
    })


def privacy_policy(request: HttpRequest):
    """개인정보처리방침 페이지"""
    return render(request, 'landing/privacy_policy.html')
