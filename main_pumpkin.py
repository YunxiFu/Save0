clear() # 清屏
# import plant_vegetable
import water

list = [North,East,South,West]
target = [Entities.Carrot, Entities.Tree,Entities.Pumpkin] # 需要浇水的作物类型列表

step = 0 # 步数计数器

# def circle(n,m,j): # n为当前圈数，m为当前方向，j为当前收割数
# 	while True:
# 		for i in range(n + 1):
# 			if get_ground_type() != Grounds.Soil: # 土壤直接种
# 				till()
# 				plant(Entities.Pumpkin)
# 				water.water(target)

# 			if not can_harvest(): 
# 				plant(Entities.Pumpkin)
# 				water.water(target)
# 				j = 0
# 			else:
# 				j = j + 1

# 			move(list[m])
# 		m = (m + 1) % 4

# 		if get_pos_x() == 0 and get_pos_y() == 0 and j >= (n + 1) * 4: # 收割判断
# 			n = (n + 1) % 7
# 			if n == 0:
# 				harvest()

# clear()
# circle(0,0,0)

def circle(n,m,j): # n为当前圈数起始为1，m为当前方向，j为当前收割数
	step = 0 # 步数计数器

	while True:		
		for i in range(n):
			step = step + 1 # 步数计数器
			if get_ground_type() != Grounds.Soil: # 土壤直接种
				till()
				plant(Entities.Pumpkin)
				water.water(target)
			else:
				if not can_harvest(): 
					plant(Entities.Pumpkin)
					water.water(target)
					j = 0
				else:
					j = j + 1
			move(list[m])

			if step == n : # 走完一条边
				step = 0
				m = (m + 1) % 4 #
			
			quick_print("n:",n,"m:",m,"j:",j) # 调试用输出当前圈数、方向和收割数
				

		if j >= (n * 4) - 1 and get_pos_x() == 0 and get_pos_y() == 0: # 圈数判断
			n = n + 1 # 增加圈数
			j = 0 # 
			
		if n == 6: # 走完六圈后收割
			harvest()
			n = 1 # 重置圈数

circle(1,0,0)



				

		
		
