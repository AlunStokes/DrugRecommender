# A Psychiatric Drug Recommender System
## When will drugs interact in the body --- and can we predict this without knowing anything about them?

In this repository lays the result of a project into exactly that question; one with a perhaps shocking positive answer in that using our matrix-factorisation-based recommender system (bolstered by some bagging+boosing) trained on a set of user-reported reactions to various mential health-related pharmaceuticals scraped from drugs.com, we were alble to predict outcomes for patients' 'trying' drugs, knowing only how other people reacted to that drug and the complex overlaps bewtween the tens of thousands of records to which the models were privy. Of course, no one was actually trying the drugs, and we just obscured that knowledge in the training, but in whole, both [my colleague, Mehrunnisa Shiraz](https://ca.linkedin.com/in/mehrunnisa-shiraz-b203101a4) and myself were surprised by the efficacy of the methods.
