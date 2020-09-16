import json
import urllib.parse
from coupang.common import coupang


##############################################################################
# 상품 관련 함수                                                             # 
##############################################################################


@coupang
def create_product(body):
    '''상풍 등록

    [주의]
    초당 10건이하
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/seller_api/apis/api/v1/"+\
                    "marketplace/seller-products",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def approve_product(path):
    '''상품 승인 요청

    임시저장 상태에서만 승인요청이 가능합니다.

    상품생성, 수정 API 에서
    requested 파라메터를  true 로 입력할 경우
    자동으로 판매 승인요청이 진행됩니다.
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{path.get('sellerProductId')}/approvals"
    }


@coupang
def get_partial_product_by_product_id(path):
    '''상품 조회(승인불필요)

    해당 상품의 배송 및 반품지 등의 관련 정보를 조회할 수 있습니다.
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{path.get('sellerProductId')}/partial"
    }


@coupang
def get_product_by_product_id(path):
    '''등록상품ID로(seller_product_id) 등록된 상품의 정보를 조회

    옵션ID(vendor_item_id)를 얻을 수 있으며,
    상품에 관련된 전문을 얻을 수 있다

    옵션ID(vendor_item_id)는 아래 코드를 이용해서 얻을 수 있다
    for item in 반환된dict.get('data').get('items'):
        item.get('vendorItemId')

    자세한 반환값 예시는 아래 주소 참조 
    https://developers.coupang.com/hc/ko/articles/360033644994-상품-조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{path.get('sellerProductId')}"
    }


@coupang
def update_product(body):
    '''상품 수정(승인필요)

    상품 조회를 이용하여 조회된 JSON 전문에서 원하는 값 만 수정 후
    전체 JSON 전문을 전송하여 수정이 가능
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/seller-products",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def update_partial_product(body):
    '''상품 수정(승인불필요)

    배송 및 반품지 관련 정보를 별도의 승인 절차 없이 빠르게 수정
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{body.get('sellerProductId')}/partial",
            'body': json.dumps(body).encode('utf-8')
    }


@coupang
def get_products_by_query(query):
    '''상품 목록 페이징 조회'''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/seller-products",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_products_by_time_frame(query):
    '''상품 목록 구간 조회

    등록된 상품 목록을 생성일시 기준으로 조회
    최대 조회 범위는 10분
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/seller-products/time-frame",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_product_status_history(query):
    '''상품 상태변경 이력 조회'''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{query.get('sellerProductId')}/histories",
            'query': urllib.parse.urlencode(query)
    }


@coupang
def get_product_by_external_sku(path):
    '''상품 요약 정보 조회

    판매자 상품코드(externalVendorSku)로 상품 요약 정보를 조회
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    "/seller-products/external-vendor-sku-codes"+\
                    f"/{path.get('externalVendorSkuCode')}"
    }


@coupang
def delete_product(path):
    '''등록된 상품을 삭제한다

    상품이 승인대기중 상태가 아니며,
    상품에 포함된 옵션(아이템)이 모두 판매중지된 경우에 삭제가 가능하다

    [반환값 예시]
    {
        'code': 'SUCCESS',
        'data': '10779906515',
        'message': '10779906515가 삭제되었습니다.'
    }
    '''

    return {
            'method': "DELETE",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/seller-products/{path.get('sellerProductId')}"
    }


##############################################################################
# 아이템 관련 함수                                                           # 
##############################################################################


@coupang
def stop_product_sales_by_item(path):
    '''아이템별 판매 중지(or 품절)

    이미 판매중지 상태인 아이템을 상대로 호출해도 SUCCESS가 반환됨

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '판매 중지 처리되었습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{path.get('vendorItemId')}/sales/stop"
    }


@coupang
def resume_product_sales_by_item(path):
    '''아이템별 판매 재개

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '판매가 재개되었습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{path.get('vendorItemId')}/sales/resume"
    }


@coupang
def update_product_price_by_item(path):
    ''' 아이템별 가격 변경
    
    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '가격 변경을 완료했습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{path.get('vendorItemId')}/prices"+\
                    f"/{path.get('price')}",
            'query': "forceSalePriceUpdate=true"
    }


@coupang
def update_product_quantity_by_item(path):
    '''아이템별 재고 수량 변경

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '재고 변경을 완료했습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{path.get('vendorItemId')}"+\
                    f"/quantities/{path.get('quantity')}"
    }


@coupang
def get_product_quantity_price_status(path):
    '''아이템별 재고, 가격, 판매상태 조회

    [반환값 예시]
    {'code': 'SUCCESS',
     'data': {'amountInStock': 100,
              'onSale': True,
              'salePrice': 5700,
              'sellerItemId': 70869886485},
     'message': ''}
    '''

    return {
            'method': "GET",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{path.get('vendorItemId')}/inventories"
    }

