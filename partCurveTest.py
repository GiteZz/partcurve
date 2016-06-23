import bpy
import bmesh
import math

def createPartCircle(rot,m_point,angle,radius,a_verts,bm,o,rot1,rot2):
    

    
    loc_verts = []
    verts = []
    edges = []
    p_angle = angle/(a_verts-1)
    
    for i in range(0,a_verts):
            loc_verts.append([radius*math.cos(i*p_angle),radius*math.sin(i*p_angle),0])
            
    if rot1 != "O":
        if rot1 == "X":
            print("X rotatie")
            for i in range(0,a_verts):
                loc_verts[i] = rotatexaxis(rot[0],loc_verts[i])
        if rot1 == "Y":
            print("Y rotatie")
            for i in range(0,a_verts):
                loc_verts[i] = rotateyaxis(rot[1],loc_verts[i])
        if rot1 == "Z":
            print("Z rotatie")
            for i in range(0,a_verts):
                loc_verts[i] = rotatezaxis(rot[2],loc_verts[i])
     
    if rot2 != "O":
        if rot2 == "X":
            for i in range(0,a_verts):
                loc_verts[i] = rotatexaxis(rot[0],loc_verts[i])
        if rot2 == "Y":
            for i in range(0,a_verts):
                loc_verts[i] = rotateyaxis(rot[1],loc_verts[i])
        if rot2 == "Z":
            for i in range(0,a_verts):
                loc_verts[i] = rotatezaxis(rot[2],loc_verts[i])
                
    for i in range(0,a_verts):
            loc_verts[i][0]+=m_point[0]
            loc_verts[i][1]+=m_point[1]
            loc_verts[i][2]+=m_point[2]
     
    for i in range(0,a_verts):
        verts.append(bm.verts.new(loc_verts[i]))       
    for i in range(0,a_verts-1):
            edges.append(bm.edges.new((verts[i],verts[i+1])))
            
         
    bmesh.update_edit_mesh(o.data)


def rotatexaxis(a,p):
        X = p[0]
        Y = math.cos(a)*p[1]-math.sin(a)*p[2]
        Z = math.sin(a)*p[1]+math.cos(a)*p[2]

        return [X,Y,Z]

def rotateyaxis(a,p):
        X = math.cos(a)*p[0]+math.sin(a)*p[2]
        Y = p[1]
        Z = -math.sin(a)*p[0]+math.cos(a)*p[2]
        
        return [X,Y,Z]

def rotatezaxis(a,p):
        X = math.cos(a)*p[0]-math.sin(a)*p[1]
        Y = math.sin(a)*p[0]+math.cos(a)*p[1]
        Z = p[2]

        return [X,Y,Z]


def inp(v,w):
    return v[0]*w[0]+v[1]*w[1]+v[2]*w[2]

def m_matrix(X,Y):
    w, h = len(Y[0]), len(X) 
    result = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    return result
                
def t_matrix(X):
    w,h = len(X),len(X[0])
    result = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(X)):
        for j in range(len[0]):
            result[j][i] = X[i][j]
            
    return result

def angle_v(v1,v2):
    if inp(v1,v2) == 0:
        return math.pi/2
    else:
        incos = (v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2])/(math.sqrt(math.pow(v1[0],2)+math.pow(v1[1],2)+math.pow(v1[2],2))*math.sqrt(math.pow(v2[0],2)+math.pow(v2[1],2)+math.pow(v2[2],2)))
        return math.acos(incos)

def crosDet(u1,u2):
    return [u1[1]*u2[2]-u2[1]*u1[2],-(u1[0]*u2[2]-u2[0]*u1[2]),u1[0]*u2[1]-u1[1]*u2[0]]

def v_Norm(v):
    w = math.sqrt(math.pow(v[0],2)+math.pow(v[1],2)+math.pow(v[2],2))
    
    return [v[0]/w,v[1]/w,v[2]/w]


def p_Distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2)+math.pow(p1[2]-p2[2],2))

def v_to_co(v):
    return [v.co.x,v.co.y,v.co.z]

def r_from_v(v1,v2):
    return [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]



print("")
print("")
print("====================================")
print("")
print("")


obj = bpy.context.active_object
bm = bmesh.from_edit_mesh(obj.data) 

sel_v = []
v_o = []
e_v = []
edges_m = []
inc = True

for v in bm.verts:
    if v.select:
        sel_v.append(v)

for e in bm.edges:
    if e.select:
        e_n = []
        e_n.append(e.verts[0])
        e_n.append(e.verts[1])
        edges_m.append(e_n)

'''      
print("amount of verts")
print(len(sel_v))
print("amount of edges")
print(len(edges_m))
'''

if len(edges_m)!=len(sel_v)-1:
    print("niet voldaan aan vw")
    #return {'FINISHED'}

v_o.append(sel_v[0])
c_i = 0

while(inc):
    inc = False
    for a in range(0,len(edges_m)):
        sel_v[c_i]
        edges_m[a]
        if sel_v[c_i] in edges_m[a]:
            inc = True
            if edges_m[a][0] == sel_v[c_i]:
                v_o.append(edges_m[a][1])
            else:
                v_o.append(edges_m[a][0])
            e_v.append(edges_m[a])
            del sel_v[c_i]
            del edges_m[a]
            c_i = sel_v.index(v_o[len(v_o)-1])
            break
del sel_v[c_i]
        
'''
print("amount of verts after first loop")
print("originel " + str(len(sel_v)))
print("nieuw " + str(len(v_o)))
print("amount of edges after first loop")
print("originel " + str(len(edges_m)))
print("nieuw " + str(len(e_v)))  
'''

while(len(edges_m)!=0):
    '''
    print("length in while loop")
    print(len(sel_v))
    print(len(edges_m))
    '''
    for a in range(0,len(edges_m)):
        if v_o[0] in edges_m[a]:
            inc = True
            if edges_m[a][0] == v_o[0]:
                v_o.insert(0,edges_m[a][1])
            else:
                v_o.insert(0,edges_m[a][0])
            e_v.insert(0,edges_m[a])
            del sel_v[sel_v.index(v_o[0])]
            del edges_m[a]
            break

v_gem = [0,0,0]

for i in range(0,len(v_o)-1):
    v_gem[0] += v_o[i].co.x
    v_gem[1] += v_o[i].co.y
    v_gem[2] += v_o[i].co.z

v_gem[0]=v_gem[0]/len(v_o)
v_gem[1]=v_gem[1]/len(v_o)
v_gem[2]=v_gem[2]/len(v_o)

u1 = [v_o[0].co.x-v_gem[0],v_o[0].co.y-v_gem[1],v_o[0].co.z-v_gem[2]]
u2 = [v_o[len(v_o)-1].co.x-v_gem[0],v_o[len(v_o)-1].co.y-v_gem[1],v_o[len(v_o)-1].co.z-v_gem[2]]

face_n = crosDet(u1,u2)

print(face_n)

'''
if face_n[0] == 0 and face_n[0] == 0:
    h_XY = math.pi/2
else:
    h_XY = angle_v(face_n,[face_n[0],face_n[1],0])


h_ZX = angle_v([face_n[0],face_n[1],0],[1,0,0])
'''
a_c = angle_v(u1,u2)

#print(h_XY)
#print(h_ZX)
print(a_c)

middle = [(v_o[0].co.x+v_o[len(v_o)-1].co.x)/2,(v_o[0].co.y+v_o[len(v_o)-1].co.y)/2,(v_o[0].co.z+v_o[len(v_o)-1].co.z)/2]

l_l = [v_o[0].co.x-v_o[len(v_o)-1].co.x,v_o[0].co.y-v_o[len(v_o)-1].co.y,v_o[0].co.z-v_o[len(v_o)-1].co.z]

m_l = crosDet(l_l,face_n)
m_l = v_Norm(m_l)

s = 1

c_m = [middle[0]+s*m_l[0],middle[1]+s*m_l[1],middle[2]+s*m_l[2]]

rad = p_Distance(c_m,[v_o[0].co.x,v_o[0].co.y,v_o[0].co.z])

angle = angle_v(r_from_v(c_m,v_to_co(v_o[0])),r_from_v(c_m,v_to_co(v_o[len(v_o)-1])))

print("circle angle" + str(angle))

print("midlle" + str(middle))

print("hfsdqhsdfhs")

secangle = math.pi/4

if p_Distance(v_gem,c_m) < p_Distance(middle,c_m):
    angle = 2*math.pi-angle
    secangle = -1*secangle


t_angle = angle_v([m_l[0],m_l[1],0],[0,1,0])
o_angle = angle_v(m_l,[m_l[0],m_l[1],0])

print("dkdk")
print(o_angle)

secangle = t_angle+secangle

createPartCircle([o_angle,0,secangle],c_m,angle,rad,24,bm,obj,'Z','X')

#createPartCircle([h_ZX,h_XY,0],v_gem,3.14/2,1,24,bm,obj,'Y','Z')