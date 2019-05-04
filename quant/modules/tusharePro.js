var mongoose = require("mongoose");

var Schema = mongoose.Schema;

var tushareProApiSchema = new Schema({
    api: [{}]
});
var tusharePro = mongoose.model('tusharePro', tushareProApiSchema, 'tusharePro');

var TS = tusharePro = {
    tusharePro: tusharePro
};
module.exports = TS;