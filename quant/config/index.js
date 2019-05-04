var path = require("path");

var quantPath = path.resolve(__dirname, '../');
var qPath = function(str){
    return quantPath + '/' + str;
};

var config = {
    'root': quantPath,
    'qPath': qPath
};

module.exports = config;