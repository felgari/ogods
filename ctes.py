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

"""Constants for ctesuse and to test ctesuse.
"""

NUM_ARGS = 3

MIN_NUMBER = 1
MAX_NUMBER = 300

MIN_YEAR = 2013 
MAX_YEAR = 2017

URL_BASE = 'http://juntadeandalucia.es/eboja/'

SECTIONS = {'s1': 'Disposiciones generales',
            's2.1': 'Nombramientos, situaciones e incidencias',
            's2.2': 'Oposiciones, concursos y otras convocatorias',
            's3': 'Otras disposiciones',
            's4': 'Administración de justicia',
            's5.1': 'Licitaciones públicas y adjudicaciones',
            's5.2': 'Otros anuncios oficiales'}

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
FORMATS_ACCEPTED = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
REQUEST_HEADERS = { "User-Agent": USER_AGENT, "Accept": FORMATS_ACCEPTED }

ENC_NAME = 'ascii'

ITEM_LABEL = "div"
ITEM_LABEL_DICT = {"class": "item"}
ORG_LABEL = "h3"
CONTENT_GROUP = "div"
CONTENT_LABEL = "p"
URL_LABEL = "a" 
URL_LABEL_DICT = {"class": "item_html"}
URL_ATTR = 'href'
