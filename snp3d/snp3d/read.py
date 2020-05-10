import struct
import numpy as np

def read_snp3d(dir):
    with open(dir,'rb') as fl:
        data=fl.read()
        N1,N2,N3=struct.unpack('iii',data[0:4*3])
        snapshop_time,dx,dt=struct.unpack('ddd',data[4*3:4*3+8*3])
        print("N1:{}, N2:{}, N3:{}".format(N1,N2,N3))
        print("snapshot time:{} micro sec".format(snapshop_time))
        print("dx:{} mm, dt:{} ms".format(dx,dt))

        fl.seek(4*3+8*3)
        p=np.fromfile(fl, np.float32)
        if p.shape[0]!=N1*N2*N3:
            print("ERROR: not match data size")
        p=np.reshape(p,(N1,N2,N3))

        return N1,N2,N3,snapshop_time,dx,dt,p