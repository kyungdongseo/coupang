import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 교환 관련 함수                                                             #
##############################################################################


@coupang
def get_exchange_request(path, query):
    '''교환 요청 목록 조회

    최대 7일 이내의 교환 내역을 확인할 수 있음
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/exchangeRequests",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def confirm_exchange_request(body):
    '''교환 요청 상품 입고 확인

    고객이 반송한 상품을 접수한 후
    판매자는 이 api를 통해서
    교환상품 입고 확인 상태로 변경
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/exchangeRequests"+\
                    f"/{body.get('exchangeId')}/receiveConfirmation",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def reject_exchange_request(body):
    '''교환요청 거부 처리

    고객이 요청한 교환 요청을 수락할 수 없는 경우
    이 API를 사용하여 교환 요청을 거부

    [거부조건]
    교환 상품이 매진된 상태일 경우
    고객이 교환 요청을 철회한 경우
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/exchangeRequests"+\
                    f"/{body.get('exchangeId')}/rejection",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_invoice_exchange_request(body):
    '''교환상품 송장 업로드

    교환할 상품의 운송장을 입력

    [주의]
    교환상품 입고확인 후,
    10분이 지난 후,
    교환요청 목록 조회를 통해서
    새로 생성된 shipmentBoxId 를 발급받아 사용해야함
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/exchangeRequests"+\
                    f"/{body.get('exchangeId')}/invoices",
            'body': json.dumps(body).encode('utf-8')
    }

