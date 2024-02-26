import datetime
import os

class Logger:
  def __init__(self, toFile = True, toStdout = False):
    self.on = True
    self.toFile = toFile
    self.toStdout = toStdout
    if(toFile):
      try:
        now = datetime.datetime.now()
        log_dir = os.getcwd() + "\\" + "logs"
        if not os.path.exists(log_dir):
          os.mkdir(log_dir)
        absolute_path = log_dir + "\\" + now.strftime("%Y-%m-%d %H-%M-%S") + ".log"
        self.log_file = open(absolute_path, "w")
      except:
        self.log_file = None
        print(f"Cannot create {absolute_path}")
  
  def log(self, str, format):
    now = datetime.datetime.now()
    msg = format.replace("%t", now.strftime("%Y/%m/%d %H-%M-%S")).replace("%s", str)
    if(self.toFile and self.log_file is not None):
      self.log_file.write(msg)
    if(self.toStdout):
      print(msg)
  
  def info(self, str):
    self.log(str, "%t INFO   : %s\n")
  
  def error(self, str):
    self.log(str, "%t ERROR  : %s\n")