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

#### 1.5 null和undefined

null表示一个“空”的值，它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空”。

在其他语言中，也有类似JavaScript的null的表示，例如Java也用null，Swift用nil，Python用None表示。但是，在JavaScript中，还有一个和null类似的undefined，它表示“未定义”。

JavaScript的设计者希望用null表示一个空的值，而undefined表示值未定义。事实证明，这并没有什么卵用，区分两者的意义不大。大多数情况下，我们都应该用null。undefined仅仅在判断函数参数是否传递的情况下有用。


#### 1.6 数组

数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括任意数据类型。例如：

```javascript
[1, 2, 3.14, 'Hello', null, false, true]

```
上述数组包含6个元素。数组用[]表示，元素之间用,分隔。

另一种创建数组的方法是通过Array()函数实现：

```javascript
new Array(1, 2, 3) //创建了数组 [1, 2, 3]
```
然而，出于代码的可读性考虑，强烈建议直接使用[]。

数组的元素可以通过索引来访问。请注意，索引的起始值为0：

```javascript
var arr = [1, 2, 3.14, 'Hello', null, true];
arr[0]; // 返回索引为0的元素，即1
arr[5]; // 返回索引为5的元素，即true
arr[6]; // 索引超出了范围，返回undefined
```

#### 1.7 对象

JavaScript的对象是一组由键-值组成的无序集合，例如：
```javascript
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
```
JavaScript对象的键都是字符串类型，值可以是任意数据类型。上述person对象一共定义了6个键值对，其中每个键又称为对象的属性，例如，person的name属性为'Bob'，zipcode属性为null。

要获取一个对象的属性，我们用对象变量.属性名的方式：

```javascript
person.name; // 'Bob'
person.zipcode; // null
```

### 2. 字符串操作

1. `toUpperCase()`把一个字符串全部变为大写：
2. `toLowerCase()`把一个字符串全部变为小写：
3. `indexOf()`会搜索指定字符串出现的位置：
4. `substring()`返回指定索引区间的子串：













