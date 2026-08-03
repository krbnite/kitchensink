# Word Embeddings Notes

This mini-project preserves and cleans up a 2018-era intro NLP note about the path from symbolic word resources to dense word vectors.

The original source note lives in `original-2018-intro-nlp-notes.md`. The cleaned version below keeps the same conceptual arc, but trims the scratch-notebook roughness and adds a short 2026 perspective.

## Files

- `original-2018-intro-nlp-notes.md`: preserved source note.
- `word-embeddings-demo.ipynb`: small runnable notebook showing WordNet, one-hot vectors, co-occurrence vectors, cosine similarity, and LSA-style SVD.
- `nlp-env.sh`: local Conda environment helper.
- `.gitignore`: keeps local envs, caches, and generated scratch output out of git.

## Environment Setup

First make the script executable:

```bash
chmod +x nlp-env.sh
```

Then create and activate the local environment:

```bash
./nlp-env.sh
conda activate ./.conda-word-embeddings
jupyter lab word-embeddings-demo.ipynb
```

The script installs `nltk`, `numpy`, `scikit-learn`, `matplotlib`, and Jupyter. It also downloads the NLTK WordNet data into a project-local `nltk_data/` folder, which is ignored by git.

## The 2018 Learning Arc

The original note is about a central question in older NLP:

How should a program represent the meaning of a word?

### 1. Symbolic Lexicons

WordNet represents words through explicit human-curated relations: synonyms, lemmas, hypernyms, hyponyms, and related senses.

That is useful because it makes meaning inspectable. You can ask for a word's place in a hierarchy and get a readable path: panda -> carnivore -> mammal -> animal -> entity.

It is limited because language changes, word sense is contextual, coverage is incomplete, and hand-built symbolic resources are expensive to maintain.

### 2. One-Hot Vectors

A one-hot vector gives each word one coordinate in a vocabulary-sized space.

If the vocabulary has 500,000 words, every word gets a 500,000-dimensional vector with one `1` and 499,999 zeroes.

This is clean for indexing, but bad for meaning. Under a simple dot product, `cat` is no closer to `kitten` than it is to `couch`. Every distinct word is orthogonal to every other distinct word.

That is the core weakness the old note was circling: one-hot encoding is a convenient address system, not a semantic representation.

### 3. Distributional Similarity

The next move is the distributional hypothesis:

Words that occur in similar contexts tend to have related meanings.

Instead of representing a word as an isolated symbol, represent it through its neighbors. If `cat`, `kitten`, and `dog` appear near words like `pet`, `food`, `fur`, and `home`, their vectors begin to look more similar than the vectors for unrelated words.

This is the conceptual bridge from symbolic NLP to embedding-based NLP.

### 4. Dense Word Vectors

Co-occurrence vectors can still be huge, so the next question is whether the high-dimensional space has lower-dimensional structure.

LSA answers this with linear algebra: build a term-document or term-context matrix, then apply truncated SVD to project sparse word/document patterns into a lower-dimensional semantic space.

Word2Vec answers it with prediction: learn vectors that help predict a word from context or context from a word.

The original note was right to focus on this shift. Word vectors were exciting because they turned the old hand-built similarity problem into a learned geometry problem.

## Word2Vec In One Paragraph

Word2Vec is a family of shallow neural methods for learning word embeddings from local context. The two famous architectures are:

- Continuous Bag of Words: predict the target word from neighboring context words.
- Skip-gram: predict neighboring context words from a target word.

The expensive part is predicting over a large vocabulary, so practical Word2Vec training uses approximations such as negative sampling or hierarchical softmax.

## 2026 Perspective

Word2Vec, GloVe, LSA, and WordNet are no longer the center of modern NLP practice, but they are still worth knowing.

They teach the idea that language can be represented geometrically. That idea survives directly in modern transformer systems.

The main difference is context:

- A Word2Vec-style embedding gives a word type a mostly fixed vector.
- A transformer gives each token a vector that depends on the sentence, document, prompt, or conversation around it.

So the old question was:

What vector should represent this word?

The modern question is:

What vector should represent this token, span, sentence, document, or tool-using state in this context?

That is why this old note still belongs in kitchensink. It captures the conceptual step that made modern NLP feel possible.

## References

- NLTK WordNet HOWTO: https://www.nltk.org/howto/wordnet.html
- TensorFlow Word2Vec tutorial: https://www.tensorflow.org/text/tutorials/word2vec
- scikit-learn `TruncatedSVD`: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html
- Hugging Face Transformers quickstart: https://huggingface.co/docs/transformers/main/en/quicktour
