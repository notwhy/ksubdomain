package core

import (
	"bufio"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
	"github.com/google/gopacket/pcap"
	"ksubdomain/gologger"
	"os"
	"regexp"
	"strconv"
	"strings"
	"sync/atomic"
	"time"
)

var ipRegex = regexp.MustCompile("((?:(?:25[0-5]|2[0-4]\\d|((1\\d{2})|([1-9]?\\d)))\\.){3}(?:25[0-5]|2[0-4]\\d|((1\\d{2})|([1-9]?\\d))))")
var cnameRegex = regexp.MustCompile("CNAME (.*?) ")


func getIp(ip string) string {
	groups := ipRegex.FindAllString(ip, -1)
	if len(groups) > 0 {
		ip = groups[0]
	}
	return ip
}

func getAllIp(ip string) []string{
	var groups = ipRegex.FindAllString(ip, -1)
	return groups
	//if len(groups) > 0 {
	//	ip = groups[0]
	//}
	//return ip
}
func getCname(cname string) string {
	groups := cnameRegex.FindAllString(cname, -1)
	if len(groups) > 0 {
		cname = groups[0]
	}
	return cname
}

func Recv(device string, options *Options, flagID uint16, retryChan chan RetryStruct) {
	var (
		snapshotLen int32         = 1024
		promiscuous bool          = false
		timeout     time.Duration = -1 * time.Second
	)
	windowWith := GetWindowWith()
	if options.Silent {
		windowWith = 0
	}
	handle, _ := pcap.OpenLive(device, snapshotLen, promiscuous, timeout)
	err := handle.SetBPFFilter("udp and src port 53")
	if err != nil {
		gologger.Fatalf("SetBPFFilter Faild:%s\n", err.Error())
	}
	packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
	defer handle.Close()

	var udp layers.UDP
	var dns layers.DNS
	var eth layers.Ethernet
	var ipv4 layers.IPv4
	var ipv6 layers.IPv6
	var subNextData []string
	if options.SubNameFileName == "" {
		subNextData = GetDefaultSubNextData()
	} else {
		if !FileExists(options.SubNameFileName) {
			gologger.Fatalf("三级域名文件:%s 不存在\n", options.SubNameFileName)
		}
		rs, err := LinesInFile(options.SubNameFileName)
		if err != nil {
			gologger.Fatalf("读取三级域名文件失败:%s\n", err.Error())
		}
		if len(rs) == 0 {
			gologger.Fatalf("三级域名文件内容为空\n")
		}
		subNextData = rs
	}
	parser := gopacket.NewDecodingLayerParser(
		layers.LayerTypeEthernet, &eth, &ipv4, &ipv6, &udp, &dns)
	var isWrite bool = false
	var isttl bool = options.TTL
	var isSummary bool = options.Summary
	if options.Output != "" {
		isWrite = true
	}
	var foutput *os.File
	if isWrite {
		foutput, err = os.OpenFile(options.Output, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0664)
		if err != nil {
			gologger.Errorf("写入结果文件失败：%s\n", err.Error())
		}
	}
	for {
		packet, err := packetSource.NextPacket()
		if err != nil {
			continue
		}
		var decoded []gopacket.LayerType
		err = parser.DecodeLayers(packet.Data(), &decoded)
		if err != nil {
			continue
		}
		if !dns.QR {
			continue
		}
		if dns.ID/100 == flagID {
			if options.CheckOrigin {
				if !IsContain(options.Resolvers, ipv4.SrcIP.String()) {
					continue
				}
			}
			atomic.AddUint64(&RecvIndex, 1)
			udp, _ := packet.Layer(layers.LayerTypeUDP).(*layers.UDP)
			index := GenerateMapIndex(dns.ID%100, uint16(udp.DstPort))
			data, err := LocalStauts.SearchFromIndexAndDelete(uint32(index))
			if err == nil {
				// 处理多级域名
				if dns.ANCount > 0 && data.v.DomainLevel < options.DomainLevel {
					running := true
					if options.SkipWildCard {
						if IsWildCard(data.v.Domain) {
							running = false
						}
					}
					if running {
						for _, sub := range subNextData {
							subdomain := sub + "." + data.v.Domain
							retryChan <- RetryStruct{Domain: subdomain, Dns: data.v.Dns, SrcPort: 0, FlagId: 0, DomainLevel: data.v.DomainLevel + 1}
						}
					}
				}
				if LocalStack.Len() <= 50000 {
					LocalStack.Push(uint32(index))
				}
			}
			// return
			if dns.ANCount > 0 {
				if len(dns.Questions) == 0 {
					continue
				}
				data := RecvResult{Subdomain: string(dns.Questions[0].Name)}
				data.Answers = dns.Answers

				msg := data.Subdomain + " => "
				if !options.Silent {
					for _, v := range data.Answers {
						msg += v.String()
						if isttl {
							msg += " ttl:" + strconv.Itoa(int(v.TTL))
						}
						msg += " => "
					}
				}

				msg = strings.Trim(msg, " => ")
				if options.CheckCname{
					var cname string = ""
					//cname = strings.Trim(getCname(msg),"CNAME ")

					var cnameblack int8 = 0
					for i:=0;i<len(cnameRegex.FindAllString(cname, -1));i++{
						if strings.Contains(options.Fcname,cnameRegex.FindAllString(msg, -1)[i]){
							//gologger.Infof("\nfip %s\n", options.Fip)
							//gologger.Infof("\ncurrent ip %s\n", ipRegex.FindAllString(msg, -1)[i])
							//gologger.Infof("\n检测泛解析msg %s\n", msg)
							//gologger.Infof("\n检测泛解析ip %s\n", ipRegex.FindAllString(msg, -1))
							cnameblack = 1
							break
						}
					}
					if cnameblack == 1{
						continue
					}


					//if strings.Contains(options.Fcname,cname){
					//	//  处理cname 黑名单
					//	gologger.Silentf("\n%s black cname found: %s", msg ,cname)
					//	gologger.Silentf("%s\n", msg)
					//	continue
					//}
				}
				//return
				if options.CheckIp{

					//var ip string = ""
					//ip = getIp(msg)
					//var array [...] string := ipRegex.FindAllString(msg, -1)
					var ipblack int8 = 0
					for i:=0;i<len(ipRegex.FindAllString(msg, -1));i++{
						if strings.Contains(options.Fip,ipRegex.FindAllString(msg, -1)[i]){
							//gologger.Infof("\nfip %s\n", options.Fip)
							//gologger.Infof("\ncurrent ip %s\n", ipRegex.FindAllString(msg, -1)[i])
							//gologger.Infof("\n检测泛解析msg %s\n", msg)
							//gologger.Infof("\n检测泛解析ip %s\n", ipRegex.FindAllString(msg, -1))
							ipblack = 1
							break
						}
					}
					if ipblack == 1{
						continue
					}


					//continue
					//var ip string = ""
					//gologger.Infof("\n检测泛解析成功 %s\n", strings.Contains(options.Fip,ip))
					//
					//if strings.Contains(options.Fip,ip){
					//	//  处理cname 黑名单
					//	gologger.Infof("\n%s black ip found: %s", msg ,ip)
					//	gologger.Infof("%s\n", msg)
					//	continue
					//}
				}

				// gologger.Silentf("\r2222222 %s\n", msg)
				atomic.AddUint64(&SuccessIndex, 1)

				ff := windowWith - len(msg) - 1
				if !options.Silent {
					if windowWith > 0 && ff > 0 {
						gologger.Silentf("\r%s% *s\n", msg, ff, "")
					} else {
						gologger.Silentf("\r%s\n", msg)
					}
				} else {
					gologger.Silentf("%s\n", msg)
				}
				if isSummary {
					AsnResults = append(AsnResults, data)
				}

				if isWrite {
					w := bufio.NewWriter(foutput)
					_, err = w.WriteString(msg + "\n")
					if err != nil {
						gologger.Errorf("写入结果文件失败.Err:%s\n", err.Error())
					}
					w.Flush()
				}
			}
			PrintStatus()
		}
	}
}
