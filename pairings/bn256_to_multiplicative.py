""" Wrapper to represent bn256 groups as multiplicative groups.

CurvePoint and CurveTwist classes from bn256 are overwritten.

Copyright (c) 2020 Toon Segers 
"""    


import sys, os
project_root = sys.path.append(os.path.abspath('..')) 
if project_root not in sys.path:
    sys.path.insert(0, project_root)
import logging

from zk_helpers.pairings.bn256 import *


logger_bn_mul = logging.getLogger("bn256_mul")
logger_bn_mul.setLevel(logging.INFO)

pow_counter_regular = 0
pow_counter_twist = 0



class CurvePointMult(CurvePoint):
    def __add__(self, other): 
        return NotImplementedError("Addition not defined in multiplicative notation.")

    def __mul__(self, other): 
        return self.add(other)

    def __pow__(self, scalar): 
        global pow_counter_regular
        pow_counter_regular += 1
        logger_bn_mul.debug(f"pow_counter_regular={pow_counter_regular}")
        # return self.scalar_mul(scalar)
        return self.scalar_mul(int(scalar))



# Any point (1,y) where y is a square root of b+1 is a generator
curve_G = CurvePointMult(GFp_1(1), GFp_1(p-2))

assert curve_G.is_on_curve()


class CurveTwistMult(CurveTwist):
    def __add__(self, other): 
        return NotImplementedError("Addition not defined in multiplicative notation.")

    def __mul__(self, other): 
        return self.add(other)

    def __pow__(self, scalar): 
        global pow_counter_twist
        pow_counter_twist += 1
        logger_bn_mul.debug(f"pow_counter_twist={pow_counter_twist}")        
        # return self.scalar_mul(scalar)
        return self.scalar_mul(int(scalar))


# TODO derive this
twist_G = CurveTwistMult(
    GFp_2(21167961636542580255011770066570541300993051739349375019639421053990175267184,
          64746500191241794695844075326670126197795977525365406531717464316923369116492),
    GFp_2(20666913350058776956210519119118544732556678129809273996262322366050359951122,
          17778617556404439934652658462602675281523610326338642107814333856843981424549),
    GFp_2(0,1))

assert twist_G.is_on_curve()