from __future__ import absolute_import, division, print_function

import csv
import os
import codecs

import nlp

#Here we have to specify the path where the dataset is
#Since i'm using colab, i simply put the colab "path"
_TEST_FILE_NAME = "test.tsv"

class AssertionConfig(nlp.BuilderConfig):

    """BuilderConfig for Break"""

    def __init__(self, **kwargs):
        """BuilderConfig for BlogAuthorship
        Args:
          data_url: `string`, url to the dataset (word or raw level)
          **kwargs: keyword arguments forwarded to super.
        """
        super(AssertionConfig, self).__init__(
            version=nlp.Version("1.0.0", "New split API (https://tensorflow.org/datasets/splits)"), **kwargs
        )


class Assertion(nlp.GeneratorBasedBuilder):

    VERSION = nlp.Version("0.1.0")
    BUILDER_CONFIGS = [
        AssertionConfig(
            name="assertion",
            #data_url=_DATA_URL,
        )
    ]

    def _info(self):
        return nlp.DatasetInfo(
            # nlp.features.FeatureConnectors
            features=nlp.Features(
                {
                    "method": nlp.Value("string"),
                    "assertion": nlp.Value("string")
                }
            ),
            
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        

        test_csv_file = _TEST_FILE_NAME

        if self.config.name == "assertion":
            return [
                
                nlp.SplitGenerator(
                    name=nlp.Split.TEST,
                    # These kwargs will be passed to _generate_examples
                    gen_kwargs={"file_path": test_csv_file},
                )
                
            ]
        else:
            raise NotImplementedError("{} does not exist".format(self.config.name))

    def _generate_examples(self, file_path):
        """Yields examples."""

        with open(file_path, encoding="ISO-8859-1") as f:
            #data = csv.reader(f,delimiter='\t', quotechar='"')
            data = csv.reader((line.replace('\0','') for line in f), delimiter="\t", quotechar='"')
            for row_id, row in enumerate(data):
                method,assertion = row
                yield "{}".format(row_id), {
                    "method": method,
                    "assertion": assertion
                }
