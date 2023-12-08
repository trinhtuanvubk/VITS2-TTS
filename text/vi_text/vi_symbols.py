""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''

_pad = '_'
_punctuation = ' !¿,'

# Phonemes
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_non_pulmonic_consonants = 'ʘɓǀɗǃʄǂɠǁʛ'
_pulmonic_consonants = 'pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ'
_suprasegmentals = 'ˈˌːˑ'
_other_symbols = 'ʍwɥʜʢʡɕʑɺɧ'
_diacrilics = 'ɚ˞ɫ'
_extra_phons = ['g', 'ɝ', '̃', '̍', '̥', '̩', '̯', '͡', '̪']  # some extra symbols that I found in from wiktionary ipa annotations
_vi_phons = '124567'

phonemes = list(
   _pad + _punctuation + _vowels + _non_pulmonic_consonants
   + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics + _vi_phons) + _extra_phons

phonemes_set = set(phonemes)