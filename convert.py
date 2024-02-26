import uuid
import os
import datetime
import imageio.v3 as iio
from logger import Logger
from shutil import copyfile

def convert_files(src_dir: str, dst_dir: str = "", image_format: str = "", out_fname_format: str = "%d_%u", delete_source: bool = False, logger: Logger = Logger()):
  """Convert filenames of every images to uuid format.
  
  ### Function Arguments:
   - src_dir: absolute path of source directory
   - dst_dir `optional`: absolute path of destination directory; default = `src_dir`
   - image_format `optional`: format of output image; defaults to save original format
   - out_fname_format `optional`: template string for output image filename; defaults to `%d_%u`; `%u`: `uuid_v4`; `%d`: `timestamp`
   - delete_source `optional`: delete source images; defaults to `False`
   - logger `optional`: Logger for errors; default save logs to file

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
  if not src_dir or not os.path.exists(src_dir) or not os.path.isdir(src_dir):
    return Logger.error(f"Cannot read {src_dir}")
  
  if not dst_dir:
    dst_dir = src_dir
  
  if not os.path.exists(dst_dir):
    Logger.info(f"Directory {dst_dir} created.")
    os.mkdir(dst_dir)
  
  tot_filecnt, success_cnt, skipped_cnt = 0, 0, 0

  for filename in os.listdir(src_dir):
    _, src_ext = os.path.splitext(filename)
    dst_ext = "." + image_format if image_format else src_ext

    src = src_dir + "\\" + filename
    dst_filename = out_fname_format.replace("%u", str(uuid.uuid4())).replace("%d", str(datetime.datetime.now().timestamp()))
    dst = dst_dir + "\\" + dst_filename + dst_ext

    if not os.path.isfile(src):
      continue

    tot_filecnt += 1
    
    if image_format:
      try:
        img = iio.imread(src)
      except:
        logger.error(f"{src} is not an image. skipped")
        skipped_cnt += 1
        continue

      try:
        iio.imwrite(dst, img)
      except:
        logger.error(f"Error saving image to {dst}.")
        continue

      if delete_source:
        try:
          os.remove(src)
        except:
          logger.error(f"Error removing {src}")

    else:
      try:
        if delete_source:
          os.rename(src, dst)
        else:
          copyfile(src, dst)
      except:
        logger.error(f"Error handling file {src} to {dst}")
    
    success_cnt += 1
  
  logger.info(f"Converted {success_cnt} images among {tot_filecnt} files. {skipped_cnt} files skipped.")