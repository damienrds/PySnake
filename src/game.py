# *-* coding: utf-8 *-*
# -------------------------------------------------------------------------------------------------
#   @AUTHOR:    Damien RUDAS
#   @FILE:      grid.py
#   @DATE:      05/11/2023
#   @VERSION:   1.0
#   @DESC:      Class for game managment
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
import threading

import grid
import snake

from keyboard import is_pressed
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class game( ):
    
    def __init__( self ):
        
        kSize = ( 20, 20 )
        self.kDelay = 1.5
        self.Continue = True
        self.GameOver = False
        
        self.nextMove = "up"
        
        self.oGrid = grid.grid( kSize )
        self.oGrid.displayGrid( )
        
        self.oSnake = snake.snake( )
        self.oSnake.addPosition( kSize[ 0 ] // 2, kSize[ 1 ] // 2 )
        self.oGrid.displaySnake( self.oSnake.position, "up" )
        self.oGrid.displayGrid( )
        
        return
    
    def waitingDelay( self, inTime ):
        time.sleep( inTime )
        self.Continue = False
        
    def waitingMove( self ):
        vThread = threading.Thread( target = self.waitingDelay, args = ( self.kDelay, ) )
        vThread.start( )
        while self.Continue:
            if is_pressed( "z" ):
                self.nextMove = "up"
                vThread.join( )
                return
            
            if is_pressed( "q" ):
                self.nextMove = "left"
                vThread.join( )
                return
            
            if is_pressed( "s" ):
                self.nextMove = "down"
                vThread.join( )
                return
            
            if is_pressed( "d" ):
                self.nextMove = "right"
                vThread.join( )
                return
            
            if is_pressed( "p" ):
                self.nextMove = "STOP"
                vThread.join( )
                return
        
        vThread.join( )
        self.Continue = True
        return
    
    def Move( self ):
        self.waitingMove( )
        
        match self.nextMove:
            case "STOP":
                self.GameOver = True
                
            case "up":
                self.oSnake.position[ 0 ][ 0 ] -= 1
            case "down":
                self.oSnake.position[ 0 ][ 0 ] += 1
            case "left":
                self.oSnake.position[ 0 ][ 1 ] -= 1
            case "right":
                self.oSnake.position[ 0 ][ 1 ] += 1
                
        self.oGrid.displaySnake( self.oSnake.position, self.nextMove )
        self.oGrid.displayGrid( )
        
    def gameSequence( self ):
        self.Move( )
        self.oGrid.initGrid( )
        self.oGrid.displaySnake( self.oSnake.position, self.nextMove )
        self.oGrid.displayGrid( )