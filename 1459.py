import re
x = '赞[0] 原文转发[1] 原文评论[2]'
pat1 = '赞[(\d+)] 原文转发[(\d+)] 原文评论[(\d+)]'
a1 = re.search(pat1, x)
print(a1.group(1))