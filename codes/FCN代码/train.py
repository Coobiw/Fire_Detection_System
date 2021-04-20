import torch as t
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from datetime import datetime
from dataset import CamvidDataset
from evalution_segmentaion import eval_semantic_segmentation
from FCN import FCN
import cfg
from torch.utils.tensorboard import SummaryWriter
import time




def train(model):
    best = [0]
    writer = SummaryWriter(log_dir='train_log',comment='train')
    model.train()
    # 训练轮次
    for epoch in range(cfg.EPOCH_NUMBER):
        t1 = time.time()
        print("Eopch is [{}/{}]".format(epoch + 1, cfg.EPOCH_NUMBER))
        if epoch % 50 == 0 and epoch != 0:
            for group in optimizer.param_groups:
                group["lr"] *= 0.1

        train_loss = 0
        train_acc = 0
        train_miou = 0
        train_class_acc = 0

        for i, sample in enumerate(train_data):
            img_data = Variable(sample["img"].to(device))
            img_label = Variable(sample["label"].to(device))

            out = model(img_data)
            out = F.log_softmax(out, dim=1)
            loss = criterion(out, img_label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print("Epoch %d/%d| Step %d/%d| Loss: %.5f" % (epoch, cfg.EPOCH_NUMBER, i, (247// cfg.BATCH_SIZE), loss))
            train_loss += loss.item()

            pre_label = out.max(dim=1)[1].data.cpu().numpy()
            pre_label = [i for i in pre_label]

            true_label = img_label.data.cpu().numpy()
            true_label = [i for i in true_label]
            for index,sample in enumerate(pre_label):
                eval_metric = eval_semantic_segmentation(pre_label[index], true_label[index])
                train_acc += eval_metric["mean_class_accuracy"]
                train_miou += eval_metric["miou"]
                train_class_acc += eval_metric["class_accuracy"]

            print(".........")
            print("finished No.%d batch computing ! "%(i+1))
        if (epoch+1)%50 ==0:
            t.save(model,"./models_save/FCN_epoch"+str(epoch+1)+".pth")
        t2 = time.time()
        print('the training time per epoch:  ',t2-t1)
        writer.add_scalar('train_loss_line',loss,epoch)
        writer.add_scalar('miou', train_miou/247, epoch)
        writer.add_scalar('train_acc', train_acc/247, epoch)
    print("finish training")


if __name__ == '__main__':
    device = t.device("cuda") if t.cuda.is_available() else t.device("cpu")

    Cam_train = CamvidDataset([cfg.TRAIN_ROOT, cfg.TRAIN_LABEL], cfg.crop_size)
    # Cam_val = CamvidDataset([cfg.VAL_ROOT, cfg.VAL_LABEL], cfg.crop_size)

    train_data = DataLoader(Cam_train, batch_size=cfg.BATCH_SIZE, shuffle=True, num_workers=1)
    # val_data = DataLoader(Cam_val, batch_size=cfg.BATCH_SIZE, shuffle=True, num_workers=1)

    fcn = FCN(2)
    fcn = fcn.to(device)
    criterion = nn.NLLLoss().to(device)
    optimizer = optim.Adam(fcn.parameters(), lr=5e-3,betas = (0.9,0.99))
    train(fcn)




