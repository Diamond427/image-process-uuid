import uuid
import os
import imageio as iio

def convert_files(directory: str, format: str = ""):
  """Convert filenames of every images to uuid format.
  
  Keyword arguments:
  directory -- absolute path of directory
  format -- format of output image (can be ommited to save original format)

  Sample Usage:
  convert_files("C:/Users/Admin/Pictures/sample", "jpg")
  convert_files("C:/Users/Admin/Pictures/sample")
  """

  for filename in os.listdir(directory):
    _, source_ext = os.path.splitext(filename)
    dest_ext = "." + format if format else source_ext

    src = directory + "\\" + filename
    dst = directory + "\\" + str(uuid.uuid4()) + dest_ext

    if not os.path.isfile(src):
      continue
    
    if(format):
      img = iio.imread(src)
      iio.imwrite(dst, img)
      os.remove(src)
    else:
      os.rename(src, dst)


if __name__ == "__main__":
  convert_files("C:/Users/Admin/Pictures/sample")