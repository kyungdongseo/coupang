import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 정산 관련 함수                                                             #
##############################################################################


@coupang
def get_customer_service_request(query):
    '''상품별 고객문의 조회

    고객과 셀러간의 Q&A를 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{query.get('vendorId')}/onlineInquiries",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def update_customer_service_request(path, body):
    '''상품별 고객문의 답변

    고객문의(inquiryId)에 대해 답변
    하나의 고객문의(inquiryId)에 답변할 수 있습니다.
    먼저 상품별 고객문의 조회 API를 사용하여 inquiryId를 확인

    답변내용(content)을 JSON 형식에 맞게 작성하시기 바랍니다.
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/onlineInquiries"+\
                    f"/{path.get('inquiryId')}/replies",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def get_inquiry_by_query(query):
    '''쿠팡 콜센터 문의 조회

    고객이 특정 상품에 대해 쿠팡 콜센터에 접수한 문의를 조회 할 수 있습니다.
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{query.get('vendorId')}/callCenterInquiries",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def update_inquiry(body):
    '''쿠팡 콜센터 문의 답변

    판매자가 쿠팡 콜센터를 통해 접수된 문의에 대해 답변합니다.
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{body.get('vendorId')}/callCenterInquiries"+\
                    f"/{body.get('inquiryId')}/replies",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def confirm_inquiry(path, body):
    '''쿠팡 콜센터 문의확인'''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v4/vendors"+\
                    f"/{path.get('vendorId')}/callCenterInquiries"+\
                    f"/{path.get('inquiryId')}/confirms",
            'body': json.dumps(body).encode('utf-8')
    }

