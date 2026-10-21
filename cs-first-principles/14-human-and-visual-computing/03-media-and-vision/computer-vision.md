# Computer Vision

> **Layer:** [14 Human and Visual Computing](../README.md) › [Media and vision](README.md)
> **Builds on:** [Geometry and transformations](../02-computer-graphics/geometry-and-transformations.md), [Convolutional networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md), [Attention and transformers](../../13-artificial-intelligence/03-deep-learning/attention-and-transformers.md), [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)
> **Enables:** [Interaction design principles](../01-human-computer-interaction/interaction-design-principles.md), [Large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md), [Law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md)

## Essence

Computer vision extracts meaning and structure from images and video: what objects are present, where they are, how the camera moved, what 3D shape produced the picture. It is the inverse of graphics. Graphics maps a known scene to pixels, a well-defined computation; vision maps pixels back to a scene, which is **ill-posed** because projection discards depth and many scenes produce the same image. Vision resolves the ambiguity with prior knowledge: geometric constraints from multiple views, and statistical regularities of the world. Since 2012, those regularities are learned almost entirely by deep networks trained on large datasets, which turned recognition from a research problem into a commodity. Geometry still governs 3D reconstruction, tracking and robotics, increasingly combined with learned components.

## Core tenets

1. **Vision is inverse graphics, and inverse problems need priors.** A pixel's value depends on geometry, material, lighting and camera together; a single image cannot separate them uniquely. A small object nearby and a large object far away project identically. Every vision method adds assumptions (rigid scenes, smooth surfaces, typical object shapes, learned statistics of natural images) to pick the most plausible explanation.

2. **The pinhole camera model links 3D points to pixels.** A point X in the world projects to x = K [R | t] X in homogeneous coordinates, where R and t give the camera's pose and the intrinsic matrix K holds focal length and image centre. Calibration estimates K and lens distortion. This is the same projection used in [graphics](../02-computer-graphics/geometry-and-transformations.md), run in the other direction.

3. **Multiple views recover depth.** A point seen in two images lies on corresponding epipolar lines; finding the match and triangulating gives its 3D position. Depth precision falls with distance because disparity is inversely proportional to depth. Structure from motion and Simultaneous Localisation And Mapping (SLAM) estimate camera poses and 3D points jointly by minimising reprojection error over many images (bundle adjustment), a large sparse non-linear least-squares problem.

4. **Correspondence is the core difficulty, and robust estimation handles outliers.** Matching points between images is error-prone because of repeated textures, occlusion and lighting change. Hand-designed descriptors such as the Scale-Invariant Feature Transform (SIFT, 2004) and, more recently, learned descriptors provide candidates. Random Sample Consensus (RANSAC) fits a model to many random minimal subsets and keeps the one most matches agree with, tolerating large fractions of wrong matches.

5. **Recognition became learning.** Before 2012, recognition used hand-crafted features fed to classifiers and plateaued on hard benchmarks. Convolutional Neural Networks (CNNs) trained on ImageNet (1.2 million labelled images, 1,000 classes) cut error dramatically and learn their own features. The same backbone, with different output heads, performs classification (what), detection (what and where, as boxes), semantic segmentation (a label per pixel) and pose estimation.

6. **Pre-training on huge data and language supervision made vision general.** Contrastive image-text models such as Contrastive Language-Image Pre-training (CLIP, 2021) learn from hundreds of millions of image-caption pairs scraped from the web, so they can recognise categories described in words without task-specific training. As of the mid-2020s, vision transformers and multimodal large language models answer questions about images, read documents and describe scenes, and promptable segmentation models segment arbitrary objects.

7. **Benchmark accuracy overstates real-world robustness.** Deep vision models can be fooled by imperceptible adversarial perturbations, fail under distribution shift (new cameras, weather, demographics), and exploit spurious cues such as backgrounds or texture. Safety-critical uses, such as driving and medical imaging, need evaluation on the deployment distribution, uncertainty estimates and redundancy with other sensors.

8. **Vision systems raise distinctive social risks.** Face recognition and tracking enable surveillance at scale, and error rates have been shown to differ across demographic groups. Generated images undermine trust in photographs as evidence. These are why vision features prominently in privacy law and Artificial Intelligence (AI) regulation.

## Key concepts

| Term | Meaning |
|---|---|
| Ill-posed problem | Problem without a unique solution unless extra assumptions are added |
| Intrinsic / extrinsic parameters | Camera's internal geometry (focal length, centre) / its pose in the world |
| Epipolar geometry | Constraint that a point's match in a second view lies on a specific line |
| Disparity | Horizontal shift of a point between stereo images, inversely proportional to depth |
| Bundle adjustment | Joint optimisation of camera poses and 3D points to minimise reprojection error |
| Feature descriptor | Vector summarising a local image patch for matching |
| RANSAC | Robust model fitting by repeated random minimal samples and consensus voting |
| Object detection | Locating and classifying objects with bounding boxes |
| Semantic segmentation | Assigning a class label to every pixel |

## How it fits

- **Below:** Projection is the camera model from [geometry and transformations](../02-computer-graphics/geometry-and-transformations.md); reconstruction is [optimisation](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md) and [statistical estimation](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md); recognition is [supervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md) with [convolutional networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md) and [transformers](../../13-artificial-intelligence/03-deep-learning/attention-and-transformers.md); inputs arrive as [compressed media](digital-media-and-compression.md).
- **Above:** Vision enables gesture, gaze and handwriting input in [interaction design](../01-human-computer-interaction/interaction-design-principles.md), multimodal [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md), robotics and autonomous vehicles; face recognition and surveillance are central topics in [law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** [Digital media and compression](digital-media-and-compression.md) keeps images faithful for people; vision interprets them for machines. Both now use learned models, and both depend on how perception and cameras sample the world.

## Common misconceptions

- **"Vision is solved."** Recognition on curated benchmarks is very strong, but robustness under shift, fine 3D understanding and reliable reasoning about scenes remain open problems.
- **"Deep learning made geometry obsolete."** SLAM, calibration and photogrammetry still rest on projective geometry; learned components improve matching and priors rather than replace the geometry.
- **"A model that sees the object understands it as people do."** Models often rely on texture and context cues, failing in ways no human would.

## Go deeper

- Richard Szeliski, *Computer Vision: Algorithms and Applications* (2nd ed., 2022): the broad modern reference, freely available.
- Richard Hartley and Andrew Zisserman, *Multiple View Geometry in Computer Vision* (2nd ed., 2004): the mathematics of cameras and reconstruction.
- David Lowe, "Distinctive Image Features from Scale-Invariant Keypoints" (2004): SIFT, the landmark hand-designed descriptor.
- Alec Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (2021): CLIP.
