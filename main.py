clear()

import judgement_canharv 
import plant_carrot 
import water 

target = [Entities.Carrot, Entities.Tree] # 需要浇水的作物类型列表

while True:
	for x in range(get_world_size()):
		for y in range (get_world_size()):
			is_harvest = judgement_canharv.judgement() # 判断是否能收割

			if x == 0 or x == 5: # 第0行或第5行种植胡萝卜和树
				if y % 2 == 0: # 偶数行种植胡萝卜
					plant_carrot.plant_carrot() # 种植胡萝卜

				else: # 奇数行种植树
					plant(Entities.Tree)
			
			if y == 0 or y == 5: # 第0列或第5列种植胡萝卜和树
				if x % 2 == 0: # 偶数列种植胡萝卜
					plant_carrot.plant_carrot() # 种植胡萝卜

				else: # 奇数列种植树
					plant(Entities.Tree)

			if x == 1 or x == 4: # 第1行或第4行种植灌木
				plant(Entities.Bush)
			
			water.water(target) # 浇水

			move(North)

		move(East)
	


