# webfortune
This a Dockerized Flask application
that provides a Web front-end to the well-known Linux programs 'cowsay'
and 'fortune'.

## Build Instructions

### Command Line Build and Run
```flask run --host=0.0.0.0 --port=<your PORT>```

  Then type in the url bar:
  ```http://127.0.0.1:<your PORT>```
  
### Docker Build and Run
```docker build -t jasonkonz/webfortune .```

```docker run -dp <your PORT>:5000 jasonkonz/webfortune```

Then type in the url bar:
  ```http://<your IP>:<your PORT>```
  
## Different routes
```http://<your IP>:<your PORT>/fortune/```

```http://<your IP>:<your PORT>/cowsay/<message>```

```http://<your IP>:<your PORT>/cowfortune/```


## Pytest in Command Line
``` pytest-3 ```
