# cookies and session

## cookies

### 介绍

在网站中，HTTP请求是无状态的。也就是说即使第一次使用和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求的是哪个用户。cookie的出现就是为了解决这个问题，第一次登录后服务器返回一些数据(cookie)给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个。cookie存储的数据量有限，不同的浏览器有不同的存储大小。单一般不超过40kb。因此使用cookie只能存储一些小量的数据。

1. cookie有有效期：服务器可以设置cookie的有效期，以后浏览器会自动的清除过期的cookie。
2. cookie有域名的概念：只有访问同一个域名，才会把之前相同域名返回的cookie携带给服务器。也就是说，访问Google的时候，不会把baidu的cookie发送给Google。

### flask操作cookie

1. 设置cookie：设置cookie是应该在 Response 的对象上设置。 flask.Response 对象有一个 set_cookie 方法， 可以通过这个方法来设置 cookie 信息。
2. 删除cookie：通过 Response.delete_cookie 指定删除的key，就可以删除了
3. 设置cookie的有效时间：
   1. max_age：以秒为单位，距离现在多少秒后 cookie 会过期。
   2. expires：是datetime类型，这个时间需要设置为格林尼治时间，也就是要距离北京少8个小时的时间。
   3. 如果max_age和expires都设置了，那么这个时候已 max_age 为准
   4. max_age在IE8以下的浏览器是不支持的，expires 虽然在新版的HTTP协议中是被废弃了，但是到目前为止，多有的浏览器都还是能够支持，所以如果想要兼容ie8以下的浏览器，那么应该使用expires，否则可以使用 max_age
   5. 默认的过期时间：如果没有显示的指定过期时间，那么这个cookie将会在浏览器关闭后过期。
4. 设置cookie的有效域名： 
