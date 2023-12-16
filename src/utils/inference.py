from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import os
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

def predict_image(modelpath: str, imagepath: str) -> str:

    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-stage1').to(device)
    # set special tokens used for creating the decoder_input_ids from the labels
    model.config.decoder_start_token_id = processor.tokenizer.cls_token_id
    model.config.pad_token_id = processor.tokenizer.pad_token_id
    # make sure vocab size is set correctly
    model.config.vocab_size = model.config.decoder.vocab_size

    # set beam search parameters
    model.config.eos_token_id = processor.tokenizer.sep_token_id
    model.config.max_length = 64
    model.config.early_stopping = True
    model.config.no_repeat_ngram_size = 3
    model.config.length_penalty = 2.0
    model.config.num_beams = 4

    checkpoint = torch.load(modelpath, map_location=device)
    print(checkpoint)
    # Load the state_dict from the OrderedDict in the checkpoint
    model.load_state_dict(checkpoint)


    image = Image.open(imagepath).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print(generated_text)

if __name__ == '__main__':
    PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    MODEL = "trOCR.pth"
    MODEL_PATH = os.path.join(PARENT_DIR, "saved", MODEL)
    print(MODEL_PATH)

    IMAGE = "1233.png"
    IMAGE_PATH = os.path.join(PARENT_DIR, "test", IMAGE)
    print(IMAGE_PATH)

    # text = predict_image()