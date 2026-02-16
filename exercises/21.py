class_a = {'小明', '小红', '小刚', '小华', '小丽'}
class_b = {'小红', '小军', '小华', '小芳', '小强'}

both_class =(class_a & class_b)
all_class =(class_a | class_b)
only_A = (class_a - class_b)
only_one_class =( class_a ^class_b)
print (both_class,all_class,only_A,only_one_class)