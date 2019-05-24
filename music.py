import requests


url = "http://music.zhuolin.wang/api.php?callback=jQuery11130487793109583637_1558602345564"
header = requests.get(url)
t = header.json()
print(t)