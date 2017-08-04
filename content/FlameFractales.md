Title:  FlamePython2 - how to use that code
Date: 2017-08-01
tags: Python, Art
Category: Fractals
Summary: This is the guidelines to use the code in the repo. It's also useful for me.


What is the purpose of this article?
------------------------------------

Mostly it's to help people use the code in the [repo](https://github.com/DrAnaximandre/FlamePython2).


What are Flames Fractals ?
--------------------------
The main reference is [Draves and Reckase](http://flam3.com/flame_draves.pdf). You could read it through and through, but let me propose a shorter, simplified version.


Let us have a colored point, called Robert. Robert is a white point, with coordinates somewhere in $[-1, 1]^2$ (and RGB 255, 255, 255).


![Image of Robert](/images/robert.png)

Let us also have a "function", $F$, that goes from $[-1, 1]^2 * [0,255]^3$ to $[-1, 1]^2 * [0,255]^3$. In other words, $F$ takes a colored point such as Robert and return another colored point.

The result of inputing Robert into $F$ will be denoted Robertson, and you can also put Robertson into F, you'd get Robertsonson and so on.

![Image of Robert and some sons](/images/robertson.png)

Now why did I put some quotes around "function" when talking about $F$? Actually $F$ is not quite a function but a random variable. You can see on the above example that the one application of $F$ transformed Robert into Robertson moved it up, whereas the application of $F$ that transformed Robertson into Robertsonson moved it left. What happened ? Well, for this example, $F$ was such that one application had one chance out of two to move the point up, and one chance out of two to move it right.



