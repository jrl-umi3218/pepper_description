import sys; sys.path.append('..')

import rbdyn as rbd

import pepper


mb, mbc, mbg, limits, visual_tf, collision_tf =\
  pepper.readUrdf('pepper', pepper.rootBody,
                       pepper.virtualJoints, [],
                       pepper.halfSitting)


def robot(fixed=False):
  if not fixed:
    return mb, mbc, mbg
  else:
    mbF = mbg.makeMultiBody(mbg.bodyIdByName(pepper.rootBody), True)
    mbcF = rbd.MultiBodyConfig(mbF)
    mbcF.zero(mbF)
    return mbF, mbcF, mbg

'''
def convexHull():
  fileByBodyName = pepper.stdCollisionsFiles(mb)
  return pepper.convexHull(fileByBodyName, mb)


def stpbvHull():
  fileByBodyName = pepper.stdCollisionsFiles(mb)
  return pepper.stpbvHull(fileByBodyName, mb)


def collisionTransforms():
  return collision_tf


def bounds():
  return pepper.nominalBounds(limits)


def stance():
  return pepper.halfSittingPose(mb), ('LeftFoot', 'RightFoot')


def forceSensors():
  return pepper.forceSensors


def accelerometerBody():
  return pepper.accelBody
'''
