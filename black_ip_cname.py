#!/usr/bin/env python
# -*- encoding: utf-8 -*-

black_dict = {
    'zto.com': {
        'ip': {
            'xingruan.zto.cn': ['115.231.17.15'],
            'zto.sg': ['203.175.174.7']
        },
        'cname': {
            'zto.sg': ['zto.sg']
        }
    },
    'baidu.com': {
        'ip': {
            'baeapps.com': ['182.61.62.50'],
        },
        'cname': {
            'baeapps.com': ['domain-offline.baidu.com']
        }
    },
    'jd.com': {
        'ip': {
            'jdcloud-openapi.com': ['101.124.17.23,101.124.12.131'],
            'jd.shop': ['120.52.148.114,36.110.181.192,111.13.28.89'],
            'joybuy.com': ['202.77.129.189'],
        },
        'cname': {
            '360buy.com': ['160923000752.360buy.com.gslb.qianxun.com'],
            'jdcloud-api.com': ['180530202328.jdcloud-api.com.jcloudlb.com,191217140944.jcloudec.com.jcloudlb.com']
            
        }
    },
    'https://itslearning.com/global/your-data-matters/responsible-disclosure/': {
        'ip': {
            'aaasdsda.itslearning.com': ['104.16.102.21'],
        },
        'cname': {
        }
    },
    'ximalaya.com': {
        'ip': {
            'asddasdasda.qingxuetang.com': ['61.172.194.143']
        },
        'cname': {
            'xmcdn.com': ['wsall.xmcdn.com.cdn20.com'],
            'dasadaaa.xiaoyastar.com': ['qkadtjfi.sched.d0.tdnsv5.com']
            
        }
    },
    'megvii.com': {
        'ip': {
            'xingrua.koalacam.net': ['101.201.171.88'],
            'xo.megvii.com': ['60.205.120.33'],
            'zoonek2.faceplusplus.com.cn': ['60.205.132.121']
            
        },
        'cname': {
            'zonafringe.faceplusplus.com': ['www-1216800532.ca-central-1.elb.amazonaws.com']
        }
    },
    'paypal.com': {
        'ip': {
            'venmo.com': ['54.173.217.72,52.71.175.48,52.4.45.40,54.152.19.176'],
        }
    },
    'https://hackerone.com/shopify': {
        'ip': {
        },
        'cname': {
            '23-227-36-100.shopify.com': ['wc.shopify.com']
        }
    },
    'https://hackerone.com/innogames': {
        'ip': {
            'innogames.com': ['212.48.98.12'],
        },
        'cname': {
            'forgeofempires.com': ['gmrs.innogames.de']
        }
    },
    'https://hackerone.com/qiwi': {
        'ip': {
            'flocktory.com': ['52.18.135.124,34.249.11.93,54.154.151.82,52.48.251.121'],
        },
        'cname': {
        }
    },
    'https://hackerone.com/statuspage': {
        'ip': {
            'statuspage.io': ['52.215.192.133'],
            's2tatuspage.io': ['52.215.192.131'],
            
        },
        'cname': {
            'statuspage.io': ['elb-status-us.statuspage.io']
        }
    },
    'https://hackerone.com/pixiv': {
        'ip': {
            'booth.pm': ['210.140.131.248,210.140.131.242,210.140.131.244,210.140.131.246'],
        },
        'cname': {
        }
    },
    'https://explore.researchgate.net/display/support/Security+and+vulnerability': {
        'ip': {
            'researchgate.net': ['209.15.209.74,209.15.209.75,209.15.209.72,209.15.209.70'],
        },
        'cname': {
        }
    },
    'https://hackerone.com/vkcom': {
        'ip': {
            'cs608920.vk.me': ['87.240.129.187,87.240.190.64'],
            'cs608921.vk.me': ['87.240.190.64,87.240.129.187'],
            
        },
        'cname': {
        }
    },
    'facebook.com': {
        'ip': {
            'journal.beatgames.com': ['37.9.175.19'],
            'beatsaber2.com': ['37.9.175.13']
            
        },
        'cname': {
            'gungun1.facebookhome.ru': ['star.c10r.facebook.com']
        }
    },
    'apple.com': {
        'ip': {
            'iphone5.com': ['165.160.13.20,165.160.15.20'],
            'gotochinashopping.com': ['156.234.180.98'],
            'gotochinashopping.com': ['156.234.180.98'],
            'apple-downloads.com': ['17.168.114.155'],
            'ibook.com': ['165.160.15.20'],
            'apples-stores.com': ['195.186.208.193']
            
        },
        'cname': {
            'apple-hk.com': ['apple-hk.com'],
            'applemanager.com': ['school-apple.com'],
            'appke.com': ['appke.com']
        }
    },
    'paypal.com': {
        'ip': {
            'venmo.com': ['52.4.45.40,52.71.175.48,54.152.19.176,54.173.217.72'],
        },
        'cname': {
        }
    },
    'meituan.com': {
        'ip': {
            'zuitu.com': ['140.143.51.240']
        },
        'cname': {}
    },
    'hackerone.com': {
        'ip': {
            'mail.ru': ['217.69.139.87,94.100.180.87'],
            'quora.com': ['157.240.8.41'],
            'tesla.services': ['72.52.10.14'],
            'api.dailymotion.com': ['31.13.92.35'],
            'periscope.tv': ['88.191.249.182'],
            'adobeaemcloud.com': ['151.101.231.10'],
            'browser.cloud.com': ['31.13.66.23'],
            'base.de': ['213.95.38.173'],
            'developer.cloud.com': ['148.163.48.215'],
            'vk.cc': ['87.240.190.64,87.240.129.187'],
            'acrobat.com': ['192.243.241.135'],
            'livestream.com': ['202.160.128.16'],
            'binance.com': ['118.193.240.37'],
            'tmall.com': ['203.119.169.18'],
            'duckduckgo.com': ['104.31.142.88'],
            'netzclub.net': ['87.79.3.108'],
            'wordpress.net': ['66.155.40.164'],
            'staging-airtableblocks.com': ['18.215.119.149,34.238.101.99'],
            'line.naver.jp': ['31.13.95.17'],
            'betfair.com': ['84.20.210.33'],
            'pscp.tv': ['108.160.169.181'],
            'tweakers.net': ['213.239.154.30,31.22.80.152,213.239.154.31'],
            'flickr.com': ['31.13.84.34'],
            'speakap.com': ['83.149.119.8'],
            'monster.no': ['208.71.193.147'],
            'sameroom.io': ['18.215.105.249,18.210.31.97,34.195.251.200'],
            'semrush.com': ['104.17.153.1,104.17.154.1'],
            'buddypress.org': ['198.143.164.252'],
            'aliexpress.com': ['106.11.47.43'],
            'ok.ru': ['114.43.24.59'],
            'nordvpn.com': ['108.160.172.200'],
            'new.livestream.com': ['128.121.146.101'],
            'vhx.tv': ['54.235.93.80,23.21.105.212,50.16.193.214'],
            'twago.es': ['144.76.39.130'],
            'volkskrant.nl': ['157.240.1.9'],
            'prod.cloud.netflix.com': ['52.89.124.203,54.148.37.5,34.210.42.111'],
            'apisoundcloud.com': ['108.160.170.33'],
            'urbandictionary.com': ['74.86.142.55'],
            'tzero.com': ['104.18.185.23,104.18.188.23,104.18.189.23,104.18.187.23,104.18.186.23'],
            'manywho.com': ['18.204.152.134,3.217.108.151,52.70.122.214'],
            'dailymotion.com': ['157.240.17.50'],
            'naspers.co.in': ['165.160.13.20,165.160.15.20'],
            'norma-mobil.de': ['194.245.170.18'],
            'web-security-academy.net': ['18.200.141.238'],
            'twago.de': ['144.76.39.130'],
            'zendesk.com': ['162.159.128.7,162.159.138.6'],
            'highwebmedia.com': ['64.38.230.2'],
            'taobao.com': ['203.119.169.17'],
            'mycontactual.com': ['52.8.202.129'],
            'vk.com': ['87.240.190.78,87.240.190.72,87.240.137.158,87.240.139.194,87.240.190.67,93.186.225.208'],
            'pinterest.com': ['208.43.237.140'],
            'tumblr.com': ['103.246.246.144'],
            'cloud.vimeo.com': ['157.240.15.8'],
            'flocktory.com': ['52.209.217.27,52.51.37.61,52.16.27.189,99.80.114.232'],
            'jimdosite.com': ['108.128.204.189,52.50.104.40,52.214.219.69,54.229.198.190'],
            'trouw.nl': ['31.13.75.12'],
            'tweakblogs.net': ['213.239.154.31'],
            '1688.com': ['203.119.169.166'],
            'bitmex.com': ['31.13.95.37'],
            'wordpress.org': ['198.143.164.252'],
            'twitter.com': ['162.125.7.1'],
            'hs-sites.com': ['104.16.116.104,104.16.113.104,104.16.115.104,104.16.117.104,104.16.114.104'],
            'urbanup.com': ['35.188.229.180'],
            'line-apps.com': ['203.98.7.65'],
            'challonge.com': ['202.160.128.14'],
            'twago.fr': ['144.76.39.130'],
            'vimeo.com': ['179.60.193.9'],
            'naspers.co': ['165.160.15.20,165.160.13.20'],
            'srvcs.tumblr.com': ['31.13.68.22'],
            '8x8.vc': ['44.237.22.53,54.191.4.127'],
            'vivy.com': ['3.122.58.103,52.59.131.169,18.193.141.92'],
            'tweakimg.net': ['213.239.154.30'],
            'wordcamp.org': ['198.143.164.106'],
            'sandbox.directly.com': ['3.221.224.5,3.211.110.114'],
            'gulp.ch': ['52.17.15.217,52.31.147.123'],
            'sip.twilio.com': ['54.172.60.0,54.172.60.2,54.172.60.1,54.172.60.3'],
            'forum.ibood.com': ['34.102.172.225'],
            'vine.co': ['31.13.67.33'],
            'risesmart.com': ['54.87.238.50,54.85.22.140'],
            'twago.it': ['144.76.39.130'],
            'binary.com': ['192.133.77.59'],
            'jimdofree.com': [
                '54.171.94.77,52.213.24.106,54.72.122.12,34.247.223.189,52.48.165.245,54.194.187.236,52.49.55.14,52.209.209.208'],
            'mein.simfinity.de': ['194.245.166.8'],
            'myndr.nl': ['149.210.195.149'],
            'dev.blockchain.info': ['35.201.64.161'],
            'yelo.be': ['213.224.149.248'],
            'naspers.fr': ['165.160.15.20,165.160.13.20'],
            'expressvpn.com': ['249.129.46.48'],
            'line.me': ['118.184.26.113'],
            'spotifyforbrands.com': ['172.217.160.115'],
            'naspers.us': ['165.160.15.20,165.160.13.20'],
            'alditalk-kundenbetreuung.de': ['194.245.166.2'],
            'vk.me': ['87.240.190.64,87.240.129.187'],
            'randstadrisesmart.com': ['54.85.22.140,54.87.238.50'],
            'shopify.com': ['23.227.38.64'],
            'innogames.com': ['212.48.98.12'],
            'upserve.com': ['34.231.80.4'],
            'statuspage.io': ['52.215.192.131'],
            'europe-west1.dev.blockchain.info': ['35.201.64.161'],
            'ratelimited.me': ['172.67.182.143,104.18.44.170,104.18.45.170'],
            'tt.omtrdc.net': ['13.250.75.226,54.151.139.123,52.221.145.65,52.220.44.99'],
            '8x8.com': ['52.8.202.129'],
            'contactnow.8x8.com': ['52.8.202.129'],
            'monster.dk': ['208.71.193.147'],
            'vcc-8x8.com': ['35.205.61.67']
        },
        'cname': {
            'upserve.com': ['redirect.upserve.com'],
            'my.com': ['my.com'],
            'jimdosite.com': [
                'web.jimdosite.com,dolphin-renderserve-prod.jimdo-platform.net,dolphin-render-ce5083-1529577379-1289163597.eu-west-1.elb.amazonaws.com'],
            'adobeaemcloud.com': ['adobe-aem.map.fastly.net'],
            'jimdofree.com': [
                'web.jimdo.com,web-prod.jimdo-platform.net,web-prod-3fab4a-1499954829-1392918184.eu-west-1.elb.amazonaws.com'],
            'vhx.tv': ['toyama-4893.herokussl.com,elb052863-618370844.us-east-1.elb.amazonaws.com'],
            'acrobat.com': ['redirect.acrobat.com'],
            'prod.cloud.netflix.com': [
                'prod.cloud.dradis.netflix.com,prod.cloud.us-west-2.internal.dradis.netflix.com,dualstack.apiproxy-device-prod-http-nlb-86bcd7bf0017d79e.elb.us-west-2.amazonaws.com'],
            'betfair.es': ['redirect.betfair.com,rdr.lb.betfair.com,ie2-rdr.betfair.com'],
            'risesmart.com': ['apps-na1.risesmartapps.com,apps-na1-external-alb-79711611.us-east-1.elb.amazonaws.com'],
            'wordpress.net': ['wordpress.net'],
            'spotifyforbrands.com': ['ghs.googlehosted.com'],
            'wordpress.org': ['wordpress.org'],
            'alditalk-kundenbetreuung.de': ['alditalk-kundenbetreuung.de'],
            'betfair.ro': ['redirect.betfair.ro,redirect.betfair.com,rdr.lb.betfair.com,ie2-rdr.betfair.com'],
            'betfair.com': ['rdr.lb.betfair.com,ie2-rdr.betfair.com'],
            'randstadrisesmart.com': [
                'apps-na1.risesmartapps.com,apps-na1-external-alb-79711611.us-east-1.elb.amazonaws.com'],
            'shopify.com': ['wc.shopify.com'],
            'challonge.com': ['k8b7e9t2.stackpathcdn.com'],
            'statuspage.io': ['elb-status-us.statuspage.io'],
            'taobao.com': [
                'shop.taobao.com,na61-na62.wagbridge.alibaba.taobao.com,na61-na62.wagbridge.alibaba.taobao.com.gds.alibabadns.com'],
            'mycontactual.com': ['8x8.com'],
            'ratelimited.me': ['owo.rl.wtf'],
            'monster.no': ['redirector.gslb.monster.com'],
            'wordcamp.org': ['wordcamp.org'],
            'sameroom.io': ['sameroom.io'],
            'gulp.ch': ['www.gulp.ch'],
            'buddypress.org': ['buddypress.org'],
            'monster.dk': ['redirector.gslb.monster.com'],
            'aliexpress.com': [
                'adnswildcardproxy.aliexpress.com,hz-aebridge.aliexpress.com,hz-aebridge.aliexpress.com.gds.alibabadns.com']
        }
    },
    'meizu.com': {
        'ip': {
            'meizu.com': ['115.28.238.198'],
            'flyme.cn': ['14.152.79.198'],
            'meizu.cn': ['115.28.238.198']
        },
        'cname': {}
    },
    'mi.com': {
        'ip': {
            'miliao.com': ['203.100.92.21']
        },
        'cname': {
            'miliao.com': ['www.miliao.com,site.static.g.mi.com']
        }
    },
    'https://clickup.com/bug-bounty': {
        'ip': {
        },
        'cname': {
            'clickup.com': ['app.clickup.com']
        }
    },
    'https://hackerone.com/paddypowerbetfair': {
        'ip': {
            'betfair.com': ['84.20.210.33', '84.20.208.107']
        },
        'cname': {
            'betfair.com': ['rdr.lb.betfair.com']
        }
    },
    'https://hackerone.com/mailru': {
        'ip': {
            'delivery-club.ru': ['128.140.175.205', '128.140.175.206'],
            'zakazaka.ru': ['128.140.175.214', '128.140.175.215', '217.69.139.87,94.100.180.87',
                            '95.163.215.5,95.163.181.225', '217.69.139.203']
            
        },
        'cname': {
        }
    },
    'https://hackerone.com/spotify': {
        'ip': {
        },
        'cname': {
            'spotifyjobs.com': ['ghs.googlehosted.com']
        }
    },
    'zhaopin.com': {
        'ip': {
            'highpin.cn': ['39.107.197.2'],
            'zhaopin.com': ['124.236.32.117,106.117.252.243'],
            'zhaopin.cn': ['124.236.32.117,106.117.252.243']
        },
        'cname': {
            'highpin.cn': ['ddooak4inmfjx0alxqando9prittfmam.aliyundunwaf.com'],
            'zhaopin.com': ['feac3f65.zhaopin.com.cdn.dnsv1.com,763807.s1txipv6.cdntip.com'],
            'zhaopin.cn': ['df6113df.zhaopin.cn.cdn.dnsv1.com,665798.s1txipv6.cdntip.com']
        }
    },
    'jj.cn': {
        'ip': {
            'jj.cn': ['115.182.2.84']
        },
        'cname': {}
    },
    'kuaishou.com': {
        'ip': {
            'kuaishou.cn': ['123.56.237.178,203.107.47.98'],
            'kuaishou.com': ['64.33.88.161,203.161.230.171,4.36.66.178']
            
        },
        'cname': {}
    },
    'sangfor.com': {
        'ip': {
            'sangfor.com.cn': ['113.105.88.225']
        },
        'cname': {
            'sangfor.com.cn': ['site.sangfor.com.cn']
        }
    },
    'baidu.com': {
        'ip': {
            'yjs-cdn3.com': ['150.138.151.207'],
            'smartapps.cn': ['180.149.144.114'],
            'aipage.com': ['14.215.177.111']
        },
        'cname': {
            'yjs-cdn3.com': ['yjs-any.yjs-cdn3.com.cname.yunjiasu-cdn.net'],
            'smartapps.cn': ['smartapp.n.shifen.com'],
            'aipage.com': ['gz01.aipage.baidu-itm.com']
        }
    },
    'aliyun.com': {
        'ip': {
            'fliggy.com': ['203.119.169.224'],
            'uueasy.com': ['165.160.15.20,165.160.13.20'],
            'xianzhi.com': ['45.207.58.181'],
            'qutao.com': ['165.160.13.20,165.160.15.20'],
            'alitrip.com': ['140.205.248.8,140.205.61.87,106.11.248.2,106.11.61.141'],
            'aliyuniot.com': ['165.160.13.20,165.160.15.20'],
            'alisports.com': ['121.43.186.183'],
            'lazada.com.sg': ['54.179.114.75'],
            'kaola.com': ['106.11.186.7,106.11.208.135,203.119.245.60,203.119.245.94']
        },
        'cname': {
            'tmall.com': [
                'shop.tmall.com,shop.tmall.com.gds.alibabadns.com,na61-na62.wagbridge.alibaba.tmall.com,na61-na62.wagbridge.alibaba.tmall.com.gds.alibabadns.com'],
            '1688.com': [
                'cn.1688.com,na61-na62.wagbridge.alibaba.1688.com,na61-na62.wagbridge.alibaba.1688.com.gds.alibabadns.com'],
            'fliggy.com': [
                'na61-na62.wagbridge.alibaba.alibabacorp.com,na61-na62.wagbridge.alibaba.alibabacorp.com.gds.alibabadns.com'],
            'alitrip.com': [
                'sh.wagbridge.alitrip.com,sh.wagbridge.alibaba-inc.com,sh.wagbridge.alibaba-inc.com.gds.alibabadns.com'],
            'kaola.com': ['kaola.com,kaola-wagbridge.alibaba.com,kaola-wagbridge.alibaba.com.gds.alibabadns.com'],
            'xianzhi.com': ['do-s1.nodes.gz.com,hcs1.nodes.gz.com']
        }
    },
    'vipkid.com': {
        'ip': {
            'vipkid-qa.com.cn': ['10.32.68.3,10.32.33.155']
        },
        'cname': {}
    },
    '360.net': {
        'ip': {
            'zhiye.com': ['182.92.193.246,123.56.162.191,101.200.148.50,123.56.159.186'],
            'design.cn': ['221.214.14.234'],
            'zjmi.com': ['115.236.161.183'],
            'italent.cn': ['124.250.100.144'],
            'autohome.com.cn': ['219.148.35.254'],
            '51zhangdan.com': ['115.238.29.11'],
            '17u.cn': ['61.155.159.18'],
            'huanqiu.com': ['192.144.195.11'],
            'elong.com': ['119.18.193.144'],
            'tourzj.edu.cn': ['223.93.161.241,60.191.79.169'],
            'dszc-amc.com': ['119.29.165.139,139.199.35.34'],
            'ceping.com': ['124.250.100.136'],
            'u51.com': ['115.238.29.11'],
            'fenqileloan.com': ['119.29.165.139,139.199.35.34'],
            'che168.com': ['219.148.35.190,221.192.136.190'],
            'zjmiit.com': ['115.236.161.184']
        },
        'cname': {
            '51zhangdan.com': ['enniuapi.u51.com'],
            '17u.cn': ['ebkwww.17u.cn.tcylgslb.com'],
            'huanqiu.com': ['huanqiu.com.f1.zlibs.com,f1.zlibs.com,qcloud.f1.zlibs.com,qcloud-cn-bj.f1.zlibs.com'],
            'fenqileloan.com': ['www.fenqileloan.com'],
            'dszc-amc.com': ['www.dszc-amc.com'],
            'u51.com': ['enniuapi.u51.com']
        }
    },
    'starbucks.com.cn': {
        'ip': {
            'starbucks.com.cn': ['180.153.48.188']
        },
        'cname': {}
    },
    'bytedance.com': {
        'ip': {
            'everphoto.cn': ['36.110.162.58']
        },
        'cname': {
            'tuchong.com': ['all.tuchong.com.w.kunlunca.com'],
            'duoshanapp.com': ['www.duoshanapp.com.w.kunluncan.com']
        }
    },
    '163.com': {
        'ip': {
            'g4wl.com': ['3.223.115.185'],
            '166dns.com': ['45.156.216.237,103.75.44.172'],
            '126.com': ['220.181.12.218,123.126.96.210']
        },
        'cname': {
            'g4wl.com': ['HDRedirect-LB7-5a03e1c2772e1c9c.elb.us-east-1.amazonaws.com'],
            '166dns.com': ['hhtm.ufocdn.vip'],
            '126.com': ['email.163.com']
        }
    },
    'shuidihuzhu.com': {
        'ip': {
            'shuidi.cn': ['47.103.47.30']
        },
        'cname': {}
    },
    'wanmei.com': {
        'ip': {
            'hongen.com': ['123.56.76.58'],
            'pwrdedu.com': ['123.59.99.222'],
            'xmkanshu.com': ['111.13.108.110'],
            
        },
        'cname': {
            'hongen.com': ['www.hongen.com']
        }
    },
    'qschou.com': {
        'ip': {
            'qschou.com': ['120.55.250.237']
        },
        'cname': {}
    },
    '58.com': {
        'ip': {
            '58.com': ['115.159.231.124'],
            'ganji.com': ['154.8.241.69'],
            'jikejia.cn': ['123.206.235.144'],
            'anjuke.com': ['123.206.235.145'],
            'jxedt.com': ['115.159.231.124']
        },
        'cname': {
            '58.com': ['ngx-fan.58.com'],
            'ganji.com': ['ganji-ngx-fan.ganji.com'],
            'jikejia.cn': ['fe-fan.anjuke.com'],
            'anjuke.com': ['ngx-fan.anjuke.com'],
            'jxedt.com': ['ngx-fan.58.com']
        }
    },
    'mogu.com': {
        'ip': {
            'mogu.com': ['212.64.117.182'],
            'meili-inc.com': ['172.81.232.152']
        },
        'cname': {
            'mogu.com': ['qihe.mogujie.com'],
            'meili-inc.com': ['lb.mogujie.org']
        }
    },
    'pingan.com': {
        'ip': {
            'ph.com.cn': ['124.196.43.1,210.83.240.67,218.18.229.67']
        },
        'cname': {}
    },
    'qunar.com': {
        'ip': {
            'qunar-bnb.com': ['123.59.180.130,117.122.224.156']
        },
        'cname': {
            'qunar-bnb.com': ['bnb.qunar.com,bnb.qunar.quner.com,bnb.ct.glbs.qunar.com']
        }
    },
    'qianmi.com': {
        'ip': {
            '1000.com': ['120.55.198.201'],
            'qianmi.com': ['120.55.198.118']
        },
        'cname': {
            'qianmi.com': ['qmslb.qianmi.com']
        }
    },
    'microsoft.com': {
        'ip': {
            'joinms.com.cn': ['47.75.37.155']
        },
        'cname': {
            'joinms.com.cn': ['a.mb.cn']
        }
    },
    'qq.com': {
        'ip': {
            'discuz.net': ['101.227.130.115'],
            'myqcloud.net': ['140.143.178.92'],
            'fyeds5.com': ['123.150.76.205,123.151.79.41'],
            'onwork.com': ['113.96.233.160'],
            'qq.wang': ['0.0.0.1'],
            'fyeds.com': ['123.150.76.205,123.151.79.41'],
            'qcloudapps.com': ['193.112.255.177'],
            'qcloudcdn.com': ['124.236.32.117,106.117.252.243'],
            'fyeds0.com': ['123.150.76.205,123.151.79.41'],
            'prayaya.com': ['184.22.123.24'],
            'shuame.la': ['8.210.177.162,156.236.72.239'],
            'fsphere.cn': ['118.24.227.108'],
            'bkapigw.com': ['0.0.0.1'],
            'gcloudcs.com': ['115.159.16.176'],
            'hkgcloudcs.com': ['119.28.39.186'],
            'agcloudcs.com': ['45.113.69.32'],
            'flzhan.com': ['0.0.0.1'],
            'tencentcloudapi.com': ['0.0.0.1'],
            'tencent.com': ['124.156.189.163'],
            'bkclouds.cc': ['121.14.76.42'],
            'tencentcloud.io': ['49.51.41.231'],
            'tswjs.org': ['61.129.7.121'],
            'qq.zone': ['0.0.0.1'],
            'nintendoswitch.com.cn': ['100.113.212.57']
            
        },
        'cname': {
            'qcloudcdn.com': ['cloud.cdntip.com,temp.p23.tc.cdntip.com'],
            'prayaya.com': ['v3uc.prayaya.com'],
            'onwork.com': ['tp.exmail.qq.com'],
            'discuz.net': ['faq.comsenz.com'],
            'myqcloud.net': ['speedx.myqcloud.net'],
            'nintendoswitch.com.cn': ['dev.nintendoswitch.com.cn']
        }
    },
    'eastmoney.com': {
        'ip': {
            'dfcfw.com': ['61.152.229.228'],
            'eastmoney.cn': ['61.129.249.219'],
            'dfcfs.com': ['61.129.248.120'],
            'asdasdasaaaa.eastmoney.cn': ['61.129.249.219'],
            '1234567.com.cn': ['61.129.249.39'],
            'asdasdasaaaa.eastmoney.com.cn': ['61.152.229.228'],
            'asdasdasaaaa.1234567.com.cn': ['61.129.249.39'],
            'zhaiba.com': ['61.152.229.165'],
            'asdasdasaaaa.dfcfw.com': ['61.152.229.228'],
            'caifutong.com.cn': ['114.80.234.189'],
            'asdasdasaaaa.18.com.cn': ['61.152.229.228'],
            'asdasdasaaaa.eastmoney.com': ['61.152.229.228'],
            'eastmoney.com': ['61.152.229.228'],
            '18.com.cn': ['61.152.229.228']
        },
        'cname': {}
    },
    'suning.com': {
        'ip': {
            'suning.com': ['103.254.188.41']
        },
        'cname': {
            'suning.com': ['httppubv46.suning.com,webhttpsnipv46.suninggslb.cn,wshttppubv46.suning.com.wsglb0.com']
        }
    }
}
