# coding=utf-8
import sys
import math
import random

kana_list = [
    (u'あ', u'ア', 'a'),
    (u'い', u'イ', 'i'),
    (u'う', u'ウ', 'u'),
    (u'え', u'エ', 'e'),
    (u'お', u'オ', 'o'),
    (u'か', u'カ', 'ka'),
    (u'き', u'キ', 'ki'),
    (u'く', u'ク', 'ku'),
    (u'け', u'ケ', 'ke'),
    (u'こ', u'コ', 'ko'),
    (u'さ', u'サ', 'sa'),
    (u'し', u'シ', 'shi'),
    (u'す', u'ス', 'su'),
    (u'せ', u'セ', 'se'),
    (u'そ', u'ソ', 'so'),
    (u'た', u'タ', 'ta'),
    (u'ち', u'チ', 'chi'),
    (u'つ', u'ツ', 'tsu'),
    (u'て', u'テ', 'te'),
    (u'と', u'ト', 'to'),
    (u'な', u'ナ', 'na'),
    (u'に', u'ニ', 'ni'),
    (u'ぬ', u'ヌ', 'nu'),
    (u'ね', u'ネ', 'ne'),
    (u'の', u'ノ', 'no'),
    (u'は', u'ハ', 'ha'),
    (u'ひ', u'ヒ', 'hi'),
    (u'ふ', u'フ', 'fu'),
    (u'へ', u'ヘ', 'he'),
    (u'ほ', u'ホ', 'ho'),
    (u'ま', u'マ', 'ma'),
    (u'み', u'ミ', 'mi'),
    (u'む', u'ム', 'mu'),
    (u'め', u'メ', 'me'),
    (u'も', u'モ', 'mo'),
    (u'や', u'ヤ', 'ya'),
    (u'ゆ', u'ユ', 'yu'),
    (u'よ', u'ヨ', 'yo'),
    (u'ら', u'ラ', 'ra'),
    (u'り', u'リ', 'ri'),
    (u'る', u'ル', 'ru'),
    (u'れ', u'レ', 're'),
    (u'ろ', u'ロ', 'ro'),
    (u'わ', u'ワ', 'wa'),
    # (u'を', u'ヲ', 'wo'), # pronounced 'o' not 'wo', so confusing
    (u'ん', u'ン', 'n'),
    (u'が', u'ガ', 'ga'),
    (u'ぎ', u'ギ', 'gi'),
    (u'ぐ', u'グ', 'gu'),
    (u'げ', u'ゲ', 'ge'),
    (u'ご', u'ゴ', 'go'),
    (u'ざ', u'ザ', 'za'),
    (u'じ', u'ジ', 'ji'),
    (u'ず', u'ズ', 'zu'),
    (u'ぜ', u'ゼ', 'ze'),
    (u'ぞ', u'ゾ', 'zo'),
    (u'だ', u'ダ', 'da'),
    (u'で', u'デ', 'de'),
    (u'ど', u'ド', 'do'),
    (u'ば', u'バ', 'ba'),
    (u'び', u'ビ', 'bi'),
    (u'ぶ', u'ブ', 'bu'),
    (u'べ', u'ベ', 'be'),
    (u'ぼ', u'ボ', 'bo'),
    (u'ぱ', u'パ', 'pa'),
    (u'ぴ', u'ピ', 'pi'),
    (u'ぷ', u'プ', 'pu'),
    (u'ぺ', u'ペ', 'pe'),
    (u'ぽ', u'ポ', 'po'),
    (u'きゃ', u'キャ', 'kya'),
    (u'きゅ', u'キュ', 'kyu'),
    (u'きょ', u'キョ', 'kyo'),
    (u'しゃ', u'シャ', 'sha'),
    (u'しゅ', u'シュ', 'shu'),
    (u'しょ', u'ショ', 'sho'),
    (u'ちゃ', u'チャ', 'cha'),
    (u'ちゅ', u'チュ', 'chu'),
    (u'ちょ', u'チョ', 'cho'),
    (u'にゃ', u'ニャ', 'nya'),
    (u'にゅ', u'ニュ', 'nyu'),
    (u'にょ', u'ニョ', 'nyo'),
    (u'ひゃ', u'ヒャ', 'hya'),
    (u'ひゅ', u'ヒュ', 'hyu'),
    (u'ひょ', u'ヒョ', 'hyo'),
    (u'みゃ', u'ミャ', 'mya'),
    (u'みゅ', u'ミュ', 'myu'),
    (u'みょ', u'ミョ', 'myo'),
    (u'りゃ', u'リャ', 'rya'),
    (u'りゅ', u'リュ', 'ryu'),
    (u'りょ', u'リョ', 'ryo'),
    (u'ぎゃ', u'ギャ', 'gya'),
    (u'ぎゅ', u'ギュ', 'gyu'),
    (u'ぎょ', u'ギョ', 'gyo'),
    (u'じゃ', u'ジャ', 'ja'),
    (u'じゅ', u'ジュ', 'ju'),
    (u'じょ', u'ジョ', 'jo'),
    (u'びゃ', u'ビャ', 'bya'),
    (u'びゅ', u'ビュ', 'byu'),
    (u'びょ', u'ビョ', 'byo'),
    (u'ぴゃ', u'ピャ', 'pya'),
    (u'ぴゅ', u'ピュ', 'pyu'),
    (u'ぴょ', u'ピョ', 'pyo'),
]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: iroha.py ENTROPY_BITS'
        sys.exit(1)

    min_entropy_bits = float(sys.argv[1])
    gen_count = 10

    # only use mora that romanize to two characters or less, to reduce typing
    used_kana_list = [k for k in kana_list if len(k[2]) <= 2]

    bits_per_mora = math.log(len(used_kana_list), 2)

    required_mora = int(math.ceil(min_entropy_bits / bits_per_mora))

    print 'For a minimum of %d bits of entropy, we need to pick %d random mora from the set of %d, which gives %d actual bits of entropy. Here are %d random passwords:' % (min_entropy_bits, required_mora, len(used_kana_list), required_mora*bits_per_mora, gen_count)

    rand = random.SystemRandom() # ensures that OS generator is used (/dev/urandom on unix-like systems)

    for n in range(gen_count):
        romaji_parts = []
        for i in range(required_mora):
            romaji_parts.append(rand.choice(used_kana_list)[2])
        print '-'.join(romaji_parts)
