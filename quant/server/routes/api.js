var express = require('express');
var router = express.Router();

var config = require('../../config/index');
var TS = require( config.qPath('modules/tusharePro') );

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

//返回tusharePro网站接口数据
router.get('/getTushareProApi', function(req, res, next) {
  TS.tusharePro.find(function(err, docs){
      res.json(docs);
  }); 
});
module.exports = router;