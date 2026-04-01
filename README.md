How to use it :
---------------------------------------------------
import loading_bar as ld

total = your number (I recommend 50, this is the speed of the loading)

for i in range(total + 1):
	ld.bar(i, total, prefix="loading", length=30)
