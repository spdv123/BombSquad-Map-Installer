# coding=utf-8
import bs
import math
import random
from bsMap import *


class YinYangMap(Map):
    import yinYangLevelDefs as defs
    name = 'Sword & Tai Chi'
    playTypes = ['melee', 'keepAway', 'teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'yinyangPreview'

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

        data['swordModel'] = bs.getModel('sword')
        data['swordTex'] = bs.getTexture('swordColor')
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

        self.swordExtra = {}
        self.initSword()

    def initSword(self):
        swordModel = self.preloadData['swordModel']
        swordTex = self.preloadData['swordTex']

        class swordActor(bs.Actor):
            def __init__(self, horizontal=True):
                bs.Actor.__init__(self)
                self.horizontal = horizontal
                self.node = None
                self.initNode()

            def initNode(self):
                ru = random.uniform
                ra = (-2, 2)
                self.node = bs.newNode("prop",
                                       attrs={'position': (2 + ru(*ra), 8 + ru(*ra), ru(*ra)),
                                              'velocity': (0, 0, 0),
                                              'model': swordModel,
                                              'body': 'sphere',
                                              'colorTexture': swordTex,
                                              'modelScale': 1,
                                              'isAreaOfInterest': False,
                                              'bodyScale': 1,
                                              'materials': [],
                                              'density': 1.0,
                                              'gravityScale': 0.0,
                                              },
                                       delegate=self)
                self._move2D(8, self.horizontal)

            def _move2D(self, value, horizontal=True):
                """
                Moves the platform horizontally back and forth.
                You spawn it in the middle to make it move.
                velocity keeps the platform running and stable
                extraAcceleration makes the platform not slow down
                """
                v = self.node.velocity

                def _safeSetAttr(node, attr, val, l=False):
                    if node.exists():
                        if l:
                            valu = val[0] + val[2]
                            valueAbs = abs(valu)
                            valueSign = -1 if value < 0 else 1
                            rx = random.uniform(0, valueAbs)
                            ry = math.sqrt(valueAbs ** 2 - rx ** 2)
                            val = (valueSign * rx, val[1], valueSign * ry)
                        setattr(node, attr, val)

                def _repeatMove():
                    bs.gameTimer(1, bs.Call(_safeSetAttr, self.node, 'velocity', (-value / 3, 0, 0)))
                    bs.gameTimer(1, bs.Call(_safeSetAttr, self.node, 'extraAcceleration', (-value / 1.25, 0, 0)))
                    bs.gameTimer(2000, bs.Call(_safeSetAttr, self.node, 'velocity', (value / 3, 0, 0), True))
                    bs.gameTimer(2000,
                                 bs.Call(_safeSetAttr, self.node, 'extraAcceleration', (value / 1.25, 0, 0), True))
                    bs.gameTimer(4000, bs.Call(_repeatMove))

                def _keepHorizontal():
                    v = self.node.velocity
                    bs.gameTimer(1, bs.Call(_safeSetAttr, self.node, 'extraAcceleration', (0, -v[1], -v[2])))
                    bs.gameTimer(1, bs.Call(_keepHorizontal))

                bs.gameTimer(1, bs.Call(_safeSetAttr, self.node, 'velocity', (value / 3, 0, 0)))
                bs.gameTimer(1, bs.Call(_safeSetAttr, self.node, 'extraAcceleration', (value / 1.25, 0, 0)))
                bs.gameTimer(1000, bs.Call(_repeatMove))

            def handleMessage(self, m):
                if isinstance(m, bs.OutOfBoundsMessage):
                    self.handleMessage(bs.DieMessage())
                    self.initNode()
                if isinstance(m, bs.DieMessage):
                    if self.node is not None:
                        self.node.delete()
                        self.node = None
                bs.Actor.handleMessage(self, m)

        self.swordExtra['swords'] = []
        for i in range(6):
            self.swordExtra['swords'].append(
                swordActor(horizontal=bool(i % 2))
            )

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
