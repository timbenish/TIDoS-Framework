#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework 

from colors import *
import time

def activeban():

    time.sleep(0.4)
    print G+'     +----------------+'
    print G+'     |  '+O+'ACTIVE RECON'+G+'  |'
    print G+'     +----------------+'
    time.sleep(0.3)
    print ''
    print B+'     [1]'+C+' Ping/NPing Enumeration'+W+' (Adaptative+Debug)'
    time.sleep(0.1)
    print B+'     [2]'+C+' Grab HTTP Headers'+W+' (Live Capture)'
    time.sleep(0.1)
    print B+'     [3]'+C+' Find Allowed HTTP Methods'+W+' (Via OPTIONS)'
    time.sleep(0.1)
    print B+'     [4]'+C+' Examine robots.txt and sitemap.xml'
    time.sleep(0.1)
    print B+'     [5]'+C+' Enumerate Subnets'+W+' (Class Based)'
    time.sleep(0.1)
    print B+'     [6]'+C+' Perform Advanced Traceroute'+W+' (TTL Based)'
    time.sleep(0.1)
    print B+'     [7]'+C+' Find Shared DNS Hosts'+W+' (NameServer Based)'
    time.sleep(0.1)
    print B+'     [8]'+C+' Examine SSL Certificate'+W+' (Absolute)'
    time.sleep(0.1)
    print B+'     [9]'+C+' CMS Detection '+W+'(185+ CMSs supported)'
    time.sleep(0.1)
    print B+'     [10]'+C+' Enumerate Server behind website'+W
    time.sleep(0.1)
    print B+'     [11]'+C+' Operating System Fingerprinting'+W+' (Response Based)\n'
    time.sleep(0.1)
    print B+'     [A]'+C+' The Auto-Awesome Module\n'
    time.sleep(0.1)
    print B+'     [99]'+C+' Back\n' 

