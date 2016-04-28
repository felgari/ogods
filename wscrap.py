# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Class to scrap web sites.
"""

import requests
import urllib2
from bs4 import BeautifulSoup
import re

from ctes import *
from diary import Diary

class WScrap(object):
    """Scraping on web pages.
    """
    
    @staticmethod
    def _encode_utf8_to_ascii(utxt):
        """Encode the given UTF-8 text as ASCII.
        """
        
        if not isinstance(utxt, basestring):
            return utxt
        
        # Replace single-quote.
        utxt = re.sub(
            u'[\u02bc\u2018\u2019\u201a\u201b\u2039\u203a\u300c\u300d]', 
            chr(39), 
            utxt)
        
        # Replace double-quote.
        utxt = re.sub(
            u'[\u00ab\u00bb\u201c\u201d\u201e\u201f\u300e\u300f]', chr(34), 
            utxt)
        
        utxt = re.sub(u'[\u00ba]', 'º', utxt) # ''
        
        utxt = re.sub(u'[\u00e1]', chr(97), utxt) # 'á'
        utxt = re.sub(u'[\u00e9]', chr(101), utxt) # 'é'
        utxt = re.sub(u'[\u00ed]', chr(105), utxt) # 'í'
        utxt = re.sub(u'[\u00f3]', chr(111), utxt) # 'ó'
        utxt = re.sub(u'[\u00fa]', chr(117), utxt) # 'ú'
        
        utxt = re.sub(u'[\u00c1]', chr(65), utxt) # 'Á'       
        utxt = re.sub(u'[\u00c9]', chr(69), utxt) # 'É'
        utxt = re.sub(u'[\u00cd]', chr(73), utxt) # 'Í'
        utxt = re.sub(u'[\u00d3]', chr(79), utxt) # 'Ó'
        utxt = re.sub(u'[\u00da]', chr(85), utxt) # 'Ú'
        
        utxt = re.sub(u'[\u00f1]', chr(110), utxt) # 'ñ'
        utxt = re.sub(u'[\u00d1]', chr(78), utxt) # 'Ñ'        
        
        # Replace all the characters to ASCII.
        return utxt.encode('ascii', 'ignore')    
    
    @staticmethod
    def _encode_utf8_to_ISO8859_1(utxt):
        """Encode the given UTF-8 text as ISO-8859-1.
        """
        
        if not isinstance(utxt, basestring):
            return utxt
        
        # Replace single-quote.
        utxt = re.sub(
            u'[\u02bc\u2018\u2019\u201a\u201b\u2039\u203a\u300c\u300d]', 
            chr(39), 
            utxt)
        
        # Replace double-quote.
        utxt = re.sub(
            u'[\u00ab\u00bb\u201c\u201d\u201e\u201f\u300e\u300f]', chr(34),
            utxt)
        
        utxt = re.sub(u'[\u00ba]', chr(186), utxt) # 'º'
        
        utxt = re.sub(u'[\u00e1]', chr(225), utxt) # 'á'
        utxt = re.sub(u'[\u00e9]', chr(233), utxt) # 'é'
        utxt = re.sub(u'[\u00ed]', chr(237), utxt) # 'í'
        utxt = re.sub(u'[\u00f3]', chr(243), utxt) # 'ó'
        utxt = re.sub(u'[\u00fa]', chr(250), utxt) # 'ú'
        
        utxt = re.sub(u'[\u00c1]', chr(193), utxt) # 'Á'       
        utxt = re.sub(u'[\u00c9]', chr(201), utxt) # 'É'
        utxt = re.sub(u'[\u00cd]', chr(205), utxt) # 'Í'
        utxt = re.sub(u'[\u00d3]', chr(211), utxt) # 'Ó'
        utxt = re.sub(u'[\u00da]', chr(218), utxt) # 'Ú'
        
        utxt = re.sub(u'[\u00f1]', chr(241), utxt) # 'ñ'
        utxt = re.sub(u'[\u00d1]', chr(209), utxt) # 'Ñ'        
        
        # Replace all the characters to ISO-8859-1.
        return utxt.encode('ISO-8859-1', 'replace')

    @staticmethod
    def _prepare_request(url):
        """Prepare a http request to the url received.
        """
        
        session = requests.Session()
    
        return session.get(url, headers = REQUEST_HEADERS)    
    
    @staticmethod
    def _retrieve_from_url(url):
        """Retrieve the diary page from the url received.
        """
        
        bsObj = None
        
        req = WScrap._prepare_request(url)
        
        print "Reading page from: %s" % url
        
        try:    
            _ = urllib2.urlopen(url)
        except urllib2.HTTPError:
            pass
        except urllib2.URLError:
            pass
        else:
            try:
                bsObj = BeautifulSoup(req.text, "lxml")
            except AttributeError:
                pass
                
        return bsObj 
           
    @staticmethod
    def _process_page(bsObj, dia):
        """Process a page and stores the data in the Diary object received.
        """
        
        for item in bsObj.findAll(ITEM_LABEL, ITEM_LABEL_DICT):
            
            for organism in item.findAll(ORG_LABEL):                     
                dia.add_org(organism.get_text().strip())            
            
            for content in item.findAll(CONTENT_GROUP):
                
                for cont_lab in content.findAll(CONTENT_LABEL):   
                    dia.add_content(cont_lab.get_text().strip())
                
                for url in content.findAll(URL_LABEL, URL_LABEL_DICT):
                    dia.add_url(url[URL_ATTR].strip())
     
    @staticmethod
    def scrap_page(url, dia):
        """Scrap the page indicated and pass the Diary object to the 
        function that processes the page.
        """
        
        success = False
    
        bsObj = WScrap._retrieve_from_url(url)

        if bsObj: 
            try:
                WScrap._process_page(bsObj, dia)
                success = True
            except KeyError:
                pass
                
        return success
                