# Nautilus

This repository contains the code and the results of "Nautilus: A Framework for Cross-Layer Cartography of Submarine Cables and IP Links" paper which is set to appear in the Proceedings of ACM SIGMETRICS 2024. (The ArXiv version of this paper can be viewed at [Nautilus](https://arxiv.org/abs/2302.14201))

This repository is split into code and results which contain the codebase and the major results of Nautilus respectively. A detailed documentation of (i) the usage of various pieces of the codebase is detailed in the README file within the code directory and (ii) the results structure is detailed in the README file within the results directory.

The requirements.txt file contains the python libraries that need to be installed for execution of various pieces of the Nautilus codebase. In addition to the python libraries additional tools needs to be installed, which are (i) scamper (specifically sc_warts2json) from CAIDA (https://www.caida.org/catalog/software/scamper/), (ii) ripe-atlas tool from RIPE NCC (https://github.com/RIPE-NCC/ripe-atlas-tools). 

Note: In addition to these, specific files or commands might need to be downloaded or executed. Specific instructions for these are detailed in the README file within code directory and will also be displayed as error messages when executing the code if not done apriori.

Note: The results directory includes some very large files, which will need Git LFS to be installed.

In case of any issues with the codebase, reach out to Alagappan Ramanathan (alagappr@uci.edu).
