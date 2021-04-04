from argparse import ArgumentParser
from imutils import paths 
import os 
import shutil
import random

def prepare_dataset(filenames,dir): 
    try: 
      os.makedirs(dir)
    except:
      print("Directory already exists. Deleting and creating new directory.")
      shutil.rmtree(dir)
      os.makedirs(dir)
      # os.makedirs(os.path.join(dir, 'train'))

    for x in filenames:
      # if x.split("/")[-2] not in os.listdir(os.path.join(dir,"train")):
      if x.split("/")[-2] not in os.listdir(dir):
        # os.mkdir(os.path.join(os.path.join(dir,"train"),x.split("/")[-2]))
        os.mkdir(os.path.join(dir,x.split("/")[-2]))
        shutil.copy(x, os.path.join(os.path.join(dir,x.split("/")[-2])))
      else:
        shutil.copy(x, os.path.join(os.path.join(dir,x.split("/")[-2])))
    print('Subset moved to directory. Dataset abiding formats created successfully')

def random_sample_dataset(source,dest,subset_size):
  directories = [name for name in os.listdir(source) if os.path.isdir(os.path.join(source, name)) ]
  subset_size_per_dir = int(subset_size*(len(list(paths.list_images(source)))/len(directories)))
  print("Number of images to be selected per folder:",subset_size_per_dir)
  filenames = []
  for folder in os.listdir(source):
    images = list(paths.list_images(os.path.join(source,folder)))
    random_points_fnames = random.sample(images, subset_size_per_dir)
    filenames.extend(random_points_fnames)
    print(folder,len(random_points_fnames))
  prepare_dataset(filenames, os.path.join(dest,'Images'))

def main():

  parser = ArgumentParser()
  parser.add_argument("--subset_size", type=float, help="Total percent of images needed to be sampled from the entire dataset")
  parser.add_argument("--source", type=str, default = None, help="Path to source dataset")
  parser.add_argument("--dest", type=str, default = None, help="Path to destination dataset to be created")

  args, _ = parser.parse_known_args()

  random_sample_dataset(args.source,args.dest,args.subset_size)

if __name__ == '__main__':
  main()
