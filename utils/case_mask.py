class CaseMask:
    @staticmethod
    def get_uppercase_mask(text):
        mask = ""
        for i in text:
            if i.isupper():
                 mask += "1"
            else:
                 mask += "0"

        return mask

    @staticmethod
    def use_uppercase_mask(text : str, mask : str):
        result = ""
        for i in range(len(text)):
            if mask[i] == "1":
                result += text[i].upper()
            else:
                result += text[i].lower()
        return result
