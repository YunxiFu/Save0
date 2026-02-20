def water(target):
	staus = get_water()
	type = get_entity_type()

	if type in target: # 如果作物类型在目标列表中
		while staus <= 0.25: # 水分低于25%时浇水
			use_item(Items.Water)
			staus = get_water()
	return 1