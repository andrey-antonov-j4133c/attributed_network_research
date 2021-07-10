# Experimental resesearch on metnods of node-attributed networks generation


This research is used to evalueate methods of node attributed network generation. The generation is done based on the real world dataset:
https://drive.google.com/drive/folders/1SDWWiOQ0mOtXqoEat5FRIgVNzKsE2D8v?usp=sharing

Currently we have evaluated the following methods:

- "MAG" (https://arxiv.org/abs/1009.3499, https://github.com/snap-stanford/snap/tree/master/examples/maggen)
- "CABAM" (http://nshah.net/publications/CABAM.MLG.2020.pdf, https://github.com/nshah171/cabam-graph-generation)
- "acMark" (https://www.semanticscholar.org/paper/General-Generator-for-Attributed-Graphs-with-Maekawa-Zhang/b113704d38cc9109ac4f2b24c2b897c82686d67e, https://github.com/seijimaekawa/acMark)
- "Attributed netwok generation algorithm" by C. Largeron (https://www.semanticscholar.org/paper/General-Generator-for-Attributed-Graphs-with-Maekawa-Zhang/b113704d38cc9109ac4f2b24c2b897c82686d67e, https://perso.univ-st-etienne.fr/largeron/ANC_Generator/#download)

Each method is in it's own way making a copy of a real-world network, so we evaluate each method's ability to replicate the initial attributed network. We then calculate metrics to understand the quality of method's performance. 

