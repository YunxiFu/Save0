def plant_carrot():
	# 在soil或grassland上种植胡萝卜
	if get_ground_type() == Grounds.Soil: # 土壤直接种
		plant(Entities.Carrot)
			
	if get_ground_type() == Grounds.Grassland: # 草地翻地再种
		till()
		plant(Entities.Carrot)
	return 1