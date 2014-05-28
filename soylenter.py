class Attribute():
	def __init__(self, name, minimum=0, maximum=9999999, target=0):
		self.name = name
		self.minimum = minimum
		self.maximum = maximum
		self.target = target

class DRI:
	def __init__(self, name):
		# custom to me; needs to be abstracted!
		self.name = "Josh.0"
		self.calories = Attribute("Calories", target=2000)
		self.carbohydrates = Attribute("Carbohydrates", target=129)
		self.protein = Attribute("Protein", target=207)
		self.total_fat = Attribute("Total fat", target=80)
		self.saturated_fat = Attribute("Saturated fat", target=25)
		self.monounsaturated_fat = Attribute("Monounsaturated fat", target=25)
		self.polyunsaturated_fat = Attribute("Polyunsaturated fat", target=25)
		self.omega3_fatty_acids = Attribute("Omega-3 fatty acids", target=1.6)
		self.omega6_fatty_acids = Attribute("Omega-6 fatty acids", target=17)
		self.total_fiber = Attribute("Total fiber", target=21)
		self.soluble_fiber = Attribute("Soluble fiber", target=11)
		self.insoluble_fiber = Attribute("Insoluble fiber", target=10)
		self.cholesterol = Attribute("Cholesterol", target=0)
		self.vitamin_a = Attribute("Vitamin A", target=3000, maximum=10000)
		self.vitamin_b6 = Attribute("Vitamin B6", target=1.3, maximum=100)
		self.vitamin_b12 = Attribute("Vitamin B12", target=2.4)
		self.vitamin_c = Attribute("Vitamin C", target=90, maximum=2000)
		self.vitamin_d = Attribute("Vitamin D", target=600, maximum=4000)
		self.vitamin_e = Attribute("Vitamin E", target=20, maximum=1000)
		self.vitamin_k = Attribute("Vitamin K", target=120)
		self.thiamin = Attribute("Thiamin", target=1.2)
		self.riboflavin = Attribute("Riboflavin", target=1.3)
		self.niacin = Attribute("Niacin", target=16, maximum=35)
		self.folate = Attribute("Folate", target=400, maximum=1000)
		self.pantothenic_acid = Attribute("Pantothenic acid", target=5)
		self.biotin = Attribute("Biotin", target=30)
		self.choline = Attribute("Choline", target=550, maximum=3500)
		self.calcium = Attribute("Calcium", target=1, maximum=2.5)
		self.chloride = Attribute("Chloride", target=2.3, maximum=3.6)
		self.chromium = Attribute("Chromium", target=35)
		self.copper = Attribute("Copper", target=0.9, maximum=10)
		self.iodine = Attribute("Iodine", target=150, maximum=1100)
		self.iron = Attribute("Iron", target=8, maximum=45)
		self.magnesium = Attribute("Magnesium", target=420)
		self.manganese = Attribute("Manganese", target=2.3, maximum=11)
		self.molybdenum = Attribute("Molybdenum", target=45, maximum=2000)
		self.phosphorus = Attribute("Phosphorus", target=0.7, maximum=4)
		self.potassium = Attribute("Potassium", target=3.5)
		self.selenium = Attribute("Selenium", target=55, maximum=400)
		self.sodium = Attribute("Sodium", target=1.5, maximum=2.3)
		self.sulfur = Attribute("Sulfur", target=2)
		self.zinc = Attribute("Zinc", target=11, maximum=40)

class Ingredient:
	def __init__(self, name_):
		self.name = name_
		self.calories = float(raw_input("Calories (kcal): "))
		self.carbohydrates = float(raw_input("Carbohydrates (g): "))
		self.protein = float(raw_input("Protein (g): "))
		self.total_fat = float(raw_input("Total fat (g): "))
		self.saturated_fat = float(raw_input("Saturated fat (g): "))
		self.monounsaturated_fat = float(raw_input("Monounsaturated fat (g): "))
		self.polyunsaturated_fat = float(raw_input("Polyunsaturated fat (g): "))
		self.omega3_fatty_acids = float(raw_input("Omega-3 fatty acids (g): "))
		self.omega6_fatty_acids = float(raw_input("Omega-6 fatty acids (g): "))
		self.total_fiber = float(raw_input("Total fiber (g): "))
		self.soluble_fiber = float(raw_input("Soluble fiber (g): "))
		self.insoluble_fiber = float(raw_input("Insoluble fiber (g): "))
		self.cholesterol = float(raw_input("Cholesterol (mg): "))
		self.vitamin_a = float(raw_input("Vitamin A (IU): "))
		self.vitamin_b6 = float(raw_input("Vitamin B6 (mg): "))
		self.vitamin_b12 = float(raw_input("Vitamin B12 (ug): "))
		self.vitamin_c = float(raw_input("Vitamin C (mg): "))
		self.vitamin_d = float(raw_input("Vitamin D (IU): "))
		self.vitamin_e = float(raw_input("Vitamin E (IU): "))
		self.vitamin_k = float(raw_input("Vitamin K (ug): "))
		self.thiamin = float(raw_input("Thiamin (mg): "))
		self.riboflavin = float(raw_input("Riboflavin (mg): "))
		self.niacin = float(raw_input("Niacin (mg): "))
		self.folate = float(raw_input("Folate (ug): "))
		self.pantothenic_acid = float(raw_input("Pantothenic acid (mg): "))
		self.biotin = float(raw_input("Biotin (ug): "))
		self.choline = float(raw_input("Choline (mg): "))
		self.calcium = float(raw_input("Calcium (g): "))
		self.chloride = float(raw_input("Chloride (g): "))
		self.chromium = float(raw_input("Chromium (ug): "))
		self.copper = float(raw_input("Copper (mg): "))
		self.iodine = float(raw_input("Iodine (ug): "))
		self.iron = float(raw_input("Iron (mg): "))
		self.magnesium = float(raw_input("Magnesium (mg): "))
		self.manganese = float(raw_input("Manganese (mg): "))
		self.molybdenum = float(raw_input("Molybdenum (ug): "))
		self.phosphorus = float(raw_input("Phosphorus (g): "))
		self.potassium = float(raw_input("Potassium (g): "))
		self.selenium = float(raw_input("Selenium (ug): "))
		self.sodium = float(raw_input("Sodium (g): "))
		self.sulfur = float(raw_input("Sulfur (g): "))
		self.zinc = float(raw_input("Zinc (mg): "))
		
		self.attributes = [
			self.calories,
			self.carbohydrates,
			self.protein,
			self.total_fat,
			self.saturated_fat,
			self.monounsaturated_fat,
			self.polyunsaturated_fat,
			self.omega3_fatty_acids,
			self.omega6_fatty_acids,
			self.total_fiber,
			self.soluble_fiber,
			self.insoluble_fiber,
			self.cholesterol,
			self.vitamin_a,
			self.vitamin_b6,
			self.vitamin_b12,
			self.vitamin_c,
			self.vitamin_d,
			self.vitamin_e,
			self.vitamin_k,
			self.thiamin,
			self.riboflavin,
			self.niacin,
			self.folate,
			self.pantothenic_acid,
			self.biotin,
			self.choline,
			self.calcium,
			self.chloride,
			self.chromium,
			self.copper,
			self.iodine,
			self.iron,
			self.magnesium,
			self.manganese,
			self.molybdenum,
			self.phosphorus,
			self.potassium,
			self.selenium,
			self.sodium,
			self.sulfur,
			self.zinc,
		]

class Recipe:
	def __init__(self, ingredients=[], dri=global_dri):
		self.ingredients = ingredients
		self.dri = dri
		
	def fitness_score():
		total_points_possible = 0.0
		earned_points = 0.0
		
		for ingredient in self.ingredients:
			if ingredient in dri.allergens:
				return 0.0
			
			for attribute in ingredient.attributes:
				if attribute > dri.attribute.minimum and attribute < dri.attribute.maximum:
					adjusted_attribute = 0.0
					
					if attribute > dri.attribute.target:
						adjusted_attribute = attribute - 2 * (attribute - dri.attribute.target)
						earned_points += float(adjusted_attribute) / float(dri.attribute.target)
					else:
						earned_points += float(attribute) / float(dri.attribute.target)
					
				total_points_possible += 1.0
				
		return earned_points / total_points_possible
		
	def DNA_first_half():
		return self.ingredients[:len(self.ingredients)/2]
		
	def DNA_second_half():
		return self.ingredients[len(self.ingredients)/2:]
	
class GA:
	"""
	Classes on which this genetic algorithm can work
	must implement three methods:
		fitness_score()
		DNA_first_half()
		DNA_second_half()
	"""
	
	def __init__(self, population_class=None, population_size=100, mutability=0.01, fitness_threshold=0.90):
		self.population_class = population_class
		self.population_size = population_size
		self.mutability = mutability
		self.fitness_threshold = fitness_threshold
		
		self.population = []
		
		for i in range(0, population_size):
			self.population.append(population_class())
		
	def evolve(self):
		unfit = True
		winner = None
		
		while unfit:
			# test individual fitness
			scores = []
			
			for individual in self.population:
				score = individual.fitness_score()
				print score
				
				if score > self.fitness_threshold:
					winner = individual
					unfit = False
					
				scores.append([score, individual])
				
			# select fittest individuals
			scores.sort()
			scores.reverse()
			
			fittest = scores[:0.25*len(scores)]
			
			# mate fittest individuals
			children = []
			
			while len(children) < len(self.population):
				p1 = fittest[random.randint(0, len(fittest)-1)]
				p2 = fittest[random.randint(0, len(fittest)-1)]
				
				child_DNA = []
				
				for thing in p1.DNA_first_half():
					if random.random() < mutability:
						# add random ingredient
					else:
						child_DNA.append(thing)
						
				for thing in p2.DNA_second_half():
					if random.random() < mutability:
						# add random ingredient
					else:
						child_DNA.append(thing)
				
				child = self.population_class(child_DNA)
				children.append(child)
				
			self.population = children
			
		return winner

global_dri = DRI()
ga = GA()
winner = ga.evolve()
print winner
