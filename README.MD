# Demo stand. Model: Ranking (English)

## Installation and start
1. Clone the repo and `cd` to project root:
    ```
    git clone https://github.com/deepmipt/stand_ranking_en.git
    cd stand_ranking_en
    ```
2. Create a virtual environment with `Python 3.6`:
    ```
    virtualenv env -p python3.6
    ```
3. Activate the environment:
    ```
    source ./env/bin/activate
    ```
4. Install DeepPavlov:
    1. Clone the repo and `cd` to project root
        ```
        git clone https://github.com/deepmipt/DeepPavlov.git
        cd DeepPavlov
        ```
    2. Install the requirements:
        ```
        python setup.py develop
        ```
    3. Install `spacy` dependencies:
        ```
        python -m spacy download en
        ```
    4. Download pre-trained models:
        ```
        python -m deeppavlov.download 
        ```
5. Return to the `stand_ranking_en` dir
6. Specify model endpoint host (`api_host`) and port (`api_port`) in `ranking_agent_config.json`
7. Specify virtual environment path (if necessary) in `run_en_ranking.sh`
8. Run model:
    ```
    ./run_en_ranking.sh
    ```
<!---
## Building and running with Docker:
1. If necessary, build Base Docker image from:

   https://github.com/deepmipt/stand_docker_cuda
  
2. Clone the repo and `cd` to project root:
    ```
    git clone https://github.com/deepmipt/stand_intent_en.git
    cd stand_intent_en
    ```
3. Build Docker image:
   ```
   sudo docker build -t stand/intent_en .
   ```
4. Run Docker image:
   ```
   sudo docker run -p <host_port>:6007 -v /path/to/host/vol/map/dir:/vol stand/intent_en
   ```
-->