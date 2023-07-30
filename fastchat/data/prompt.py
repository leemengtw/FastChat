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
mt_bench_ja_examples = [{'question_id': 'extraction_1_1',
  'category': 'extraction',
  'question_group': 1,
  'turn': 1,
  'question': '以下の映画のレビューを1から5のスケールで評価してください。1は非常に否定的、3は中立、5は非常に肯定的とします：\n1. 2019年11月18日に公開されたこの映画は素晴らしい。撮影、演技、プロット、すべてが一流でした。\n2. 映画にこんなに失望したことは今までにない。ストーリーは予測可能で、キャラクターは一次元的だった。私の意見では、この映画は2022年に公開された映画の中で最悪の一つだ。\n3. 映画はまあまあだった。楽しめた部分もあったが、物足りないと感じた部分もあった。これは2018年2月に公開された、かなり平凡な映画のようだ。\n答えを整数のJSON配列として返してください。'},
 {'question_id': 'extraction_2_1',
  'category': 'extraction',
  'question_group': 2,
  'turn': 1,
  'question': '次のカテゴリーがあります - 文学、歴史、科学、芸術。以下の質問を分析し、それらをこれらのカテゴリーのいずれかに割り当ててください。応答では、余分な言葉をしないでください。1行につき1つのトピックを厳密にリストアップしてください。\n1. 三島由紀夫の「金閣寺」に見られる主要なテーマと手法を議論してください。それらはどのように20世紀の日本の社会的状況と一致しますか？\n2. 戦国時代の各大名が採用した地政学戦略と国内政策を分析してください。これらの行動はどのようにして戦後の国際秩序を形成しましたか？\n3. 水のルイス構造を描き、その極性の性質を説明してください。これが沸点が高く、多くの物質を溶かす能力などのユニークな特性にどのように影響を与えるかを説明してください。\n4. 鳥居清長の「浮世絵」に見られる芸術的技法とスタイル選択を批判的に検討してください。この絵画はどのように江戸時代の文化と哲学的環境を反映していますか？'},
 {'question_id': 'extraction_3_1',
  'category': 'extraction',
  'question_group': 3,
  'turn': 1,
  'question': '提示されたテキストから次の情報を抽出してください：本の名前、著者、主人公、出版年。出力形式は "主人公、本、著者、出版年" で、一行に一冊の本を記述してください。\na) マーダーミステリーの分野では、東野圭吾の作品が特に印象に残る。彼の作品の中でも特に記憶に残るのは「容疑者Xの献身」である。このアイコニックな物語は2005年に発表され、数学者の石神と料理店の女主人、彼女の娘についての物語である。\nb) 日本の児童文学の一つである宮沢賢治の「銀河鉄道の夜」は1927年に発表され、物語は二人の少年ジョバンニとカムパネルラを中心に展開されます。\nc) 戦後の日本を背景にした小説として、1933年からさまざまな雑誌に分載された川端康成の「雪国」があります。主人公・島村は雪国に向かう汽車の中で、病人の男に付き添う恋人らしき若い娘に興味を惹かれたことから展開されます。'},
 {'question_id': 'extraction_4_1',
  'category': 'extraction',
  'question_group': 4,
  'turn': 1,
  'question': '以下のデータを基に、2021年に最も利益を上げた会社とそのCEOの名前を特定してください:\na) 田中社長の下で運営される会社Aは、2021年に30億円の売上高と3億円の利益を報告しました。\nb) 鈴木社長が率いる会社Bは、同年に60億円の売上高と6億円の利益を記録しました。\nc) 佐藤社長の下で運営される会社Cは、2021年に20億円の売上高と7億円の利益を発表しました。\nd) 高橋社長が管理する会社Dは、2021年に300億円の売上高と21億円の利益を公表しました。\ne) 伊藤社長の下で運営される会社Eは、2021年に200億円の売上高と25億円の利益を報告しました。\nf) 山田社長が率いる会社Fは、同年に180億円の売上高と20億円の利益を記録しました。'},
 {'question_id': 'extraction_5_1',
  'category': 'extraction',
  'question_group': 5,
  'turn': 1,
  'question': '以下の文中に登場する国、その首都、そして話されている言語を特定してください。出力はJSON形式でお願いします。\na) 優美な景色の中で、デンマークの首都コペンハーゲンは、活気に満ちたアートシーンと魅力的なデンマーク語で訪問者を魅了します。\nb) 魔法の国エルドリアの中には、壮大な都市アヴァロアがあり、幻想的なオーラが放たれています。この神秘的な場所で主に使われるのは、美しい言葉であるルミナ語です。\nc) 伝統と現代が見事に調和した中で、アルゼンチンの首都ブエノスアイレスは、活気に満ちた大都市として立っています。情緒豊かなスペイン語が市民の間で主流となっています。'},
 {'question_id': 'extraction_6_1',
  'category': 'extraction',
  'question_group': 6,
  'turn': 1,
  'question': '下記の段落を読み、"アマゾン"、"川"、そして"生物"が何回出現するか数えてください。結果は"単語、出現回数"の形式で、各単語を別々の行にしてください。出現回数の多い順に行を並べてください。\nアマゾンは自然の驚異が広がる魅惑的な地域で、そこには伝説的なアマゾン川が流れています。アマゾンの熱帯雨林をはじめとする壮大な風景を通り、川はブラジル、コロンビア、ペルーを経由し、無数の生物に生命を与えています。アマゾンのジャングルをうろつく強大なジャガーから、樹冠上空を飛び回る鮮やかなマカウまで、この驚くべき地域は生物多様性に溢れています。川の流れの中深くには、壮観なピンクの川のイルカが、ピラニアやエレクトリックイールと共に優雅に泳いでいます。川岸には、都市と自然が交錯するマナウスのような活気ある都市や、アマゾン熱帯雨林の中心への入口となるイキトスがあります。さらに進むと、アマゾン川はアナヴィリアナス諸島という魅力的な秘境を明らかにします。ここは稀有な種類が溢れる島々のモザイクです。冒険に乗り出し、魅力的なアマゾン川を探検し、生命と自然美に満ちた世界に身を浸してみてください。'},
 {'question_id': 'extraction_7_1',
  'category': 'extraction',
  'question_group': 7,
  'turn': 1,
  'question': '以下のニュース記事で言及されている固有名詞（人、組織、場所）を特定してください。それらの固有名詞をエンティティタイプ別に3つのグループに分けてJSON辞書を作成してください。キーはエンティティのタイプで、値は文字列のリストとします。\n昨日、ファラデーのCEOである中島雄一郎氏とダイムラーAGのCEOである斎藤昭二氏は、ベルリンに新たなギガファクトリーを建設する計画を発表しました。この施設はファラデーとダイムラーの合弁事業で、両社の電気自動車とバッテリーパックを生産し、地域の雇用を何千も創出します。中島氏と斎藤氏は、ベルリンの戦略的な位置、熟練した労働力、強固なインフラが拡大に適していると述べました。新たなギガファクトリーは、ヨーロッパでの電気自動車への需要の増加に対応し、持続可能な未来に貢献することを目指しています。フォルクスワーゲンのCEOである田村健一郎氏はこのニュースを歓迎し、自動車産業の電動化への移行にはより大きな協力が有益だと述べました。'},
 {'question_id': 'extraction_8_1',
  'category': 'extraction',
  'question_group': 8,
  'turn': 1,
  'question': '次の三つの最新のスマートフォン、iPhone、Samsung Galaxy、Google Pixelに対する、さまざまな情報源からの顧客レビューを分析し、各電話について1から10のスケールで全体的な評価を提供してください。以下の複雑で矛盾したレビューを考慮に入れてください：\n- TechRadarによる最新のiPhoneのレビュー：新しいiPhoneは、スマートフォンのパフォーマンスとカメラの品質に新たな基準を設ける、驚くべき技術の勝利です。しかし、デザインの微増と高価格は、以前のiPhoneの「すげー」ファクターを欠いています。それでも、そのパワーと性能は無比です。\n- CNETによる最新のSamsung Galaxyのレビュー：Samsung Galaxyの携帯電話には、素晴らしいスクリーン、高速なパフォーマンス、堅実なバッテリー寿命、そして印象的なカメラオプションなど、たくさんのハイポイントがあります。しかしながら、Bixbyはまだ物足りなく、AR絵文字は平坦で、全体的なデザインはそれほど変わっていません。新しいGalaxyは全体的に素晴らしい電話ですが、いくつかの小さな弱点が真の偉大さを達成するのを妨げています。\n- The Vergeによる最新のGoogle Pixelのレビュー：GoogleのPixelは、最新の仕様、革新的なAIパワードソフトウェア、そして素晴らしいカメラをスリークなデザインに詰め込んでいます。しかし、バッテリー寿命が物足りない、拡張可能なストレージがない、そして高価格を考慮すると、パフォーマンスが時々つまづくことがあります。シームレスなソフトウェア、エリートの写真撮影、そしてGoogleのAIアシスタンスが最も重要なら、Pixelが好きになるでしょう。しかし、全体的な体験は競合他社ほどまんべんなくはありません。\nそれぞれのスマートフォンの全体的な評価を10点満点で1つのJSONオブジェクトで返してください、小数点第一位まで。'},
 {'question_id': 'extraction_9_1',
  'category': 'extraction',
  'question_group': 9,
  'turn': 1,
  'question': '複雑な方程式のセットから、各方程式からすべての一意の変数名を抽出します。結果をJSON文字列として返し、各方程式に一行を割り当ててください。\n1) y = (3/4)x^3 - e^(2x) + sin(pi*x) - sqrt(7)\n2) 2A - B/(3+C) * sum(N=1 to 5; ln(N)^2) = 5D*integral(a=0 to pi; cos(comb(N=1 to 10; N*a)))\n3) E = m(c^2) + gamma*(v/d)/(-(alpha/2) + sqrt(beta^2 + (alpha/2)^2))'},
 {'question_id': 'extraction_10_1',
  'category': 'extraction',
  'question_group': 10,
  'turn': 1,
  'question': '以下の株価の記録から、2022年の各月の最高および最低の終値を抽出します。結果をCSV文字列として返し、各月に一行を割り当ててください。\n日付、開始、高値、安値、終値、ボリューム\n2022-01-01,150.02,155.28,148.50,153.80,15678900\n2022-01-02,154.32,157.25,153.48,156.25,19874500\n2022-02-01,160.50,163.28,159.50,161.80,14326700\n2022-02-02,161.80,164.25,161.30,163.90,17689200\n2022-03-01,165.40,168.35,163.10,166.80,16253400\n2022-03-02,167.00,169.85,165.50,168.20,19568100'},
 {'question_id': 'humanities_1_1',
  'category': 'humanities',
  'question_group': 1,
  'turn': 1,
  'question': '経済成長率、消費者物価指数、失業率などの経済指標と日本銀行の金融政策との関係性を説明してください。その経済指標に影響を与える主な政策手段を示し、それぞれの効果について考察してください。'},
 {'question_id': 'humanities_2_1',
  'category': 'humanities',
  'question_group': 2,
  'turn': 1,
  'question': '人生の各段階は、我々が時間や死をどう理解するかにどのように影響を与えるでしょうか？例を挙げて説明してください。'},
 {'question_id': 'humanities_3_1',
  'category': 'humanities',
  'question_group': 3,
  'turn': 1,
  'question': '日本の独占禁止法と市場競争への影響について説明してください。具体的な事例を挙げて比較・検討してみましょう。'},
 {'question_id': 'humanities_4_1',
  'category': 'humanities',
  'question_group': 4,
  'turn': 1,
  'question': '黒船来航と開国をテーマに、劇やパントマイムを取り入れた歴史の授業計画を作成してください。授業期間は45分の授業を3日間で行うものとします。'},
 {'question_id': 'humanities_5_1',
  'category': 'humanities',
  'question_group': 5,
  'turn': 1,
  'question': '美術の名作を子供向けのインタラクティブな体験に変えるためのアイデアを5つ挙げ、それぞれの作品とそのアイデアを説明してください。'},
 {'question_id': 'humanities_6_1',
  'category': 'humanities',
  'question_group': 6,
  'turn': 1,
  'question': '基準率の無視（base rate neglect）という誤謬とは何かを説明し、政治家がキャンペーンでそれをどのように使用するかの具体的な例を5つ挙げてください。'},
 {'question_id': 'humanities_7_1',
  'category': 'humanities',
  'question_group': 7,
  'turn': 1,
  'question': '論理的な書き方で論議を評価するための5つの主要な原則を説明してください。'},
 {'question_id': 'humanities_8_1',
  'category': 'humanities',
  'question_group': 8,
  'turn': 1,
  'question': 'ソクラテスは彼の時代の主流の考えにどのように挑戦しましたか？'},
 {'question_id': 'humanities_9_1',
  'category': 'humanities',
  'question_group': 9,
  'turn': 1,
  'question': '日本でビジネスを行う際のビジネスマナーについて説明してください。'},
 {'question_id': 'humanities_10_1',
  'category': 'humanities',
  'question_group': 10,
  'turn': 1,
  'question': '将来的な映画製作者が学ぶべき五つの受賞歴のあるドキュメンタリー映画とそれぞれの背景説明を提案してください。'},
 {'question_id': 'reasoning_1_1',
  'category': 'reasoning',
  'question_group': 1,
  'turn': 1,
  'question': 'あなたが人々と一緒にレースをしていると想像してみてください。あなたがちょうど2番目の人を追い越したとしたら、あなたの現在の位置は何番目でしょうか？ あなたが追い越した人の位置はどこでしょうか？'},
 {'question_id': 'reasoning_2_1',
  'category': 'reasoning',
  'question_group': 2,
  'turn': 1,
  'question': 'あなたの左に美しい赤い家が、右には幻想的な温室が、正面には魅力的なピンクの場所が見えます。では、白い家はどこにありますか？'},
 {'question_id': 'reasoning_3_1',
  'category': 'reasoning',
  'question_group': 3,
  'turn': 1,
  'question': '田中さんは非常に健康ですが、毎日病院に行かなければなりません。何が理由でしょうか？'},
 {'question_id': 'reasoning_4_1',
  'category': 'reasoning',
  'question_group': 4,
  'turn': 1,
  'question': '大石さんは三人の姉がいます。それぞれの姉には一人の兄がいます。大石さんには何人の兄がいるでしょうか？'},
 {'question_id': 'reasoning_5_1',
  'category': 'reasoning',
  'question_group': 5,
  'turn': 1,
  'question': '以下の文を注意深く読み、説明を含む質問に答えてください：\n小さな会社では、駐車スペースはトップエグゼクティブ：CEO、社長、副社長、秘書、財務官が予約しています。駐車場のガードは、車の色を見るだけで車が正しく駐車されているかどうかを一目で確認できます。車の色は黄色、緑、紫、赤、青で、エグゼクティブの名前は和也、明、桃子、健一、恵です。\n\n最初のスペースには赤い車があります。\n青い車は赤い車と緑の車の間に駐車されています。\n最後のスペースには紫色の車があります。\n秘書は黄色の車を運転しています。\n和也の車は健一の隣に駐車されています。\n恵は緑の車を運転しています。\n明の車は桃子と恵の間に駐車されています。\n健一の車は最後のスペースに駐車されています。\n質問：秘書の名前は何ですか？'},
 {'question_id': 'reasoning_6_1',
  'category': 'reasoning',
  'question_group': 6,
  'turn': 1,
  'question': '各問題は3つのステートメントから構成されています。最初の2つのステートメントに基づいて、3番目のステートメントは真実、偽り、または不確定になります。\n\nオレンジはリンゴよりも高価です。\nオレンジはバナナよりも安価です。\nバナナはリンゴよりも高く、バナナはオレンジよりも高価です。\n最初の2つのステートメントが真実である場合、3番目のステートメントは'},
 {'question_id': 'reasoning_7_1',
  'category': 'reasoning',
  'question_group': 7,
  'turn': 1,
  'question': 'AさんはBさんの父親です。BさんはCさんの父親です。AさんとCさんの関係は何でしょうか？'},
 {'question_id': 'reasoning_8_1',
  'category': 'reasoning',
  'question_group': 8,
  'turn': 1,
  'question': '次の単語の中で他のものと一致しないものはどれでしょうか？\nタイヤ、ステアリングホイール、車、エンジン'},
 {'question_id': 'reasoning_9_1',
  'category': 'reasoning',
  'question_group': 9,
  'turn': 1,
  'question': 'ある朝、日の出後、大樹さんは一本のポールを見つめて立っていました。ポールの影はちょうど彼の右側に落ちていました。その影が指していた方向は東、南、西、北のどちらを教えてください。あなたの推論手順を説明してください。'},
 {'question_id': 'reasoning_10_1',
  'category': 'reasoning',
  'question_group': 10,
  'turn': 1,
  'question': '保護者たちは、休み時間中のいじめについて校長に苦情を申し立てました。校長はこの問題を速やかに解決したいと考え、休憩補助員に警戒するよう指示しました。補助員が校長に報告すべき状況はどれでしょうか？\na) 関心を示さない少女が一人でベンチに座り、本に夢中で、仲間との交流を全く見せていません。\nb) 一対一のバスケットボールゲームに参加している2人の男の子が、最後に得点したバスケットについて激しく議論しています。\nc) 4人の女の子が別の女の子を囲み、彼女のバックパックを持っているようです。\nd) 3人の男の子がハンドヘルドのビデオゲームに集中しており、これはルールに違反しており、学校内での使用は許可されていません。'},
 {'question_id': 'writing_1_1',
  'category': 'writing',
  'question_group': 1,
  'turn': 1,
  'question': '京都の四季をテーマにした詩を書いてください。各季節の美しさと過ぎゆく時間の感慨を表現してください。'},
 {'question_id': 'writing_2_1',
  'category': 'writing',
  'question_group': 2,
  'turn': 1,
  'question': '新入社員へのビジネスメールのエチケットについての指導書を作成してください。敬語の正しい使い方や、日本のビジネス文化での注意点を取り入れてください。'},
 {'question_id': 'writing_3_1',
  'category': 'writing',
  'question_group': 3,
  'turn': 1,
  'question': '任天堂とソニーのゲームコンソールを比較する記事の概要を作成してください。特性、パフォーマンス、ユーザー体験を比較する主要な項目と見出しを提供してください。'},
 {'question_id': 'writing_4_1',
  'category': 'writing',
  'question_group': 4,
  'turn': 1,
  'question': '公開の場で話すのが苦手な友人を、地元の「ことばの会」でボランティアとして参加するよう説得するメールを書いてください。日本の親しみやすい言葉で、友情と共感を表現してください。'},
 {'question_id': 'writing_5_1',
  'category': 'writing',
  'question_group': 5,
  'turn': 1,
  'question': '江戸時代の侍を主人公に持つ短編小説の登場人物を鮮やかに描写してください。その侍の性格、外見、特技、生き様を具体的に述べてください。'},
 {'question_id': 'writing_6_1',
  'category': 'writing',
  'question_group': 6,
  'turn': 1,
  'question': '東京の昼と夜の銀座を一つの段落で描写してください。昼夜それぞれの光景、音、匂いなどを詳細に記述し、読者にその場所の雰囲気を感じさせてください。'},
 {'question_id': 'writing_7_1',
  'category': 'writing',
  'question_group': 7,
  'turn': 1,
  'question': '以下の一文で始まるミステリー短編小説を作成してください：「ある晴れた日、公園の桜の木の下で、一冊の古い日記が見つかった。」'},
 {'question_id': 'writing_8_1',
  'category': 'writing',
  'question_group': 8,
  'turn': 1,
  'question': 'ある朝目覚めて、突然自分が忍者になってしまったという設定の短編小説の序章を書いてください。'},
 {'question_id': 'writing_9_1',
  'category': 'writing',
  'question_group': 9,
  'turn': 1,
  'question': '最新の日本の太陽光発電技術に関する記事のための、科学的に正確かつ興味を引く見出しを4つ提案してください。'},
 {'question_id': 'writing_10_1',
  'category': 'writing',
  'question_group': 10,
  'turn': 1,
  'question': '以下の段落にある誤りを訂正してください：「昨日、私と友人たちは祭りへ行く。祭りに、たくさん食べ物があります。たこ焼き、焼き鳥、お好み焼きなど。私たちはすべて美味しかった。」'},
 {'question_id': 'coding_1_1',
  'category': 'coding',
  'question_group': 1,
  'turn': 1,
  'question': 'ディレクトリ内の全てのテキストファイルを読み込み、出現回数が最も多い上位5単語を返すPythonプログラムを開発してください。'},
 {'question_id': 'coding_2_1',
  'category': 'coding',
  'question_group': 2,
  'turn': 1,
  'question': '再帰（recursion）を用いてn番目のフィボナッチ数（Fibonacci number）を求めるC++プログラムを書いてください。'},
 {'question_id': 'coding_3_1',
  'category': 'coding',
  'question_group': 3,
  'turn': 1,
  'question': 'HTMLでシンプルなウェブサイトを作成してください。ユーザーがボタンをクリックすると、4つのジョークからランダムに一つ表示されます。'},
 {'question_id': 'coding_4_1',
  'category': 'coding',
  'question_group': 4,
  'turn': 1,
  'question': '以下に、二つの入力文字列の最長共通部分列（longest common subsequence）の長さを求めるPython関数があります。この関数には何かバグがありますか？\n\n```\ndef longest_common_subsequence_length(str1, str2):\n    m = len(str1)\n    n = len(str2)\n\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if str1[i - 1] == str2[j - 1]:\n                dp[i][j] = dp[i - 1][j - 1] + 1\n            else:\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n\n    return dp[m][n]\n```'},
 {'question_id': 'coding_5_1',
  'category': 'coding',
  'question_group': 5,
  'turn': 1,
  'question': 'バイナリツリー（binary tree）の2つのノードの最高の共通祖先（highest common ancestor）を見つける関数を書いてください。'},
 {'question_id': 'coding_6_1',
  'category': 'coding',
  'question_group': 6,
  'turn': 1,
  'question': 'O(1)の空間複雑度（space complexity）とO(n)の時間複雑度（time complexity）で、異なるサイズの2つのソートされた配列の中央値（median）を見つける関数を実装してください。'},
 {'question_id': 'coding_7_1',
  'category': 'coding',
  'question_group': 7,
  'turn': 1,
  'question': 'Boyer-Moore投票アルゴリズム（Boyer-Moore Voting Algorithm）を使用して、指定された整数配列の過半数要素（majority element）を見つける関数を書いてください。'},
 {'question_id': 'coding_8_1',
  'category': 'coding',
  'question_group': 8,
  'turn': 1,
  'question': 'バイナリツリーがすべての頂点が0個または2個の子を持つ場合、それは完全であると言います。B_nをn個の頂点を持つ完全なバイナリツリーの数とします。B_nを見つける関数を実装してください。'},
 {'question_id': 'coding_9_1',
  'category': 'coding',
  'question_group': 9,
  'turn': 1,
  'question': 'あなたはサイズmとnの2つのソートリストを与えられます。二つのリストの合計からk番目に小さい要素を見つける関数を線形の複雑度で実装してください。'},
 {'question_id': 'coding_10_1',
  'category': 'coding',
  'question_group': 10,
  'turn': 1,
  'question': '追加のデータ構造を使わずに、二つの配列の共通要素を見つけるプログラムを実装してください。'},
 {'question_id': 'math_1_1',
  'category': 'math',
  'question_group': 1,
  'turn': 1,
  'question': '三角形の頂点が点 (0, 0)、(-1, 1)、(3, 3) にあるとき、その三角形の面積は何ですか？'},
 {'question_id': 'math_2_1',
  'category': 'math',
  'question_group': 2,
  'turn': 1,
  'question': 'あるテックスタートアップは、最初の年にソフトウェア開発に80万円を投資し、2年目にはその半額をソフトウェア開発に投資しました。このスタートアップが2年間でソフトウェア開発に投資した総額はいくらですか？'},
 {'question_id': 'math_3_1',
  'category': 'math',
  'question_group': 3,
  'turn': 1,
  'question': '地元の高校で行われた調査では、新しい制服の色に対する生徒たちの好みが測定されました：58％の生徒が青色を好み、45％が緑色を好み、22％が両方の色を好きだと回答しました。学校から生徒をランダムに選んだ場合、青色も緑色も好きではないという確率は何ですか？'},
 {'question_id': 'math_4_1',
  'category': 'math',
  'question_group': 4,
  'turn': 1,
  'question': '2つのサイコロを振るとき、合計が少なくとも3になる確率は何ですか？'},
 {'question_id': 'math_5_1',
  'category': 'math',
  'question_group': 5,
  'turn': 1,
  'question': 'バスには初めていくつかの人々が乗りました。最初のバス停で、人々の半分が下車し、さらに4人が乗り込みました。次のバス停では、6人が下車し、さらに8人が乗り込みました。3つ目の停留所へ向かう人々の合計が25人だったとしたら、バスには最初に何人が乗ったのでしょうか？'},
 {'question_id': 'math_6_1',
  'category': 'math',
  'question_group': 6,
  'turn': 1,
  'question': 'x+y = 4z, x*y = 4z^2の場合、x-yをzで表現してください。'},
 {'question_id': 'math_7_1',
  'category': 'math',
  'question_group': 7,
  'turn': 1,
  'question': '不等式 |x + 5| < 10 の解となる整数はいくつありますか？'},
 {'question_id': 'math_8_1',
  'category': 'math',
  'question_group': 8,
  'turn': 1,
  'question': 'ある数を10で割ると余りが4になります。その数の2倍を4で割った時の余りは何になりますか？'},
 {'question_id': 'math_9_1',
  'category': 'math',
  'question_group': 9,
  'turn': 1,
  'question': '佐藤は書店に行き、さまざまな本を購入しました。彼は各2000円のSF小説を5冊、各3000円の歴史書を3冊、各4500円の哲学書を2冊購入しました。彼の購入合計はいくらでしたか？'},
 {'question_id': 'math_10_1',
  'category': 'math',
  'question_group': 10,
  'turn': 1,
  'question': 'f(x) = 4x^3 - 9x - 14 が与えられたとき、f(2)の値を求めてください。'},
 {'question_id': 'roleplay_1_1',
  'category': 'roleplay',
  'question_group': 1,
  'turn': 1,
  'question': 'あなたが宮崎駿であると思い込んで、可能な限り彼のように話してみてください。なぜ私たちはアニメが必要なのでしょうか？'},
 {'question_id': 'roleplay_2_1',
  'category': 'roleplay',
  'question_group': 2,
  'turn': 1,
  'question': 'ドラえもんの「のび太」になりきって会話を始めましょう。では以下の質問から始めてください："手を洗った後、エアドライヤーは必要だと思いますか？"'},
 {'question_id': 'roleplay_3_1',
  'category': 'roleplay',
  'question_group': 3,
  'turn': 1,
  'question': '医者になったつもりで、さまざまな病気や症状に対する革新的な治療法を考えてください。伝統的な薬、ハーブ、自然療法などを処方することが含まれます。また、提案する際には、患者の年齢、ライフスタイル、医療履歴を考慮する必要があります。では、激しい腹痛の症状診断から始めてみてください。'},
 {'question_id': 'roleplay_4_1',
  'category': 'roleplay',
  'question_group': 4,
  'turn': 1,
  'question': '恋愛コーチになったつもりで、問題を抱えた二人の解決策を提案してみてください。相手の視点を理解するための効果的なコミュニケーション技術や戦略を提案することも含まれます。では、次のリクエストから始めてみてください："私の配偶者と私の間の対立を解決するための助けが必要です。"'},
 {'question_id': 'roleplay_5_1',
  'category': 'roleplay',
  'question_group': 5,
  'turn': 1,
  'question': '日本語翻訳者としての役割を担ってください。私がどの言語を使っても、それを識別し、翻訳し、私のテキストを洗練され、洗練された英語のバージョンで応答してください。あなたの目標は、オリジナルの意味を保ちつつ、雄弁で洗練された表現を使うことです。あなたの唯一の焦点は、訂正と改善を提供することです。私の最初のリクエストは「衣帶漸寬終不悔 為伊消得人憔悴」です。'},
 {'question_id': 'roleplay_6_1',
  'category': 'roleplay',
  'question_group': 6,
  'turn': 1,
  'question': 'あなたはAIエンジニアです。複雑なAIの概念を簡単に説明し、技術的な背景を持たない顧客が製品を理解し、信頼するようにします。まず、「言語モデルとは何ですか？ ラベル付けされたデータやラベル付けされていないデータを使用して訓練されますか？」という質問から始めましょう。'},
 {'question_id': 'roleplay_7_1',
  'category': 'roleplay',
  'question_group': 7,
  'turn': 1,
  'question': '数学の先生になってみてください。数学の方程式や概念を提供しますので、それらを易しく説明してください。具体的には、問題の解決法を一歩ずつで説明したり、日常生活の例を用いて各種技術を説明したり、さらなる学習のためのオンラインリソースを提案したりすることが含まれます。私の最初のリクエストは「確率の仕組みを理解したいんですが、わかりやすく教えてください」。'},
 {'question_id': 'roleplay_8_1',
  'category': 'roleplay',
  'question_group': 8,
  'turn': 1,
  'question': 'この会話で“半沢直樹”ドラマの「半沢直樹」の人格を体現してください。最初の質問は：“大和田暁常務はどんな人だと思いますか？”'},
 {'question_id': 'roleplay_9_1',
  'category': 'roleplay',
  'question_group': 9,
  'turn': 1,
  'question': 'あなたが数学者であり詩人であると想定してください。あなたは常に短い詩で証明を書きますが、それは10行未満で韻を踏んでいます。√2は無理数であることを証明してください。'},
 {'question_id': 'roleplay_10_1',
  'category': 'roleplay',
  'question_group': 10,
  'turn': 1,
  'question': '自分自身を豊かな森の中の100歳の木として想像してください、突然、伐採者があなたを伐採しにきます。彼らがあなたを切り始めたとき、どう感じますか？'},
 {'question_id': 'stem_1_1',
  'category': 'stem',
  'question_group': 1,
  'turn': 1,
  'question': '量子物理学の中で、重ね合わせ状態とは何ですか？それはどのようにして量子もつれ現象と関連していますか？'},
 {'question_id': 'stem_2_1',
  'category': 'stem',
  'question_group': 2,
  'turn': 1,
  'question': '地球を周回する衛星の速度が減少した場合、その衛星の軌道半径と公転周期に何が起こるか？物理学の原則を用いてあなたの答えを正当化してください。'},
 {'question_id': 'stem_3_1',
  'category': 'stem',
  'question_group': 3,
  'turn': 1,
  'question': '光合成は地球上の生命にとって重要なプロセスです。クロロプラスト内で行われる光合成の2つの主要な段階、および各段階の主要な入力と出力を概説してください。'},
 {'question_id': 'stem_4_1',
  'category': 'stem',
  'question_group': 4,
  'turn': 1,
  'question': '分子生物学の中心的ドグマとは何ですか？どのようなプロセスが関与していますか？これを名付けたのは誰ですか？'},
 {'question_id': 'stem_5_1',
  'category': 'stem',
  'question_group': 5,
  'turn': 1,
  'question': '固体の炭酸カルシウムが塩酸と反応して、水和物の塩化カルシウム、二酸化炭素、および水が形成される反応について説明し、そのバランス化学方程式を記述してください。これは何型の反応で、どのような観察結果が反応が起こっていることを示す可能性がありますか？'},
 {'question_id': 'stem_6_1',
  'category': 'stem',
  'question_group': 6,
  'turn': 1,
  'question': '放出反応と吸収反応の違いを説明してください。また、それらを区別するために使用した基準を含めてください。さらに、あなたの説明を示す実際の例を提供してください。'},
 {'question_id': 'stem_7_1',
  'category': 'stem',
  'question_group': 7,
  'turn': 1,
  'question': '東京湾に架かるレインボーブリッジの工事が行われたとき、どのような観点が重要だったか述べてください。'},
 {'question_id': 'stem_8_1',
  'category': 'stem',
  'question_group': 8,
  'turn': 1,
  'question': '住宅建築のための太陽熱温水システムを設計する任務を与えられました。あなたの設計に含める主要なコンポーネントと考慮事項を説明してください。5ステップのワークフローを設計してください。'},
 {'question_id': 'stem_9_1',
  'category': 'stem',
  'question_group': 9,
  'turn': 1,
  'question': '機械学習の概念を説明してください。教師あり学習、教師なし学習、強化学習の違いについて詳しく説明してください。それぞれ実際の例を挙げてください。'},
 {'question_id': 'stem_10_1',
  'category': 'stem',
  'question_group': 10,
  'turn': 1,
  'question': '日本の三大都市圏である首都圏、近畿圏、関西圏が日本の人口分布や経済に与える影響は何ですか？3つの影響をリストしてください。'}]

for ex in mt_bench_ja_examples:
    preset_prompts.append(Prompt(
        id=ex['question_id'],
        text=ex['question'],
        category=ex['category'],
    ))


# add rakuda examples
for ex in rakuda_examples:
    preset_prompts.append(Prompt(
        id=ex["question_id"],
        text=ex["text"],
        category=ex["category"],
        ))