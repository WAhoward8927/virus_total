"""virus total的API功能，有Domain、url、ip、file"""
import requests
import storge_result
# from virus_total import storge_result
import base64


class General:

    def __init__(self):
        """使用院內proxy(需要AD與證書)"""
        self.headers = {'x-apikey': '4a2d6c8102f8a59ab987ff33302074027f6cc4ee99230b6cc3f84fbe11308ea6',
                        'Accept': 'application/json',
                        'Connection': 'close'}
        self.domain_url = 'https://virustotal.com/api/v3/domains/'
        self.base_url = 'https://www.virustotal.com/api/v3/urls'
        self.ip = "https://www.virustotal.com/api/v3/ip_addresses/"
        self.file_url = 'https://www.virustotal.com/api/v3/files/'
        '''auth1 = "wang85"  # 院內用
        auth2 = "Saber297"
        self.proxy = {"http": "http://{}:{}@192.168.8.29:8080".format(auth1, auth2),
                      "https": "https://{}:{}@192.168.8.29:8080".format(auth1, auth2)}'''

    def domain(self, target):
        response = requests.get(f"{self.domain_url}{target}", headers=self.headers)
        storge_result.create('Domain', target, response)

    def urls(self, target):
        post_data = requests.post(self.base_url, headers=self.headers, data={'url': target})
        if post_data.status_code != 200:
            storge_result.create('Url', target, post_data)
        encode_url = base64.urlsafe_b64encode(target.encode())
        get_data = requests.get(self.base_url + '/{}'.format(encode_url.decode().replace('=', '')),
                                headers=self.headers)
        storge_result.create('Url', target, get_data)

    def ip_scan(self, target):
        response = requests.get(f"{self.ip}{target}", headers=self.headers)
        storge_result.create('Ip', target, response)

    def file(self, target):
        response = requests.get(f"{self.file_url}{target}", headers=self.headers)
        storge_result.create('File', target, response)
