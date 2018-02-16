#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################################
#   PARTICLE MODULE
#########################################################################################

#========================================================================================
#		IMPORTS
#========================================================================================
from nephila import *

#========================================================================================
#		MODULE CONFIGURATION
#========================================================================================
confmech=loadconf("particlesrc")

#========================================================================================
#		MODULE COMPATIBILITY
#========================================================================================
from main import *

#========================================================================================
#		PARTICLES CLASS
#========================================================================================
class particles(object):
    """Planet class
    
    Class of rocky planets
    
    Attributes
    ----------
    snapshot : int
      Snapshot number.
    
    type : int array
      Type of particle to be load 

    """
    #************************************************************************************
    #	ATTRIBUTES
    #************************************************************************************
    #General properties
    snapshot = 0
    type=[0,]
    
    #************************************************************************************
    #	METHODS
    #************************************************************************************
    def __init__(self,**kwargs):
        #Set attributes using: default and argument values
        updatedic(self.__dict__,particles.__dict__,**kwargs)
                    
        #Set global properties
        if self.M is None:
            self.M=self.mrvec[-1]
        else:
            self.mrvec[-1]=self.M
        #Set properties vector according to urvec
        if len(self.urvec)>2:
            for func in self.funcs+['c']:
                if len(self.__dict__["%svec"%func])==2:
                    ini=self.__dict__["%svec"%func][0]
                    end=self.__dict__["%svec"%func][-1]
                    self.__dict__["%svec"%func][1:-1]=[ini]*(len(self.urvec)-2)
                    self.__dict__["%svec"%func][0]=ini
                    self.__dict__["%svec"%func][-1]=end
        #Verify size of property vectors
        lu=len(self.urvec)
        for func in self.funcs:
            if func=='urvec':continue
            lp=len(self.__dict__["%svec"%func])
            if lp!=lu:
                error("Property vector '%s' has a length (%d) different than urvec (%d)"%(func,lp,lu))
        #Set interpolant functions
        self.resetinterp()
