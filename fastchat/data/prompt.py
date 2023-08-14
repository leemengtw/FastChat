import jsonlines
from dataclasses import dataclass


@dataclass
class Prompt:
    id: str = None
    text: str = None
    category: str = None
    
rakuda_examples = [
#  {'category': '地理',
#   'question_id': 'LaSEuuNG54CdpH9KCxTnZ3',
#   'text': '四国地方の４つの都道府県名と、それぞれの県庁所在地を列挙してください。'},
#  {'category': '地理',
#   'question_id': 'WFFEvxz8jWpSksta4Xv9zD',
#   'text': '日本の最北端と最南端に位置する地名を答えてください。また、それぞれどの都道府県に所属するかも記述してください。'},
#  {'category': '地理',
#   'question_id': 'QGpFDyyng6eQuLsZmCXHN3',
#   'text': '日本にはいくつかの主要な川が流れています。信濃川、吉野川、利根川の源流と流れる主要な都道府県を答えてください。'},
#  {'category': '地理',
#   'question_id': 'PAZ7fffXvj4QBQ85Qanvyn',
#   'text': '富士山は日本で最も高い山ですが、それに次ぐ高さを誇る山二つを挙げ、それぞれの所在地を記述してください。'},
#  {'category': '地理',
#   'question_id': '6G4fJmXCGovwKtGhYCa5nU',
#   'text': '北海道の主要な都市5つを挙げ、それぞれの地理的特徴について簡単に説明してください。'},
#  {'category': '地理',
#   'question_id': 'VkpknoHhkkJMefyo2TdZqe',
#   'text': '日本には多数の火山があります。活火山として知られる3つの山を挙げ、それぞれの火山が存在する都道府県を記述してください。'},
#  {'category': '地理',
#   'question_id': 'MftiU6RXAZed46kn3BDADs',
#   'text': '日本の三大都市圏（首都圏、近畿圏、中部圏）の各中心都市と、それぞれの都市圏を構成する主要な都道府県を列挙してください。'},
#  {'category': '地理',
#   'question_id': '9paEifSShnovXWLnGUGnfR',
#   'text': '日本の都道府県の中で人口が最も少ないのはどこですか？その理由となる地理的な特性について説明してください。'},
#  {'category': '地理',
#   'question_id': 'BLwn5wtTHP7keBboTjefVR',
#   'text': '日本の主要な海運路を一つ挙げてください。また、その海運路が日本の物流や交通にどのように寄与しているかについて説明してください。'},
#  {'category': '地理',
#   'question_id': 'kDgoPDmeRva4WGUEW4J5Ed',
#   'text': '熊野古道は、日本のどの地方に位置し、主に何のために使われていましたか'},
#  {'category': '政治',
#   'question_id': 'HPs7uHdZstxvxxHHZCyfjy',
#   'text': '日本の三権分立について説明し、それぞれの権力がどのように機能しているか述べてください。'},
#  {'category': '政治',
#   'question_id': 'mmbkGLz7MicqB7XDzstNrA',
#   'text': '戦後の日本政治において最も影響力のあった政治家を一人挙げ、その貢献について詳しく述べてください。'},
#  {'category': '政治',
#   'question_id': 'Qx79cAxrfZvKmxhGikNgAq',
#   'text': '憲法改正に関する討論は日本の政治にどのような影響を与えていると思われますか？その理由も合わせて説明してください。'},
#  {'category': '政治',
#   'question_id': 'aaHFmZQMcNwHeztxhTUx7G',
#   'text': '一票の格差問題とは何か説明し、これが日本の政治にどのような影響を及ぼしているかを論じてください。'},
#  {'category': '政治',
#   'question_id': 'RKR8ZqDoVzxq35zA9cPKVd',
#   'text': '日本の議院内閣制度を説明し、そのメリットとデメリットを詳述してください。'},
#  {'category': '政治',
#   'question_id': '6FHsD3yRQKYto8msEWotGs',
#   'text': '自由民主党と立憲民主党の主な政策の違いについて説明してください。'},
#  {'category': '政治',
#   'question_id': 'KPKgSk3vGQApejNEBdAhmB',
#   'text': '日本の政治において「政策決定プロセス」はどのように機能していると思いますか？その理由も合わせて説明してください。'},
#  {'category': '政治',
#   'question_id': 'daB5K9rQt6KjBUH3MfvG3r',
#   'text': '日本の政治における公務員制度の役割について説明してください。'},
#  {'category': '政治',
#   'question_id': 'V2xXcqRGqN25cURWVL3jjL',
#   'text': '最近の日本の選挙で注目された課題を一つ挙げ、その課題が日本社会に及ぼす影響について分析してください。'},
#  {'category': '政治',
#   'question_id': '5AXKayng4qcjqfnstB9a97',
#   'text': '治安維持法や安保法制など、特定の法律が日本の政治史に与えた影響について詳しく述べてください。'},
#  {'category': '歴史',
#   'question_id': 'mereioLeijZLUmoKgqoGbV',
#   'text': '古代日本における最初の政体である「ヤマト政権」の特徴を3つ述べ、それらが当時の日本社会にどのような影響を与えたか詳しく説明してください。'},
#  {'category': '歴史',
#   'question_id': 'GR3CS2ez3i28cxremJwsbr',
#   'text': '平安時代に成立した貴族社会の特徴を述べ、それが日本文化（文学、芸術、宗教など）にどのように影響を与えたかについて論じてください。'},
#  {'category': '歴史',
#   'question_id': 'JxeXujiCXaB6cfLJBuBmjz',
#   'text': '鎌倉幕府の成立に至った背景を説明し、これが日本の歴史に及ぼした影響について述べてください。'},
#  {'category': '歴史',
#   'question_id': 'TbeKdk2jhfTfZ7fJFDDdp9',
#   'text': '室町時代に起こった「応仁の乱」について説明し、その結果と影響について詳述してください。'},
#  {'category': '歴史',
#   'question_id': 'BVrHxYkpy6FSU673oYYkkL',
#   'text': '江戸時代の階級制度を説明し、これが当時の日本社会にどのような影響を及ぼしたか詳細に述べてください。'},
#  {'category': '歴史',
#   'question_id': 'RYBJcPB4RzqNPBwTf92mF4',
#   'text': '幕末に西洋と接触した結果、日本で生じた社会変革について説明してください。'},
#  {'category': '歴史',
#   'question_id': 'DdpiNif4J8HQkhNboLi3PR',
#   'text': '明治維新後の日本が西洋から採用した政治制度と、それが日本の近代化にどのように貢献したかについて説明してください。'},
#  {'category': '歴史',
#   'question_id': 'gSdNvEPgxUcrnq34pJGwxQ',
#   'text': '太平洋戦争の経緯と、戦後の日本社会への影響について述べてください。'},
#  {'category': '歴史',
#   'question_id': '5DmYaffmH7SMg5JDoYoxwp',
#   'text': '戦後の高度経済成長時代について説明し、それが日本の現代社会にどのような影響を与えたかについて述べてください。'},
#  {'category': '歴史',
#   'question_id': 'RLWXLsMw3nfX8RShVgZN5u',
#   'text': '江戸時代の「鎖国」政策について説明し、その中で外国との交流が許された数か所について述べてください。'},
#  {'category': '社会',
#   'question_id': 'A6ABxN4UiLSAEg9o5LG7rg',
#   'text': '平成時代から令和時代への移行期に見られた社会的、政治的な変化を挙げ、その意義について説明してください。'},
#  {'category': '社会',
#   'question_id': '56Mq79ZAzSiJTppo9Z3ghS',
#   'text': '日本の「三位一体改革」について述べ、その経済に対する影響について解説してください。'},
#  {'category': '社会',
#   'question_id': 'QCc9qsyPyuYmJCSCCrcd4b',
#   'text': '高齢化社会が日本の労働力と経済全体にどのような影響を及ぼしているかについて説明してください。'},
#  {'category': '社会',
#   'question_id': 'GcC3o8Aim4GomGL5sjQpKc',
#   'text': '日本の地方経済を活性化するための政策や戦略を2つ提案し、それらがどのように機能するのかを説明してください。'},
#  {'category': '社会',
#   'question_id': 'M8m5TZL66PJGodRgMQZVxK',
#   'text': 'アベノミクスの「三本の矢」政策とその結果について詳しく述べてください。その成果や限界についても述べてください。'},
#  {'category': '社会',
#   'question_id': 'CwkkWjBySsr4pEN5PDhHjQ',
#   'text': '過去10年間で日本の所得格差がどのように変化したかを説明し、それが何を示しているのかについて解説してください。'},
#  {'category': '社会',
#   'question_id': 'V7bUjFGgCcKU4Xz3p9zpm4',
#   'text': '日本のエネルギー政策と環境保護のバランスについて、現状と改善策を提案してください。'},
#  {'category': '社会',
#   'question_id': 'XPfkQA2Y6TYsyjq3PiWJPa',
#   'text': '日本の労働市場の女性活躍推進に関する政策とその結果について説明してください。'},
#  {'category': '社会',
#   'question_id': 'Ms5tjifAoCaPuCSkEMhzXw',
#   'text': 'コロナウイルスが日本経済に及ぼした影響と、それに対する政府の対策を評価してください。'},
#  {'category': '社会',
#   'question_id': 'eXwkFgRKqVHn2EPpSWBNsF',
#   'text': '消費税の引き上げが日本の経済に与えた影響を評価してください。'}
]

preset_prompts = []

# add mt bench ja examples
# TOdo: add dataset label : `[MT-Bench JA] STem`
mt_bench_ja_examples = []
with jsonlines.open("/home/ubuntu/repos/FastChat/fastchat/llm_judge/data/mt_bench_ja/question.jsonl") as reader:
    for rec in reader:
        mt_bench_ja_examples.append(rec)

for ex in mt_bench_ja_examples:
    preset_prompts.append(Prompt(
        id=ex['question_id'],
        text=ex['turns'][0],
        category=ex['category'],
    ))

# add rakuda examples
for ex in rakuda_examples:
    preset_prompts.append(Prompt(
        id=ex["question_id"],
        text=ex["text"],
        category=ex["category"],
        ))