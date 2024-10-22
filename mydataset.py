import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

class my_dataset(Dataset):
    def __init__(self, root_dir):
        super(my_dataset, self).__init__()
        self.image_path = [os.path.join(root_dir, image_name) for image_name in os.listdir(root_dir)]
        self.transforms = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Resize((60, 160)),
                transforms.Grayscale()
            ]
        )
        # print(self.image_path)

    def __len__(self):
        return self.image_path.__len__()
    
    def __getitem__(self, index):
        image_path = self.image_path[index]
        # image = Image.open(image_path)
        # image.show()

        image = self.transforms(Image.open(image_path))
        label = image_path.split("_")[-1]
        label = label.split("_")[0]
        return image, label


if __name__ == "__main__":
    writer = SummaryWriter("logs")

    train_data = my_dataset("./datasets/train/")
    img, label = train_data[0]
    print(img.shape, label)

    writer.add_image("img", img, 1)
    writer.close()
