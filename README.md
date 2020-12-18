# CS492(I) NLP Project

KAIST CS492(I) Special Topics in Computer Science[Deep Learning for Real-World Problems]

## Original Author
Seonhoon Kim (Naver)

Authorized [DonghwanKim](https://github.com/DonghwanKIM0101)

Authorized [SeungilLee](https://github.com/ChoiIseungil)

-----------

The final model output

[Google Drive link](https://drive.google.com/file/d/1k8KLB3umUVo7ink178cfITobQ2F5wRzB/view?usp=sharing)

# Table of contents

1. [Summary](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#summary)
2. [Method](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#method)

    2.1 [Preprocessing](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#preprocessing)

    2.2 [Sampling Strategy](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#sampling-strategy)
    
    2.3 [Loss Function](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#loss-function)

3. [Result](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#result)
4. [Conclusion](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#conclusion)
5. [Reference](https://github.com/ChoiIseungil/CS492I_NLP/blob/master/README.md#reference)

# Summary

It is project in KAIST CS492(I) course. With NSML of NAVER, implement Korean SQuAD v2.0 model.

SQuAD is one of the important NLP processes that predict answers from question and passage pairs, and SQuAD v2.0 covers answerable questions and unanswerable ones.

Our team's approaches are preprocessing, sampling strategy, and loss function with verification loss. 

# Method

## Preprocessing

Threshold is one of main concept of FixMatch.

<img src="Image/threshold.png" width="450px"></img><br/>
> https://arxiv.org/pdf/2001.07685.pdf

By using threshold while guessing pseudo label, the model only learn for confident unlabeled data.
Original method use fixed threshold value, 0.95. Compared to original method, our team have to use non-pretrained model for this project.
We suggest new concept threshold scheduling.

<img src="Image/threshold_scheduling.png" width="450px"></img><br/>

In the graph, X-axis is current_epoch/total_epoch and Y-axis is the probability that unused unlabeled data.
For first epoch, the model learn the most confident 30% unlabeled data, and for last epoch, the model learn all of the unlabeled data. 

## Sampling Strategy

FixMatch uses both weakly augmented data and strongly augmented data.

<img src="Image/data_augmentation.png" width="450px"></img><br/>
> https://arxiv.org/pdf/2001.07685.pdf

For weak data augmentation, Crop, Horizontal Flip, and Vertical Flip
For strong data augmentaion, Crop, Horizontal Flip, Vertical Flip, Rotation, Color Jitter, and Cutout

## Loss Function

# Result

To check our own model, compare MixMatch, ThresholdMixMatch, FixMixMatch.
ThresholdMixMatch is MixMatch with threshold scheduling,
FixMixMatch is MixMatch with threshold scheduling, weak and strong data augmentation.
We use DenseNet121 for all tests.

<img src="Image/avg_top1_np.png" width="300px"></img><br/>
<img src="Image/avg_top5_np.png" width="300px"></img><br/>

For non-pretrained model, ThresholdMixMatch shows the best result and FixMixMatch shows the worst result.

<img src="Image/avg_top1_p.png" width="300px"></img><br/>
<img src="Image/avg_top5_p.png" width="300px"></img><br/>

For pretrained model, three models show similar result although FixMixMatch shows the worst result in average top1.

# Conclusion

We wanted to exploit FixMatch to MixMatch; FixMixMatch.
From the result, FixMixMatch does not show good result for non-pretrained model.
We guessed that it is because the strong data augmentation does not work well in non-pretrained model.

<img src="Image/conclusion.png" width="300px"></img><br/>

The graph proves our guess.

However, threshold scheduling improves the result.
Compared to original threshold concept, our new concept focuses more on non-pretrained model.
Also, by testing the models in pretrained option, we can get FixMatch works well in pretrained option but does not in non-pretrained option.

# Reference
D Berthelot, N Carlini, I Goodfellow, N Papernot, A Oliver, CA Raffel, MixMatch: A Holistic Approach to Semi-Supervised Learning, 2019 
Kihyuk Sohn, David Berthelot, Chun-Liang Li, Zizhao Zhang, FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence, 2020
