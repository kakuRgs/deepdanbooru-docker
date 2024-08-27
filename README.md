# deepdanbooru-docker

Docker service for <[https://github.com/KichangKim/DeepDanbooru](https://github.com/nanoskript/deepdanbooru-docker)>.

## Threshold

API's param add with Threshold.
By default, this is set to `0.1`.

```
curl -X 'POST' \
  'http://192.168.10.15:4321/deepdanbooru?threshold=0.8' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@./xiaoxin-6.png;type=image/png'
```
