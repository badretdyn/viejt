from models.syllable_model import Syllable
from models.app_config import AppConfig

class SyllableValidator:
    def __init__(self, phoneme_inventory, restrictions, app_config = None):
        self.phoneme_inventory = phoneme_inventory

        for restriction in restrictions:
            if restriction.get("mode") not in ("and", "or"):
                restriction["mode"] = "and"
        
        self.restrictions = restrictions
        self.app_config = app_config or AppConfig()

    def is_valid(self, syl : Syllable):
        
        if self.app_config: print(f"syva\tsyl={syl}")

        if syl.initial and syl.initial not in self.phoneme_inventory.initials:
            if self.app_config: print("syva\trt=fl, initial does not exist")
            return False
        if syl.medial and syl.medial not in self.phoneme_inventory.medials:
            if self.app_config: print("syva\trt=fl, medial does not exist")
            return False
        if syl.nucleus and syl.nucleus not in self.phoneme_inventory.nuclei:
            if self.app_config: print("syva\trt=fl, nucleus does not exist")
            return False
        if syl.coda and syl.coda not in self.phoneme_inventory.codas:
            if self.app_config: print("syva\trt=fl, coda does not exist")
            return False

        if self.restrictions == []:
            if self.app_config: print("syva\trt=tr, there are no restrictons")
            return True

        for restriction in self.restrictions:

            if self.app_config: print(f"syva\tfr rstr={restriction}, mode={restriction.get("mode")}")
            
            inInitials = syl.initial in (restriction.get("initials") or [])
            inMedials = syl.medial in (restriction.get("medials") or [])
            inNuclei = syl.nucleus in (restriction.get("nuclei") or [])
            inCodas = syl.coda in (restriction.get("codas") or [])
            
            true_count = sum([inInitials, inMedials, inNuclei, inCodas])

            specified_parts = 0
            if restriction.get("initials") is not None:
                specified_parts += 1
            if restriction.get("medials") is not None:
                specified_parts += 1
            if restriction.get("nuclei") is not None:
                specified_parts += 1
            if restriction.get("codas") is not None:
                specified_parts += 1

            if self.app_config: print(f"syva\t\tcmpnts=[{inInitials}, {inMedials}, {inNuclei}, {inCodas}]")
            
            mode = restriction.get("mode")

            match mode:
                case "and":
                    if self.app_config: print("syva\t\trstr=and")
                    if true_count == specified_parts and specified_parts > 0:
                        if self.app_config: print("syva\t\trt=fl")
                        return False
                case "or": # need to think about this mode
                    if self.app_config: print("syva\t\trstr=or")
                    if true_count > 0:
                        if self.app_config: print("syva\t\trt=fl")
                        return False

        if self.app_config: print("syva\trt=tr")
        return True

    def dump(self, separator = " "):
        return f"SyllableValidator {{ phoneme_inventory:{self.phoneme_inventory!r},{separator}restrictions:{self.restrictions},{separator}debug_mode:{self.app_config.debug_mode!r} }}"

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return f"SyllableValidator(app_config={self.app_config!r})"