import Bose_Resolution as BR
import Test
import Three_v_plus_one_construction as TVP1
import sys

if __name__ == '__main__':
    # Note: testFile contains an ingredient S(2,4,76) that you may use to test the program; if you
    # do opt to do this, set u (number of files) to 76*3 + 1 = 229

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

        if not Test.is_s24v(v, s24v_ingred):
            print("Error: The provided putative ingredient S(2,4,v) is not an S(2,4,v)!")
        # get the storage system ss, represented as an S(2,4,u)
        ss = TVP1.three_v_plus_one_construction(v, s24v_ingred)
        if not Test.is_s24v(3*v + 1, ss):
            print("OH NOOOOOOO")
        print("Here is the resulting storage system on", u, "points, having guaranteed MinSum at least (4*u + 2)/3 =", (4*u + 2)//3, ":")
        for block in ss:
            print(block)
    else:
        print("Error: The number of files must be congruent to 13 or 40 modulo 108.")


