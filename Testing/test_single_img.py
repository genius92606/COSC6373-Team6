from ultralytics import YOLO
import argparse
import cv2
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', '--model')
    parser.add_argument('-img',  '--img')

    args = parser.parse_args()
    # Load a model
    model = YOLO(args.model)  # load the best model
    model
    res = model(args.img)
    res_plotted = res[0].plot()
    cv2.imshow("result",res_plotted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()