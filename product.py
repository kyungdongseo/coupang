import json
from coupang.common import coupang


##############################################################################
# 상품 관련 함수                                                             # 
##############################################################################


@coupang
def create_product(data):
    '''상풍 등록

    [주의]
    초당 10건이하
    '''

    return {
            'method': "POST",
            'path': "/v2/providers/seller_api/apis/api/v1/"+\
                    "marketplace/seller-products",
            'body': json.dumps(data).encode('utf-8')
    }


@coupang
def get_product_by_product_id(seller_product_id):
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
                    f"/seller-products/{seller_product_id}"
    }


@coupang
def delete_product(seller_product_id):
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
                    f"/seller-products/{seller_product_id}"
    }


##############################################################################
# 아이템 관련 함수                                                           # 
##############################################################################


@coupang
def stop_product_sales_by_item(vendor_item_id):
    '''아이템별 판매 중지(or 품절)

    이미 판매중지 상태인 아이템을 상대로 호출해도 SUCCESS가 반환됨

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '판매 중지 처리되었습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{vendor_item_id}/sales/stop"
    }


@coupang
def resume_product_sales_by_item(vendor_item_id):
    '''아이템별 판매 재개

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '판매가 재개되었습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{vendor_item_id}/sales/resume"
    }


@coupang
def update_product_price_by_item(vendor_item_id, price):
    ''' 아이템별 가격 변경
    
    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '가격 변경을 완료했습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{vendor_item_id}/prices/{price}",
            'query': "forceSalePriceUpdate=true"
    }


@coupang
def update_product_quantity_by_item(vendor_item_id, quantity):
    '''아이템별 재고 수량 변경

    [반환값 예시]
    {'code': 'SUCCESS', 'data': None, 'message': '재고 변경을 완료했습니다.'}
    '''

    return {
            'method': "PUT",
            'path': "/v2/providers/seller_api/apis/api/v1/marketplace"+\
                    f"/vendor-items/{vendor_item_id}/quantities/{quantity}"
    }


@coupang
def get_product_quantity_price_status(vendor_item_id):
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
                    f"/vendor-items/{vendor_item_id}/inventories"
    }

