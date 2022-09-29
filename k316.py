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
    
  def l(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.m3()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.tl()
    self.m3()
    
def main():
    """ Karel code goes here! """
    kt= ktools()
    kt.m3()
    kt.tl()
    kt.m()
    kt.m()
    kt.pick()
    kt.tr()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tl()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tl()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tl()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.tl()
    
    pass


if __name__ == "__main__":
    run_karel_program()