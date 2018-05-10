#!/usr/bin/env python
# pycurl.py
#
# A Python >= 2.7 command line utility for querying JSON data using dot notation.
#

import re
import argparse
import sys
import os
from os.path import expanduser

from pip import PipError

# adjust for python2/3 input() vs raw_input
try: input = raw_input
except NameError: pass

cmd = ''
for a in sys.argv:
    if re.search(r'[\s"]',a):
        cmd += " '%s'" % a
    else:
        cmd += " " + a

parser = argparse.ArgumentParser(description="Python-based Curl Replacement")
parser.add_argument("-s","--silent",help="Silent mode",action="store_true")
parser.add_argument("-k","--insecure",help="Allow insecure connections",action="store_true")
parser.add_argument("-u","--user",help="Environment variable to read for USER:PASSWORD")
parser.add_argument("-X","--request",help="Request Type")
parser.add_argument("-H","--header",help="Environment variable to read for a header",action="append")
parser.add_argument("-d","--data",help="HTTP POST data",action="append")
parser.add_argument("--data-urlencode",help="HTTP POST data",action="append")
parser.add_argument("--data-binary",help="HTTP POST data")
parser.add_argument("--globoff",help="Disable URL sequences and ranges using {} and []",action="store_true")
parser.add_argument("-F","--form",help="Specify HTTP multipart POST data",action="append")
parser.add_argument("url",nargs="?")
args = parser.parse_args()

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    global input

    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stderr.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def loader(val,require_secure=False):
    g = re.match(r'^\s*(@|\$)(.*)',val)
    if g:
        if g.group(1) == '@':
            try:
                if g.group(2) == '-':
                    return sys.stdin
                else:
                    return open(expanduser(g.group(2)),"rb")
            except:
                sys.stderr.write('curl: couldn\'t open file "%s"' % g.group(2))
                return ""
        else: # g.group(1) == '$'
            try:
                return os.environ[g.group(2)]
            except:
                sys.stderr.write('curl: couldn\'t read environment variable "%s"' % g.group(2))
                return ""
    else:
        if require_secure:
            raise Exception("Credentials Exposed: "+cmd)
        return val

# check for requests package. If missing and pip is installed,
# prompt the user to install it. Otherwise, fail with a helpful
# message
try:
    import pip

    flat_installed_packages = [package.project_name for package in pip.get_installed_distributions()]

    if 'requests' in flat_installed_packages:
        import requests
    else:
        if query_yes_no('One or more required Python modules are missing: "requests"\nWould you like to install them now?'):
            REQUIREMENTS = [ 'requests' ]
            pip_args = ['-vvv', 'install']
            for req in REQUIREMENTS:
                pip_args.append(req)
            print('Installing requirements: ' + str(REQUIREMENTS))
            try:
                pip.main(pip_args)
                import requests
            except PipError as e:
                sys.stderr.write('{"status":"error","message": "python: \"%s\""}' % e.message)
                sys.exit(0)
            except NameError as e:
                sys.stderr.write('{"status":"error","message": "python: \"Unable to import requests package after installation. Please run \'pip install requests\' manually before continuing.\""}')
                sys.exit(0)
        else:
            sys.stdout.write('{"status":"error","message": "Couldn\'t contact remote server. Required python module, \'requests,\' is not installed."}')
            sys.exit(0)
except ImportError as e:
    try:
        import requests
    except ImportError as f:
        sys.stderr.write('{"status":"error","message": "python: \"%s\""}' % f.message)
        sys.exit(0)

verify = True
if args.insecure:
    pass #verify = not args.insecure

request = "GET"
if args.request:
    request = args.request

headers = {}
if args.header:
    for arg in args.header:
        s = arg.split(":")
        if s[0] == "Authorization":
            headers[s[0]]=loader(s[1],True)
        else:
            headers[s[0]]=loader(s[1],False)

data = []

if args.data:
    for d1 in args.data:
        for d in d1.split('&'):
            g = re.match(r'(.*?)=(.*)',d)
            if g:
                data += [(g.group(1),loader(g.group(2)))]
            else:
                data += [(loader(d),'')]

if args.data_urlencode:
    for d1 in args.data_urlencode:
        for d in d1.split('&'):
            g = re.match(r'(.*?)=(.*)',d)
            if g:
                data += [(g.group(1),loader(g.group(2)))]
            else:
                data += [(loader(d),'')]

if args.data_binary:
    data = loader(args.data_binary)
    if hasattr(data,"read"):
        data = data.read()

if args.user:
    s = args.user.split(":")
    auth = (s[0],loader(s[1],True))
else:
    auth = None

form_data = {}
if args.form:
    for f in args.form:
        g = re.match(r'^(.*?)=(.*)$',f)
        if g:
            form_data[g.group(1)] = loader(g.group(2))

res = ''

if request == "GET":
    if args.user:

        res = requests.get(args.url,headers=headers,data=data,auth=auth,verify=verify)
    else:
        res = requests.get(args.url,headers=headers,data=data,verify=verify)

elif request == "POST":
    if args.user:
        res = requests.post(args.url,headers=headers,data=data,auth=auth,files=form_data,verify=verify)
    else:
        res = requests.post(args.url,headers=headers,data=data,files=form_data,verify=verify)

elif request == "DELETE":
    if args.user:
        res = requests.delete(args.url,headers=headers,data=data,auth=auth,verify=verify)
    else:
        res = requests.delete(args.url,headers=headers,data=data,verify=verify)

elif request == "PUT":
    if args.user:
        res = requests.put(args.url,headers=headers,data=data,auth=auth,verify=verify)
    else:
        res = requests.put(args.url,headers=headers,data=data,verify=verify)

else:
    raise Exception("Not supported: "+cmd)

# Python 3 issue
if type(res.text) == str:
    sys.stdout.write(res.text)
else:
    sys.stdout.write(res.text.encode('utf-8'))