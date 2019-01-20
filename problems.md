# Python基础学习
Python基础学习阶段问题记录
1. 关于map()和reduce()问题
	```
	from functools import reduce

	def fn(x, y):
		return x * 10 + y

	def char2num(s):
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[s]

	reduce(fn, map(char2num, '13579'))
	```
    输出：```13579```

    + **问题：**这边倒数第一行 map(char2num, '13579') 返回的应该是一个 iterator 可是 reduce的第二个参数要是一个list 那不是应该对map(char2num, '13579')用list()转换一下吗？
    + **答案：** reduce需要传入两个参数：函数和序列。reduce第二个参数是序列，序列包含list。其次，map()传入的第一个参数是函数对象本身，结果是一个Iterator，Iterator是惰性序列。所以，对map()的结果不需要进行list()转换。
    + Reference：
    	- [廖雪峰的官方网站 map/reduce](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000)
    	- [廖雪峰的官方网站 迭代器](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000)