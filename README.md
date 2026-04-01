How to use it :
---------------------------------------------------
import loading_bar as ld

total = your number (I recommend 50, this is the speed of the loading)

for i in range(total + 1):
	ld.bar(i, total, prefix="loading", length=30)
	time.sleep(0.05)

<img width="275" height="29" alt="image" src="https://github.com/user-attachments/assets/9e54818f-7eb5-48d7-8cbf-2e5f5aad77a6" />

