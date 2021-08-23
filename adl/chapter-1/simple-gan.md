---
layout: default
title: Simple GAN Attack
parent: Chapter 1
grand_parent: Adversarial Deep Learning
---
<!-- ![Test Image 1](3DTest.png) -->
## Generative adversarial networks:
A generative adversarial network is a class of machine learning frameworks designed by Ian Goodfellow and his colleagues in 2014. Two neural networks contest with each other in a game. Given a training set, this technique learns to generate new data with the same statistics as the training set. TODO
![Simple Gan](/assets/chapter-1/simple_cn_gan.png)
*A caption for GAN* <br/>
Generative adversarial networks (GANs) are algorithmic architectures that use two neural networks, pitting one against the other (thus the “adversarial”) in order to generate new, synthetic instances of data that can pass for real data. They are used widely in image generation, video generation and voice generation. TODO

## Some code for GAN
This is some code for the constructor of a gan
```python
    def __init__(self, image_size: int, channels: int, latent_dims: int, lr: float):
        """
        Parameters
        ----------
        image_size : int
            Number of input dimensions aka side length of image
        channels: int
            Number of channels in image
        latent_dims : int
            Number of dimensions in the projecting layer
        lr : float
            Learning rate
        """
        super(Generator, self).__init__()
        self.image_size = image_size
        self.channels = channels
        self.latent_dims = latent_dims
        self.main = nn.Sequential(
            nn.Linear(self.latent_dims, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, self.image_size * self.image_size * self.channels),
            nn.Tanh(),
        )
        self.optimizer = optim.Adam(self.parameters(), lr=lr)
```