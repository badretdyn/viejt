from models.language_model import *

if __name__ == "__main__":
#     text = "_duoi_nganh_nghiao_nguyen_oang_mưá_a_ba"
#     text2 = """Xin chào! Tôi tên là Nguyễn Văn A. 
# Hôm nay, tôi học tiếng Việt tại Hà Nội.
# Cô giáo nói: "Các em hãy đọc bài tập 1, 2, 3 nhé!"
# Em ơi, cho tôi hỏi: "Thế nào là yêu thương?"
# Không có gì quý hơn độc lập tự do.
# TRƯỜNG HỌC MỚI ĐƯỢC XÂY DỰNG.
# Ông ấy làm việc tại ngân hàng Vietcombank.
# Mẹ bảo: "Con hãy ăn cơm đi!"
# Buổi sáng, tôi uống một cốc sữa đậu nành."""
#     print(text)
#     syls = SyllableValidator.extract_syllables(text2)
#     print(*syls, sep='\n')
    lang : Language = Language.from_json_file("data\\zh.json")
    # for i in range(0, 10):
    #     print(viet.random_syl())

    lang.debug_mode = True

    syls = [
        # Syllable("w", "u", "a", "n"),
        # Syllable("w", "u", "u", "n"),
        # Syllable("", "u", "u", ""),
        # Syllable("", "", "", ""),
        # Syllable("", "", "u", ""),
        # Syllable("", "u", "", ""),
        # Syllable("x", "i", "", ""),
        # Syllable("x", "u", "", ""),
        # Syllable("x", "", "u", ""),
        # Syllable("x", "i", "a", ""),
        # Syllable("x", "", "i", ""),
        # Syllable("x", "u", "i", ""),
        # Syllable("x", "", "a", ""),
        # Syllable("x", "", "u", ""),
        # Syllable("x", "", "ü", ""),
        Syllable("q", "a", "u", ""),
        Syllable("q", "u", "a", ""),
        # Syllable("q", "", "a", ""),
        # Syllable("q", "i", "a", ""),
    ]

    for i in syls:
        print(f"{i}\t{lang.is_valid_syllable(i)}")