clear()
from judgement_canharv import judgement
from plant_carrot import plant_carrot
import water
while True:
	for i in range(get_world_size()):
		for j in range (get_world_size()):
			is_harvest = judgement() # 判断是否能收割

			water.water() # 浇水

			if i == 0: # 第0行种植胡萝卜
				plant_carrot()

			if i == 1 :
				plant(Entities.Bush)

			move(North)

		move(East)
	


