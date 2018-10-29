#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:32:50 2018

@author: martinbensch
"""
import matplotlib.pyplot as plt

class grid:
    def __init__(self, size=None):
        if size is None:
            self.size = (8,8)
        else:
            self.size = size
        
    def draw_grid_arrow(self,policy, value_fct=None):
        """ Gets policy and visualizes it"""
        " Policy consists of state direciton pairs: "
        " e.g. policy = [ [x,y,'direction'],...], direction is given by a char "
        " direction: 'l','r','u' and 'd' "
        
        #Step through all fields 
        self.build_grid()
        for pi_s in policy:
            x,y, direction = pi_s
            self.draw_dir([x,y],direction)
            
        plt.show()
        
        
        
    def build_grid(self):
        """ Build a (n,n) grid with matplotlip """
        print(self.size)
        # Build horizontal lines
        # x coorinates list  is a tupel (0,1)
        h_lines = [[n-.5,n-.5] for n in range(self.size[0]+2)]
        for l in h_lines:
            plt.plot([-.5,self.size[1]+.5],l,'black')
        # Build vertical lines
        # y coordinates list is tupel (0,1)
        v_lines = [[n-.5,n+.5] for n in range(self.size[1]+2)]
        for l in h_lines:
            plt.plot(l,[-.5,self.size[0]+.5],'black')
   
    
    def draw_dir(self,cords, direction):
        """Draws an direction to the grid"""
        " Cords is the field tupel and direction is a character r,l,u,d "
        x_dir = {
                'l': self.l_dir,
                'r': self.r_dir,
                'u':self.up_dir,
                'd':self.dw_dir,
                }

        if  (cords[0] in range(0,self.size[0])) and \
            (cords[1] in range(0,self.size[1])) and \
            (direction in ['l','r','u','d']):    
                x_dir[direction](cords)
        else:
            raise Exception('From draw_arrow(): cords out of grid range')
                
        
    def l_dir(self, cords):
        x,y = cords
        x_l, y_l = x - 0.25, y
        plt.plot([x,x_l],[y,y_l],'b')
        #plt.show()
        
    def r_dir(self,cords):
        x,y = cords
        x_l, y_l = x + 0.25, y
        plt.plot([x,x_l],[y,y_l],'r')
        #plt.show()
    
    def up_dir(self,cords):
        x,y = cords
        x_l, y_l = x, y+0.25
        plt.plot([x,x_l],[y,y_l],'orange')
        #plt.show()
        
    def dw_dir(self,cords):
        x,y = cords
        x_l, y_l = x, y-0.25
        plt.plot([x,x_l],[y,y_l],'green')
        #plt.show()
        
    
a = grid()
direction = ['r','r','l','l','u','u','d','d']
policy = [[idx,idx,d] for idx,d in enumerate(direction)]
print(policy)
a.draw_grid_arrow(policy)