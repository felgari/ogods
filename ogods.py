#!/usr/bin/env python
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

"""Script to retrieve information from a web site and populate a database
with the information of interest to perform searches based on the semantics of
the data.
"""

import sys

from oparser import ProgramArguments
from wutil import retrieve_terms, retrieve_orgs, retrieve_diary

if __name__ == "__main__":
    
    # Object to process the program arguments.
    progargs = ProgramArguments()  
    
    # Perform the action indicated by program arguments.
    if progargs.year_provided and progargs.number_provided:     
        if progargs.retrieve_terms:
            sys.exit(retrieve_terms(progargs.year, progargs.number))
        elif progargs.retrieve_orgs:
            sys.exit(retrieve_orgs(progargs.year, progargs.number))
        else:
            sys.exit(retrieve_diary(progargs.year, progargs.number))
        
    else:
        progargs.print_help()
            
        sys.exit(1)