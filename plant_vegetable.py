import water
def plant_carrot():
	# 在soil上种植胡萝卜
	if get_ground_type() == Grounds.Soil: # 土壤直接种
		plant(Entities.Carrot)
			
	if get_ground_type() == Grounds.Grassland: # 草地翻地再种
		till()
		plant(Entities.Carrot)
	return 1

def plant_tree(tag): # tag为0表示上次种了树，1表示上次种了灌木
	# 间隔种树和灌木
	if tag % 2 == 0:
		plant(Entities.Tree)
		return 1
	else:
		plant(Entities.Bush)
		return 0

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil: # 土壤直接种
		till()
		plant(Entities.Pumpkin)
		water.water(target)
			
	if not can_harvest(): # 草地翻地再种
		plant(Entities.Pumpkin)
		water.water(target)
	return 1