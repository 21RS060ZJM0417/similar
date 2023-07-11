import Levenshtein

def calculate_similarity(text1, text2):
    # 将文本转换为小写
    text1 = text1.lower()
    text2 = text2.lower()

    # 计算Levenshtein距离
    distance = Levenshtein.distance(text1, text2)

    # 计算文本长度的最大值
    max_length = max(len(text1), len(text2))

    # 计算重复度
    similarity = 1 - (distance / max_length)
    return similarity

# 示例用法
text1 = "The morning sun cast a golden glow over the peaceful meadow. Birds chirped happily as they flitted from branch to branch, filling the air with their melodious songs. The gentle breeze rustled the leaves, creating a soothing symphony. A group of children played and laughed, their joy echoing through the open space. The flowers bloomed in vibrant colors, painting a picturesque scene. It was a moment of serenity and beauty, where nature and tranquility embraced each other in perfect harmony"
text2 = "The bustling city streets were alive with energy and excitement. Cars honked their horns, and people hurriedly walked along the crowded sidewalks. Skyscrapers towered above, their windows reflecting the vibrant city life below. Street vendors offered an array of delicious smells, tempting passersby with their culinary delights. The city pulsated with the rhythm of life, a symphony of diversity and culture. From the street performers entertaining the crowds to the laughter echoing from cafes, it was a place where dreams were chased, and possibilities seemed endless."

similarity_score = calculate_similarity(text1, text2)
print(f"Similarity score: {similarity_score}")