import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import random

from ultralytics.utils import plotting
from ultralytics import YOLO
from diffusers import StableDiffusionInpaintPipeline

import torch
from safetensors.torch import load_file, save_file
from diffusers import StableDiffusionPipeline
from diffusers import DPMSolverMultistepScheduler

from diffusers import StableDiffusionControlNetPipeline
from diffusers.utils import load_image
import cv2
from PIL import Image
import numpy as np
from diffusers import DiffusionPipeline

import math
#import lora

from model_utils import *
from config import *

pipe1=StableDiffusionInpaintPipeline.from_pretrained(
            "runwayml/stable-diffusion-inpainting", safety_checker=None
        )

pipe2=StableDiffusionInpaintPipeline.from_pretrained(
            "SG161222/Realistic_Vision_V2.0",  safety_checker=None
      )

    
    
# pipe1.from_single_file(local_files_only=False, pretrained_model_link_or_path="/home/yerin/code/stable-diffusion-cubig/models/Stable-diffusion/realistic.safetensors",
#                         use_safetensors=True)

pipe1 = pipe1.to("cuda")
pipe2 = pipe2.to("cuda")
print("model is ready")


def generate_room(image, mask, width, height):
    try: 
        seed=mask["seed"]
        mask=mask["style"]
                
    except:
        seed=int(random.random()*10000)    
    try:
        style=style_list[mask-1]
    except:
        mask=1
        style=style_list[mask-1]
    main_prompt = f"a photo of a {style} styled room"
    
    base64_image=base64.b64encode(image.getvalue()).decode("utf8")
    # with open(image, "rb") as f_img:
    #     base64_image = base64.b64encode(f_img.read()).decode('utf-8')
    
    # base64_image=base64.b64encode(encoded_image.getvalue()).decode("utf8")
    
    
   # print(base64_image)
    
    
    payload = {
                "prompt": main_prompt,
                "negative_prompt": "",
                "batch_size": 1,
                "steps": 20,
                "cfg_scale": 7,
                "width": width,
                "height": height,
                # "enable_hr": False,
                # "hr_upscaler": "ESRGAN_4x",
                "sampler_index": "Euler a",
                "save_images": True,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "input_image": base64_image,
                                "module": controlnet_module,
                                "model": controlnet_model
                                # "processor_res": 512,
                            }
                        ]
                    }
                }
            }
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()
    result = r['images'][0]
    image = Image.open(io.BytesIO(base64.b64decode(result.split(",", 1)[0])))
    
   
    matrix={
        "seed":seed,
        "style": mask        
    }
    print("room_done")
    return image, matrix
    
    
    
## face1, face2 모두 이 함수를 쓰고, face 2일 경우 None이던 mask에 (a, b, c, d, e,f seed) 담아서 해당 부분 픽스하기.
def generate_character(image, age, gender, mask):
    if gender: negative_prompt=negative_prompt_woman
    
    else: negative_prompt=negative_prompt_man
    
    image=Image.open(image).convert('RGB')
    image=image.resize([1024, 1024])
    #base64_image=base64.b64encode(image.getvalue()).decode("utf8")
    if mask==None:
        a=random.random()
        b=random.random()
        c=random.random()
        d=random.random()
        e=random.random()
        f=random.random()
        seed=int(random.random()*10000)
    else:
        a, b,c, d, e, f=mask["lora"]
        seed=mask["seed"]      
    
    # print(a, b, c, d, e, f, seed)
    
    RATIOS=[a, b, c, d, e, f]
    SEED=random.random()
    
    if gender:
        prompt=prompt_girl
    else: prompt=prompt_man
    
    # print(age-1)
    # print(prompt[int(age)])
    
    print("start face diffusion")
    try:
       # detect_objects(image, _file)
        masks=make_mask(image)
        masks=Image.fromarray(np.uint8(masks*255), "L")
        image=Image.fromarray(image).convert("RGB") 
    except:
        print("detection is failed") 
        masks=np.ones(image.size)
        masks=Image.fromarray(np.uint8(masks*255), "L")

    #p
    
    generator = torch.manual_seed(SEED)

    print(image.size)
    image = pipe1(prompt=prompt[int(age)], negative_prompt=negative_prompt, mask_image=masks, image=image, strength=0.3, generator=generator).images[0]
    #print(image.size)
    image = pipe2(prompt=prompt[int(age)], negative_prompt=negative_prompt, mask_image=masks, image=image, strength=0.3, generator=generator).images[0]
    
    #image.save(f"./{seed}.jpg")
    matrix={
        "seed":seed ,
        "lora":[a, b, c, d, e, f]       
    }
    
    return image, matrix
#(128), (128)
#(128, 1)(128, 1)
