import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 반품 관련 함수                                                             #
##############################################################################


@coupang
def get_return_request_by_query(path, query):
    '''반품(취소)요청 목록 조회

    자세한 설명은 아래주소 참조
    https://developers.coupang.com/hc/ko/articles/360033919613
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnRequests",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_return_request_by_receipt(path):
    '''반품 조회(단건)

    반품(취소) 접수번호(receipt_id)를 이용한 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnRequests"+\
                    f"/{path.get('receiptId')}"
    }


@coupang
def get_return_request_confirmation(body):
    '''반품상품 입고(회수) 확인

    빠른환불 대상(10만원 미만) 상품이 아니거나,
    회수 송장이 트랙킹 되지 않는 상품이
    receiptStatus가 반품접수(RETURNS_UNCHECKED)인 반품 건에 대해 처리 가능

    이 api 호출 후에는, 무조건 고객에게 환불이 됨.

    환불이 되었으나 반품된 물건 또는 배송비에 문제가 있을 경우에는
    WING에서 ‘쿠팡 확인 요청’

    자세한 프로세스 이해는 아래 주소 참조
    https://developers.coupang.com/hc/ko/articles/360033643294
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/returnRequests"+\
                    f"/{body.get('receiptId')}/receiveConfirmation",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def approve_return_request_by_receipt(body):
    '''반품요청 승인

    반품 프로세스의 마지막
    receiptStatus가 입고완료(VENDOR_WAREHOUSE_CONFIRM)인 반품 건에 대해 처리

    입고확인이 완료된 반품 건의 경우,
    일정 시간 경과 후 쿠팡시스템에 의해 반품이 자동승인 처리
    이 경우, api 호출이 불필요

    [주의]
    반품요청 승인 전에,
    반품된 상품에 문제가 있을 경우, 쿠팡에 조정및 보상요
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/returnRequests"+\
                    f"/{body.get('receiptId')}/approval",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def get_return_withdraw_request(path, query):
    '''반품철회 이력 조회(기간별)

    최대 7일간 조회가능
    조회시작일과 조회종료일이 검색기간에 포함됨
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnWithdrawRequests",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_return_withdraw_by_cancel_ids(path, body):
    '''반품철회 이력 조회(반품(취소) 접수번호 사용)'''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/returnWithdrawList",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def create_return_exchange_invoice(path, body):
    '''회수 송장 등록

    반품자동연동 서비스를 사용하지 않고
    자체적으로 반품을 회수하는 판매자

    반품: 반품접수(RETURNS_UNCHECKED) 인 경우에 사용 가능
    교환: 회수연동전(BeforeDirection)인 경우에 사용 가능

    [주의]
    반품된 물건을 확인 후, 고객에게 환불되기를 원할 경우에는
    트랙킹 되지 않는 송장번호를 사용할 것
    그러면, 반품상품 입고 확인 후에 고객에게 환불됨
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/return-exchange-invoices/manual",
            'body': json.dumps(body).encode('utf-8')
    }

