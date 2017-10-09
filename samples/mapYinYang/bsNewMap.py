# coding=utf-8
import bs
from bsMap import *


class YinYangMap(Map):
    import yinYangLevelDefs as defs
    name = 'Yin Yang'
    playTypes = ['melee', 'keepAway', 'teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'yinYangPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('yinyangMap')
        data['collideModel'] = bs.getCollideModel('yinyangMap')
        data['tex'] = bs.getTexture('yinyangMap')
        data['bgTex'] = bs.getTexture('yinyangbg')
        data['bgModel'] = bs.getModel('yinyangbg')
        data['vrFillModel'] = bs.getModel('rampageVRFill')
        data['collideBG'] = bs.getCollideModel('doomShroomStemCollide')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel': self.preloadData['collideModel'],
                                      'model': self.preloadData['model'],
                                      'colorTexture': self.preloadData['tex'],
                                      'materials': [bs.getSharedObject('footingMaterial')]})
        self.foo = bs.newNode('terrain',
                              attrs={'model': self.preloadData['bgModel'],
                                     'lighting': False,
                                     'background': True,
                                     'colorTexture': self.preloadData['bgTex']})
        bs.newNode('terrain',
                   attrs={'model': self.preloadData['vrFillModel'],
                          'lighting': False,
                          'vrOnly': True,
                          'background': True,
                          'colorTexture': self.preloadData['bgTex']})
        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.82, 1.10, 1.15)
        bsGlobals.ambientColor = (0.9, 1.3, 1.1)
        bsGlobals.shadowOrtho = False
        bsGlobals.vignetteOuter = (0.76, 0.76, 0.76)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.99)

    def _isPointNearEdge(self, p, running=False):
        x = p.x()
        z = p.z()
        xAdj = x * 0.125
        zAdj = (z + 3.7) * 0.2
        if running:
            xAdj *= 1.4
            zAdj *= 1.4
        return (xAdj * xAdj + zAdj * zAdj > 1.0)


registerMap(YinYangMap)
