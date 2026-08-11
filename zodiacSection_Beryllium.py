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
