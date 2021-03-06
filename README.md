## 项目名：猫耳影评网


### 开发环境：
	antiorm==1.2.1
	db-sqlite3==0.0.1
	Django==1.11
	django-ckeditor==5.6.1
	django-js-asset==1.1.0
	mysqlclient==1.3.12
	Pillow==5.1.0
	pytz==2018.4
	Python==3.6
	Mysql==5.7.21
	Redis==3.2.12
	Nginx==1.12.2

### 数据
利用Python多线程爬虫网上数据并进行清洗，将数据格式与Django的字段类型以及外键关系做正确转化，再将数据存入Mysql数据库中。主要使用了request、beautifulsoup、threading、re模块来进行爬取数据，pymysql模块入库。
 
  
### 功能
#####  1、登录
登录过程中使用到的验证码，使用Ajax加载，调用后端的api，加载验证码，将验证码存入session中，校验验证码直接从session中取出与用户输入的前端验证码进行校验。
![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E7%99%BB%E5%BD%95.png?raw=true)
#####  2、注册
注册时使用Ajax动态加载，对用户输入的数据进行前端初步验证：输入是否合法，用户名是否重复等，手机验证码利用云之讯平台，调用其接口实现向用户发送验证码，由于需要具有时效性，因此服务端将验证码存入redis数据库，校验时从redis数据库中取出校验即可。
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E6%B3%A8%E5%86%8C.png?raw=true)
##### 3、主页
主页上半部分由轮播图组成，下半部分分页显示全部的电影信息，当鼠标放在电影海报上，将提示电影的基本信息。
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E4%B8%BB%E9%A1%B5.png?raw=true)
##### 4、分类
影片分类与高分经典主要是通过视图函数的查询，将获取结果返回给前端。
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E5%88%86%E7%B1%BB.png?raw=true)
##### 5、搜索
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E6%90%9C%E7%B4%A2.png?raw=true)
##### 6、页面跳转
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E5%BD%B1%E8%AF%84%E5%88%97%E8%A1%A8.png?raw=true)
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E5%BD%B1%E8%AF%84%E6%96%87%E7%AB%A0.png?raw=true)
##### 7、提交
该界面必须登录用户才可以访问，在前段和后端都验证成功即可提交。提交成功则入库成功。即可进入想应的电影页面进行查看自己的影评
 ![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E5%8F%91%E8%A1%A8.png?raw=true)
##### 8、用户中心
主要定制用户的个人界面，目前只做了修改密码功能，例如上传、修改头像，展示用户收藏以及发表的影评等功能尚未完成。
![](https://github.com/LiuLiRongLyon/maoer/blob/master/%E7%BD%91%E7%AB%99%E6%88%AA%E5%9B%BE/%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83.png?raw=true)


### 部署
使用Linux服务器运维该项目，使用gunicorn启动Django，使用supervisor监控gunicorn，将该项目部署上线。


### 联系方式
QQ：940757154






