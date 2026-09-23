class Food:
  def __init__(self, category, is_healthy):
    self.value = category
    self.value2 = is_healthy

class Rice(Food):
  def __init__(self, category, weight, brand):
    super().__init__(category)
      self.extra = weight
      self.extra2 = brand
