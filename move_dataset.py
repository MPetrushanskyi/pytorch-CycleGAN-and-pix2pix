#import cv2
import PIL
import os

#function to traverse the directory and get the list of *.png files
def get_file_list(dir_name):
    file_list = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith(".png"):
                file_list.append(os.path.join(root, file))
    print("Total number of files: " + str(len(file_list)))
    return file_list

#function to convert *.png to *.jpg and save it in the different directory
def convert_png_to_jpg_in_different_dir(file_list, output_dir):
    for file in file_list:
        im = PIL.Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(os.path.join(output_dir, os.path.basename(file).replace(".png", ".jpg")))
        print(os.path.basename(file) + " converted to jpg")

#function to move 5% of the images from one directory to another
def move_5_percent_images_to_another_dir(file_list, output_dir,output_dir2):
    for file in file_list:
        if file_list.index(file) % 20 == 0:
            os.rename(file, os.path.join(output_dir, os.path.basename(file)))
            print(os.path.basename(file) + " moved to " + output_dir)
        else:
            os.rename(file, os.path.join(output_dir2, os.path.basename(file)))
            print(os.path.basename(file) + " moved to " + output_dir2)
        
if __name__=="__main__":
    file_list = get_file_list("~/datasets/face/ffhq/images1024x1024/")
    # convert_png_to_jpg_in_different_dir(file_list, "~/datasets/face/pix2pix/A/train")
    # file_list= get_file_list("~/datasets/face/pix2pix/A/train")
    move_5_percent_images_to_another_dir(file_list, "~/datasets/face/pix2pix/A/val/","~/datasets/face/pix2pix/A/train/")
    
    file_list1 = get_file_list("~/datasets/face/hqr/ffhqr/ffhq/")
    # convert_png_to_jpg_in_different_dir(file_list1, "~/datasets/face/pix2pix/B/train")
    # file_list1= get_file_list("~/datasets/face/pix2pix/A/train")
    move_5_percent_images_to_another_dir(file_list1, "~/datasets/face/pix2pix/B/val/","~/datasets/face/pix2pix/B/train/")