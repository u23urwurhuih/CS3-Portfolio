**Requirements:**

a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

i. Rat (鼠 / Shǔ)
ii. Ox (牛 / Niú)
iii. Tiger (虎 / Hǔ)
iv. Rabbit (兔 / Tù)
v. Dragon (龙 / Lóng)
vi. Snake (蛇 / Shé)
vii. Horse (马 / Mǎ)
viii. Goat (羊 / Yáng)
ix. Monkey (猴 / Hóu)
x. Rooster (鸡 / Jī)
xi. Dog (狗 / Gǒu)
xii. Pig (猪 / Zhū)

e. CONSIDER only the year of birth.

**CODE:**
a = int(input("Enter your birth year: "))
if a < 1900:
  print("Year of birth must not be earlier than the year 1900.")
else:
  k = (a-1900) %12
    
  if k == 1:
    chinese_zodiac_sign = "Rat (鼠 / Shǔ)"
  elif k == 2:
    chinese_zodiac_sign = "Ox (牛 / Niú)"
  elif k == 3:
    chinese_zodiac_sign = "Tiger (虎 / Hǔ)"
  elif k == 4: 
    chinese_zodiac_sign = "Rabbit (兔 / Tù)"
  elif k == 5:
    chinese_zodiac_sign = "Dragon (龙 / Lóng)"
  elif k == 6:
    chinese_zodiac_sign = "Snake (蛇 / Shé)"
  elif k == 7: 
    chinese_zodiac_sign = "Horse (马 / Mǎ)"
  elif k == 0:
    chinese_zodiac_sign = "Goat (羊 / Yáng)"
  elif k == 9:
    chinese_zodiac_sign = "Monkey (猴 / Hóu)"
  elif k == 10: 
    chinese_zodiac_sign = "Rooster (鸡 / Jī)"
  elif k == 11:
    chinese_zodiac_sign = "Dog (狗 / Gǒu)"
  elif k == 12: 
    chinese_zodiac_sign = "Pig (猪 / Zhū)"
  print(f"Your Chinese Zodiac Sign is: {chinese_zodiac_sign}")

**Screenshot:**
