from stanfordkarel import *

class ktools:
  def m(self):
    """Shorthand for move"""
    move()  

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m3()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m3()
    self.m()
    
  def m3(self):
    """Move 3 Spaces"""
    self.m()
    self.m()
    self.m()

  def fic(self):
    """Front is Clear"""
    return front_is_clear()

  def fib(delf):
    """Front is Blocked"""
    return not self.fic()
    
  def ric(self):
    """Right id Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True 
    self.tl()
    return False 
      
  def rib(self):
    """Right id Blocked"""
    return not delf.ric()

  def l(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.tl()
    self.m3()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put()

  def mm(self, num):
    for number in range(num):
      self.m() 

  def pickm(self, num):
    """Pick multiple"""
    for i in range(num-1):
      self.pick()
      self.m()
    self.pick()

  def putm(self, num):
    """Put multiple"""
    for _ in range(0, num-1):
      self.put()
      self.m()
    self.put()
    

  
def main():
    """ Karel code goes here! """
     kt= ktools()
    
    pass


if __name__ == "__main__":
    run_karel_program()