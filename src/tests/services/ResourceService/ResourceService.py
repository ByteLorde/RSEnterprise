from src.base.services.ResourceService.ResourceService import ResourceService


def runTestingSuite():
    resourceServiceShouldLoadAssets()
    resourceServiceShouldLoadImages()

def resourceServiceShouldLoadAssets():
    assets = ResourceService.viewAssets()
    print('ASSETS', assets)

def resourceServiceShouldLoadImages():
    images = ResourceService.viewImages()
    print('IMAGES', images)





if __name__ == '__main__':
    runTestingSuite()
