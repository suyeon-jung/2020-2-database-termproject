# 🇰🇷 대한민국 올림픽 기록 검색 시스템 

2020년도 2학기 경희대학교 데이터베이스 설계프로젝트


## 🔌 실행 방법
Step 1. [Anaconda](https://www.anaconda.com/products/individual) 설치

Step 2. Git Clone
```bash
git clone http://khuhub.khu.ac.kr/2020-02-database/2017104025.git 
```

Step 3. `가상환경` 생성 및 시작
```bash
$ conda create -n [YOUR_ENV] python=3.6
$ source activate [YOUR_ENV]
```

Step 4. Django 및 프로젝트에 필요한 라이브러리 설치
```bash
([YOUR_ENV]) 프로젝트_폴더 $ pip install -r requirements.txt
```

Step 5-1. Database configuration  
프로젝트 디렉토리에서 `my_settings.py` 파일 생성 후 데이터베이스 접속정보를 입력
```
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : "DB이름",
        'USER' : "DB유저",
        'PASSWORD' : "DB유저암호",
        'HOST': "DB호스트주소",
        'PORT' : "DB포트번호",
    }
}
```

Step 5-2. Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

Step 6. 서버 실행 및 확인
```bash
$ python manage.py runserver
```
http://localhost:8000 에서 확인!

## 📄 LICENSE
[MIT License]()