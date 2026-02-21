clear() # 清屏
# import plant_vegetable
import water

list = [North,East,South,West]
target = [Entities.Carrot, Entities.Tree,Entities.Pumpkin] # 需要浇水的作物类型列表

def circle(n,m,j):
	while True:
		for i in range(n + 1):
			if get_ground_type() != Grounds.Soil: # 土壤直接种
				till()
				plant(Entities.Pumpkin)
				water.water(target)

			if not can_harvest(): 
				plant(Entities.Pumpkin)
				water.water(target)
				j = 0
			else:
				j = j + 1

			move(list[m])
		m = (m + 1) % 4

		if get_pos_x() == 0 and get_pos_y() == 0 and j >= (n + 1) * 4: # 收割判断
			n = (n + 1) % 7
			if n == 0:
				harvest()

clear()
circle(0,0,0)


