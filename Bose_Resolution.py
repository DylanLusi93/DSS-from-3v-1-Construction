# Note 1: The variable names used here are taken directly from my paper "The Spectrum of Resolvable Bose Triple Systems"
# Note 2: A cell is a list of 3 integers. An LSPC is a list of cells.
from typing import Optional
import math
import Max_BPM
import Test

def generate_standard_PLSPC(n: int, gamma: int, m : int, k: int, d: int, j: int, alpha: int) -> list:
    """Generates the PLSPC P_{k,d,j,\alpha} in (3) of Lemma 3"""
    # The base cell in C_k(B_n)
    plspc = []
    c = [0, k, k//2]
    for h in range(math.floor(n//(3*gamma))):
        for i in range(3):
            plspc.append([(x + alpha + gamma//3*(h*m + i*d) + j*k//2) % n for x in c])

    return plspc

def standard_method(n: int, k: int, d: int) -> Optional[list]:
    """Applies the standard method with parameter d \not\equiv 0 \pmod{3} to handle diagonal pair C_k(B_n)
    Returns a list of six LSPCs of B_n, with the last two LSPCs being the remaining
    two Lemma 1-type LSPCs of the completing diagonal pair"""

    LSPCs = [[] for x in range(6)]
    scriptP_alpha_all = []
    N_alpha_all = []
    plspc_all = []
    T_alpha_all = []
    # Some error checking
    if n % 6 != 3:
        print("Error: The order n of the averaging latin square must be equivalent to 3 mod 6.")
        return None
    if k % 6 != 0:
        print("Error: The index of the diagonal pair must be equivalent to 0 mod 6.")
        return None
    if d % 3 == 0:
        print("Error: The standard method parameter d must not be divisible by 3.")
        return None

    gamma = math.gcd(k, n)
    ell = k//2
    m_prime = ell//gamma*pow(n//(3*gamma), -1, n//gamma)
    m = 3*m_prime % (3*n//gamma)
    c_hat = [0,k,ell]

    beta = (2*d*gamma//3) % n
    beta_flag = 0
    # Ensures that beta is always even
    if beta % 2 == 1:
        beta = (-beta) % n
        beta_flag = 1

    for j in range(3):
        for alpha in range(gamma//3):
            R_alpha = [alpha + i * gamma // 3 for i in range(n // (gamma // 3))]
            plspc_current = generate_standard_PLSPC(n, gamma, m, k, d, j, alpha)
            plspc_all = plspc_all + plspc_current

            if j == 0:
                if beta_flag == 0:
                    scriptP_alpha = [[x, (x + 2*d*gamma//3) % n, (x + d*gamma//3) % n] for x in R_alpha if x % 3 == alpha % 3]
                else:
                    scriptP_alpha = [[(x + 2*d*gamma//3) % n, x, (x + d*gamma//3) % n] for x in R_alpha if x % 3 == alpha % 3]

                scriptP_alpha_all = scriptP_alpha_all + scriptP_alpha

            if j == 0:
                plspc_current_allShifts_rows = [(c[0] + idx*ell) % n for c in plspc_current for idx in range(3)]
                N_alpha = [[(c_hat[idx] + x) % n for idx in range(3)] for x in [(alpha + h*gamma//3) % n for h in range(3*n//gamma)] if x not in plspc_current_allShifts_rows]
                N_alpha_all = N_alpha_all + N_alpha

                if beta_flag == 0:
                    for c in N_alpha:
                        if c[0] % 3 == alpha % 3:
                            for i in range(3):
                                T_alpha_all = T_alpha_all + [[c[i], (c[i] + 2 * d * gamma // 3) % n, (c[i] + d * gamma // 3) % n]]
                else:
                    for c in N_alpha:
                        if c[0] % 3 == alpha % 3:
                            for i in range(3):
                                T_alpha_all = T_alpha_all + [[(c[i] + 2 * d * gamma // 3) % n, c[i], (c[i] + d * gamma // 3) % n]]

            # Flatten plspc_current
            scriptY_j = [item for cell in plspc_current for item in cell]
            # Get elements in R_alpha that do not belong to plspc_current and are congruent to alpha (mod 3)
            scriptN_j_alpha = [x for x in R_alpha if x not in scriptY_j and x % 3 == alpha % 3]
            # Form (alpha,beta)-completing set S_alpha_j for P_{k,d,j,alpha} (i.e., plspc_current)
            if beta_flag == 0:
                S_alpha_j = [[x, (x + 2*d*gamma//3) % n, (x + d*gamma//3) % n] for x in scriptN_j_alpha]
            else:
                S_alpha_j = [[(x + 2*d*gamma//3) % n, x, (x + d*gamma//3) % n] for x in scriptN_j_alpha]
            LSPCs[j] = LSPCs[j] + plspc_current + S_alpha_j

    # Test.partitions_DPs(n, plspc_all + N_alpha_all, [k])

    # Now form the last LSPC, LSPCs[3]
    LSPCs[3] = N_alpha_all + [c for c in scriptP_alpha_all if c not in T_alpha_all]

    # Obtain the last two LSPCs by applying Lemma 1 to obtain three LSPCs of C_beta, and taking only the last
    # two.
    if beta_flag == 0:
        C_beta_LSPCs = lemma_1_lspcs(n, d, gamma)
    else:
        C_beta_LSPCs = lemma_1_lspcs(n, -d, gamma)

    # Find which LSPC of C_beta_LSPCs is equal to LSPCs[3]
    j = 4
    for idx, LSPC in enumerate(C_beta_LSPCs):
        for c in LSPC:
            if c[2] == scriptP_alpha_all[0][2]:
                for i in range(idx):
                    LSPCs[j] = C_beta_LSPCs[i]
                    j += 1
                for i in range(idx + 1, 3):
                    LSPCs[j] = C_beta_LSPCs[i]
                    j += 1
                return LSPCs

def lemma_1_lspcs(n: int, d: int, gamma: int) -> list:
    """Applies Lemma 1 to partition C_{k == 2*d*gamma/3} into three LSPCs; returns a list of these three LSPCs.
    Note that k must be even and not congruent to 0 mod 6."""
    LSPCs = [0, 0, 0]
    scriptB = [[i % n, (i + 2*d*gamma//3) % n, (i + d*gamma//3) % n] for i in range(gamma//3)]
    LSPCs[0] = [[(c[idx] + i*gamma) % n for idx in range(3)] for c in scriptB for i in range(n//gamma)]
    LSPCs[1] = [[(c[idx] + gamma//3) % n for idx in range(3)] for c in LSPCs[0]]
    LSPCs[2] = [[(c[idx] + 2*gamma // 3) % n for idx in range(3)] for c in LSPCs[0]]
    return LSPCs

def get_completing_candidate_sets(n: int):
    """Get the set of all completing candidate sets for all C_k, k \equiv 0 \pmod{6}"""
    completing_cand_sets = []
    for k in range(1, n):
        if k % 6 == 0:
            mu_k = math.gcd(k, n)//3
            completing_cand_sets = completing_cand_sets + [[d*mu_k for d in range(2,n//mu_k) if d % 2 == 0 and d % 3 != 0]]

    return completing_cand_sets

def completing_candidate_sets_to_bpg(n, completing_cand_sets) -> Max_BPM.BipartiteGraph:
    """Converts family of all completing candidate sets to bipartite graph, where left partite set L has |\frak{C}_k|
    elements and right partite R set has remaining even diagonal pair indices"""

    R_raw = [beta for beta in range(2,n) if beta % 2 == 0 and beta % 3 != 0]
    bpg_graph_IM = [[0 for _ in range(len(completing_cand_sets) + len(R_raw))] for _ in range(len(completing_cand_sets) + len(R_raw))]

    # Remember that edges in our bipartite graph representation only go from L to R (and not R to L)
    for idx, ccs in enumerate(completing_cand_sets):
        for raw in ccs:
            bpg_graph_IM[idx][R_raw.index(raw) + len(completing_cand_sets)] = 1

    return Max_BPM.BipartiteGraph(bpg_graph_IM, [x for x in range(len(completing_cand_sets))], [x + len(completing_cand_sets) for x in range(len(R_raw))])

def get_bose_resolution(n: int):
    br = []
    if n % 5 == 0:
        pass
    else:
        test = get_completing_candidate_sets(n)
        bpg = completing_candidate_sets_to_bpg(n, get_completing_candidate_sets(n))
        one_factor = bpg.get_max_bpm()

        # corresponds to the left partite set of bpg
        dps_to_handle = [x for x in range(1,n) if x % 6 == 0]
        # corresponds to the right partite set of bpg
        completing_diag_idxs_all = [x for x in range(1,n) if x % 2 == 0 and x % 3 != 0]

        for idx, beta_idx in enumerate(one_factor):
            if beta_idx != -1:
                for d in [_ for _ in range(1,n) if _ % 3 != 0]:
                    if (2*d*math.gcd(dps_to_handle[idx], n)//3) % n == completing_diag_idxs_all[beta_idx - len(dps_to_handle)] % n:
                        break
                br = br + standard_method(n, dps_to_handle[idx], d)

        # treat remaining diagonal pairs that have not been used by the standard method as completing diagonal pairs
        for idx in [_ for _ in range(len(completing_diag_idxs_all)) if _ not in [x - len(dps_to_handle) for x in one_factor]]:
            br = br + lemma_1_lspcs(n, completing_diag_idxs_all[idx]//2, 3)

    return br






