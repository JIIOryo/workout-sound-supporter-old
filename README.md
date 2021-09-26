# workout-sound-supporter-old

筋トレ音声支援アプリ

## deploy

ラズパイのGPIO(BCM:21)とGNDに圧電スピーカを接続

ラズパイで以下を実行

```bash
git clone https://github.com/JIIOryo/workout-sound-supporter-old.git
cd workout-sound-supporter-old
pip install -r requirements.txt
python server/server.py
```

```
http://{raspiのipアドレス}:8000
```
で接続

![test](https://raw.githubusercontent.com/JIIOryo/workout-sound-supporter-old/img/img/a.png)
![test](https://raw.githubusercontent.com/JIIOryo/workout-sound-supporter-old/img/img/b.png)
