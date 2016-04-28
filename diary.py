# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This file is part of ycas: https://github.com/felgari/ogods
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

"""Class to store the information retrieved from a diary.
"""

import unicodedata as un

class Content(object):
    """Store information about contents.    
    """    
    
    def __init__(self, txt):
        
        self._txt = txt
        self._url = None
        self._terms = []
        
    @property
    def txt(self):
        return self._txt
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self._url = url        
        
    @property
    def terms(self):
        return self._terms
    
    @property
    def has_contents(self):
        
        return len(self._txt) > 0   
    
    def __str__(self):
        txt = un.normalize('NFKD', self._txt).encode('ascii', 'ignore')
        return "- %s\n- %s" % (txt, self._url)
    
    __repr__ = __str__
    
    def show(self):
        
        print self
        
    def generate_terms(self):
        
        # TODO
        print "Someday, near in the future, those terms will be generated ..."      
    
class Organism(object):
    """Store information about organisms.    
    """
    
    def __init__(self, name):
        
        self._name = name
        self._contents = []

    @property
    def name(self):
        return self._name
    
    @property
    def contents(self):
        return self._contents 
    
    @property
    def has_contents(self):
        
        return len(self._contents) and \
            any([c.has_contents for c in self._contents]) 
    
    def __str__(self):
        name = un.normalize('NFKD', self._name).encode('ascii', 'ignore')
        return "Organism: %s" % name
    
    __repr__ = __str__      
    
    def show(self):
        
        print self
        
        for c in self.contents:
            c.show()
    
    def add_content(self, con):
        
        self._contents.append(con)
        
    def add_url(self, url):
        
        if len(self._contents): 
            current_con = self._contents[-1]  
            current_con.url = url        
        else:
            print "ERROR: Adding url in Organism %s." % self._name           
            
    def generate_terms(self):   
                        
        if len(self._contents): 
            current_con = self._contents[-1]  
            current_con.generate_terms()        
        else:
            print "ERROR: Adding generating terms in Organism %s." % self._name 
                        
    def retrieve_terms(self):
        
        terms = set()
        
        for c in self._contents:
            terms = terms | c.terms
        
        return sorted(list(terms))         
                
class Section(object):
    """Store information about sections.    
    """    
    
    def __init__(self, name):
    
        self._name = name
        self._orgs = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def orgs(self):
        return self._orgs
    
    @property
    def has_contents(self):
        
        return len(self._orgs) and \
            any([o.has_contents for o in self._orgs])    

    def __str__(self):
        return "Section: %s" % self._name
    
    __repr__ = __str__   
    
    def show(self):
        
        print self
        
        for o in self.orgs:
            o.show()
    
    def add_org(self, org):         
        self._orgs.append(org)
        
    def add_content(self, con):  
        
        if len(self._orgs): 
            current_org = self._orgs[-1]  
            current_org.add_content(con)        
        else:
            print "ERROR: Adding content in Section %s." % self._name
            
    def add_url(self, url):  
        
        if len(self._orgs): 
            current_org = self._orgs[-1]  
            current_org.add_url(url)        
        else:
            print "ERROR: Adding url in Section %s." % self._name 
            
    def retrieve_orgs(self):
        
        orgs = set()
        
        for o in self.orgs:
            orgs.add(o.name)
        
        return orgs                        
            
    def generate_terms(self):  
        
        if len(self._orgs): 
            current_org = self._orgs[-1]  
            current_org.generate_terms()        
        else:
            print "ERROR: Adding generating terms in Section %s." % self._name
            
    def retrieve_terms(self):     
        
        terms = set()
        
        for o in self.orgs:
            terms = terms | o.retrieve_terms()
        
        return sorted(list(terms))                   

class Diary(object):
    """ Stores the information from a diary.
    """
    
    def __init__(self, year, number, url):

        self._year = year
        self._number = number
        self._url = url
        self._sections = []
        
    def __str__(self):
        return "Diary: %d %d %s" % (self._year, self._number, self._url)
    
    __repr__ = __str__     
    
    @property
    def year(self):
        return self._year          
    
    @property
    def number(self):
        return self._number   
    
    @property
    def url(self):
        return self._url   
    
    @property
    def sections(self):
        return self._sections 
    
    @property
    def has_contents(self):
        
        return any([s.has_contents for s in self._sections])
    
    def show(self):
        
        print self
        
        for s in self.sections:
            s.show()
        
    def add_content(self, con_name):  
        
        if len(self._sections):
            current_section = self._sections[-1]      
            current_section.add_content(Content(con_name))
        else:
            print "ERROR: Adding content %s in Diary: %d %d" % \
                (con_name, self.year, self._number)
       
    def add_url(self, url):  
        
        if len(self._sections):
            current_section = self._sections[-1]      
            current_section.add_url(url)
        else:
            print "ERROR: Adding url %s in Diary: %d %d" % \
                (url, self.year, self._number)                
                        
    def add_org(self, org_name):
        
        if len(self._sections):
            current_section = self._sections[-1]      
            current_section.add_org(Organism(org_name))
        else:
            print "ERROR: Adding organization in Diary: %d %d" % \
                (self.year, self._number)                        
        
    def add_section(self, sec_name):
        
        self._sections.append(Section(sec_name))
        
    def retrieve_orgs(self):
        
        orgs = set()
        
        for s in self.sections:
            orgs = orgs | s.retrieve_orgs()
        
        return sorted(list(orgs))             
        
    def generate_terms(self):
        
        if len(self._sections):
            current_section = self._sections[-1]      
            current_section.generate_terms()
        else:
            print "ERROR: Generating terms in Diary: %d %d" % \
                (self.year, self._number)   
                
    def retrieve_terms(self):
        
        terms = set()
        
        for s in self.sections:
            terms = terms | s.retrieve_terms()
        
        return sorted(list(terms))     