# FlaskNotes

Flask Nots

## 第一章：

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

## 第二章：

介绍：