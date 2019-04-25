## JavaScript

### 1. 数据类型

#### 1.1 Number

JavaScript不区分整数和浮点数，统一用Number表示，以下都是合法的Number类型：

```javascript

123; //整数
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
```

#### 1.2 布尔值

```JavaScript
true  
false

```

#### 1.3 运算

```javascript

&& // and 与运算
|| // or  或运算
!  // not 非运算
```

#### 1.4 比价运算

要特别注意相等运算符==。JavaScript在设计时，有两种比较运算符：

第一种是==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

第二种是===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较。

由于JavaScript这个设计缺陷，不要使用==比较，始终坚持使用===比较。

isNaN(): 判断NaN 是能使用isNaN 使用 if NaN == NaN 返回 false。












