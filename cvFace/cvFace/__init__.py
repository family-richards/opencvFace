import cv2
from threading import Thread
class smartFrameReader:
  def __init__(self):
    vidcap = cv2.VideoCapture(0)
  def foreverRead(self):
    """ don't worry about this. """
    while True:
      ret, tempFrame = self.vidcap.read()
      if self.status != 0:
        self.frame = tempFrame
        self.status = 0
  def getFrame(self):
    """ gets frame from frame reader. """
    self.status = 1
    while self.status == 1:
      pass
    return self.frame
  def startReading(self):
    """ starts reading frames. i consistently read frames to remove lag. """
    rdr = Thread(target=self.foreverRead)
    rdr.start()
class faceFinder:
  pass
class faceIDer:
  pass
