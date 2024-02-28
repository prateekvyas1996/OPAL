from pathlib import Path
import streamlit as st
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors

files_path = st.text_input("Give path of text files: ", "./cache")

# Create a list of text files
txt_files_path = [str(file) for file in Path(files_path).rglob("*.txt")]

tokenize_bt = st.button("Build Tokenizer")

if tokenize_bt:
    # Initialize a tokenizer
    tokenizer = Tokenizer(models.BPE())

    # Customize pre-tokenization and decoding
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
    tokenizer.decoder = decoders.ByteLevel()
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)

    # Train the tokenizer
    trainer = trainers.BpeTrainer(
        vocab_size=20000,
        min_frequency=2,
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet()
    )
    tokenizer.train(txt_files_path, trainer=trainer)

    # Save the tokenizer
    tokenizer.save("tokenizer.json", pretty=True,)
