# DSS-from-3v-1-Construction
Constructs an access-balanced (distributed) storage system by applying the 3v+1 construction with an ingredient S(2,4,v) (provided by the user in a text file) together with a resolvable Bose-averaging triple system that is automatically constructed (see the attached paper "The Spectrum of Resolvable Bose Triple Systems" for details as to how this triple system is constructed). The user-provided text file must have the following format: (1) each block occurs on a single line and (2) points in a block are separated by whitespace. We also assume that the input S(2,4,v) occurs on point set [0, v-1].

A sample ingredient S(2,4,76) (obtained via the Moore construction) is provided in testFile, which you may use to test the program. If you do opt to do this, set u (number of files) to 76*3 + 1 = 229 when prompted.

For an introduction on the mathematical model used here to construct access-balanced storage systems, see the introduction + background section of my attached dissertation. 
