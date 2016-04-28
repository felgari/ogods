# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This file is part of kuicl: https://github.com/felgari/ogods
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

"""Process the program arguments received by the main function.

Define the arguments available, check for its correctness and coherence, 
and provides these arguments to other modules. 
"""

import argparse

from ctes import MIN_NUMBER, MAX_NUMBER, MIN_YEAR, MAX_YEAR

class ProgramArgumentsException(Exception):
    
    def __init__(self, msg):
        
        self._msg = msg
        
    def __str__(self):
        return self._msg

class ProgramArguments(object):
    """Encapsulates the definition and processing of program arguments.    
    """                   
    
    def __init__(self):
        """Initializes parser. 
        """               
            
        # Initialize arguments of the parser.
        self.__parser = argparse.ArgumentParser()  
        
        self.__parser.add_argument("-n", dest="n", metavar="number",
                                   help="Number of first diary to explore.",
                                   type=int, 
                                   choices=xrange(MIN_NUMBER, MAX_NUMBER))              

        self.__parser.add_argument("-y", dest="y", metavar="year",
                                   help="Number of the year to explore.",
                                   type=int, 
                                   choices=xrange(MIN_YEAR, MAX_YEAR))
        
        self.__parser.add_argument("-t", dest="t", action="store_true", 
                                   help="Retrieve terms.")       
        
        self.__parser.add_argument("-o", dest="o", action="store_true", 
                                   help="Retrieve organizations.")  
        
        self.__parser.add_argument("-f", dest="f", action="store_true", 
                                   help="Force the retrieving of all numbers.")          
        
        self.__args = self.__parser.parse_args()
        
    @property    
    def number_provided(self): 
        return MIN_NUMBER <= self.__args.n <= MAX_NUMBER 
    
    @property    
    def year_provided(self): 
        return MIN_YEAR <= self.__args.y <= MAX_YEAR         
        
    @property
    def number(self):
        return self.__args.n     
    
    @property
    def year(self):
        return self.__args.y          
    
    @property
    def retrieve_terms(self):
        return self.__args.t     
    
    @property
    def retrieve_orgs(self):
        return self.__args.o               
 
    def print_usage(self):
        """Print arguments options.
        
        """
                
        self.__parser.print_usage()     
        
    def print_help(self):
        """Print help for arguments options.
        
        """
                
        self.__parser.print_help()  