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
