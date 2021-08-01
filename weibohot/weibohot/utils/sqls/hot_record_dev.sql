/*
Navicat MySQL Data Transfer

Source Server         : jingjianqian
Source Server Version : 50728
Source Host           : 39.104.205.172:3306
Source Database       : weibo_hot

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2021-08-01 11:47:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hot_record_dev
-- ----------------------------
DROP TABLE IF EXISTS `hot_record_dev`;
CREATE TABLE `hot_record_dev` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `temp_index` varchar(255) NOT NULL COMMENT '排序',
  `title` varchar(255) NOT NULL COMMENT '热搜名_关键字_标题',
  `hit` varchar(255) DEFAULT NULL COMMENT '点击数',
  `type` varchar(255) DEFAULT NULL COMMENT '类型',
  `date` datetime(6) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '热搜时间',
  `href` varchar(255) DEFAULT NULL,
  `hot_details` mediumblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
