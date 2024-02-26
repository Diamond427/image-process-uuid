import uuid
import os
import datetime
import imageio.v3 as iio
from shutil import copyfile

def get_datetime_string():
  """Returns current date and time in YYYY-MM-DD HH:MM:SS format"""
  now = datetime.datetime.now()
  return now.strftime("%Y-%m-%d.%H-%M-%S")

def convert_files(src_dir: str, dst_dir: str = "", format: str = "", delete_source: bool = False):
  """Convert filenames of every images to uuid format.
  
  Function Arguments:
   - src_dir: absolute path of source directory
   - dst_dir `optional`: absolute path of destination directory; default = `src_dir`
   - format `optional`: format of output image; defaults to save original format
   - delete_source `optional`: delete source images; defaults to `False`

  Sample Usage:
  convert_files("C:/Users/Admin/Pictures/sample", "jpg")
  convert_files("C:/Users/Admin/Pictures/sample")
  """
  if not dst_dir:
    dst_dir = src_dir
  
  if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

  for filename in os.listdir(src_dir):
    _, source_ext = os.path.splitext(filename)
    dest_ext = "." + format if format else source_ext

    src = src_dir + "\\" + filename
    dst = dst_dir + "\\" + str(uuid.uuid4()) + "." + get_datetime_string() + dest_ext

    if not os.path.isfile(src):
      continue
    
    if format:
      img = iio.imread(src)
      iio.imwrite(dst, img)
      if delete_source:
        os.remove(src)
    else:
      if delete_source:
        os.rename(src, dst)
      else:
        copyfile(src, dst)