
function test(x){
    console.log('x = ' + x)
    for(var i=0; i < arguments.length; i++){
        console.log('arg ' + i + '=' + arguments[i])
    }
}

test(10, 20, 30, 40)
// console.log(i)

// alert('外部引入文件。');
/*
var x = 100;

console.log(x)

console.log('zhgs\nlsjfl\nlsjflsj')
*/

// var name = "小明";
// var age = 19;
// // var message = '你好' + name + '你的年龄' + age + '岁了！';
// // console.log(message);


// var mess = '你好 ${name} 你今年已经${age}岁了，该上学了小伙，哈哈哈哈哈'
// console.log(mess);

// var len = "Hello, world!"
// console.log(len.length)

// console.log(len[5])

// if (2 > 1) {
//     console.log('True')
// } else {
//     console.log('False')
// }

// if (1 == '1') {
//     console.log('True' + '与上面区分')
// } else {
//     console.log('False' + '与上面区分')
// }



// name = 'angela'
// na = name.toUpperCase()
// console.log(na)
// console.log(name.toLowerCase())

/*
var ren = {
    name: 'xiaoming',
    'age': 18,
    'birth': 1990,
    'height': 1.70,
    'weight': 65,
    score: null,
    'middle-school': 'No.1 Middle School'
}

console.log(ren.name)
console.log(ren.age)
console.log(ren.height)
console.log(ren.score)
console.log(ren["middle-school"])

console.log('is' in ren)

var x = 1;
var i;
for (i = 1; i < 11; i ++){
    console.log(i)
    console.log('----------')
    console.log(i * i++)
    // x = x * i++
    // console.log(i * i++)
}
// console.log(x)

*/


// var s = ['a', 'b', 'c']

// for(i in s){
//     console.log(i)
//     console.log(s[i])
// }


// var arr = ['Bart', 'Lisa', 'Adam'];

// for(i in arr){
//     console.log('hello, ' + arr[i])
//     console.log('hello, ' + i)
// }

// for(i=0; i < arr.length; i++){
//     console.log(arr[i])
// }

// 'use strict';
// var m = new Map();
// var s = new Set();
// console.log('你的浏览器支持Map和Set！');


// key = {
//     1: 'jslfe',
//     2: 'fjels',
// }

// console.log(key[1])



// var m = new Map([['zhangsan', 99], ['lisi', 89], ['wangwu', 98]])

// console.log(m.get('zhangsan'))



// var a = ['A', 'B', 'C'];
// var s = new Set(['A', 'B', 'C']);
// var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
// for (var x of a) { // 遍历Array
//     console.log(x);
// }
// for (var x of s) { // 遍历Set
//     console.log(x);
// }
// for (var x of m) { // 遍历Map
//     console.log(x[0] + '=' + x[1]);
// }




