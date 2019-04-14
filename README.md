# FlaskNotes

Flask Nots

## 第一章： Flask入门

### URL详解

URL是Uniform Resource Locator的简写，统一资源定位符

```python
scheme://host:post/path/?query-string=xxx#anchor
```

- scheme: 代表的是访问的协议，一般为HTTP或者HTTPS以及tfp等
- host: 主机名、域名，比如：www.baidu.com
- post: 端口号，当你访问一个网站的时候，浏览器默认使用80端口。
- path: 查找路径，比如：www.jianshu.com/trending/now, 后面的trending/now就是路径
- ？query-string: 查询字符串，比如：www.baidu.com/?wd=python, 后面的wd=python就是查询字符串
- anchor: 锚点，后台一般不用管，前段用来做页面的定位，比如：www.baidu.com/item/xxx/xxx?fr=XXX#7

### Flask简介

Flask是一个非常流行的python web框架，出生于2010年，作者是Armin Ronacher, 本来这个项目只是作者愚人节的一个玩笑，后来由于非常受欢迎，进而成为一个正式的项目。

Flask自2010年发布第一版依赖，大受欢迎，深受开发者的喜爱，并且在多个公司已经得到了应用。Flask能够如此流行的原因，可以分为以下几点：

- 微框架，简洁，只做他需要做的，给开发者提供了很大的扩展性。
- Flask和相关的依赖设计的非常优秀，用起来很爽
- 开发效率非常高，比如：SQLAlchemy的ORM操作数据库可以节省大量书写sql的时间。
- 社会活跃度非常高

Flask的灵活度非常之高，他不会帮你做太多的决策，即使已经帮你做出了选择，你也能非常用以更换成你需要的，比如：

- 使用Flask开发数据库时，具体使用SQLAlchemy 还是MogoEngine或者是不用ORM而是直接基于MYSQL-Pyton这样的底层驱动进行开发都是可以的。选择权完全掌握在你自己的手中，区别于Django， Django内置了非常完善和丰富的功能，并且加入如果你想替换成你自己想要的，要么不支持，要么非常麻烦。
- 把默认的Jinjia2模板引擎替换成Mako引擎或者是其他模板引擎是非常容易的。



## 第二章：

介绍：