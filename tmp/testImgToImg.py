import torch
import requests
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline

device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "nitrosocke/Ghibli-Diffusion",
).to(device)

# init_image = Image.open("data/output/saveCanvas - 2023-10-05T212050.177.png").convert("RGB")
init_image = Image.open("data/output/img_to_img_after_3.jpg").convert("RGB")
init_image.thumbnail((768, 768))
init_image

print(init_image)

with open('data/output/img_to_img.jpg', 'wb') as input_file:
    init_image.save(input_file, format='JPEG')

prompt = "meteor, oil painting, fantastic"
# prompt = "oil painting, Hellfire, fantastic, sacred water"
# prompt = "ukiyoe style, yellow mountain, beautiful lake and sea, orange villages"
# prompt = "ghibli style, a fantasy landscape with castles"
generator = torch.Generator(device=device).manual_seed(1024)
image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5, generator=generator).images[0]
image

with open('data/output/img_to_img_after.jpg', 'wb') as input_file:
    image.save(input_file, format='JPEG')