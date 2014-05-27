import pickledb

db = pickledb.load("db.db", False)

class DRI:
	pass

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

class Recipe:
	pass
	
class GA:
	pass
