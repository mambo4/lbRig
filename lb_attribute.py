__author__='logan.e.bender@gmail.com'

"""
maya addAttr, listAttr, is confusing with its datatype vs attributetype 

atrribute type values
boolean	        -at bool
32 bit integer	-at long
16 bit integer	-at short
8 bit integer	-at byte
char	        -at char
enum	        -at enum (specify the enum names using the enumName flag)
float	        -at "float" (use quotes since float is a mel keyword)
double	        -at double
angle value	    -at doubleAngle
linear value	-at doubleLinear
compound	    -at compound
message(no data)-at message
time	        -at time
4x4 float mat	-at fltMatrix
<dt value>(compound)	-at <dt value>

datatype values
string	        -dt "string" (use quotes since string is a mel keyword)
4x4 double mat	-dt "matrix" (use quotes since matrix is a mel keyword)
array of strings-dt stringArray
reflectance	    -dt reflectanceRGB
spectrum	    -dt spectrumRGB
2 floats	    -dt float2
3 floats	    -dt float3
2 doubles	    -dt double2
3 doubles	    -dt double3
2 32-bit integers	-dt long2
3 32-bit integers	-dt long3
2 16-bit integers	-dt short2
3 16-bit integers	-dt short3
array of doubles	-dt doubleArray
array of floats	    -dt floatArray
array of 32-bit ints-dt Int32Array
array of vectors	-dt vectorArray
nurbs curve	        -dt nurbsCurve
nurbs surface	    -dt nurbsSurface
polygonal mesh	    -dt mesh
lattice	            -dt lattice
array of double 4D points	-dt pointArray
"""
import pymel.core as pm

class MayaAttribute(object):

    def __init__(self,name,value,type=None,data_type=None):
        self.name=name
        self.value=value
        self.type=type
        self.data_type=data_type

