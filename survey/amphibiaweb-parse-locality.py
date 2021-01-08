#!/usr/bin/env python3
import sys

# Install xmltodict first. See https://pypi.org/project/xmltodict/
import xmltodict

f_iso = open('iso_country_code.txt', 'r')
for line in f_iso:
    tokens = line.strip().split("\t")
    tmp_country_name = tokens[0]
    tmp_code = tokens[1].lower()
    #if tmp_code != 'bh':
    #    continue
    
    filename_xml = 'amphibiaweb_locality/amphibiaweb_locality.%s.xml' % tmp_code
    
    with open(filename_xml) as f_xml:
        rv_xml = xmltodict.parse(f_xml.read(), force_list=('amphibian'))

        if 'amphibian' not in rv_xml['amphibiaweb']:
            sys.stderr.write('No record: %s\n' % filename_xml)
        else:
            sys.stderr.write('Read %s\n' % filename_xml)
            for tmp in rv_xml['amphibiaweb']['amphibian']:
                print("%s\t%s\t%s\t%s\t%s" % 
                        (tmp_code, tmp_country_name, tmp['order'], tmp['family'], 
                         tmp['scientificname'].replace(' ', '_')))
