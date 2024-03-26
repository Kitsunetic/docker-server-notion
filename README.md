# docker-server-notion
서버 도커 관리용... 서버좀 깨끗하게 씁시다


# 

Print docker container and images as notion table format

```sh
python main.py
```

```txt
Images:
| REPOSITORY                       | TAG    | IMAGE ID     | CREATED      | SIZE   |
|----------------------------------|--------|--------------|--------------|--------|
| kitsunetic/alpine-openssh-client | latest | c8f9cfe99759 | 6 months ago | 12.3MB |
| alpine-openssh-client            | latest | c8f9cfe99759 | 6 months ago | 12.3MB |


Containers:
| CONTAINER ID | NAMES           | IMAGE                            | STATUS                    | SIZE                |
|--------------|-----------------|----------------------------------|---------------------------|---------------------|
| 2b33238d1fd0 | wonderful_elion | kitsunetic/alpine-openssh-client | Exited (0) 56 minutes ago | 0B (virtual 12.3MB) |
```
