# *-* coding: utf-8 *-*
# -------------------------------------------------------------------------------------------------
#   @AUTHOR:    Damien RUDAS
#   @FILE:      snake.py
#   @DATE:      05/11/2023
#   @VERSION:   1.0
#   @DESC:      Class for snake managment
# 
# 
#   Release:    
#       Version    Date           Description
#       ---------------------------------------------------------------
#       1.0        05/11/2023     Creation of this script
#
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# -- Import section
# -------------------------------------------------------------------------------------------------
import os
import time
import sys

# -------------------------------------------------------------------------------------------------
kUpHead = " ▲ "
kDownHead = " ▼ "
kLeftHead = " ◀ "
kRightHread = " ▶ "

kBody = " ■ "

# -------------------------------------------------------------------------------------------------
class snake( ):
    def __init__( self ):
        self.position = [ ]
        
        return
    
    def addPosition( self, inLength, inWidth):
        self.position.append( [ inLength, inWidth ] )