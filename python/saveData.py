import queryDataFn as queryData
import saveDataFn as saveData

#查询当前所有正常上市交易的股票列表
# df = queryData.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,exchange,list_date')
# saveData.stock_basic(df)

#查询一只股票数据
# code = '000001'
# df = queryData.code('000001')
# saveData.code(code, df)

#保存指数基本信息
saveData.index_basic(queryData.index_basic)
