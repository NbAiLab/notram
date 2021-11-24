"""Norwegian Colossal Corpus v2 dataset."""
import gzip
import json
import datasets

logger = datasets.logging.get_logger(__name__)
_DESCRIPTION = """\\nNorwegian Colossal Corpus v2. Short sequences of maximum 100k characters."""
_CITATION = """
@inproceedings{kummervold-etal-2021-operationalizing,
    title = "Operationalizing a National Digital Library: The Case for a {N}orwegian Transformer Model",
    author = "Kummervold, Per E  and
      De la Rosa, Javier  and
      Wetjen, Freddy  and
      Brygfjeld, Svein Arne",
    booktitle = "Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)",
    month = may # " 31--2 " # jun,
    year = "2021",
    address = "Reykjavik, Iceland (Online)",
    publisher = {Link{\"o}ping University Electronic Press, Sweden},
    url = "https://aclanthology.org/2021.nodalida-main.3",
    pages = "20--29",
    abstract = "In this work, we show the process of building a large-scale training set from digital and digitized collections at a national library. The resulting Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian outperforms multilingual BERT (mBERT) models in several token and sequence classification tasks for both Norwegian Bokm{\aa}l and Norwegian Nynorsk. Our model also improves the mBERT performance for other languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore, we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.",
}
"""
_URL = "https://github.com/NbAiLab/notram"
_DATA_URL = "https://huggingface.co/datasets/NbAiLab/<corpusname>/resolve/main/data/{split_suffix}-shard-{index:04d}-of-{n_shards:04d}.json.gz"
_N_SHARDS_PER_SPLIT = {
    "train": <nosplits>, "validation": 1
}


class <corpusname>Config(datasets.BuilderConfig):
    """BuilderConfig for NbNn."""

    def __init__(self, *args, **kwargs):
        """BuilderConfig for NbNn.
        Args:
            **kwargs: keyword arguments forwarded to super.
        """
        super().__init__(
            *args,
            name="<corpusname>",
            **kwargs,
        )


class <corpusname>(datasets.GeneratorBasedBuilder):
    """Norwegian Colossal Corpus v2."""
    BUILDER_CONFIGS = [<corpusname>Config()]
    BUILDER_CONFIG_CLASS = <corpusname>Config

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "doc_type": datasets.Value("string"),
                    "publish_year":  datasets.Value("int32"),
                    "lang_fasttext":  datasets.Value("string"),
                    "lang_fasttext_conf":  datasets.Value("string"),
                    "text":  datasets.Value("string"),

                }
            ),
            supervised_keys=None,
            homepage=_URL,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        data_urls = {}
        for split in ["train", "validation"]:
            data_urls[split] = [
                _DATA_URL.format(
                    language=self.config.name,
                    split_suffix=split,
                    index=index,
                    n_shards=_N_SHARDS_PER_SPLIT[split],
                )
                for index in range(1, _N_SHARDS_PER_SPLIT[split] + 1)
            ]
        train_downloaded_files = dl_manager.download(data_urls["train"])
        validation_downloaded_files = dl_manager.download(data_urls["validation"])

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepaths": train_downloaded_files}),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs={"filepaths": validation_downloaded_files}
            ),

        ]

    def _generate_examples(self, filepaths):
        """This function returns the examples in the raw (text) form by iterating on all the files."""
        id_ = 0
        for filepath in filepaths:
            logger.info("generating examples from = %s", filepath)
            with gzip.open(open(filepath, "rb"), "rt", encoding="utf-8") as f:
                for line in f:
                    if line:
                        example = json.loads(line)
                        yield id_, example
                        id_ += 1