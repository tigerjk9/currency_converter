from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip') # 최신 환율 정보로 업데이트하기
print(cc.convert(1,'USD','KRW')) # 1달러를 원화로 변경할 때 금액 출력하기