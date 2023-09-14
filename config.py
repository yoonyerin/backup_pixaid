


MODELS=[
    "/home/yerinyoon/pixaid/models/27751.safetensors",
    "/home/yerinyoon/pixaid/models/29136?type=Model&format=SafeTensor&size=full&fp=fp16.safetensors",
    "/home/yerinyoon/pixaid/models/81867?type=Model&format=SafeTensor.safetensors",
    ]
file_path="/home/yerinyoon/pixaid/experiment/sample/im1.png"
result_path="/home/yerinyoon/pixaid/experiment/result/im1.png"


# print(a, b, c, d, e, f)models
prompt_girl=[
    ## age_1
    f" A one-year-old adorable baby girl, age:1, extremely clear white skin, baby eyes,   1baby, Korean baby, extremely young baby, cuty face, innocent baby, extremely beautiful big black sparkling eyes, clear skin,  chubby face,\
ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), baby lips, The scene's atmosphere is joyful and tender, with a sense of innocence and wonder. Illustration style with soft, rounded shapes and a gentle color palette,", 
    ## age_2
    f" A cute seven-year-old girㅣ, age:7 , 1baby, Korean baby, extremely young girl, cuty face, innocent baby, extremely beautiful big black sparkling eyes, clear skin,  \
ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The atmosphere is joyful and carefree, with a sense of innocence and wonder. The illustration style is whimsical and playful, with soft lines and pastel colors",
    ## age_3
    f"A pretty and innocent-looking 13-year-old girl with big brown eyes, age:13, Korean young beautiful teenager girl, 1girl, cuty face, innocent girl,  \
        beautiful big black sparkling eyes, clear skin, very small face, oval face, Photo of a Beautiful Korean kpop idol girl,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The scene's atmosphere is peaceful and dreamy, with a sense of wonder and tranquility. Illustration style with soft, pastel colors and delicate linework, executed with watercolor or digital painting techniques.\
    ",
    ##age_4
    f"A beautiful young woman in her twenties, The atmosphere is joyful and carefree, with a sense of innocence and wonder. The illustration style is whimsical and playful, with soft lines and pastel colors,extremely clear skin, extremely realistic face, age:20, Korean young beautiful girl, 1girl, cuty face, innocent girl,  beautiful big black sparkling eyes, actress face, mascara, clear skin, very small face, oval face, Photo of a Beautiful Korean kpop idol girl,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), Illustration style with soft, painterly textures and a warm color palette, executed with digital painting techniques reminiscent of impressionist art",
    ##age_5
    f"A confident and successful career woman in her forties, extremely realistic face, age:70, old woman, Korean beautiful graceful woman, wrinkle face, 1woman, cuty face, innocent girl,  beautiful big black sparkling eyes, actress face, mascara, clear skin, very small face, oval face, Photo of a Beautiful Korean kpop idol girl,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The atmosphere is professional and efficient, with a hint of ambition and determination. The color palette is dominated by cool tones of blue and gray, with pops of bright colors that reflect the woman's personality and style. The illustration style is clean and contemporary, with a focus on geometric shapes and sharp lines. The final image portrays a powerful and inspiring figure that represents the modern working woman ",
    ##age_6
    f"A kind-hearted grandmother in her 70s, extremely realistic face, beautiful Korean woman, age:70, beautiful graceful woman, 1woman, beautiful grandma, innocent girl,  beautiful big black sparkling eyes, actress face, mascara,  very small face, oval face,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The atmosphere is calm and peaceful, with a sense of comfort and security. The illustration style is realistic and detailed, with soft shading and warm colors that evoke a sense of nostalgia and sentimentality. The image is completed with a handwritten quote from the grandmother, expressing her love and wisdom."       
        ]

prompt_man=[
    ## age_1
    f"A chubby-cheeked one-year-old baby with big bright eyes and a toothless smile, age:1 ,baby face, 1baby, Korean baby, extremely young baby, cuty face, innocent baby, extremely beautiful big black sparkling eyes, clear skin,  chubby face,\
ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), baby lips The scene's atmosphere is joyful and lighthearted, with a sense of innocence and wonder. Illustration style with soft, rounded shapes and a gentle color palette", 
    ## age_2
    f"A mischievous seven-year-old boy with a cheeky grin, age:7 , 1boy, 1baby, Korean baby, extremely young boy, cuty face, innocent baby, extremely beautiful big black sparkling eyes, clear skin,  \
ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The atmosphere is energetic and chaotic, with a sense of adventure and creativity. The illustration style is lively and dynamic",
    ## age_3
    f"A handsome 13-year-old boy with a mischievous smile, age:13,thick eyebrows, young handsome teenager boy, 1boy, beautiful face, innocent boy,  beautiful big black sparkling eyes, clear skin, very small face, oval face, Photo of a Beautiful Korean kpop idol boy,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), The atmosphere is energetic and rebellious, with a sense of adventure and freedom.",
    ##age_4
    f"A charming young man in his twenties, age:20, thick eyebrows,expert man, boyish, masculine, young handsome boy, 1boy, beautiful face, charming man,  beautiful big black sparkling eyes, actor face,  clear skin,  oval face, Photo of a Beautiful Korean kpop idol boy,  very slim chin,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), straight teeth, The scene's atmosphere is energetic and rebellious, with a hint of danger and excitement.",
    ##age_5
    f"A seasoned career man in his forties, age:50,thick eyebrows,old Korean man, wrinkle face, beard, expert man,mustache, masculine, boyish ,beautiful graceful man,gentle man, 1man, beautiful face, charming man,  beautiful big black sparkling eyes, actor face,  clear skin, oval face, Photo of a Beautiful Korean kpop idol boy,\
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo), straight teeth, his expression is calm and confident. The atmosphere is professional and efficient, with a touch of sophistication. The color palette is neutral with pops of blue and green, and the image is executed in a realistic style with attention to detail and texture. The final result is a powerful and inspiring portrait of a successful and experienced professional.",
    ##age_6
    f"A kind and gentle 70-year-old grandfather,  age:90,thick eyebrows, old Korean man, extremely wrinkle face, old gentle man,  beard,expert man ,mustache, masculine, boyishbeautiful graceful man, 1man, grandpa, charming man,  beautiful big black sparkling eyes, actor face, \
    ultra detailed eyes, black eyes, extremely detailed, simple nostalgic, nice spring afternoon lighting, (professional iPhone photo) , straight teeth, with a warm color palette and soft lighting. The scene's atmosphere is nostalgic and heartwarming, with a sense of community and comfort"       
        ]

negative_prompt_woman="blue skin, (worst_quality:2.0) low quality, blur ,deformed ugly, pixelated, accessory, ring, ear ring, face distortion, monkey face, big lip, bloodshot eyes"
negative_prompt_man="blue skin, woman, madam, makeup, mascara, lipstick(worst_quality:2.0) low quality, blur ,deformed ugly, pixelated, accessory, ring, ear ring, face distortion, monkey face, big lip, bloodshot eyes"
    
    
#####################################################################################################
#               ROOM
#####################################################################################################


controlnet_module =  "depth_midas"
controlnet_model="control_depth-fp16 [400750f6]"#control_v11f1p_sd15_depth [e3b0c442]",
   
style_list = [
    "modern",
    "minimal",
    "natural",
    "North European",
    "retro",
    "classic",
    "antique",
    "provence",
    "romantic",
    "industrial",
]


