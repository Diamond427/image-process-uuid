import uuid
import os
import imageio.v3 as iio
from shutil import copyfile

def convert_files(src_dir: str, dst_dir: str = "", format: str = "", delete_source: bool = False):
  """Convert filenames of every images to uuid format.
  
  Keyword arguments:
  src_dir -- absolute path of source directory
  dst_dir -- absolute path of destination directory (can be ommited to use same directory as src_dir)
  format -- format of output image (can be ommited to save original format)

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
    dst = dst_dir + "\\" + str(uuid.uuid4()) + dest_ext

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


if __name__ == "__main__":
  convert_files("C:/Users/Admin/Pictures/sample", "c:/users/admin/pictures/wdf", "png", delete_source=True)