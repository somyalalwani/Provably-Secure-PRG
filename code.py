seed_size=16
gen= 223 # generator
mod= 36389

def func_h(first_half,second_half):
    mod_exp_bin = bin(pow(gen, int(first_half, 2),mod))
    mod_exp_final = mod_exp_bin.replace('0b', '').zfill(seed_size)
    hcb = 0 #hcb
    l = len(first_half)
    for i in range(l):
        anding = int(first_half[i]) & int(second_half[i])
        x =hcb^anding
        hcb=x%2
    return mod_exp_final + second_half + str(hcb)

func_l=lambda x: x**2 - 2*x + 1

def func_g(init_seed):
    bstring = init_seed # binary_string
    ans=""
    l = func_l(seed_size)
    for i in range(l):
        x=int(len(bstring)/2)
        first , second = bstring[:x] , bstring[x:]
        bstring = func_h(first,second)
        ans= ans+bstring[-1]
        bstring = bstring[:-1]
    return ans


def main():
    seed = str(input("Enter seed : ")) # 1001100001110001
    if len(seed)>seed_size:
        print("Long initial seed")
    else:
        output = func_g(seed)
        print("Binary string produced by the seed: ")
        print(output)
        print("size:",seed_size,"->",func_l(seed_size))

if __name__ == '__main__':
    main()



#python3 p1.py 1001100001110001
