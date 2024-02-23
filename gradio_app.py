import gradio as gr
import fire
import os
from PIL import Image


import requests
from io import BytesIO
from PIL import Image
import torch
from diffusers import DDIMScheduler
from diffusers.pipelines.stable_diffusion import StableDiffusionImg2ImgPipeline

_TITLE = '''
    Sketch To Photo-Realistic Image
'''
_SUB_TITLE = '''
    <div>
        <p>Generate photo-realistic images with TensorRT Accelerated Stable Diffusion Image to Image pipeline</p>
    </div> 
'''

scheduler = DDIMScheduler.from_pretrained("stabilityai/stable-diffusion-2-1",
                                            subfolder="scheduler")

pipe = StableDiffusionImg2ImgPipeline.from_pretrained("stabilityai/stable-diffusion-2-1",
                                                custom_pipeline="stable_diffusion_tensorrt_img2img",
                                                revision='fp16',
                                                torch_dtype=torch.float16,
                                                scheduler=scheduler,)

pipe.set_cached_folder("stabilityai/stable-diffusion-2-1", revision='fp16',)
pipe = pipe.to("cuda")


def process(input_image, prompt, negative_prompt, strength, guidance_scale):
    print(f'Prompt: {prompt}')
    image = pipe(prompt, image=input_image, strength=strength, guidance_scale=guidance_scale, negative_prompt=negative_prompt,).images[0]
    image.save('result.jpg')
    new_img = image.resize((720,900))
    new_img.save("result.jpg", "JPEG", optimize=True)
    return gr.Image(interactive=False, width=720, height=900, value=new_img)
    # return input_image


enable_btn_click = lambda: gr.Button(value="Generate", interactive=True)


def run_demo():

    custom_theme = gr.themes.Soft(primary_hue="blue").set(
                    button_secondary_background_fill="*neutral_100",
                    button_secondary_background_fill_hover="*neutral_200")

    with gr.Blocks(title=_TITLE, theme=custom_theme, css="styles.css") as demo:
        with gr.Row():
            with gr.Column():
                gr.Markdown('# ' + _TITLE)
        gr.Markdown(_SUB_TITLE)

        with gr.Row(variant='panel'):
            with gr.Column(scale=1):
                input_image = gr.Image(interactive=True, width=720, height=900, type="pil")                  
        # with gr.Row(variant='panel'):
            with gr.Column(scale=1):
                result = gr.Image(interactive=False, width=720, height=900)
        with gr.Row(variant='panel', equal_height = True):
            with gr.Column(scale=1):
                prompt = gr.Textbox(label="Prompt", info="Enter the prompt", lines=1, interactive=True) 
                strength = gr.Slider(label="Strength", value="0.8", step="0.01", minimum="0", maximum="1")
            with gr.Column(scale=1):
                negative_prompt = gr.Textbox(label="Negative Prompt", info="Enter the negative prompt", lines=1, interactive=True)
                guidance_scale = gr.Slider(label="Guidance Scale", value="8", step="0.1", minimum="0", maximum="100")
        with gr.Row(variant='panel'):
            gen_button = gr.Button(value="Generate", interactive=False) 

        input_image.upload(enable_btn_click, outputs=[gen_button])
        gen_button.click(process, inputs=[input_image, prompt, negative_prompt, strength, guidance_scale], outputs=[result], show_progress='full')
        
    demo.queue().launch(share=False, max_threads=80, server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    fire.Fire(run_demo)