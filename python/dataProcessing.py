import getDataFn as getData

stock_basic = getData.stock_basic()
# print( stock_basic.symbol )

#symbol转ts_code, 000001转000001.sz
def code2ts_code(code):
    return stock_basic.ts_code[stock_basic.symbol==code]
# print( code2lq_code('000001') )