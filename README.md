coupang
-------
**coupang**은 쿠팡 오픈 API의 파이썬 래퍼(Python wrapper) 입니다.   
현재 9개의 주제에 대해 구현되어 있으며, 그 내용은 아래와 같습니다.      
1. 카테고리 API(category)
    - 카테고리 메타정보 조회
        * get_category_meta(path)
    - 카테고리 추천
        * get_product_auto_category(body)
    - 카테고리 목록조회
        * get_categories()
    - 카테고리 조회
        * get_category(path)
    - 카테고리 유효성 검사
        * get_category_validation(path)
2. 물류센터 API(shipping)
    - 출고지 생성
        * register_outbound_shipping_center(body)
    - 출고지 조회
        * outbound_shipping_place(query)
    - 출고지 수정
        * update_outbound_shipping_place(body)
    - 반품지 생성
        * update_shipping_center_by_vendor(path, body)
    - 반품지 목록 조회
        * get_shipping_center_by_vendor(path, query)
    - 반품지 수정
        * update_shipping_center_by_return_center_code(path, body)
    - 반품지 단건 조회
        * get_shipping_by_center_code(query)
3. 상품 API(product)
    - 상품 생성
        * create_product(body)
    - 상품 승인 요청
        * approve_product(path)
    - 상품 조회
        * get_product_by_product_id(path)
    - 상품 조회(승인불필요)
        * get_partial_product_by_product_id(path)
        * 해당 상품의 배송 및 반품지 등의 관련 정보를 조회
    - 상품 수정(승인필요)
        * update_product(body)
    - 상품 수정(승인불필요)
        * update_partial_product(body)
        * 배송 및 반품지 관련 정보를 별도의 승인 절차 없이 빠르게 수정
    - 상품 삭제
        * delete_product(path)
    - 상품 목록 페이징 조회
        * get_products_by_query(query)
    - 상품 목록 구간 조회
        * get_products_by_time_frame(query)
    - 상품 상태변경이력 조회
        * get_product_status_history(query)
    - 상품 요약 정보 조회
        * get_product_by_external_sku(path)
    - 상품 아이템별 수량/가격/상태 조회
        * get_product_quantity_price_status(path)
    - 상품 아이템별 수량 변경
        * update_product_quantity_by_item(path)
    - 상품 아이템별 가격 변경
        * update_product_price_by_item(path)
    - 상품 아이템별 판매 재개
        * resume_product_sales_by_item(path)
    - 상품 아이템별 판매 중지
        * stop_product_sales_by_item(path)
4. 배송/환불 API(ordersheet)
    - 발주서 목록 조회(일단위/분단위)
        * get_ordersheet(path, query)
    - 발주서 단건 조회(shipment_box_id)
        * get_ordersheet_by_shipmentboxid(path)
    - 발주서 단건 조회(order_id)
        * get_ordersheet_by_orderid(path)
    - 배송상태 변경 히스토리 조회
        * get_ordersheet_history(path)
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
        * update_invoice_delivery_by_invoice_no(path, body)
5. 반품 API(returns)
    - 반품/취소 요청 목록 조회
        * get_return_request_by_query(path, query)
    - 반품요청 단건 조회
        * get_return_request_by_receipt(path)
    - 반품상품 입고 확인 처리
        * get_return_request_confirmation(body)
    - 반품요청 승인 처리
        * approve_return_request_by_receipt(body)
    - 반품철회 이력 기간별 조회
        * get_return_withdraw_request(path, query)
    - 반품철회 이력 접수번호로 조회
        * get_return_withdraw_by_cancel_ids(path, body)
    - 회수 송장 등록
        * create_return_exchange_invoice(path, body)
6. 교환 API(exchange)
    - 교환요청 목록조회
        * get_exchange_request(path, query)
    - 교환요청상품 입고 확인처리
        * confirm_exchange_request(body)
    - 교환요청 거부 처리
        * reject_exchange_request(body)
    - 교환상품 송장 업로드 처리
        * update_invoice_exchange_request(body)
7. CS API(cs)
    - 상품별 고객문의 조회
        * get_customer_service_request(query)
    - 상품별 고객문의 답변
        * update_customer_service_request(path, body)
    - 쿠팡 콜센터 문의 조회
        * get_inquiry_by_query(query)
    - 쿠팡 콜센터 문의 답변
        * update_inquiry(body)
    - 쿠팡 콜센터 문의 확인
        * confirm_inquiry(path, body)
8. 정산 API(settlement)
    - 매출내역 조회
        * get_revenue_history(query)
    - 지급내역 조회
        * settlement_histories(query)
9. 검색(search)
    - 상품검색
        * search(keywords)
     
함수의 매개변수는 **쿠팡 오픈 API** 에서 확인할 수 있습니다.    
path는 Path Segment Parameter를 의미하며 dict 자료형입니다.    
body는 Body Parameter를 의미하며 dict 자료형입니다.    
query는 Query String Parameter 를 의미하며 dict 자료형입니다.    
마지막의 search 함수의 매개변수인 keywords는 str 타입입니다.    
     
쿠팡 오픈 API에 관한 자세한 내용은 아래 주소에서 확인하실 수 있습니다.   
[쿠팡 오픈 API 공식문서](https://developers.coupang.com/hc/ko)    

설치
----
**pip install coupang**   

사용법
-----
1. 위의 명령어를 이용하여 coupang 패키지 설치하기
2. OPEN API Key 발급받기
    - 쿠팡의 [OPEN API Key 발급받기](https://developers.coupang.com/hc/ko/articles/360033980613)를 참조하여 SecretKey, AccessKey를 준비합니다. 
3. **coupang.ini** 파일을 만들고 아래의 정보를 작성하십시오.    
```python
[DEFAULT]
SECRETKEY = 발급받은SecretKey
ACCESSKEY = 발급받은AccessKey
```
4. 파이썬 쉘에서 테스트 해보기
```python
MacBook-Pro:~/kyungdongseo$ pip install coupang

MacBook-Pro:~/kyungdongseo$ cat >> coupang.ini << EOF 
> [DEFAULT]
> SECRETKEY = 비밀키
> ACCESSKEY = 액세스키
> EOF

MacBook-Pro:~/kyungdongseo$ ls
coupang.ini    

MacBook-Pro:~/kyungdongseo$ python
>>> from coupang.category import get_product_auto_category
>>> get_product_auto_category({'productName': 'pop꽂이'})
{'code': 200, 'message': 'OK', 'data': {'autoCategorizationPredictionResultType': 'SUCCESS', 'predictedCategoryId': '80060', 'predictedCategoryName': '아크릴/POP꽂이', 'comment': None}}
```
