from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# index page
def index(request):
    olympics = Olympic.objects.all()
    sports = Sport.objects.all()
    games = Game.objects.all()
    context = {
        'olympics': olympics,
        'sports': sports,
        'games': games,
    }
    return render(request, 'index.html', context)

# 선수의 메달 랭킹 조회
def rank(request):
    # 선수별 메달 랭킹
    athletes = Participate.objects.values('athlete_id').annotate(dcount=Count('athlete_id'))
    # 종목별 메달 랭킹
    sports = Game.objects.values('sport_id').annotate(dcount=Count('sport_id'))
    temp_athlete_results = []
    # 각 선수 객체 받아오기
    for item in athletes:
        award_athlete = Athlete.objects.get(athlete_id=item['athlete_id'])
        temp_athlete_results.append({'athlete': award_athlete, 'count': item['dcount']})
    # 메달 개수를 기준으로 정렬
    athlete_results = sorted(temp_athlete_results, reverse=True, key=(lambda x: x['count']))
    temp_sport_results = []
    # 각 종목 객체 받아오기
    for item in sports:
        award_sport = Sport.objects.get(sport_id=item['sport_id'])
        temp_sport_results.append({'sport': award_sport, 'count': item['dcount']})
    sport_results = sorted(temp_sport_results, reverse=True, key=(lambda x: x['count']))
    paginator = Paginator(athlete_results, 20)
    page = request.GET.get('page')
    try:
        athlete_results = paginator.page(page)
    except PageNotAnInteger:
        athlete_results = paginator.page(1)
    except EmptyPage:
        athlete_results = paginator.page(paginator.num_pages)
    return render(request, 'rank.html', {'athlete_results': athlete_results, 'sport_results': sport_results})

# 우리나라의 역대 메달 기록을 날짜 순으로 보여주기
def record(request):
    # 날짜순으로 정렬
    date_participates = Participate.objects.all().order_by('game__olympic__host_year')

    # 올림픽별로 그룹화
    olympic_participates = Game.objects.values('olympic_id').annotate(dcount=Count('olympic'))

    # 각 올림픽 객체 받아오기
    result = []

    for item in olympic_participates:
        print('item', item)
        olympic_participate = Olympic.objects.get(olympic_id=item['olympic_id'])
        result.append({'olympic': olympic_participate, 'count': item['dcount']})

    paginator = Paginator(date_participates, 20)
    page = request.GET.get('page')

    try:
        date_participates = paginator.page(page)
    except PageNotAnInteger:
        date_participates = paginator.page(1)
    except EmptyPage:
        date_participates = paginator.page(paginator.num_pages)
    return render(request, 'record.html', {'date_participates': date_participates, 'result': result})

# 해당 올림픽에서 수상한 기록
def record_detail(request, pk):
    # olympic_id가 같은 game 추출
    games = Game.objects.filter(olympic_id=pk)
    temp_results = []
    for game in games:
        participate = Participate.objects.filter(game_id=game.game_id)
        temp_results.append(participate)
    results = []
    for temp in temp_results:
        for item in temp:
            results.append(item)
    return render(request, 'detail_record.html', {'results': results})

# 선수정보 조회
def athlete(request):

    athlete_list = Athlete.objects.all()
    # 20 athlete per page
    paginator = Paginator(athlete_list, 20)
    page = request.GET.get('page')

    try:
        athletes = paginator.page(page)
    except PageNotAnInteger:
        athletes = paginator.page(1)
    except EmptyPage:
        athletes = paginator.page(paginator.num_pages)

    return render(request, 'search_athlete.html', {'athletes': athletes})

def athlete_detail(request, pk):

    # athlete 중 pk를 이용해 한명의 athlete 검색
    athlete = Athlete.objects.get(pk=pk)
    participate = Participate.objects.filter(athlete_id=pk)
    return render(request, 'detail_athlete.html', {'athlete': athlete, 'participate': participate})

def search(request):
    selected_season= request.GET.get('season', None)

    if selected_season:
        print('시즌', selected_season)
        olympics = Olympic.objects.filter(season=selected_season)
        sports = Sport.objects.filter(season=selected_season)
    return render(request, 'search_result.html', {'olympics': olympics, 'sports': sports})

def result(request):

    selected_olympic = request.GET.get('olympic', None)
    selected_sport = request.GET.get('sport', None)
    check_olympic = request.GET.get('olympicCheck', None)
    check_sport = request.GET.get('sportCheck', None)


    # 둘다 체크 한 경우
    if check_olympic and check_sport:
        if selected_sport and selected_olympic:
            print('올림픽', selected_olympic)
            print('종목', selected_sport)
            games = Game.objects.filter(olympic_id=selected_olympic, sport_id=selected_sport)
            participates = []
            for game in games:
                result = Participate.objects.filter(game_id=game.game_id)
                print(result)
                participates.append(result)
    # 하나만 체크 한 경우
    elif check_olympic:
        if selected_olympic:
            games = Game.objects.filter(olympic_id=selected_olympic)
            participates = []
            for game in games:
                result = Participate.objects.filter(game_id=game.game_id)
                participates.append(result)
    elif check_sport:
        if selected_sport:
            games = Game.objects.filter(sport_id=selected_sport)
            participates = []
            for game in games:
                result = Participate.objects.filter(game_id=game.game_id)
                participates.append(result)
    return render(request, 'result.html', {'games': games, 'participates': participates})