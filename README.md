# Condition Based Maintenance

For assets subject to degradation, developing cost effective inspection and maintenance schemes pose significant practical challenge for managers. Despite observable decline in asset condition from condition monitoring, the residual life of the asset remains a key uncertainty, complicating decisions in inspection planning and replacement. Existing strategies assume constant failure rates supplemented by static reliability databases, which do not account for performance history and diminishing health condition. This often leads to sub-optimal condition monitoring regimes, that could result in excess costs from either over inspecting or excessively high failure rates stimulated by plant specific factors. Thankfully with past asset life data, it is possible to utilize inspection measurements as a quantitative indicator of the asset’s underlying condition and its uncertainty. This paper proposes a joint-probabilistic model between the remaining life and inspection observations, which is then used to perform prognostics on currently installed assets. At every new observation, the forward-looking belief on the asset's remaining life is Bayesian updated, granting dynamic estimations on its failure probability. Consequently, inspection times are optimally determined, with increasing frequency as the component deteriorate. The trained model is evaluated using an independent inspection history of a bearing component, and the predicted prognostics are observed to converge towards the actual failure date of the asset.
