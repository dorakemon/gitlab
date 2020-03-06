A-team

# backend
```
# 仮想環境を作る
# 作れているならばスキップ
python -m venv [仮想環境名]
source [仮想環境名]/bin/activate
```

```
pip install -r requirements.txt
cd backend
python manage.py runserver
```

認証はJWT

JWTのせいでAPIにアクセスしても見れないので見たいときは
backend/backend/settings.py
```python:settings.py
## ここから以下
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #Simple JWTの読み込み
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

from datetime import timedelta

#Simple JWTの設定
SIMPLE_JWT = {
    #トークンをJWTに設定
    'AUTH_HEADER_TYPES': ('JWT',),
    #トークンの持続時間の設定
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5)
}
```
をコメントアウト

やってフロントでプッシュするときに絶対に**コメントアウトを外して**ください