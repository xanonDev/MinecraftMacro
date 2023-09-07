import pyautogui  
import time
import keyboard 
while True:
	print("""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || |     ______   | || |  _______     | || |     ____     | |
| ||_   \  /   _|| || |     /  \     | || |   .' ___  |  | || | |_   __ \    | || |   .'    `.   | |
| |  |   \/   |  | || |    / /\ \    | || |  / .'   \_|  | || |   | |__) |   | || |  /  .--.  \  | |
| |  | |\  /| |  | || |   / ____ \   | || |  | |         | || |   |  __ /    | || |  | |    | |  | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  \  `--'  /  | |
| ||_____||_____|| || ||____|  |____|| || |   `._____.'  | || | |____| |___| | || |   `.____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
	   """)
	print("1.auto clicker mouse")
	print("2.spambot")
	choice = input("choice>")
	if choice=="1":
		print(" for the bot to start clicking click r \n if it should stop click z \n to go back to the selection click x \n to eat the food you have in slot 2 click c \n to auto clicking ctrl click v \n to throw a snowball or fireball press f to build automatically hold down")
		while True:
			time.sleep(0.01)
			if keyboard.is_pressed('r'):
				while True :
					pyautogui.doubleClick()
					keyboard.press("Space")
					if keyboard.is_pressed('z'):
						break
					else:
						if keyboard.is_pressed('c'):
							keyboard.press("2")
							pyautogui.drag(30, 0, 1.61, button='right')
							keyboard.press("1")
			else: 
				time.sleep(0.01)
				if keyboard.is_pressed('x'):
					break
				else:
					time.sleep(0.01)
					if keyboard.is_pressed('c'):
						keyboard.press("2")
						pyautogui.drag(30, 0, 1.61, button='right')
						keyboard.press("1")
					else:
						time.sleep(0.01)
						if keyboard.is_pressed('v'):
							while True:
								time.sleep(0.1)
								keyboard.press("shift")
								time.sleep(0.1)
								pyautogui.click(button='right')
								if keyboard.is_pressed('z'):
									break
						else:
							time.sleep(0.01)
							if keyboard.is_pressed('f'):
								keyboard.press("3")
								pyautogui.click(button='right')
								keyboard.press("1")




	else:
		if choice=="2":
			while True:
				message = input("message>")
				print("1.spam minecraft")
				print("2.normal spam")
				print("3.exit from spam bota")
				spammode = input("spam mode>")
				if spammode=="3":
					break
				czas = 0.1
				czas = input("how much should I spam? >")
				if spammode=="1":
					print("click r for the bot to start spamming, if it has to go back to the message writing stage, click z")
					keyboard.wait('r')
					while True:
						keyboard.press('t')
						time.sleep(float(czas))
						keyboard.write(message)
						time.sleep(float(czas))
						keyboard.press("Enter")
						time.sleep(float(czas))
						if keyboard.is_pressed('z'):
							break
				else:
					if spammode=="2":
						print("click r for the bot to start spamming, if it has to go back to the message writing stage, click z")
						keyboard.wait('r')
						while True:
							time.sleep(float(czas))
							keyboard.write(message)
							time.sleep(float(czas))
							keyboard.press("Enter")
							if keyboard.is_pressed('z'):
								break
