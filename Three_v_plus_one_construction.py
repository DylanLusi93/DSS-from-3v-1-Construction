import Bose_Resolution as BR
def three_v_plus_one_construction(v, s_2_4_v):
    """Applies the 3v+1 construction with ingredient KTS(2v + 1) (which we assume is the Bose-averaging triple system
     of order 2v + 1) and S(2,4,v). s_2_4_v must be a list of quadruples on point set [0, v-1]. The resulting points
     of the output S(2,4,u = 3v + 1) are labelled such that its MinSum is at least (4*u + 2)/3."""

    s_2_4_3v_plus_1 = [[] for _ in range(3*v*(3*v + 1)//12)]
    kts_order = 2*v + 1
    als_order = kts_order//3
    if als_order % 18 in [3, 15] and als_order > 15 and als_order % 5 != 0:
        # force s_2_4_v onto point set [2v + 1, 3v]
        for quadruple in s_2_4_v:
            quadruple += kts_order
        bats = BR.bats_from_br(als_order)
        for x in range(2*v + 1, 3*v + 1):
            for triple in bats[x - 2*v + 1]:
                s_2_4_3v_plus_1 = s_2_4_3v_plus_1 + [[x] + triple]

    else:
        print("Error: Invalid v. (2v + 1)/3 must be congruent to 3 or 15 mod 18, must be greater than 15, and must not"
              " be divisible by 5.")

    return s_2_4_3v_plus_1
