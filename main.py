import Bose_Resolution as BR
import Test
import math
import Max_BPM


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = 3*7*7
    k = 2*3*7
    ell = k//2
    d = 2
    j = 0
    # test_bpg = BR.completing_candidate_sets_to_bpg(n, BR.get_completing_candidate_sets_no_forbidden(n))
    # LSPCs = BR.standard_method(n, k, d)
    # print(Test.partitions_DPs(n, Test.lspcs_to_list_of_cells(LSPCs), [k,28]))
    # LSPCs = BR.lemma_1_lspcs(n, 13, 126)
    # cells_all = Test.lspcs_to_list_of_cells(LSPCs)
    # Test.partitions_DPs(n, cells_all, [k])
    br_test = BR.get_bose_resolution(n)
    br_test_cells = Test.lspcs_to_list_of_cells(br_test)
    print(Test.partitions_DPs(n, br_test_cells, [_ for _ in range(1, n) if _ % 2 == 0]))


    '''
    # test_bipartite_graph_IM = [[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0],[0]*9,[0]*9,[0]*9,[0]*9]
    # test_BPG = Max_BPM.BipartiteGraph(test_bipartite_graph_IM, [0,1,2,3,4], [5,6,7,8])

    test_bipartite_graph_IM = [[0]*6 + [0,1,1,0,0,0], [0]*6 + [0,0,0,0,0,0], [0]*6 + [1,0,0,1,0,0], [0]*6 + [0,0,1,0,0,0], [0]*6 + [0,0,1,1,0,0], [0]*6 + [0,0,0,0,0,1], [0]*12, [0]*12, [0]*12, [0]*12, [0]*12, [0]*12]
    test_BPG = Max_BPM.BipartiteGraph(test_bipartite_graph_IM, [0,1,2,3,4,5], [6,7,8,9,10,11])
    # test_FNR = test_BPG.get_flow_network_rep()
    test_BPG.get_max_bpm()
    '''



    test = 5

