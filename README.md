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

Korean SQuAD dataset we use is not that clear to be used for training. Therefore, we perform three steps of text preprocessing to refine the raw dataset. First, characters other than Korean, English, numbers, and a few allowed special characters are all erased. Second, we delete texts in brackets that seems unnecessary. Third, repeated characters are truncated.

<img src="image/preprocessing.jpeg" width="450px"></img><br/>

## Sampling Strategy

We have to select train datasets among a lot of paragraphs. Not only the number of selected contexts but how to select the paragraphs is also important. We suppose that a context which is irrelevant to the question would hinder the training, so we take a strategy to select a context with high similarity with the question.

<img src="image/sampling-strategy.jpeg" width="450px"></img><br/>

## Loss Function

We suggest our own loss function which is the sum of span prediction loss and verification loss. By doing so, the model is trained by where the answer is and whether the question is answerable or not.

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
