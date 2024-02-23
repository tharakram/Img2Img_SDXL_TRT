# Sketch To Realistic Image Generation
A Stable Diffusion Image-To-Image Pipeline Accelerated by TensorRT

### Steps to Deploy and Run:
Checkout the code:
```sh
git clone https://github.com/tharakram/Img2Img_SDXL_TRT.git
cd Img2Img_SDXL_TRT
```

Build Docker image:
```sh
docker build .
```

Run the container:
```sh
docker run --gpus all -it -p 7860:7860 --name CONATINER_NAME CONTAINER_ID
```
Application launches on port 7860 after a while, make sure to check the container log to confirm. Once start, hit http://localhost:7860 to launch the gradio application.

**Note:** It takes about ~35-45 minutes when you start the conatiner for the first time since it downloads all the model files and convert them to Tensor Runtime Engine. This repeats if you try to build a new image everytime. Also, feel free to mount the local drive to your container if need be.


#### Follow the instructions below to run the notebook:
* Install Docker Desktop
* Download and Run TensorRT container from NGC (nvcr.io/nvidia/tensorrt:24.01-py3)
* Run the container in interactive mode by mounting a local directory, please see the below command
    ```sh
    docker run --gpus all -it -p 8000:8000 -v .\PATH_TO_CWD\:/WS_DIR_IN_CONTAINER/ nvcr.io/nvidia/tensorrt:24.01-py3
    ```
* Install jupyterlab
    ```py
    pip install jupyterlab
    ```
* Run jupyter lab from the mount workspace [WS_DIR_IN_CONTAINER], it is optional to run the jupyter lab from this workspace, it will be easy to move files from your local to container and otherway around too.
    ```sh
    jupyter lab --port=8000 --no-browser --ip=0.0.0.0 --allow-root
    ```
    **Note:** Jupyter lab port must match your container port, otherwise you will not be able to access the lab from your browser

#### System Specifications:
* CPU (Min 2 Cores)
* Nvidia GeForce RTX 4060 Ti
* Memory 16 GB
* Storage Reqd. ~60GB
* Windows 11 Operating System

#### Command to run the conatiner
```sh
docker run --gpus all -it -p 8000:8000 -v .\PATH_TO_CWD\:/WS_DIR_IN_CONTAINER/ nvcr.io/nvidia/tensorrt:24.01-py3
```

#### References:
https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html#introduction
https://github.com/huggingface/diffusers/tree/main/examples/text_to_image
https://github.com/huggingface/diffusers/blob/main/examples/community/README.md