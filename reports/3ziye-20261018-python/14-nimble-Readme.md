# Bespoke Nimble

**Data, Model, Recipe for an open Jev**

<a href="https://trendshift.io/repositories/247294?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-247294" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/247294/daily?language=Python" alt="bespokelabsai%2Fnimble | Trendshift" width="250" height="55"/></a>

#4 repository of the day on Trendshift.

[Model](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B) · [Timeline](#timeline) · [Updates](#updates) · [Capabilities](#capabilities) · [Quickstart](#quickstart) · [Methodology](#methodology) · [Documentation and development](#documentation-and-development) · [Citation](#citation)

![Introducing Bespoke Nimble. Serving reads the prompt once and then scores one answer token per question. Data curation changes one fact so that the correct answer flips. Training fine-tunes Qwen3.5-9B with LoRA on the answer tokens only. On 324 held-out examples, Bespoke-Nimble-9B matches 90.1% of the reference labels, compared with 66.4% for its base model and 93.2% for Jev 1.13.0.](assets/diagrams/nimble-infographic.svg)

Nimble takes some text and a schema, and makes typed decisions about the text.
The schema is the list of questions to answer. Each question is either a choice
from a list that you give or a true or false question. For each question, Nimble
returns the answer it picked and the probability of each allowed answer.

Nimble makes each decision in one step and does not write out any reasoning
first, so it is fast (blazing fast!). Nimble is
inspired by the System One approach of
[TypeSafe's Jev](https://docs.typesafe.ai/primitives/choice). In this repository,
we share our recipe for training such a model.

Note that we did not distill from Jev. The point of the repository is to show how to curate data, how to train, and to serve such a model, and encourage more research!

You can run [Bespoke-Nimble-9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B)
on a Mac with Apple Silicon or on a machine with an NVIDIA GPU.

## Timeline

These are the main steps from the release of Jev to the launch of Nimble-v4.

- On September 14, 2026, TypeSafe released
  [Jev](https://docs.typesafe.ai/primitives/choice), a decision model.
- On September 18, 2026, we released Nimble-v1 as
  [Bespoke-Nimble-9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B),
  together with its data and its training recipe.
- On September 29, 2026, [Ollama](https://ollama.com) added Nimble-v2
  ([Bespoke-Nimble-9B-v2](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v2)),
  so you can run it on your own computer with `ollama pull nimble`.
- On October 6, 2026, [Nimble-v3](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v3)
  was the #1 open model under 25B on the Decision Index. Jev is the only model
  with a higher score in this view, and Jev is not open.

  <img src="assets/timeline/nimble-v3-decision-index-under-25b.png" alt="The Decision Index chart with the size filter set to models up to 24.4B. Jev, the reference model, scores 60.1. Bespoke Nimble 9B v3 scores 54.7, the highest score of the open models. The next model, Nace.AI Drex v1.5, scores 50.8." width="520">

- On October 13, 2026, we launched Nimble-v4 (9B) and Nimble-v4-max (27B) on
  the API at [console.bespokelabs.ai](https://console.bespokelabs.ai). On the
  public suite of the Decision Index, Nimble-v4-max is #1 with 68.46, and
  Nimble-v4 is #1 of 104 models under 25B with 63.70. Jev 1.13 scores 57.96, and
  Perplexity Decider v1.1 scores 62.25. We measured the scores for Nimble-v4 and
  Nimble-v4-max in our own run on October 12, 2026. They are not yet on the
  Decision Index dashboard.

## Updates

- September 24, 2026: [Bespoke-Nimble-9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B) now contains the latest checkpoint, with an 8,192-token context and up to 255 choices per field. Its default is T=1.0; the original release is preserved under the `original-2676` tag, and the separate v2 repository is unchanged. Update this checkout before loading the new release.

- On September 22, 2026, we fitted a temperature for Bespoke-Nimble-9B. With
  this temperature, the probabilities better match how often the answers are
  right. The model picks the same answers as before. Noul probabilities and
  Score values do change, so if you compare them with a threshold, test the
  threshold again. See [Probability temperature](#probability-temperature) and
  [PR #7](https://github.com/bespokelabsai/nimble/pull/7).
- On September 20, 2026, we published the 2,676 training examples and the 324
  held-out examples for Bespoke-Nimble-9B. We had left them out of the first
  release by mistake. See the [dataset guide](docs/DATASET.md) and
  [PR #5](https://github.com/bespokelabsai/nimble/pull/5).
- On September 19, 2026, we raised the prompt limit of the hosted API to 8,192
  tokens for each question. The model was trained on prom