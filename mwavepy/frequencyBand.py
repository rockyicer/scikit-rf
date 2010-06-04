'''
#       frequencyBand.py
#       
#       Copyright 2010 alex arsenovic <arsenovic@virginia.edu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later versionpy.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
'''
from pylab import linspace, gca


class frequencyBand:
	'''
	represents a frequency band. 
	
	attributes:
		start: starting frequency  (in Hz)
		stop: stoping frequency  (in Hz)
		npoints: number of points, an int
		unit: unit which to scale a formated axis, when accesssed. see
			formattedAxis
		
	frequently many calcluations are made in a given band , so this class 
	is used in other classes so user doesnt have to continually supply 
	frequency info.
	'''
	freqUnitDict = {\
		'hz':'Hz',\
		'mhz':'MHz',\
		'ghz':'GHz'\
		}
	freqMultiplierDict={
		'hz':1,\
		'mhz':1e6,\
		'ghz':1e9\
		}
	def __init__(self,start, stop, npoints, unit='hz'):
		'''
		takes:
			start: start of band.  units of unit, defaults is  Hz
			stop: end of band. units of unit, defaults is  Hz
			npoints: number of points in the band. 
			unit: unit you want the band in for plots. a string. can be:
				'hz', 'mhz','ghz', 
		
		example:
			wr1p5band = frequencyBand(500,750,401, 'ghz')
			
		note: unit sets the property freqMultiplier, which is used 
		to scale the frequncy when formatedAxis is referenced.
			
		'''
		self._unit = unit
		self.start =  self.multiplier * start
		self.stop = self.multiplier * stop
		self.npoints = npoints
		
		
	@property
	def unit(self):
		'''
		The unit to format the frequency axis in. see formatedAxis
		'''
		return self.freqUnitDict[self._unit]
	@unit.setter
	def unit(self,newUnit):
		self._unit = newUnit.lower()
	@property
	def multiplier(self):
		'''
		multiplier for formating axis
		'''
		return self.freqMultiplierDict[self.unit.lower()]
	@property
	def	axis(self):
		'''
		returns a frequency axis scaled to the correct units
		the unit is stored in freqDict['freqUnit']
		'''
		return linspace(self.start,self.stop,self.npoints)
	@property
	def	formatedAxis(self):
		'''
		returns a frequency axis scaled to the correct units
		the unit is stored in freqDict['freqUnit']
		'''
		return linspace(self.start,self.stop,self.npoints)\
			/self.multiplier
		
	def labelXAxis(self, ax=None):
		if ax is None:
			ax = gca()
		ax.set_xlabel('Frequency [%s]' % self.unit )
	