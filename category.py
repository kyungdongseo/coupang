import json
from coupang.common import coupang


##############################################################################
# 카테고리 관련 함수                                                         # 
##############################################################################


@coupang
def get_product_auto_category(body):
    '''카테고리 추천(머신러닝)

    [반환값 예시]
    {'code': 200,
     'data': {'autoCategorizationPredictionResultType': 'SUCCESS',
              'comment': None,
              'predictedCategoryId': '80061',
              'predictedCategoryName': '아크릴사인/표지판'},
     'message': 'OK'}
     '''

    return {
            'method': "POST",
            'path': "/v2/providers/openapi/apis/api/v1/categorization/predict",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def get_category_meta(path):
    '''카테고리의 고시정보,옵션,구비서류,인증정보 목록을 조회

    자세한 정보는 아래 주소 참조
    https://developers.coupang.com/hc/ko/articles/360034035713
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/meta/category-related-metas/display-category-codes"+\
                    f"/{path.get('displayCategoryCode')}"
    }


@coupang
def get_categories():
    '''카테고리 목록조회

    노출 카테고리 목록 전체를 조회한다.
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/meta/display-categories"
    }


@coupang
def get_category(path):
    '''카테고리 조회'''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/meta/display-categories"+\
                    f"/{path.get('displayCategoryCode')}"
    }


@coupang
def get_category_validation(path):
    '''카테고리 유효성 검사

    카테고리 리뉴얼(연 2회)로 인해
    기존 카테고리가 사용되지 않을 수 있음

    [반환값 예시]
    data값이 True라면 사용가능, False라면 사용불가

    {'code': 'SUCCESS', 'data': True, 'message': ''}
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/meta/display-categories"+\
                    f"/{path.get('displayCategoryCode')}/status"
    }

