#生成 json 格式文件
def to_json(df, path_or_buf, orient, force_ascii=True):
    df.to_json(path_or_buf, orient, force_ascii)

#生成 股票列表 数据
def index_basic(queryFn, marketArr=['MSCI','CSI','SSE','SZSE','CICC','SW','CNI','OTH'], path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/index_basic/', orient='records'):
    index = {}
    for market in marketArr:
        path_or_buf = path + market + '_' + orient + '.json'
        index[market] = queryFn(market)
        to_json(index[market],path_or_buf,orient)
# print( index_basic() )

#生成 股票列表 数据
def stock_basic(df, path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/stock_basic/', orientArr=['columns','records','index','split','values'], force_ascii=True):
    for orient in orientArr:
        path_or_buf = path + orient + '.json'
        to_json(df,path_or_buf,orient,force_ascii)
# print( stock_basic() )

#生成 一只股票 数据
def code(code, df, path='/Users/liujunfan/princeljf/node_lhh/lhh/src/datas/code/', orient='records', force_ascii=True):
    path_or_buf = path + orient + '/' + code + '.json'
    to_json(df,path_or_buf,orient,force_ascii)
# print( code() )