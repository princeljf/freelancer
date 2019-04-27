import tushare as ts
import dataProcessing as DP

#设置token
ts.set_token('667cebb835b7c7c4b92adf730806e90a2b7849ae573eb3a24f1c3a7a')
#初始化pro接口
pro = ts.pro_api()

'''
页面转对象
var subStrBetween = function(str, startStr, endStr){
    var sLength = startStr.length, eLength = endStr.length;
    var startIndex = str.indexOf(startStr) + sLength;
    var endIndex = str.indexOf(endStr) - startIndex;
    var result = str.substr(startIndex, endIndex);
    return result;
};
var content = $('.content').eq(0);
var html = content.html();
var obj = {
    apiName:{
        api: subStrBetween( html, '接口：', '<br>描述：' ),
        describe: subStrBetween( html, '<br>描述：', '</p>' )

    }
};
obj;
'''

tsApi = {
    #指数
    'indexApi':{
        'index_basic':{
            'api': 'index_basic', 'describe': '获取指数基础信息。',
            'input': [
                {'name': 'market', 'type': 'str', 'required': 'Y', 'describe': '交易所或服务商'},
                {'name': 'publisher', 'type': 'str', 'required': 'N', 'describe': '发布商'},
                {'name': 'category', 'type': 'str', 'required': 'N', 'describe': '指数类别'}
            ],
            'output':[
                {'name': 'ts_code', 'type': 'str', 'describe': 'TS代码'},
                {'name': 'name', 'type': 'str', 'describe': '简称'},
                {'name': 'name', 'type': 'str', 'describe': '指数全称'},
                {'name': 'market', 'type': 'str', 'describe': '市场'},
                {'name': 'publisher', 'type': 'str', 'describe': '发布方'},
                {'name': 'index_type', 'type': 'str', 'describe': '指数风格'},
                {'name': 'category', 'type': 'str', 'describe': '指数类别'},
                {'name': 'base_date', 'type': 'str', 'describe': '基期'},
                {'name': 'base_point', 'type': 'float', 'describe': '基点'},
                {'name': 'list_date', 'type': 'str', 'describe': '发布日期'},
                {'name': 'weight_rule', 'type': 'str', 'describe': '加权方式'},
                {'name': 'desc', 'type': 'str', 'describe': '描述'},
                {'name': 'exp_date', 'type': 'str', 'describe': '终止日期'}
            ],
            'map':{
                'market':{
                    'MSCI': 'MSCI指数', 'CSI': '中证指数', 'SSE': '上交所指数', 'SZSE': '深交所指数', 'CICC': '中金所指数', 'SW': '申万指数', 'OTH': '其他指数'
                },
                'category':[
                    '主题指数','规模指数','策略指数','风格指数','综合指数','成长指数','价值指数','有色指数','化工指数','能源指数',
                    '其他指数','外汇指数','基金指数','商品指数','债券指数','行业指数','贵金属指数','农副产品指数','软商品指数','油脂油料指数',
                    '非金属建材指数','煤焦钢矿指数','谷物指数','一级行业指数','二级行业指数','三级行业指数'
                ] 
            }
        }
    }
}


#查询指数基础信息
def index_basic(market, publisher='', category=''):
    return pro.index_basic(market=market, publisher=publisher, category=category)
# print( index_basic('SSE') )

#查询当前所有正常上市交易的股票列表
def stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,exchange,list_date'):
    return pro.stock_basic(exchange=exchange, list_status=list_status, fields=fields)
# print( stock_basic() )

#查询一只股票数据
def code(code, start_date='', end_date=''):
    ts_code = DP.code2ts_code(code)
    return pro.daily(ts_code=ts_code[0], start_date=start_date, end_date=end_date)
# print( code('000001') )
# print( code('000001', '20180101' ,'20190101') )

#查询某一天所有股票数据
def code2date(trade_date):
    return pro.daily(trade_date=trade_date)
# print( code2date('20180810') )

