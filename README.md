coupang
-------
**coupang**은 쿠팡 오픈 API의 파이썬 래퍼(Python wrapper) 입니다.   
현재 7개의 주제에 대해 구현되어 있으며, 그 내용은 아래와 같습니다.      
1. 카테고리 API(category)
    - 카테고리 메타정보 조회
        * get_category_meta(display_category_code)
    - 카테고리 추천
        * get_product_auto_category(body)
    - 카테고리 목록조회
        * 구현미정
    - 카테고리 유효성 검사
        * get_category_validation(display_category_code)
2. 물류센터 API(shipping)
    - 출고지 생성
        * register_outbound_shipping_center(body)
    - 출고지 조회
        * outbound_shipping_place(kwargs)
    - 출고지 수정
        * update_outbound_shipping_place(body)
    - 반품지 생성
        * 구현예정
    - 반품지 목록 조회
        * get_shipping_center_by_vendor(vendor_id, page_num, page_size)
    - 반품지 수정
        * 구현예정
    - 반품지 단건 조회
        * get_shipping_by_center_code(return_center_codes)
3. 상품 API(product)
    - 상품 생성
        * create_product(body)
    - 상품 조회
        * get_product_by_product_id(seller_product_id)
    - 상품 수정
        * 구현미정
    - 상품 삭제
        * delete_product(seller_product_id)
    - 상품 목록 페이지 조회
        * 구현미정
    - 상품 목록 구간 조회
        * 구현미정
    - 상품 상태변경이력 조회
        * 구현미정
    - 상품 요약 정보 조회
        * 구현미정
    - 상품 아이템별 수량/가격/상태 조회
        * get_product_quantity_price_status(vendor_item_id)
    - 상품 아이템별 수량 변경
        * update_product_quantity_by_item(vendor_item_id, quantity)
    - 상품 아이템별 가격 변경
        * update_product_price_by_item(vendor_item_id, price)
    - 상품 아이템별 판매 재개
        * resume_product_sales_by_item(vendor_item_id)
    - 상품 아이템별 판매 중지
        * stop_product_sales_by_item(vendor_item_id)
4. 배송/환불 API(ordersheet)
    - 발주서 목록 조회(일단위/분단위)
        * get_ordersheet(vendor_id, query)
    - 발주서 단건 조회(shipment_box_id)
        * get_ordersheet_by_shipmentboxid(vendor_id, shipment_box_id)
    - 발주서 단건 조회(order_id)
        * get_ordersheet_by_orderid(vendor_id, order_id)
    - 배송상태 변경 히스토리 조회
        * get_ordersheet_history(vendor_id, shipment_box_id)
    - 상품준비중 처리
        * update_ordersheet_status(body)
    - 송장업로드 처리
        * update_order_shipping_info(body)
    - 송장업데이트 처리
        * update_order_invoice(body)
    - 출고중지완료 처리
        * stop_return_request_shipment(body)
    - 이미출고 처리
        * stop_return_request_by_receipt(body)
    - 주문 상품 취소 처리
        * cancel_order_processing(body)
    - 장기 미배송 완료 처리
        * update_invoice_delivery_by_invoice_no(vendor_id, body)
5. 반품 API(return)
    - 반품/취소 요청 목록 조회
        * get_return_request_by_query(vendor_id, query)
    - 반품요청 단건 조회
        * get_return_request_by_receipt(vendor_id, receipt_id)
    - 반품상품 입고 확인 처리
        * get_return_request_confirmation(body)
    - 반품요청 승인 처리
        * approve_return_request_by_receipt(body)
    - 반품철회 이력 기간별 조회
        * get_return_withdraw_request(vendor_id, query)
    - 반품철회 이력 접수번호로 조회
        * get_return_withdraw_by_cancel_ids(vendor_id, body)
    - 회수 송장 등록
        * create_return_exchange_invoice(vendor_id, body)
6. 교환 API(exchange)
    - 교환요청 목록조회
        * get_exchange_request(vendor_id, query)
    - 교환요청상품 입고 확인처리
        * confirm_exchange_request(body)
    - 교환요청 거부 처리
        * reject_exchange_request(body)
    - 교환상품 송장 업로드 처리
        * update_invoice_exchange_request(body)
7. 검색(search)
    - 상품검색
        * search(keywords)
    
함수의 매개변수 이름은 **쿠팡 오픈 API** 에서 사용되는 이름을 그대로 사용했으며    
표현방식만 파이썬에 맞게끔 수정되었습니다.    
예를 들면, VendorId는 vendor_id 로 수정하였으며    
body는 Body Parameter를 의미하며 dict 자료형입니다.    
또한 query는 Query String Parameter 를 의미하며 dict 자료형입니다.    
     
쿠팡 오픈 API에 관한 자세한 내용은 아래 주소에서 확인하실 수 있습니다.   
[쿠팡 오픈 API 공식문서](https://developers.coupang.com/hc/ko)    

설치
----
**pip install coupang**   

사용법
-----
1. 위의 명령어를 이용하여 coupang 패키지 설치하기
2. OPEN API Key 발급받기
    - 쿠팡의 [OPEN API Key 발급받기](https://developers.coupang.com/hc/ko/articles/360033980613)를 참조하여 SecretKey, AccessKey, VendorId를 준비합니다. 
3. **coupang_settings.py** 파일을 만들고 아래의 정보를 작성하십시오.    
```python
SECRETKEY = '발급받은 SecretKey'
ACCESSKEY = '발급받은 AccessKey'
VENDOR_ID = 'VendorId'
```
4. 파이썬 쉘에서 테스트 해보기
```python
MacBook-Pro:~/kyungdongseo$ cat >> coupang_settings.py << EOF 
> SECRETKEY = '비밀키'
> ACCESSKEY = '액세스키'
> VENDOR_ID = '벤더ID'
> EOF

MacBook-Pro:~/kyungdongseo$ ls
coupang_settings.py   

MacBook-Pro:~/kyungdongseo$ python
>>> from coupang.category import get_product_auto_category
>>> get_product_auto_category({'productName': 'pop꽂이'})
{'code': 200, 'message': 'OK', 'data': {'autoCategorizationPredictionResultType': 'SUCCESS', 'predictedCategoryId': '80060', 'predictedCategoryName': '아크릴/POP꽂이', 'comment': None}}
```
