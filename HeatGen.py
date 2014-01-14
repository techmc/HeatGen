#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  HeatGen.py
#  
#  Copyright 2013 Zassa Kavuma
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import random
import os

global pointlistarray
pointlistarray = []

def main():
	
	totalpoints = 200
	
	# Initialize files
	page_start = open('./page_start.txt', 'r')
	page_end = open('./page_end.txt', 'r')
	pyheatmap1 = open('./pythonheatmap1.html', 'w')
	pyheatmap2 = open('./pythonheatmap2.html', 'w')
	
	# Copy page_start to the html files
	for line in page_start.readlines():
		pyheatmap1.write(line)
		pyheatmap2.write(line)
	page_start.close()
	
	# Put the latitude and longitude coordinated of the centre of your 
	# map here (set to Brighton, UK by default)
	latitude = 50.8429
	longitude = -0.1313
	
	pointlist = [latitude, longitude, 'string', 0] # lat lon string flag
	
	# Generate random points using a Gaussian distribution
	for i in range(totalpoints):
		pointlist[0] = round(random.gauss(latitude, 0.005),6)
		pointlist[1] = round(random.gauss(longitude, 0.005), 6)
		pointlist[2] = "new google.maps.LatLng(" + str(pointlist[0]) + ", " + str(pointlist[1]) + "),\n"
		pointlist[3] = 0
		pointlistarray.append(list(pointlist))
		
	# Save all of the generated points to file 1
	for i in range(totalpoints):
		if pointlistarray[i][3] == 0:
			pyheatmap1.write(pointlistarray[i][2])
	
	# Use a mask to remove points from a region
	mask = 0.006
	for i in range(totalpoints):
		if (latitude-mask) <= pointlistarray[i][0] <= (latitude+mask):
			if (longitude-mask) <= pointlistarray[i][1] <= (longitude+mask):
				pointlistarray[i][3] = 1
	# Save all of the masked points to file 2
	for i in range(totalpoints):
		if pointlistarray[i][3] == 0:
			pyheatmap2.write(pointlistarray[i][2])
	
	# Finalize the html files
	for line in page_end.readlines():
		pyheatmap1.write(line)
		pyheatmap2.write(line)
	page_end.close()
	pyheatmap1.close()
	pyheatmap2.close()
	
	# Display the heatmap files using firefox
	os.system("firefox ./pythonheatmap2.html")
	os.system("firefox ./pythonheatmap1.html")
	
	return 0

if __name__ == '__main__':
	main()

