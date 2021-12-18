# We define a list of cells to be a cell of 3 integers
def lspcs_to_list_of_cells(LSPCs):
    cells_all = [cell for idx in range(len(LSPCs)) for cell in LSPCs[idx]]
    return cells_all

# Checks if list of cells partitions collection of diagonal pairs dps
def partitions_DPs(n: int, cells: list, dps: list) -> bool:
    seen_dps = {}
    # first, partition cells according to which diagonal pair they belong
    count = 0
    for c in cells:
        count += 1
        # check that c is a valid cell
        c_base = [(val - c[0]) % n for val in c]
        if c_base[1]/2 != c_base[2]:
            print("Error: invalid cell")
            return False

        if c_base[1] in seen_dps:
            if c[2] in seen_dps[c_base[1]]:
                return False
            else:
                seen_dps[c_base[1]] = seen_dps[c_base[1]] + [c[2]]
        else:
            seen_dps[c_base[1]] = [c[2]]

    if set(seen_dps.keys()) == set(dps):
        for key in seen_dps:
            seen_dps[key].sort()
            if seen_dps[key] != [x for x in range(n)]:
                return False
    else:
        return False

    return True

def is_pc(v, pc):
    pc_flattened = [triple[idx] for triple in pc for idx in range(3)]
    if set(pc_flattened) == set(range(v)):
        return True
    else:
        return False

def is_sts(v, sts):
    """Checks if input sts of order v is, in fact, a steiner triple system (where sts is list of triples). We assume
    that the point set of the sts is [0,v-1]"""

    position_pairs = [[0, 1], [0, 2], [1, 2]]
    pairs_points_all = [[x, y] for x in range(v) for y in range(x+1, v)]
    pairs_points_seen = [0 for _ in range(len(pairs_points_all))]

    for triple in sts:
        triple.sort()
        for pp in position_pairs:
            pairs_points_seen[pairs_points_all.index([triple[pp[0]], triple[pp[1]]])] += 1

    for x in pairs_points_seen:
        if x != 1:
            return False

    return True

def get_minsum(ss):
    """Gets MinSum of input Steiner system ss."""
    block_sums = []
    for block in ss:
        block_sums = block_sums + [sum(block)]

    return min(block_sums)

def is_s24v(v, s24v):
    """Checks if input S(2,4,v) s24v is, in fact, an S(2,4,v). We assume that the point set of the input S(2,4,v)
    is [0,v-1]"""

    position_pairs = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    pairs_points_all = [[x, y] for x in range(v) for y in range(x + 1, v)]
    pairs_points_seen = [0 for _ in range(len(pairs_points_all))]

    for quadruple in s24v:
        quadruple.sort()
        for pp in position_pairs:
            pairs_points_seen[pairs_points_all.index([quadruple[pp[0]], quadruple[pp[1]]])] += 1

    for x in pairs_points_seen:
        if x != 1:
            return False

    return True
