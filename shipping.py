import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 물류센터 관련 함수                                                         #
##############################################################################


def outbound_shipping_data_template(when="create"):
    data = {
            "vendorId": "판매자ID(Axxxxxx)",
            "userId": "사용자ID(쿠팡 WING ID)",
            "shippingPlaceName": "출고지이름",
            "global": "false",
            "usable": "true",
            "placeAddresses": [
                {
                    "addressType": "JIBUN",
                    "countryCode": "KR",
                    "companyContactNumber": "전화번호(000-0000-0000)",
                    "phoneNumber2": "보조 전화번호",
                    "returnZipCode": "우편번호(5자리 or 6자리)",
                    "returnAddress": "지번 주소",
                    "returnAddressDetail": "상세주소"
                },
                {
                    "addressType": "ROADNAME",
                    "countryCode": "KR",
                    "companyContactNumber": "전화번호(000-0000-0000)",
                    "phoneNumber2": "보조 전화번호",
                    "returnZipCode": "우편번호(5자리 or 6자리)",
                    "returnAddress": "도로명 주소",
                    "returnAddressDetail": "상세주소"
                }
            ],
            "remoteInfos": [
                {
                    "deliveryCode": "택배사코드(CJGLS)",
                    "jeju": "제주지역 배송비(1000~20000)",
                    "notJeju": "제주이외의 도서산간 배송비(1000~20000)"
                }
            ]
    }

    if when == "create":
        return data
    elif when == "update" or when == "delete":
        data['outboundShippingPlaceCode'] = '출고지코드 ("null"인 경우 출고지 이름은 변하지 않음)'
        data.get('remoteInfos')[0]['remoteInfoId'] = "수정/삭제시 반드시 입력"
        return data


@coupang
def register_outbound_shipping_center(body):
    '''상품 출고지 생성

    (주의)
    도로명 주소 등록시, 지번주소도 같이 등록해야 함

    [반환값 예시]
    resultMessage 가 출고지코드임
    {
        'code': 200,
        'data': {'resultCode': 'SUCCESS', 'resultMessage': '2810326'},
        'message': 'SUCCESS'
    }

    자세한 내용은 아래주소 참조
    https://developers.coupang.com/hc/ko/articles/360033918753
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/outboundShippingCenters",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def outbound_shipping_place(query):
    '''출고지 조회

    출고지 목록조회: pageNum, pageSize
    (예시) {'pageSize': 50, 'pageNum': 1}

    특정 출고지 조회: placeNames or placeCodes
    {'placeCodes': 2475044} or {'placeNames': '이곳으로반품하지마세요'}
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/marketplace_openapi/apis/api/v1/vendor"+\
                    "/shipping-place/outbound",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def update_outbound_shipping_place(body):
    '''출고지 수정

    outboundShippingPlaceCode 와 remoteInfoId 는
    '출고지 조회'을 통해 얻을 수 있음

    [반환값 예시]
    {
        'code': 200,
        'data': {
            'resultCode': 'SUCCESS',
            'resultMessage': 'Modify successfully'
        },
        'message': 'SUCCESS'
    }
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/outboundShippingCenters"+\
                    f"/{body.get('outboundShippingPlaceCode')}",
            'body': json.dumps(body).encode('utf-8') 
    }


@coupang
def get_shipping_center_by_vendor(path, query):
    '''반품지 목록 조회'''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnShippingCenters",
            'query': urllib.parse.urlencode(query)
    }



@coupang
def get_shipping_by_center_code(query):
    '''반품지 조회

    return_center_code(반품지코드)를 콤마(,)로 연결하여
    여러개를 동시에 조회할 수 있음
    (예) 1000554021,1000554704
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/greatwall_api/apis/api/v2"+\
                    "/return/shipping-places/center-code",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def update_shipping_center_by_vendor(path, body):
    '''반품지 생성'''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnShippingCenters",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_shipping_center_by_return_center_code(path, body):
    '''반품지 수정'''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnShippingCenters"+\
                    f"/{path.get('returnCenterCode')}",
            'body': json.dumps(body).encode('utf-8')
    }

