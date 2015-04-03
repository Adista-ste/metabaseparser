#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import argparse, sys, os, re


arguments = argparse.ArgumentParser()
arguments.add_argument("-s","--https",help="Traite également les domaines HTTPS", action='store_true')
arguments.add_argument("-f","--fichier",help="Définit le fichierxml utilise")

args = arguments.parse_args()

if not args.fichier:
	print "Erreur : Pas de fichier de MetaBase indiqué"
	arguments.print_help()
	sys.exit(1)
elif not os.path.exists(args.fichier):
	print "Erreur : Le fichier MetaBase indiqué n'existe pas"
	arguments.print_help()
	sys.exit(2)

tree = etree.parse(args.fichier)



#ns={'xmlns': 'urn:microsoft-catalog:XML_Metabase_V64_0'}

liste=[]

#for i in tree.iter(tag="{%s}IIsWebServer" % ns['xmlns']):
for sites in tree.iter(tag="site"):
	for binding in sites.iter('binding'):
		bind = binding.attrib.get('bindingInformation')
		ndd = re.sub(r'\**:[0-9]+:', r' ',bind)
		if ndd:
			#print ndd
			liste+=ndd.split()
		#print bind['bindingInformation']

#		if site:
#			if args.https:
#				inter=re.sub(r':443:', r' ', site)
#			inter=re.sub(r':80:', r' ', site)
#			liste+=inter.split()
#	
liste.sort()
final=list(set(liste))
final.sort()
#	
for j in final:
	print "%s" % j
