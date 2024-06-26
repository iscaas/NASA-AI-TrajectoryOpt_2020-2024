
import argparse

cases = {
    '1': {
        'GTO_state': [67288.41965,0,-32107.258900,0.7306,0,0,0,0],
        'Isp': [1800],
        'm0': [1200],
        'force': [0.311],
        'tol_inc': [0.1], #[0.1], #[0.1],
        'tol_ecc': [0.002], #[0.1], #[0.002],
        'tol_a': [50], #[1000], #[55],  #0.5
        'w1_a': [1000],
        'w1_e': [2010],
        'w1_i': [300],
        'w1_a_': [0.010],
        'w1_e_': [0.000000198],
        'w1_i_': [0.0003],
        'c1_a': [500],
        'c1_e': [700],
        'c1_i': [300],
        'tau': [0.003],  
        'sh_flag' : [1],    
        'weights_path': ["GTO1_1stnet"],
        'max_steps_in_ep': [10000]
    },
    
    
    '2': {
        'GTO_state':  [129701.32616201644,242.22646808805715,-52.55836958415796,0.0005709976204518968,0.0012318847894861632,3.8377777777777786,0,166.52542861175831],
        'Isp': [1800],
        'm0': [1200],
        'force': [0.311],
        'tol_inc': [0.1],
        'tol_ecc': [0.00035], #[0.00009], #0.0002
        'tol_a': [0.04], #[0.6],
        'w1_a': [1000*4],
        'w1_e': [700*4],
        'w1_i': [200],
        'w1_a_':  [0.010*3],
        'w1_e_': [0.000000198*3],
        'w1_i_': [0.0003],
        'c1_a': [500*3],
        'c1_e': [700*3],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [0],
        'weights_path': ["GTO1_2ndnet"],
        'max_steps_in_ep': [2500]
    },
    
    
    '3': {
        'GTO_state': [67246.21689,0,-30529.143615,0.7310,0,0,0,0],
        'Isp': [3300],
        'm0': [450],
        'force': [0.2007],
        'tol_inc': [0.1],
        'tol_ecc': [0.01],
        'tol_a': [55],#[1000], #[50],
        'w1_a': [1000],
        'w1_e': [2010],
        'w1_i': [300],
        'w1_a_': [0.010],
        'w1_e_': [0.000000198],
        'w1_i_': [0.0003],
        'c1_a': [500],
        'c1_e': [700],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [1],
        'weights_path': ["GTO2_1stnet"],
        'max_steps_in_ep': [20000]
    },
    
    
    '4': {
        'GTO_state':  [129553.7033, 68.5070    ,190.09818  ,0.003963 ,0.003109,1.97471 ,0,35.369],
        'Isp': [3300],
        'm0': [450],
        'force': [0.2007],
        'tol_inc': [0.08],
        'tol_ecc': [0.00047],#[0.000088],
        'tol_a': [0.02], #[0.2],
        'w1_a': [1000*3],
        'w1_e': [700*3],
        'w1_i': [200],
        'w1_a_':  [0.010*3],
        'w1_e_': [0.000000198*3],
        'w1_i_': [0.0003],
        'c1_a': [500*3],
        'c1_e': [700*3],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [0],
        'weights_path': ["GTO2_2ndnet"],
        'max_steps_in_ep': [2800]
        
    },
    '5': {
        'GTO_state': [68196.3519, 0.0, -8311.0446, 0.725 ,0.0, 0.0, 0.0, 0.0],
        'Isp': [3000],
        'm0': [2000],
        'force': [0.35],
        'tol_inc': [0.1],
        'tol_ecc': [0.04], #[0.01],
        'tol_a': [55], #[1000], #[55],
        'w1_a': [1000],
        'w1_e': [2010],
        'w1_i': [300],
        'w1_a_': [0.010],
        'w1_e_': [0.000000198],
        'w1_i_': [0.0003],
        'c1_a': [500],
        'c1_e': [700],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [0],
        'weights_path': ["GTO3_1stnet"],
        'max_steps_in_ep': [20000]
    },
    
    
    '6': {
        'GTO_state': [129587.7702466053,-142.18173517005152,-143.0998837431866,0.03777324151464728,0.013683441829397463,2.6166666666666667,0,145.5640398800398],
        'Isp': [3000],
        'm0': [2000],
        'force': [0.35],
        'tol_inc': [0.1],
        'tol_ecc': [0.01], #[0.0009],
        'tol_a': [20],
        'w1_a': [1000*3],
        'w1_e': [700*6],
        'w1_i': [200],
        'w1_a_':  [0.010*3],
        'w1_e_': [0.000000198*6],
        'w1_i_': [0.0003],
        'c1_a':[ 500*3],
        'c1_e': [700*6],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [0],
        'weights_path':["GTO3_2ndnet"],
        'max_steps_in_ep': [8000]
    },
    
    
    '7': {
        'GTO_state': [70532.88179,0,-26991.765301,0.8705,0,0,0,0],
        'Isp': [3300],
        'm0': [1200],
        'force':[ 0.4015],
        'tol_inc': [0.2], #[0.1],
        'tol_ecc': [0.01],#[0.002],
        'tol_a': [50],#[50],
        'w1_a': [1000],
        'w1_e': [2010*2],
        'w1_i': [300],
        'w1_a_': [0.010],
        'w1_e_': [0.000000198*2],
        'w1_i_':[0.0003],
        'c1_a': [500],
        'c1_e': [1000*2],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [1],
        'weights_path': ["SuperGTO_1stnet"],
        'max_steps_in_ep': [20000]
    },
    
    
    '8': {
        'GTO_state': [129716.958,-94.25024,96.79678,0.001664012,-0.0008,4.842,0,-83.1957386893648], #   e0.00186 i 0.06 a50
        'Isp': [3300],
        'm0': [1200],
        'force': [0.4015],
        'tol_inc': [0.12],
        'tol_ecc': [0.000699], #[0.0002],
        'tol_a': [2],#[0.6],
        'w1_a': [1000*2*4],
        'w1_e': [2010*2*4],
        'w1_i': [300],
        'w1_a_': [0.010*4],
        'w1_e_': [0.000000198*4],
        'w1_i_': [0.0003],
        'c1_a': [500*4],
        'c1_e': [1000*4],
        'c1_i': [300],
        'tau': [0.003],
        'sh_flag' : [0],
        'weights_path': ["SuperGTO_2ndnet"],
        'max_steps_in_ep': [6000]
    }

}


