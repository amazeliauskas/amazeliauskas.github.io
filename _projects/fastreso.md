---
layout: my_project
title: Hadron resonance decays
description:
img: decays.png
caption: Resonance decay chain
importance: 5
category: current
related_publications: true
---

How the colour-neutral particles are produced from the **quark-gluon plasma**, which is a deconfined state of matter with manifest QCD colour degrees of freedom, is a poorly understood
fundamental physics problem. The current approach, called the **Cooper-Frye procedure**, converts the fluid fields like temperature and velocity directly to a distribution of hadron resonances
gas. Remarkably, the measured particle yields are in very good agreement with thermal par-
ticle production at chemical freeze-out temperature of T = 156 MeV even for a weakly
bounded hyper-nuclei.

Most of the produced hadron resonances are short lived and decay to more stable particles before detection. Therefore comparison to momentum resolved experimental data requires
numerically costly calculations of **resonance decays**. We developed a novel way of directly calculating the observed particle spectra by pre-calculating the final spectra in the fluid rest-frame {% cite Mazeliauskas:2018irt %}. The computer code [FastReso](https://github.com/amazeliauskas/FastReso) is publicly available.
Such fast and efficient technique allowed use to easily include the important effect of resonance
decays in a routine experimental analysis procedure of blast-wave fit {% cite Mazeliauskas:2019ifr %}. In addition, we integrated the fast resonance calculation in a hydrodynamic heavy-ion model and performed a detailed  of
identified particle spectra at LHC {% cite Devetak:2019lsk %}. We found that there are statistically significant deviations from experimental measured spectra in the low momentum pion spectra, which cannot be
rectified even within the range of model parameters and even a larger set of primary resonances. Currently we are exploring the effect of resonance widths to soft pion spectra.

{% nocite Andronic:2021erx %}
