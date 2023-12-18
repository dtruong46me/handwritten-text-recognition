
Since our model is too large, so you need to download manually.

- Base model: [donut.pth](https://drive.google.com/uc?export=download&id=1uHg_oCziqJdtcyZSLCxQ1v3iJ6BqPtxR&fbclid=IwAR234bt9stl6xbBQAaOBp2x3KevlIg0DSTMWk8RKq8Qz8zCBgpgEzRnKkrI) (1.5 GB)

- Our model: [trOCR.pth](https://drive.google.com/u/0/uc?id=1RF29mLXanE5Ze6J7qqhWlcK6DIgdfGo4&export=download) (1.4 GB)

> Your downloaded model should be located in `src/saved/your_model.pth`

Example:
```
..
└───src
    ├───..
    ├───saved
    │   └───trOCR.pth
    │   └───donut.pth
    ├───..
```

In file `src/utils/predict.py`, handle your model you downloaded in the **line 12**

```
MODEL = "model_downloaded.pth"
```

![](../../assets/code.png)
