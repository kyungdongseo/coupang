import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
import json
from functools import wraps
from inspect import signature


try:
    import coupang_settings
except ModuleNotFoundError:
    print('api 관한 정보가 필요합니다')
    print('coupang_settings.py 파일을 생성후')
    print('경계선 아래의 내용을 입력하십시오')
    print('='*30+'경계선'+'='*30)
    print("SECRETKEY = 'Enter your secret key here'")
    print("ACCESSKEY = 'Enter your access key here'")
    print("VENDOR_ID = 'Enter your vendor id here(Axxxxxxxx)'")
    print("USER_ID = 'Enter your user id here(Coupang Wing login ID)'")
    quit()


##############################################################################
# 공통 함수                                                                  # 
##############################################################################

# decorator
def vendor_id(f):
    @wraps(f)
    def deco(*args, **kwargs):
        key = 'vendor_id'
        sig = signature(f, follow_wrapped=True)
        keys = sig.parameters.keys()

        if key in keys:
            if len(args) < len(keys):
                position = list(keys).index(key)
                args_list = list(args)
                args_list.insert(position, coupang_settings.VENDOR_ID)
                args = tuple(args_list)

        return f(*args, **kwargs)
    return deco


# decorator
def coupang(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        secretkey = coupang_settings.SECRETKEY
        accesskey = coupang_settings.ACCESSKEY

        data = f(*args, **kwargs)
        if data.get('method') == 'PUT':
            if 'query' in data:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path'),
                        data.get('query')
                )
                url = "https://api-gateway.coupang.com"+\
                        data.get('path')+\
                        "?%s" % data.get('query')
                response = request(data.get('method'), url, authorization)
            elif 'body' in data:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path')
                )
                url = "https://api-gateway.coupang.com"+data.get('path')
                response = request(
                        data.get('method'),
                        url,
                        authorization,
                        data.get('body')
                )
            else:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path')
                )
                url = "https://api-gateway.coupang.com"+data.get('path')
                response = request(data.get('method'), url, authorization)

        elif data.get('method') == 'GET':
            if 'query' in data:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path'),
                        data.get('query')
                )
                url = "https://api-gateway.coupang.com"+\
                        data.get('path')+\
                        "?%s" % data.get('query')
            else:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path')
                )
                url = "https://api-gateway.coupang.com"+data.get('path')
            response = request(data.get('method'), url, authorization)

        elif data.get('method') == 'DELETE':
            authorization = auth(
                    secretkey,
                    accesskey,
                    data.get('method'),
                    data.get('path')
            )
            url = "https://api-gateway.coupang.com"+data.get('path')
            response = request(data.get('method'), url, authorization)

        elif data.get('method') == 'POST':
            authorization = auth(
                    secretkey,
                    accesskey,
                    data.get('method'),
                    data.get('path')
            )
            url = "https://api-gateway.coupang.com"+data.get('path')
            response = request(
                    data.get('method'),
                    url,
                    authorization,
                    data.get('body')
            )
        return response
    return decorated


def date_time():
    os.environ['TZ'] = 'GMT+0'
    return time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'


def auth(secretkey, accesskey, method, path, query=None):
    datetime = date_time()

    if query:
        message = datetime + method + path + query
    else:
        message = datetime + method + path

    signature=hmac.new(
            secretkey.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256).hexdigest()

    authorization = "CEA algorithm=HmacSHA256, access-key="+accesskey+\
            ", signed-date="+datetime+\
            ", signature="+signature

    return authorization


def request(method, url, authorization, body=None):
    req = urllib.request.Request(url)
    req.add_header("Content-type","application/json;charset=UTF-8")
    req.add_header("Authorization",authorization)
    req.add_header("X-EXTENDED-TIMEOUT", "90000") # 타임아웃 시간늘리기
    req.get_method = lambda: method

    #skipping for ssl cert.
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        if body:
            resp = urllib.request.urlopen(req, body, context=ctx)
        else:
            resp = urllib.request.urlopen(req, context=ctx)

    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.reason)
    except urllib.request.URLError as e:
        print(e.errno)
        print(e.reason)
    else:
        # 200
        decoded_resp = resp.read().decode(resp.headers.get_content_charset())
        response = json.loads(decoded_resp)
        return response

