var mongoose = require("mongoose"); //引入mongoose
mongoose.connect('mongodb://localhost:27017/pyspider_resultdb'); //连接到mongoDB的pyspider_resultdb数据库
//该地址格式：mongodb://[username:password@]host:port/database[?options]
//默认port为27017 

// var TS = require('../modules/tusharePro');

var db = mongoose.connection;
db.on('error', function callback() { //监听是否有异常
    console.log("Mongodb Connection Error!!!");
});
db.once('open', function callback() { //监听一次打开
    //在这里创建你的模式和模型
    console.log('Mongodb Connected!');
});

// TS.tusharePro.find(function(err, docs){
//     console.log('tusharePro',docs);
// });

module.exports = mongoose;