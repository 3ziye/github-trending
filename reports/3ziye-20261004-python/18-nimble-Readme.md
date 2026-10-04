# Bespoke Nimble

**Data, Model, Recipe for an open Jev**

[Model](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B) · [Updates](#updates) · [Capabilities](#capabilities) · [Quickstart](#quickstart) · [Methodology](#methodology) · [Documentation and development](#documentation-and-development) · [Citation](#citation)

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
  tokens for each question. The model was trained on prompts of up to 2,048
  tokens, so shorter prompts are better tested. See the
  [SGLang deployment guide](docs/MODAL_SERVING.md) and
  [PR #4](https://github.com/bespokelabsai/nimble/pull/4).
- On September 18, 2026, [Edgar Dyck](https://github.com/eddited17) added a
  public benchmark suite. With it, you can run Bespoke-Nimble-9B and Jev on the
  same records from 13 public subsets with human labels. The
  [public benchmarks guide](docs/PUBLIC_BENCHMARKS.md) has the steps and the
  results. See [PR #2](https://github.com/bespokelabsai/nimble/pull/2).

## Capabilities

We built Nimble in one day, so expect some rough edges. What Nimble can do comes
from two sources: the first is the base model, Qwen3.5-9B, the second is our
training data, which we curated for a few specific domains.

### What you can build

| Task | You define | You get back |
| --- | --- | --- |
| Route a request | The destinations and when each one applies | The chosen destination and the probability of each destination |
| Check a condition | A yes or no question and the evidence | True or false, and the probability of each |
| Apply a policy | The rules and the allowed outcomes | A typed decision based on the text you supply |
| Rate an outcome | Ordered levels, each with clear criteria | The chosen level and the probability of each level |

You supply a context, which is the text to judge, and a schema. The schema must
be flat, which means that it has no nested fields. Each field is an enum or a
boolean. An enum field has a fixed list of string choices, and a boolean field
is true or false.

Each allowed answer has a code that is one token long. The scorer reads the
model's logits for these codes. Logits are the raw scores that the model gives
to each token. The scorer turns the logits into probabilities with the softmax
function. Our Python code then builds the output from these probabilities, so
there is no generated JSON to parse. If a field is an ordered rating scale, your
application can use the probabilities to calculate an expected level.

On a Mac, `Paral