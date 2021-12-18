import Bose_Resolution as BR
import Test
import Three_v_plus_one_construction as TVP1
import sys

if __name__ == '__main__':
    u = input("Enter the number of files u in the storage system: ")
    u = int(u)
    if u % 108 in [13, 40]:
        v = (u - 1)//3
        s24v_ingred = []
        file_name = input("Enter the name of the file containing the input S(2,4,(u-1)/3): ")
        with open(file_name) as f:
            line = f.readline()
            line_t = line.split()
            block = map(int, line_t)
            block = list(block)
            s24v_ingred = s24v_ingred + [block.copy()]
            while line:
                line = f.readline()
                line_t = line.split()
                block = map(int, line_t)
                block = list(block)
                s24v_ingred = s24v_ingred + [block.copy()]

        s24v_ingred.pop()

        # get the storage system ss, represented as an S(2,4,u)
        ss = TVP1.three_v_plus_one_construction(v, s24v_ingred)
        print("Here is the resulting storage system on", u, "points, having guaranteed MinSum at least (4*u + 2)/3 =", (4*u + 2)//3, ":")
        for block in ss:
            print(block)
    else:
        print("Error: The number of files must be congruent to 13 or 40 modulo 108.")


