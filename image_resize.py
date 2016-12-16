import argparse


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
    parser.add_argument('--scale',
                        help='Scale result imagefile')
    parser.add_argument('--output',
                        help='The directory where the imagefile to add')
    return parser.parse_args()


def resize_image(args):
    if (args.scale is not None):
        if (args.width or args.height is not None):
            print("Do not use scale options with width or height options!")
            exit()


if __name__ == '__main__':
    args = get_args()
    resize_image(args)
