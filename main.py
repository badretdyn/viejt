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
    lang : Language = Language.from_json_file("data\\zh_syl.json")
    # for i in range(0, 10):
    #     print(viet.random_syl())

    lang.is_valid_syllable(Syllable("w", "u", "a", "n"))
    lang.is_valid_syllable(Syllable("w", "u", "u", "n"))
    lang.is_valid_syllable(Syllable("", "u", "u", ""))
    lang.is_valid_syllable(Syllable("", "", "", ""))
    lang.is_valid_syllable(Syllable("", "", "u", ""))
    lang.is_valid_syllable(Syllable("", "u", "", ""))
    lang.is_valid_syllable(Syllable("x", "i", "", ""))
    lang.is_valid_syllable(Syllable("x", "u", "", ""))
    lang.is_valid_syllable(Syllable("x", "", "u", ""))
    lang.is_valid_syllable(Syllable("x", "i", "a", ""))
    lang.is_valid_syllable(Syllable("x", "", "i", ""))
    lang.is_valid_syllable(Syllable("x", "u", "i", ""))
    lang.is_valid_syllable(Syllable("x", "", "a", ""))
    lang.is_valid_syllable(Syllable("x", "", "u", ""))
    lang.is_valid_syllable(Syllable("x", "", "ü", ""))
