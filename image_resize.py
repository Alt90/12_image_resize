import argparse
import os

from PIL import Image


def get_args():
    parser = argparse.ArgumentParser(
        description="This script can change the size of image",
    )
    parser.add_argument('path_to_file',
                        help='Path to imagefile')
    parser.add_argument('--width', type=int,
                        help='Width result imagefile')
    parser.add_argument('--height', type=int,
                        help='Height result imagefile')
    parser.add_argument('--scale', type=float,
                        help='Scale result imagefile')
    parser.add_argument('--output',
                        help='The directory where the imagefile to add')
    return parser.parse_args()


def get_image_size(image):
    return image.size


def resized_file_dir(width, height, output_path_to_file):
    path, name = os.path.split(output_path_to_file)
    resized_file_name = '%s__%sx%s%s' % (name[:name.rindex('.')],
                                         width,
                                         height,
                                         name[name.rindex('.'):])
    return(os.path.join(path, resized_file_name))


def resize_image_by_scale(image, scale, output_path_to_file):
    width, height = get_image_size(image)
    output_file = image.resize((int(width*scale), int(height*scale)))
    output_file.save(resized_file_dir(int(width*scale), int(height*scale), output_path_to_file))


def resize_image_by_size(image, width, height, output_path_to_file):
    width_old, height_old = get_image_size(image)
    width_new = width or width_old
    height_new = height or height_old
    output_file = image.resize((width_new, height_new))
    output_file.save(resized_file_dir(width_new, height_new, output_path_to_file))


def resize_image(args):
    image = Image.open(args.path_to_file)
    if args.output is not None:
        args.output = os.path.join(args.output, os.path.split(args.path_to_file)[1])
    else:
        args.output = args.path_to_file
    if args.scale is not None:
        if (args.width or args.height is not None):
            print("Do not use scale options with width or height options!")
            exit()
        resize_image_by_scale(image, args.scale, args.output)
    if args.width is not None or args.height is not None:
        resize_image_by_size(image, args.width, args.height, args.output)


if __name__ == '__main__':
    args = get_args()
    resize_image(args)
