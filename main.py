from models.syllable_model import Syllable
from utils.grapheme_extractor import *
from utils.latin_finder import *
from utils.syllable_validator import *

if __name__ == "__main__":
    text = "_duoi_nganh_nghiao_nguyen_oang_mưá_a_ba"
    text2 = """Xin chào! Tôi tên là Nguyễn Văn A. 
Hôm nay, tôi học tiếng Việt tại Hà Nội.
Cô giáo nói: "Các em hãy đọc bài tập 1, 2, 3 nhé!"
Em ơi, cho tôi hỏi: "Thế nào là yêu thương?"
Không có gì quý hơn độc lập tự do.
TRƯỜNG HỌC MỚI ĐƯỢC XÂY DỰNG.
Ông ấy làm việc tại ngân hàng Vietcombank.
Mẹ bảo: "Con hãy ăn cơm đi!"
Buổi sáng, tôi uống một cốc sữa đậu nành."""
    print(text)
    syls = SyllableValidator.extract_syllables(text2)
    print(*syls, sep='\n')