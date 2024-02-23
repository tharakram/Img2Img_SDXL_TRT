# Sketch To Realistic Image Generation
A Stable Diffusion Image-To-Image Pipeline Accelerated by TensorRT

### Steps to Deploy and Run:
Checkout the code:
```sh
git clone https://github.com/tharakram/Img2Img_SDXL_TRT.git
cd 
```


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





#### Command to run the conatiner
```sh
docker run --gpus all -it -p 8000:8000 -v .\PATH_TO_CWD\:/WS_DIR_IN_CONTAINER/ nvcr.io/nvidia/tensorrt:24.01-py3
```

