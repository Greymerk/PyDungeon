from tunnelnode import TunnelNode
from math import sqrt
from random import choice

class Maze(object):

	def __init__(self, origin):
		self.nodes = []
		self.maxNodes = 80
		self.maxRange = 300
		self.scatter = 20		
		self.origin = origin
		self.start = TunnelNode(self)
		self.nodes.append(self.start)
		self.end = None

	def update(self):
		for node in self.nodes:
			node.update()
			
		if self.end is None:
			done = True		
			for node in self.nodes:
				if not node.isDone():
					done = False
				
			if done:
				self.end = choice(self.nodes[1:])
	
	def draw(self, surface):
		for node in self.nodes:
			node.draw(surface)
		
		self.start.draw(surface, (0,0,255))
		
		if not self.end is None:
			self.end.draw(surface, (0, 255, 0))
			
		
	def spawnNode(self, builder):
	
		newNode = TunnelNode(self, builder)
		self.nodes.append(newNode)
		return newNode

	
	
	def hasNearbyNode(self, position):
	
		for node in self.nodes:
			xrel = abs(node.position.x - position.x)
			yrel = abs(node.position.y - position.y)
		
			dist = sqrt(xrel ** 2 + yrel ** 2)
				
			if dist < self.scatter:
				return True
				
		return False
		
	def inRange(self, position):
	
			if len(self.nodes) == 0:
				return True
	
			xrel = abs(self.start.position.x - position.x)
			yrel = abs(self.start.position.y - position.y)
		
			dist = sqrt(xrel ** 2 + yrel ** 2)
						
			return dist < self.maxRange
			
	def full(self):
		return len(self.nodes) >= self.maxNodes
				
				
	def __iter__(self):
		return iter(self.nodes)