import uuid
import os
import datetime
import imageio.v3 as iio
from shutil import copyfile

def convert_files(src_dir: str, dst_dir: str = "", image_format: str = "", out_fname_format: str = "%d_%u", delete_source: bool = False):
  """Convert filenames of every images to uuid format.
  
  ### Function Arguments:
   - src_dir: absolute path of source directory
   - dst_dir `optional`: absolute path of destination directory; default = `src_dir`
   - image_format `optional`: format of output image; defaults to save original format
   - out_fname_format `optional`: template string for output image filename; defaults to `%d_%u`; `%u`: `uuid_v4`; `%d`: `timestamp`
   - delete_source `optional`: delete source images; defaults to `False`

  ### Sample Usage:

  ```python
  convert_files(
    src_dir="C:/Users/Admin/Pictures/sample",
    dst_dir="c:/users/admin/pictures/normalized",
    image_format="png",
    out_fname_format="thermal_%d_%u",
    delete_source=False
  )
  ```
  """
  if not dst_dir:
    dst_dir = src_dir
  
  if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

  for filename in os.listdir(src_dir):
    _, src_ext = os.path.splitext(filename)
    dst_ext = "." + image_format if image_format else src_ext

    src = src_dir + "\\" + filename
    dst_filename = out_fname_format.replace("%u", str(uuid.uuid4())).replace("%d", str(datetime.datetime.now().timestamp()))
    dst = dst_dir + "\\" + dst_filename + dst_ext

    if not os.path.isfile(src):
      continue
    
    if image_format:
      img = iio.imread(src)
      iio.imwrite(dst, img)
      if delete_source:
        os.remove(src)
    else:
      if delete_source:
        os.rename(src, dst)
      else:
        copyfile(src, dst)