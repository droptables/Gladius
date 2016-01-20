import requests,json
from clint.textui import colored
from Launch.Launch import Launch

class BanHash(object):

	@staticmethod
	def Run(hashvalue,rulename):
		launch=Launch()
		args=launch.get_args()
		b9serverurl,b9apitoken=launch.load_b9_config(args.configfile)
		authJson={
		'X-Auth-Token': b9apitoken, 
		'content-type': 'application/json'
		}
		serverurl=b9serverurl+str("/api/bit9platform/v1/")
		fileruleurl = serverurl+"fileRule"
		b9StrongCert = True
		print colored.yellow("[*] Banning "+ hashvalue+"...")
		data = {'hash': hashvalue, 'fileState': 3, 'policyIds': '0', 'name': rulename}
		r = requests.post(fileruleurl, json.dumps(data), headers=authJson, verify=b9StrongCert)
		r.raise_for_status()      
		fileRule = r.json()
		try:
			print colored.green("[+] "+str(rulename)+" "+str(hashvalue)+" Banned!")
		except:
			print colored.yellow("[*] Can't print strange characters, need to learn 2 codec")
			pass