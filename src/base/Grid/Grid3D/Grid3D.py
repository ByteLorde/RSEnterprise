import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from src.base.objs.DepthPerception.DepthPerception import DepthPerception
from src.base.objs.modules.ContourDetection import ContourDetection
from src.base.objs.modules.Threshold.Threshold import Threshold
from src.plugins.Bot.objs.template.Template import Template


class Grid3D:

    def __init__(self, x, y, z, image, title="3D Scatter Plot"):
        t = Template.fromImage(image)

        t.setImage(t.resize(100, 100))

        # create the x and y coordinate arrays (here we just use pixel indices)
        lena = t.getImage()

        xx, yy = np.mgrid[0:t.getImage().shape[0], 0:t.getImage().shape[1]]
        print(len(xx))
        print(len(yy))
        # create the figure
        fig = plt.figure()


        ax = fig.gca(projection='3d')


        # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        ax.plot_surface(xx, yy, lena, rstride=1, cstride=1, cmap=plt.cm.coolwarm,
                        linewidth=0, vmin=0.0, vmax=0.5)

        ax.view_init(90, 1)
        # show it
        plt.show()
    def show(self):
        pass

    def setAxisLengths(self):

        depth  = 255
        domain = 1024
        range  = 1024



        self.axis.set_zlim3d([0.0, depth])
        self.axis.set_zlabel('Z')

        self.axis.set_xlim3d([0.0, domain])
        self.axis.set_xlabel('X')

        self.axis.set_ylim3d([0.0, range])
        self.axis.set_ylabel('Y')


    def setTitle(self, title):
        self.axis.set_title(title)

    def setXLabel(self, label):
        self.axis.set_xlabel(label)

    def setYLabel(self, label):
        self.axis.set_ylabel(label)

    def setZLabel(self, label):
        self.axis.set_zlabel(label)






def main():

    image = cv2.imread("C:/Users/Syndicate/Workspace/RSEnterprise/assets/faces/s1/3d-ultrasound-baby-image.jpg", 0)
    # print(image)
    detector = ContourDetection.ContourDetection()

    maxVal = max(image.shape[0], image.shape[1])
    # x = [ 0 for domain in range(0, maxVal) ]
    # y = [ 0 for rangeVal in range(0, maxVal) ]
    # z = [ 0 for zVal in range(0, maxVal) ]
    #
    x = [ ]
    y = [ ]
    z = [ ]

    for yVal in range(0,len(image),1):
        for xVal in range(0,len(image[1]), 1):

            x.append(xVal)
            y.append(yVal)
            val = image[yVal][xVal] // 8
            image[yVal][xVal] = val



    # return
    # for col in range(image.shape[0]):
    #     for row in range(image.shape[1]):
    #         color = image[col][row]
    #         if color:
    #             x.append(col)
    #             y.append(row)
    #             z.append(image[col][row])
    data = (x, y, z)

    # for i in range(0, 1):
    #     thresh_image = threshold.threshold2(image, i)
    #     conts = detector.findContours(thresh_image)
    #     print(len(images))
    #     if i > 1:
    #         thresh_image = thresh_image - images[len(images) - 1]
    #     images.append(thresh_image)
    #
    #     y = []
    #
    #     for item in thresh_image:
    #         y.append(item)
    #         # print(item)

        # for col in range(thresh_image.shape[0]):
        #     for row in range(thresh_image.shape[1]):
        #         if thresh_image[col][row] == 255:
        #             x.append(col)
        #             y.append(row)
        #
        # for contour in conts[0]:
        #     x.append(contour[0][0])
        #     y.append(contour[0][1])

    # if cv2.waitKey(100000) & 0xFF == ord('q'):
    #     exit(1)

    grid = Grid3D(x, y, z, image)
    grid.show()


def main2():


    disp = DepthPerception()
    image = disp.getDisparityMap2()

    width  = image.shape[1]
    height = image.shape[0]

    dummy = np.ones(width, height)
    cv2.imshow("Oh1", dummy)
    cv2.imshow("Oh2", image)



def generateAHKFunc(min, max):

    line1 = "FirstName := RandomName(" + str(min) + ", " + str(max) + ")"

    script = ["GenerateInfo(byRef FirstName, byref LastName, byRef BirthDay, byRef BirthYear , byRef Email) ;------------------",
              "{",
              line1,
              "LastName := RandomName( 4,8 )",
              "Random, BirthDay, 1, 28",
              "Random, BirthYear, 1975, 1999",
              "BirthYearEdit := BirthYear - 1900",
              "Email = %FirstName%%LastName%%BirthYearEdit%",
              "Return",
              "} "
              ]

    fh = open("script2.ahk", "w")
    for line in script:
        fh.write(line + "/n")
    fh.close()

# generateAHKFunc(51, 101)

main()