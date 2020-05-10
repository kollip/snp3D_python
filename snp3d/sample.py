import snp3d
import numpy as np
import matplotlib.pyplot as plt

def main():
    N1,N2,N3,snapshop_time,dx,dt,p=snp3d.read_snp3d("/Users/yusuke/Downloads/Pr_001000.snp3D")
    
    ### pressure visualize
    p_cross_section=p[:,int(N2/2),:]
    plt.imshow(p_cross_section)
    plt.colorbar()
    plt.show()
    ### 

if __name__ == "__main__":
    main()