python爆破域名没有ksubdomain速度快,简单改了下代码使其支持基于ip cname爆破。

1.基于ip
```
./ksubdomain -fip 121.4.186.15 -d sdo.com -o 1.txt
```
2.基于cname
```
./ksubdomain -fc nonexist.sdo.com -d sdo.com -o 1.txt
```
3.简单补充（有些稍微比较复杂，需要手动或者结合其他工具）
```
* 基于黑名单title过滤
* 部分多级域名泛解析
* 部分一级域名泛解析,但是二级的该域名查不到,例如1.wildcard.com指向泛解析 但是2.1.wildcard.com是真实域名(结合api等找寻域名)
* 之前跑过一些黑名单的ip或者域名,有需要自取black_ip_cname.py
* 参考 https://github.com/knownsec/ksubdomain/issues/20
......
```

git commit -m  'update'


~/python/scanner3/thirdtools/scan_linux  --max-retries=0  -i en0 -p 22 --probe-file ~/python/scanner3/thirdtools/probe.db --target-file /tmp/portscan_input_2021-05-13_ebbceoph.txt -r 6666 --output-filename-service-scan=/tmp/11.txt  --output-filename-port-scan /tmp/22.txt



def api(request, logtype, udomain, hashstr,del):
    apistatus = False
    host = "%s.%s." % (hashstr, udomain)
    if logtype == 'dns':
        res = DNSLog.objects.filter(host__contains=host)
        if del:
          res.delete()
        if len(res) > 0:
            apistatus = True
    elif logtype == 'web':
        res = WebLog.objects.filter(path__contains=host)
        if del:
            res.delete()
        if len(res) > 0:
            apistatus = True
    else:
        return HttpResponseRedirect('/')
    return render(request, 'api.html', {'apistatus': apistatus})