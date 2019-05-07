function windows_style(){
    var height = screen.availHeight
    var width = screen.availWidth
    // alert(height, width)
    if (height > width){
        console.log('使用的是手机浏览器')
        // console.log(navigator.webdriver)
    }else{
        console.log('使用的是电脑浏览器')
    }
    console.log('高度:' + height + '\n' + '宽度:' + width)
    console.log('测试使用外部js文件是否可用！')
}
windows_style()