--查看当前数据库
select database();

--创建一个数据库
create database if not exists ftp_info;

--选择一个数据库
use ftp_info;
-- 创建用户表
CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- 创建文件表
CREATE TABLE files (
    id INT(11) NOT NULL AUTO_INCREMENT,
    filename VARCHAR(50) NOT NULL,
    filepath VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- 创建下载日志表
CREATE TABLE downloads (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    filename VARCHAR(50) NOT NULL,
    op VARCHAR(50) NOT NULL,
    time VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);


--设置最大连接数
SET GLOBAL max_connections =100;



DROP TABLE IF EXISTS downloads;