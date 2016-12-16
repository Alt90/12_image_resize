import argparse
import os

from PIL import Image


def get_args():
    parser = argparse.ArgumentParser(
        description="This script can change the size of image",
    )
    parser.add_argument('path_to_file',
                        help='Path to imagefile')
    parser.add_argument('--width',
                        help='Width result imagefile')
    parser.add_argument('--height',
                        help='Height result imagefile')
    parser.add_argument('--scale', type=float,
                        help='Scale result imagefile')
    parser.add_argument('--output',
                        help='The directory where the imagefile to add')
    return parser.parse_args()


def get_image_size(image):
    return image.size


def save_resized_image(output_file, output_path_to_file):
    path, name = os.path.split(output_path_to_file)
    size = list(get_image_size(output_file))
    output_file.save('%s/%s__%sx%s%s' % (path,
                                         name[:name.rindex('.')],
                                         size[0],
                                         size[1],
                                         name[name.rindex('.'):]))


def resize_image_by_scale(image, scale, output_path_to_file):
    width, height = get_image_size(image)
    output_file = image.resize((int(width*scale), int(height*scale)))
    save_resized_image(output_file, output_path_to_file)


def resize_image(args):
    image = Image.open(args.path_to_file)
    if (args.output is not None):
        args.output = args.output + os.path.split(args.path_to_file)[1]
    else:
        args.output = args.path_to_file
    if (args.scale is not None):
        if (args.width or args.height is not None):
            print("Do not use scale options with width or height options!")
            exit()
        resize_image_by_scale(image, args.scale, args.output)


if __name__ == '__main__':
    args = get_args()
    resize_image(args)
