#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:58:36 2016
programa hecho en clase de JSON
@author: oscar
"""



import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Ingresar Ciudad: ')
    if len(address) < 1 : break
    
    url = serviceurl + urllib.urlencode({'sensor':'false','address':address})
    print 'Recuperando',url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Recuperados',len(data),'characteres'
    print data
    
#####################segunda parte 
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] !='OK':
        print '==== FAllo ====='
        print data
        continue
    print json.dumps(js,indent=4)
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js["results"][0]["formatted_address"]
    print location


    









