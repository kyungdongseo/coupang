coupang
-------
**coupang**은 쿠팡 오픈 API의 파이썬 래퍼(Python wrapper) 입니다.   
현재 7개의 주제에 대해 구현되어 있으며, 그 내용은 아래와 같습니다.      
1. 카테고리 API
    - 카테고리 메타정보 조회
    - 카테고리 추천
    - 카테고리 목록조회
    - 카테고리 유효성 검사
2. 물류센터 API
    - 출고지 생성
    - 출고지 조회
    - 출고지 수정
    - 반품지 생성
    - 반품지 목록 조회
    - 반품지 수정
    - 반품지 단건 조회
3. 상품 API
    - 상품 생성
    - 상품 조회
    - 상품 수정
    - 상품 삭제
    - 상품 목록 페이지 조회
    - 상품 목록 구간 조회
    - 상품 상태변경이력 조회
    - 상품 요약 정보 조회
    - 상품 아이템별 수량/가격/상태 조회
    - 상품 아이템별 수량 변경
    - 상품 아이템별 가격 변경
    - 상품 아이템별 판매 재개
    - 상품 아이템별 판매 중지
4. 배송/환불 API
    - 발주서 목록 조회(일단위 페이징)
    - 발주서 목록 조회(분단위)
    - 발주서 단건 조회(shipment_box_id)
    - 발주서 단건 조회(order_id)
    - 배송상태 변경 히스토리 조회
    - 상품준비중 처리
    - 송장업로드 처리
    - 송장업데이트 처리
    - 출고중지완료 처리
    - 이미출고 처리
    - 주문 상품 취소 처리
5. 반품 API
    - 반품/취소 요청 목록 조회
    - 반품요청 단건 조회
    - 반품상품 입고 확인 처리
    - 반품요청 승인 처리
    - 반품철회 이력 기간별 조회
    - 반품철회 이력 접수번호로 조회
    - 회수 송장 등록
6. 교환 API
    - 교환요청 목록조회
    - 교환요청상품 입고 확인처리
    - 교환요청 거부 처리
    - 교환상품 송장 업로드 처리
7. 검색
    - 상품검색   

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
