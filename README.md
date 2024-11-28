# Generalized property-based encoders and digital signal processing facilitate predictive tasks in protein engineering

Computational methods in protein engineering often require encoding amino acid sequences, i.e., converting them into numeric arrays. Physicochemical properties are a typical choice for encoding. However, what property (or group thereof) is best for a given predictive task remains an open problem. In this work, we generalize property-based encoding strategies to maximize the performance of predictive models in protein engineering. First, combining text mining and unsupervised learning, we partitioned the AAIndex database into eight semantically-consistent groups of properties. We then applied a non-linear PCA within each group to define a single encoder to represent it. Then, in several case studies, we assess the performance of predictive models trained using classical encoders (One Hot Encoder and TAPE embeddings) and the proposed encoders for predicting protein and peptide function, folding, and biological activity. We confirm that in most cases, models trained using our encoders outperform classical approaches both in precision and generality. Furthermore, when applying the Fast Fourier Transform (FFT) to the sequences encoded with the proposed encoders, the increase in performance and reduction in overfitting is much more drastic. Finally, we propose a preliminary and straightforward methodology to create \textit{de novo} sequences with desirable properties. All these results offer simple ways to increase the performance of general and complex predictive tasks in protein engineering.

## Summary of directories

- aaindexdb: Has different files associated to aaindex database considering the original source and the processed datasets.
- dataset testing: Has the different builded dataset to evaluate the proposed methodology.
- results: Contains the proposed encoders using the methodology developed in this work.
- sourcecode: Contains the different Python scripts implemented on this work.

## Contact us

- Sebastián Contreras: sebastian.contreras@ds.mpg.de
- Álvaro Olivera-Nappa: aolivera@ing.uchile.cl
- David Medina-Ortiz: david.medina@cebib.cl

## License

All source code, environment configurations, datasets, and models are available for non-commercial use under the Creative Commons Attribution-Non-Commercial ShareAlike International License, Version 4.0 (CC-BY-NC-SA 4.0). 
The complete source code, datasets, and models are available under the Creative Commons Attribution-Non-Commercial ShareAlike International License, Version 4.0 (CC-BY-NC-SA 4.0) for open, non-commercial use.

Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made . You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

NonCommercial — You may not use the material for commercial purposes .

ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
