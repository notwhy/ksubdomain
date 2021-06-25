python爆破域名没有ksubdomain速度快,简单改了下代码使其支持基于ip cname爆破。

1.基于ip
```
./ksubdomain -fip 121.4.186.15 -d sdo.com -o 1.txt
```
2.基于cname
```
./ksubdomain -fc nonexist.sdo.com -d sdo.com -o 1.txt
```
3.基于http字符串返回
```
cat mogu.txt | httpx -filter-string 店铺不存在 -title -status-code
```
4.简单补充（有些稍微比较复杂，需要手动或者结合其他工具）
```
* 部分多级域名泛解析(单独跑)
* 部分一级域名泛解析,但是二级的该域名查不到,例如1.wildcard.com指向泛解析 但是2.1.wildcard.com是真实域名(结合api等找寻域名)
* 扫描时如果你不主动指定排除的条件 就会导致一直发包 比如1.wildcard.com为泛解析域名 对1.wildcard.com进行递归子域名扫描就会出问题
......
```
