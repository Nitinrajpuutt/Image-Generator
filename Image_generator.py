import requests
import random
import os

def image_genrator(prompt, output_format='jpeg', aspect_ratio='16:9'): 
    print(f"Generating image for: {prompt}")
    response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"sk-0I0O0igW4lXQm7ICRk0erQKryqfi7NOC1VGCaxn5Jpja21DX",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": prompt,
        "output_format": output_format,
        "aspect_ratio": aspect_ratio
    },
    )

    if response.status_code == 200:
        output_dir = "./genratedImages/"
        os.makedirs(output_dir, exist_ok=True)  # Creates the directory if it does not exist

        file_path = os.path.join(output_dir, f"{random.random()}.png")
        with open(file_path, "wb") as f:
            f.write(response.content)
            print("Image Generated!!")
    else:
        raise Exception(str(response.json()))
