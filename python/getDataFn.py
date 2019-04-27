import pandas as pd

#读取 json 格式文件
def read_json(path_or_buf, dtype='string'):
    return pd.read_json(path_or_buf, dtype=dtype)
# print( read_json() )

#读取 指数列表 数据
def index_basic(marketArr=['MSCI','CSI','SSE','SZSE','CICC','SW','CNI','OTH'], path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/index_basic/', orient='records'):
    index = {}
    for market in marketArr:
        path_or_buf = path + market + '_' + orient + '.json'
        index[market] = read_json(path_or_buf,dtype='string')
    return index
# print( index_basic() )

#读取 股票列表 数据
def stock_basic(path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/stock_basic/', orient='records'):
    path_or_buf = path + orient + '.json'
    return read_json(path_or_buf,dtype='string')
# print( stock_basic() )

#读取 一只股票 数据
def code(code, path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/code/', orient='records'):
    path_or_buf = path + orient + '/' + code + '.json'
    return read_json(path_or_buf,dtype='string')
# print( code('000001') )