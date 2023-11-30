## LJSpeech
import torch

import commons
import utils
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence

from scipy.io.wavfile import write
import argparse

def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="logs/ckpt_vits2/G_0.pth", help="Path to model (.onnx)")
    parser.add_argument(
        "--config-path", default="./configs/vits2_ljs_nosdp.json", help="Path to model config (.json)"
    )
    parser.add_argument(
        "--output-wav-path", default= "sample_vits2.wav", help="Path to write WAV file"
    )
    parser.add_argument("--text",type=str, default="I love you so much", help="Text to synthesize")
    parser.add_argument("--sid", required=False, type=int, help="Speaker ID to synthesize")
    args = parser.parse_args()

    # CONFIG_PATH = "./configs/vits2_ljs_nosdp.json"
    # # MODEL_PATH = "./logs/ljs_base/G_14000.pth"
    # MODEL_PATH = "logs/ckpt_vits2/G_0.pth"
    # TEXT = "He was seen afterwards smoking and talking with his hosts"
    # OUTPUT_WAV_PATH = "sample_vits2.wav"

    hps = utils.get_hparams_from_file(args.config_path)

    if (
        "use_mel_posterior_encoder" in hps.model.keys()
        and hps.model.use_mel_posterior_encoder == True
    ):
        print("Using mel posterior encoder for VITS2")
        posterior_channels = 80  # vits2
        hps.data.use_mel_posterior_encoder = True
    else:
        print("Using lin posterior encoder for VITS1")
        posterior_channels = hps.data.filter_length // 2 + 1
        hps.data.use_mel_posterior_encoder = False

    net_g = SynthesizerTrn(
        len(symbols),
        posterior_channels,
        hps.train.segment_size // hps.data.hop_length,
        **hps.model
    ).cuda()
    _ = net_g.eval()

    _ = utils.load_checkpoint(args.model, net_g, None)

    stn_tst = get_text(args.text, hps)
    with torch.no_grad():
        x_tst = stn_tst.cuda().unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
        audio = (
            net_g.infer(
                x_tst, x_tst_lengths, noise_scale=0.667, noise_scale_w=0.8, length_scale=1
            )[0][0, 0]
            .data.cpu()
            .float()
            .numpy()
        )

    write(data=audio, rate=hps.data.sampling_rate, filename=args.output_wav_path)

if __name__ == "__main__":
    main()
