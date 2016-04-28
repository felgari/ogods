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

"""Some utilities to manage web pages.
"""

from ctes import URL_BASE, SECTIONS
from wscrap import WScrap
from diary import Diary

def compose_url(*args):
    """Compose a url using the arguments received as parts of these.
    """
    
    return "/".join(str(x).rstrip('/') for x in args)

def _retrieve_from_diary(year, number):
    """Retrieve the data from the data indicated.
    """
    
    url_base = compose_url(URL_BASE, year, number)
    
    dia = Diary(year, number, url_base)    
    
    print "Retrieving contents from: %s" % url_base
    
    for section in sorted(SECTIONS.keys()):
        url = compose_url(url_base, section)
        
        dia.add_section(SECTIONS[section])
        
        WScrap.scrap_page(url, dia)
        
    return dia
        
def retrieve_diary(year, number):
    """Retrieve the data in the diary whose year and number are indicated.
    """

    dia = _retrieve_from_diary(year, number)
    
    if dia.has_contents:
        dia.show()
    else:
        print "Diary %d %d hasn't any content." % (year, number)

    return 0

def retrieve_terms(year, number):
    """Retrieve the terms of the diary whose year and number are indicated.
    """
    
    dia = _retrieve_from_diary(year, number)
    
    dia.generate_terms()

    return 0

def retrieve_orgs(year, number):
    """Retrieve the organisms of the diary whose year and number are indicated.
    """    
    
    dia = _retrieve_from_diary(year, number)
    
    orgs = dia.retrieve_orgs()
    
    print "Organisms"
    
    for o in orgs:
        print o

    return 0 