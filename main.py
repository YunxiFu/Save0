clear()

import judgement_canharv 
import plant_vegetable
import water 

target = [Entities.Carrot, Entities.Tree,Entities.Pumpkin] # 需要浇水的作物类型列表



while True:
	for x in range(get_world_size()):
		for y in range (get_world_size()):

			is_harvest = judgement_canharv.judgement() # 判断是否能收割

			plant_vegetable.plant_carrot() # 种植胡萝卜用

			# tag = get_pos_x() + get_pos_y() # 用于判断上次种了树还是灌木
			# plant_vegetable.plant_tree(tag) # 种植树或灌木
			# quick_print(tag)
			


			# water.water(target) # 浇水

			move(North)
		move(East)


