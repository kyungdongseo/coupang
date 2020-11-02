import os
import time
import re
import configparser
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
import json
from functools import wraps


config = configparser.ConfigParser()
config.read('coupang.ini')
SECRETKEY = config['DEFAULT'].get('SECRETKEY')
ACCESSKEY = config['DEFAULT'].get('ACCESSKEY')

if SECRETKEY is None:
    raise Exception('SECRETKEY를 설정해주십시오.')
if ACCESSKEY is None:
    raise Exception('ACCESSKEY를 설정해주십시오.')

SECRETKEY = re.sub('^\'|^\"|\'$|\"$', '', SECRETKEY)
ACCESSKEY = re.sub('^\'|^\"|\'$|\"$', '', ACCESSKEY)


##############################################################################
# 공통 함수                                                                  # 
##############################################################################


# decorator
def coupang(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        secretkey = SECRETKEY
        accesskey = ACCESSKEY
        retry = True

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
                try:
                    response = request(data.get('method'), url, authorization)
                except:
                    if retry:
                        retry = False
                        time.sleep(1)
                        try:
                            response = request(data.get('method'), url, authorization)
                        except:
                            pass
                    else:
                        pass

            elif 'body' in data:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path')
                )
                url = "https://api-gateway.coupang.com"+data.get('path')
                try:
                    response = request(
                            data.get('method'),
                            url,
                            authorization,
                            data.get('body')
                    )
                except:
                    if retry:
                        retry = False
                        time.sleep(1)
                        try:
                            response = request(
                                    data.get('method'),
                                    url,
                                    authorization,
                                    data.get('body')
                            )
                        except:
                            pass
                    else:
                        pass

            else:
                authorization = auth(
                        secretkey,
                        accesskey,
                        data.get('method'),
                        data.get('path')
                )
                url = "https://api-gateway.coupang.com"+data.get('path')
                try:
                    response = request(data.get('method'), url, authorization)
                except:
                    if retry:
                        retry = False
                        time.sleep(1)
                        try:
                            response = request(data.get('method'), url, authorization)
                        except:
                            pass
                    else:
                        pass

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
            try:
                response = request(data.get('method'), url, authorization)
            except:
                if retry:
                    retry = False
                    time.sleep(1)
                    try:
                        response = request(data.get('method'), url, authorization)
                    except:
                        pass
                else:
                    pass

        elif data.get('method') == 'DELETE':
            authorization = auth(
                    secretkey,
                    accesskey,
                    data.get('method'),
                    data.get('path')
            )
            url = "https://api-gateway.coupang.com"+data.get('path')
            try:
                response = request(data.get('method'), url, authorization)
            except:
                if retry:
                    retry = False
                    time.sleep(1)
                    try:
                        response = request(data.get('method'), url, authorization)
                    except:
                        pass
                else:
                    pass

        elif data.get('method') == 'POST':
            authorization = auth(
                    secretkey,
                    accesskey,
                    data.get('method'),
                    data.get('path')
            )
            url = "https://api-gateway.coupang.com"+data.get('path')
            try:
                response = request(
                        data.get('method'),
                        url,
                        authorization,
                        data.get('body')
                )
            except:
                if retry:
                    retry = False
                    time.sleep(1)
                    try:
                        response = request(
                                data.get('method'),
                                url,
                                authorization,
                                data.get('body')
                        )
                    except:
                        pass
                else:
                    pass

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
        raise e
    except urllib.request.URLError as e:
        print(e.errno)
        print(e.reason)
        raise e
    else:
        # 200
        decoded_resp = resp.read().decode(resp.headers.get_content_charset())
        response = json.loads(decoded_resp)
        return response

