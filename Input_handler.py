from image_genrator import image_genrator

def main():
    prompt = input("Enter an image description: ")
    output_format = input("Enter the output format: webp, JPEG, png: ")
    aspect_ratio = input("Enter the aspect_ratio of image: 1:1, 3:4, 16:9: ")
    image_genrator(prompt=prompt, output_format=output_format, aspect_ratio=aspect_ratio)

if __name__ == "__main__":
    main()
