Title:  Sensitivity Analysis - the basics
Date: 2015-12-01
Category: Sensitivity Analysis
Summary: A bit of sensitivity analysis.



"What is a model" and numerical experiments
-------------------------------------------

I worked in different places in applied mathematics and NONE of them had the same meaning behind the word "a model". So I can't really decide for other what a model is, but I can give the global idea of what I mean by that, and I'll use it for the rest of the article. 
But first let's agree that a model is a representation, a mimic, most of time of the reality. To me it's related to the philosophical concept of ... "concept", since it's an abstraction of an idea.

For instance, let's model a tree. Ok, well a tree has leaves, and a trunk and stuff. We can also make a more detailed model for the leaves, that have cells that do photosynthesis and pipelines that carry the stem or whatever it is. We can also have a model for the cells, and so on. Ok. That's one approach, complexity-based modelling maybe ? 
But what if we're just interested in the height of a tree given the localisation of the said tree? We can also measure a bunch of trees in different locations, and say "well given the average tree heigh in that forest, we can say that blabla about this one imaginary tree" and so on. We have inputs and outputs in this model, that's more of a statistical one.
One can think of many other ways to "model" stuff, when you tell me about that I think of a hybrid approach between the two presented above, that's related to the field of "numerical experiments".
So we'll both do abstraction of ideas and measurement, put that in a big box and use the box to have predictions. We'll use the word "simulation" or "numerical simulation" sometimes, to refer to that process.

The numerical simulation can be costly, due to the time needed to prepare the set of inputs or to the possibly large number of calculations needed (for instance, model of a tree, if you model the laws of viscose fluid propagation for all the pipelines of all the leaves of the tree, well I'm not going to lie: it's gonna take forever to compute one output).
Moreover, the result of the simulation may be uncertain when randomness is involved, thus this topic is often referred to as "numerical experiments", as I said earlier.

So to me a model is basically a (potentially super-duper) function that goes from a space of dimension $d$ to a space of dimension "not so high" ($1-10$, but let's say $1$ so far). Going back to that tree example, one input could be the diameter, another input could be the type of climate (tropical, cold, temperate ...) and the last one could be the genus (oak, pine, cheese tree, money tree ...). I'm not saying this model would be a good predictive one (that's an entire topic, the "goodness" of a model) but that's an example. So our model has $d=3$ inputs, 1 living in $\mathbb{R}$, and the two other living repectively in the spaces of Köppen–Geiger climates and tree genus.
This whole example is going to be out of control really fast, so I'm changing the 2 categorical inputs to 2 quantitative ones: the number of leaves and the sunshine duration for that tree. 



Sensitivity analysis in the context of numerical experiments
------------------------------------------------------------



Sensitivity analysis (SA) is desined by Saltelli et al. [todo ref] as "the study of how the un
ertainty in the output of a model can be apportioned to different sources of uncertainty in the model input".