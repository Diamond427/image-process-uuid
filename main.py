from convert import convert_files

if __name__ == "__main__":
  convert_files(
    src_dir=r"C:\Users\Admin\Pictures\sample",
    dst_dir=r"C:\Users\Admin\Pictures\normalized",
    image_format="png",
    out_fname_format="thermal_%d_%u",
    delete_source=False
  )