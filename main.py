clear()
from judgement_canharv import judgement
while True:
	for i in range(3):
		for j in range (3):
			is_harvest = judgement() # 判断是否能收割

			if i == 0: # 第0行种植胡萝卜
				
				if get_ground_type() == Entities.Carrot: # 是否为胡萝卜地
					if is_harvest or get_ground_type() == Grounds.Soil: # 判断是否需要重新种植
						plant(Entities.Carrot)
				else:
					if is_harvest:
						till()
						plant(Entities.Carrot)

			if i == 1 :
				plant(Entities.Bush)

			move(North)

		move(East)
	
	


