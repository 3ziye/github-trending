![AI copywriter. Human tone. Explains extreme concepts easily. enso](assets/banner.png)

# AI Copywriter

by [Mickey Haslavsky](https://github.com/mikiarlo3)

A portable agent skill that does the two halves of the copy job most tools split apart: it writes copy that earns attention (clickbait titles, short descriptions, microcopy, subject lines), and it strips out every sign of AI-generated writing so the result reads like a person wrote it. It is plain Markdown, so it runs in any harness that supports skill-style instructions.

It is built on [blader's Humanizer](https://github.com/blader/humanizer), which packaged Wikipedia's "Signs of AI writing" guide into 33 detectable, fixable patterns. Those 33 patterns are all still here, unchanged. What this skill adds is the other direction: not just cleaning up prose after the fact, but writing headlines, product blurbs, and button labels that convert without tripping a single one of those patterns.

The copywriting method comes from [enso.bot/research](https://enso.bot/research), where the enso team studies how to communicate through marketing in the best possible way. The short version of what that research keeps finding: copy works when it starts from the feeling of the person on the other end and explains the concept in the simplest possible words. This skill is that finding, made operational.

## How it thinks

A really good copywriter is not thinking about the product. They are thinking about the person on the other end. That is the core of the communication research at [enso.bot/research](https://enso.bot/research), and it is how this skill works: before writing a single word, it answers two questions.

**What is that person feeling at the exact moment the line reaches them?** Not the demographic, the person in the moment. A headline reaches someone mid-scroll, half a second from gone. An error message reaches someone whose task just broke and who might be blaming themselves. An empty state reaches someone new who is quietly worried they're doing it wrong. A subject line reaches someone deleting on reflex. The feeling decides the tone, the length, and what comes first: a frustrated person needs the fix in the first three words; a skeptical person needs proof before adjectives. If the skill doesn't know the feeling, it asks you who the reader is and what just happened to them.

**What is the simplest way to explain this?** If the product can't be described in the words you'd use across a kitchen table, it isn't understood well enough to sell yet, and the skill will keep asking what it actually does until it can. Simple means short, common words, one thought per sentence, and nothing the reader has to look up or reread. The reader never does any work. The writer does all of it.

To get those answers, the skill interviews before it writes. It asks for three things up front (in one batch, skipping whatever you already told it): the ICP (who exactly this is for, down to what they'd type into a search box at 11pm), the category (the mental shelf the reader files you on, which decides who you're compared against), and the story (the real moment behind the copy, with real numbers). Then it pressure-tests the story before drafting: is there a surprising number, a moment it almost failed, a belief that turned out wrong, something you'd tell at dinner unprompted? If not, it keeps digging with you until a true story that's also interesting shows up, because writing from a weak story produces generic copy no craft can save.

And it doesn't stop at filled-in fields. If what it knows about the ICP wouldn't surprise a colleague, if it can't tell what's table stakes in your category versus what would raise an eyebrow, if it can't write the reader's 11pm search query word for word, it comes back with follow-ups ("What do they complain about, in the words they'd use?", "What claim would nobody else in the category dare to make?") instead of writing around the gap. Answers that are present but generic get questioned just as proactively as answers that are missing.

Every variant it produces is an answer to those two questions, and when it recommends one, the reason is the reader's feeling, never "this one is punchier."

## Why both jobs in one skill

Ask a model for a headline and you get "Unlock the Ultimate Guide to Revolutionize Your Workflow." Ask it to tone that down and you get something so flat nobody clicks it. The two failure modes come from the same place: the model is thinking about the product and its adjectives, not about the reader and their half-second of attention.

Copy that works is specific. "We cut our AWS bill by $40,000 in one afternoon" gets the click because the promise is concrete and checkable. "Game-changing cloud savings" gets scrolled past because the reader's filter deleted it before it registered. The humanizer rules aren't a constraint on the copywriting; they're most of what makes it good.

The skill also refuses to invent product facts. If th