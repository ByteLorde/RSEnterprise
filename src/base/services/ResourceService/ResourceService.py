import os

class ResourceService:

    ROOT_DIRECTORY = '../../../../'

    ASSETS_DIRECTORY = ROOT_DIRECTORY   + 'assets/'
    IMAGE_DIRECTORY  = ASSETS_DIRECTORY + 'images/'

    @staticmethod
    def getAsset(assetName):
        dir = os.listdir(ResourceService.ASSETS_DIRECTORY)

    @staticmethod
    def getImage(imageName):
        dir = os.listdir(ResourceService.IMAGE_DIRECTORY)

    @staticmethod
    def viewAssets():

        assets = os.listdir(ResourceService.ASSETS_DIRECTORY)
        assert assets is not None, 'ERROR: No assets to view from ' + ResourceService.ASSETS_DIRECTORY

        return assets

    @staticmethod
    def viewImages():

        images = os.listdir(ResourceService.IMAGE_DIRECTORY)
        assert images is not None, 'ERROR: No images to view from ' + ResourceService.IMAGE_DIRECTORY

        return images

