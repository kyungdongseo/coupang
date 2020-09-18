import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 정산 관련 함수                                                             #
##############################################################################


@coupang
def get_revenue_history(query):
    '''매출내역 조회

    매출인식일(구매확정일 or 배송완료 + 7일)을 기준으로
    상세한 매출 내역을 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/openapi/apis/api/v1/revenue-history",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def settlement_histories(query):
    '''지급내역 조회

    매출인식월을 기준으로 지급 확정/예정된 내역을 확인
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/marketplace_openapi/apis/api/v1"+\
                    "/settlement-histories",
            'query': urllib.parse.urlencode(query)
    }

