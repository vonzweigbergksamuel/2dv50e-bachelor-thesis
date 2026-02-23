# Student Project Proposal (SPP)

## Supervisor
*Not decided yet*

## Students
Samuel von Zweigberk (sv222rr)

Ludwig Wittenberg (lw223cq)

## Preliminary Thesis Title
An Updated Multi-Dataset Evaluation of Face Recognition Models in the DeepFace framework

## Elevator Pitch
Face recognition models are commonly evaluated using a limited set of benchmarks and models. Several newer models supported by the DeepFace framework, such as GhostFaceNet and DeepFace, are not included in earlier comparative studies. This thesis presents an updated empirical evaluation of a wide range of DeepFace-supported models across multiple datasets, including LFW, YTF, and an Indonesian face dataset. The goal is to analyze performance differences and assess how well conclusions drawn from earlier studies generalize to newer models and datasets.

## Milestones
1. Finalize research questions
2. Complete literature review
3. Implement evaluation pipeline
4. Run experiments and collect results
5. Analyze results and write discussion
6. Finalize thesis

## Risks
- **Dataset limitations**, insufficient size or lack of variation may affect generalizability.
- **Closed sourced models**, limited insight into models may restrict interpretability.
- **Computational constraints**, some models may be resource-intensive.

## Background
Face recognition is a subfield of computer vision that aims to identify or verify individuals by comparing facial features extracted from images or video frames. Face recognition is widely used in various fields today, all the way from security, mobile phone authentication, and identifying crime suspects, to social media platforms and image apps curating photo albums based on contacts [1]. Modern face recognition methods are predominantly based on deep learning, most often convolutional neural networks (CNN’s), and trained on large-scale datasets.

One of the most widely used libraries for face recognition is DeepFace, an open source Python framework that provides a unified interface for working with multiple state-of-the-art face recognition models [2]. Using a framework like DeepFace abstracts away much of the implementation details and complexities, allowing for researchers to focus on comparing different face recognition models using a consistent preprocessing pipeline.

A typical face recognition pipeline consists of multiple stages, including face detection, face alignment, feature extraction, and face recognition [3], [4]. While all stages influence system performance, this thesis focuses specifically on the face recognition stage. Face detection, alignment and extraction are treated as part of the preprocessing pipeline and are handled by the underlying framework.

The motivation for this work originates from a collaboration with Flowbic AB, a local software company that is exploring the use of face recognition in a mobile application. In order to assess which face recognition models are suitable for such an application, a systematic evaluation of the models available within the DeepFace framework is required.

## Related Work
Previous studies compared and performed benchmarks on various models, based on performance metrics. Some of the performance metrics were sensitivity, accuracy, specificity, precision and F1-score [5], [6]. One study used the dataset LFW, which has over 13,000 images [6]. The other study used an indonesia  dataset, which contains two photos of ten different humans [5]. Both studies used their dataset through their benchmark on every model. These datasets were tested on a limited number of models [5], [6].

The first study benchmarked the models FaceNet512, FaceNet and ArcFace with the Indonesia dataset. The study found that the FaceNet512 model performed best. However, they also found that the FaceNet512 model had a sensitivity score of 66% instead of the ArcFace model which performed a sensitivity score of 100% [5] This shows that the best accuracy score is not always the best model.
The second study benchmarked the models FaceNet, OpenFace, DeepFace and VGGFace with the LFW dataset. The study found that the FaceNet model performed best. [6]

Another study performed a similar experiment as we intend to do. The study benchmark different models and use multiple datasets. However the study only benchmark a limited number of models, which all have their own dataset. On top of that they only measure the accuracy score. This means that each benchmark can´t be compared to the other benchmarks. Therefore, this limits the validity of the result [7].

## Knowledge Gap
Existing comparative studies of face recognition models are several years old and do not include newer models currently supported by the DeepFace framework, such as GhostFaceNet and DeepFace. Furthermore, most studies rely on a single benchmark dataset, limiting insight into cross-dataset generalization.

## Knowledge Contribution
This thesis provides an updated empirical evaluation of face recognition models available in the DeepFace framework, including newer models not covered in previous studies. By evaluating performance across multiple datasets, the study contributes insights into the stability and generalizability of model performance beyond single-dataset benchmarks.

## Evaluation
The evaluation is conducted through benchmarking of multiple DeepFace-supported models. Performance is measured using accuracy, sensitivity, precision, F1-score and confusion matrices. Experiments are conducted across multiple datasets to analyze performance consistency and dataset dependence.

## References
[1] Y. Kortli, M. Jridi, A. Al Falou, and M. Atri, ‘Face Recognition Systems: A Survey’, Sensors, vol. 20, no. 2, 2020.

[2] S. Ilkin Serengil. “deepface 0.0.98” PyPi.org. Accessed: Feb. 2, 2026. [Online.] Available: https://pypi.org/project/deepface/

[3] E. Jiang, ‘A review of the comparative studies on traditional and intelligent face recognition methods’, in 2020 International Conference on Computer Vision, Image and Deep Learning (CVIDL), 2020, pp. 11–15.

[4] M. D. A. Munim and M. S. Rahman Kohinoor, ‘Performance Evaluation of Deep Learning-Based Facial Recognition Models on Mobile Computing Environments’, in 2023 IEEE 11th Region 10 Humanitarian Technology Conference (R10-HTC), 2023, pp. 13–18.

[5] A. Firmansyah, T. F. Kusumasari, and E. N. Alam, ‘Comparison of Face Recognition Accuracy of ArcFace, Facenet and Facenet512 Models on Deepface Framework’, in 2023 International Conference on Computer Science, Information Technology and Engineering (ICCoSITE), 2023, pp. 535–539.

[6] M. D. A. Munim and M. S. Rahman Kohinoor, ‘Performance Evaluation of Deep Learning-Based Facial Recognition Models on Mobile Computing Environments’, in 2023 IEEE 11th Region 10 Humanitarian Technology Conference (R10-HTC), 2023, pp. 13–18.

[7] Li, Minghan, ‘Research and Analysis of Facial Recognition Based on FaceNet, DeepFace, and OpenFace’, ITM Web Conf., vol. 70, p. 03009, 2025.
