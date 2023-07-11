import Levenshtein
import jieba

def calculate_similarity(text1, text2):
    # 使用jieba分词将文本拆分为单词
    words1 = jieba.lcut(text1)
    words2 = jieba.lcut(text2)

    # 将单词列表转换为字符串
    text1 = ' '.join(words1)
    text2 = ' '.join(words2)

    # 计算Levenshtein距离
    distance = Levenshtein.distance(text1, text2)

    # 计算文本长度的最大值
    max_length = max(len(text1), len(text2))

    # 计算重复度
    similarity = 1 - (distance / max_length)
    return similarity

# 示例用法
text1 = "清晨的阳光洒在湖面上，波光粼粼。花开如海，绽放着绚丽的色彩。小鸟在枝头欢快地歌唱，音符飘荡在空气中。微风拂过，带来一丝清凉。这是一个宁静而美丽的早晨，大自然的礼物让人心怀感激。"
text2 = "繁华的都市街头车水马龙，人们匆忙地走过拥挤的人行道。高楼大厦耸立，玻璃窗上倒映出繁忙的城市生活。街头摊贩散发着诱人的香气，吸引着路人品尝美食。城市充满着生命的脉动，多样的文化交织成交响乐。从街头艺人的表演到咖啡馆里的笑声，这是一个追逐梦想、无限可能的地方。"

similarity_score = calculate_similarity(text1, text2)
print(f"Similarity score: {similarity_score}")