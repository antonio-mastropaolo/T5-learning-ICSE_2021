# Studying the Usage of Text-To-Text Transfer Transformer to Support Code-Related Tasks

In this work, we explore the capabilities of novel transformers architecture, ***T5(Text-To-Text Transfer Transformer)*** to support Code-Related Tasks.

For all the details :point_right: <a href=''>:page_facing_up:</a>

#### Pipeline

In order to pre-train and then finetune a [T5 small](https://github.com/google-research/text-to-text-transfer-transformer) model, we need a new sentencepiece model to accommodate the expanded vocabulary given by the java programming language, abstracted java tokens, and technical natural language.



*  ##### How to train a new <a href='https://github.com/google/sentencepiece/blob/master/python/README.md'>SPmodel</a>

    *Pythonic way*

    ```
    pip install sentencepiece
    import sentencepiece as spm
    spm.SentencePieceTrainer.train('--input=pretraining.txt --model_prefix=dl4se --vocab_size=32000 --bos_id=-1  --eos_id=1 --unk_id=2 --pad_id=0') 
    ```
    The new model has to be trained on the entire pre-training corpus.

* ##### Set up a GCS Bucket
    To Set up a new GCS Bucket for training and fine-tuning a T5 Model, please follow the orignal guide provided by <a href='https://www.google.com'> Google </a>. 
    Here the link: https://cloud.google.com/storage/docs/quickstart-console
    Subsequently, by following the jupyter notebook we provide for pre-train and fine-tune the network, you should be able to set up the final environment.

* ##### About the datasets

    The datasets for the pre-training and the fine-tuning can be found here: https://drive.google.com/drive/folders/1uJv-kljY1Q59fa-TdkpXOOd9QEG5OZDa?usp=sharing


* ##### Pre-trainig/Fine-tuning 
  
    To pre-train and then, fine-tune T5, please use the script we provide here:
    - <a href ='https://github.com/antonio-mastropaolo/T5-learning-ICSE_2021/blob/main/Code/pre-training.ipynb'>Pre-Training</a> 
    -  <a href ='https://github.com/antonio-mastropaolo/T5-learning-ICSE_2021/blob/main/Code/fine-tuning.ipynb'>Fine-Tuning</a> 

* ##### How to generate the predictions

    First you need to convert the TF model into a pytorch model by using <a href='https://github.com/antonio-mastropaolo/T5-learning-ICSE_2021/blob/main/Code/Miscellaneous/tf_2_pytorch_T5.py'> TF_to_Pytorch </a>, then run <a href='https://github.com/antonio-mastropaolo/T5-learning-ICSE_2021/blob/main/Code/run-on-test-set/generate_results.ipynb'> Generate Results </a>

* ##### Our results
    
    To check our predictions: https://drive.google.com/drive/folders/14ywfhJorNNeWxgSV1bI0XIzlLAFu8odH?usp=sharing


**Additional:** In <a href='https://github.com/antonio-mastropaolo/T5-learning-ICSE_2021/tree/main/Code/Miscellaneous'>Miscellaneous</a> folder, you can find all the additional scripts we used for computing the BLEU score and the overlap metrics. Furthermore, <a href='https://drive.google.com/file/d/1BWhr4KbAp6_NKc_BH3lPTjfM1Hzq71Ct/view?usp=sharing'>here</a> and <a href='https://drive.google.com/drive/folders/1caP5-OpurKOMhkqfsrkHxKarEoYVjiFI?usp=sharing'>here</a> you can also experiment with our pre-trained and fine-tuned models.
