import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 배송(일부 환불) 관련 함수                                                  #
##############################################################################


@coupang
def get_ordersheet(path, query):
    '''발주서 목록 조회

    (일단위 조회)
    최대 31일까지 조회가능
    날짜는 yyyy-mm-dd 형태(2020-09-03)

    (분단위 조회)
    24시간 이내의 분단위 구간 조회
    날짜는 yyyy-mm-ddT00:00 형태(2020-09-03T21:52)
    쿼리에 searchType=timeFrame 추가
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/ordersheets",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_ordersheet_by_shipmentboxid(path):
    '''발주서 조회

    shipment_box_id(배송번호)를 이용하여 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/ordersheets"+\
                    f"/{path.get('shipmentBoxId')}"
    }


@coupang
def get_ordersheet_by_orderid(path):
    '''발주서 조회

    order_id(주문번호)를 이용하여 발주서 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}"+\
                    f"/{path.get('orderId')}/ordersheets"
    }


@coupang
def get_ordersheet_history(path):
    '''배송상태 변경 히스토리 조회

    특정 주문에 대한 배송상태 히스토리 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/ordersheets"+\
                    f"/{path.get('shipmentBoxId')}/history"
    }


@coupang
def update_ordersheet_status(body):
    '''주문상태를 '결제완료'에서 '상품준비중'으로 변경

    묶음배송번호를 이용하여 상태변경
    한번에 최대 50개까지 처리 가능
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/ordersheets/acknowledgement",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_order_shipping_info(body):
    '''송장 업로드

    '상품준비중'에서 '배송지시'로 상태가 변경됨
    6개월 이내에 중복된 송장번호 입력시 에러 발생
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/orders/invoices",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_order_invoice(body):
    '''송장 업데이트(수정)

    잘못 등록한 운송장 내용을 변경
    배송상태는 배송지시(DEPARTURE)로 변경되며 이후 트래킹 정보 연동에 따라 변경

    [주의]
    배송지시(DEPARTURE),
    배송중(DELIVERING),
    배송완료(FINAL_DELIVERY),
    업체직송(NONE_TRACKING)
    위 4가지 상태일 때만 운송장 정보 변경이 가능
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/orders/updateInvoices",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def stop_return_request_shipment(body):
    '''출고중지 완료
    
    아직 상품을 발송하지 않아,
    고객 요청대로 상품을 출고하지 않았을 때 사용

    고객이 주문을 취소하여
    상태가 출고중지요청(RELEASE_STOP_UNCHECKED) 이거나
    반품접수미확인(RETURNS_UNCHECKED) 이면서
    releaseStatus가 "N" 일 경우에 사용가능
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/returnRequests"+\
                    f"/{body.get('receiptId')}/stoppedShipment",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def stop_return_request_by_receipt(body):
    '''이미출고

    판매자가 상품을 발송한 후,
    송장 업로드를 하기 전에
    고객이 주문을 취소했을 때 사용

    고객이 주문을 취소하여
    출고중지요청(RELEASE_STOP_UNCHECKED) 이거나
    반품접수미확인(RETURNS_UNCHECKED) 이면서
    releaseStatus가 "N" 일 경우에 사용

    [주의]
    왕복 반품 배송비는 판매자의 귀책
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/returnRequests"+\
                    f"/{body.get('receiptId')}/completedShipment",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def cancel_order_processing(body):
    '''주문상품 취소

    [결제완료] 또는 [상품준비중] 상태에 있는 주문을 취소
    [결제완료] 상태에 있는 주문에 대해서는 즉시 취소
    [상품준비중] 상테애 있는 주문에 대해서는 출고중지됨

    [주의]
    판매자 점수 하락
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v5/vendors"+\
                    f"/{body.get('vendorId')}/orders"+\
                    f"/{body.get('orderId')}/cancel",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_invoice_delivery_by_invoice_no(path, body):
    '''장기미배송 배송완료 처리

    송장 업로드 후 1달이 경과하였으나,
    배송추적 결과를 확인할 수 없는 내용에 대해 배송완료로 상태를 변경

    송장 업로드 후 1달이 지난,
    배송지시, 배송중 상태인 주문만 처리 가능
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/completeLongTermUndelivery",
            'body': json.dumps(body).encode('utf-8')
    }

