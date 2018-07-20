import cv2

class ContourDetection:

    """
    --RETRIEVAL MODES--
        EXTERNAL - Retrieves only the extreme outer contours. It sets hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
        LIST     - Retrieves all of the contours without establishing any hierarchical relationships.
        CCOMP    - Retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components.
                   At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
        TREE     - Retrieves all of the contours and reconstructs a full hierarchy of nested contours. This full hierarchy is built and shown in the OpenCV contours.c demo.

    --APPROXIMATION METHODS--
        CHAIN_APPROX_NONE   - Stores absolutely all the contour points. That is, any 2 subsequent points (x1,y1) and (x2,y2) of the contour will be either horizontal, vertical or diagonal neighbors,
                              that is, max(abs(x1-x2),abs(y2-y1))==1.
        CHAIN_APPROX_SIMPLE - Compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with 4 points.
        CHAIN_APPROX_TC89_L1   - See external documentation
        CHAIN_APPROX_TC89_KCOS - see external documentation
    """

    # Retrieval Modes
    EXTERNAL = cv2.RETR_EXTERNAL
    LIST     = cv2.RETR_LIST
    CCOMP    = cv2.RETR_CCOMP
    TREE     = cv2.RETR_TREE

    # Approximation Methods
    CHAIN_APPROX_NONE      = cv2.CHAIN_APPROX_NONE
    CHAIN_APPROX_SIMPLE    = cv2.CHAIN_APPROX_SIMPLE
    CHAIN_APPROX_TC89_L1   = cv2.CHAIN_APPROX_TC89_L1
    CHAIN_APPROX_TC89_KCOS = cv2.CHAIN_APPROX_TC89_KCOS

    def __init__(self):
        self.mode = ContourDetection.TREE
        self.method = ContourDetection.CHAIN_APPROX_SIMPLE

    def getResult(self):
        return self.result

    def findContours(self, image, mode=TREE, method=CHAIN_APPROX_SIMPLE):
        self.result, contours, hierarchy = cv2.findContours(image, mode, method)
        return contours


    def findExternalContours(self, image):
        self.result, contours, hierarchy = cv2.findContours(image, ContourDetection.EXTERNAL, ContourDetection.CHAIN_APPROX_SIMPLE)
        return contours

    def drawContours(self, image, contours, heiarchyPosition=-1, color=(0, 0, 255), thickness=2):
        self.result = cv2.drawContours(image, contours, heiarchyPosition, color, thickness, cv2.FILLED)
        return self.result
