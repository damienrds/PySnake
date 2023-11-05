# *-* coding: utf-8 *-*
# -------------------------------------------------------------------------------------------------
#   @AUTHOR:    Damien RUDAS
#   @FILE:      grid.py
#   @DATE:      05/11/2023
#   @VERSION:   1.0
#   @DESC:      Class for grid managment
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

import snake
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class grid( ):
    def __init__( self, inSize ):
        self.length = inSize[ 0 ]
        self.width = inSize[ 1 ]
        self.grid = [ ]
        self.initGrid( )
        
        self.apple = "*"
        
    def initGrid( self ):
        self.grid = [ [ " . " for i in range( self.length ) ] for j in range( self.width ) ]
        
    def displayGrid( self ):
        sys.stdout.write( "\033[2J\033[1;1H" )
        for i in range( self.width ):
            for j in range( self.length ):
                print( self.grid[ i ][ j ], end = "" )
            print( "" )
            
    def displaySnake( self, inPosition, inDirection):
        for lLength, lWidth in inPosition:
            self.grid[ lLength ][ lWidth ] = snake.kBody
                
        match inDirection:
            case "up":
                self.grid[ inPosition[ 0 ][ 0 ] ][ inPosition[ 0 ][ 1 ] ] = snake.kUpHead
            case "down":
                self.grid[ inPosition[ 0 ][ 0 ] ][ inPosition[ 0 ][ 1 ] ] = snake.kDownHead
            case "left":
                self.grid[ inPosition[ 0 ][ 0 ] ][ inPosition[ 0 ][ 1 ] ] = snake.kLeftHead
            case "right":
                self.grid[ inPosition[ 0 ][ 0 ] ][ inPosition[ 0 ][ 1 ] ] = snake.kRightHread
            case _:
                self.grid[ inPosition[ 0 ][ 0 ] ][ inPosition[ 0 ][ 1 ] ] = snake.kUpHead
        
        