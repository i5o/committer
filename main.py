import os
a = 0
while a < 1000000:
	d = open("README.md", "r").read()
	d += "Commit %d\n" % a
	open("README.md", "w").write(d)
	os.system("git add . &&  git commit -m 'test' --date='Fri April 08 00:00 2050 +0300'")
	a += 1
