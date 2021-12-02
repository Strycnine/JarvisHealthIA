import torch
from torchvision import transforms
from mednet import MedNet
from PIL import Image
import base64
import io


def traitement(imgs):
    data = []
    for img in imgs:
        img_name = str(img).split("'")[1]
        img_link = link(img)
        img_predict = predict(img)

        x = {
                'img_name':img_name,
                'img_link':img_link,
                'img_predict':img_predict
            }

        data.append(x)
    return data


def link(img):
    img_open = Image.open(img)
    x = io.BytesIO()
    img_open.save(x, "JPEG")
    encoded_img_data = base64.b64encode(x.getvalue())
    return encoded_img_data.decode('utf-8')


def predict(img):
    model = MedNet(64, 64, 6)
    model.load_state_dict(torch.load('model_dict', map_location='cpu'))
    model.eval()
    classNames = ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

    toTensor = transforms.ToTensor()
    def scaleImage(x):
        y = toTensor(x)
        if(y.min() < y.max()):
            y = (y - y.min())/(y.max() - y.min())
            z = y - y.mean()
        return z

    imageTensor = torch.stack([scaleImage(Image.open(img))])
    with torch.no_grad():
        outputs = model(imageTensor)
    return format(classNames[outputs.argmax()])
