# So, are these two genes the same?

... my PhD supervisor used to ask me, as I stared at the BlastP results page trying to figure out how to say "I have absolutley no idea". 

I think at the time I was probably trying to see if some sort of outer-membrane beta-barrel receptor from _E. coli_ had an ortholog in _K. pneumoniae_.
For many (molecular) microbiologists living in the 21st century, this process is fairly straightforward. 

What became apparent pretty quickly, was that these cutoffs are completley arbritrary


Proteins have structural domains that perform the actual function, and the geometry surrounding that backbone is a consequence of the organism that protein has envolved to work inside. w


## My solution: SPARCS

In trying to choose a sequence-based clustering program, I realsied that there are two main problems they are trying to solve:
1. Sensitivity
2. Scaleability

And actually, the more I read into the papers describing the algorithms, the more I realised that scaleability is always the higher priority.

But, whilst scale is a growing problem in bioinformatics, most of us aren't trying to cluster the known protein universe.
Actually, most computational microbiologists I work with are trying to extract biological meaning from their datasets, which most of the time aren't HUGE. So when it came to protein clustering/annotation I often end up trying different convoluted approaches to solve this problem - most of the time is very computationally slow and time consuming, not to mention the manual curation effort required.





Both MCL (Markov Cluster) and Leiden are popular algorithms used to detect communities or clusters within complex networks (graphs). However, they rely on fundamentally different mathematical approaches: 
MCL uses random walks and matrix simulation, while Leiden uses statistical optimization.

MCL (Markov Cluster Algorithm): Simulates random walks (flows) on a graph. It alternates between expansion (taking matrix powers to simulate longer walks) and inflation (raising entries to a power to boost strong connections and weaken weak ones) until the network divides into distinct, disconnected components.

Leiden Algorithm: A modularity-based algorithm (an extension of the Louvain algorithm). It works by grouping nodes together to optimize a quality function, primarily Modularity (the density of links inside communities compared to between them). Leiden refines partitions and guarantees that all discovered communities are strictly connected.

Use MCL if you are working with biological data (such as sequencing data) or networks where data behaves like "flow" or continuous probability.Use Leiden if you are clustering large, sparse networks (like social networks or single-cell data) where you want well-connected communities and need high computational speed