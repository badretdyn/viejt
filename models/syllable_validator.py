from models.syllable_model import Syllable
from models.app_config import AppConfig

class SyllableValidator:
    def __init__(self, phoneme_inventory, restrictions, app_config):
        self.phoneme_inventory = phoneme_inventory

        for restriction in restrictions:
            if restriction.get("mode") not in ("and", "or"):
                restriction["mode"] = "and"
        
        self.restrictions = restrictions
        self.app_config = app_config or AppConfig()

    def is_valid(self, syl : Syllable):
        
        print(f"syl\t{syl}") if self.app_config.debug_mode else False

        if syl.initial and syl.initial not in self.phoneme_inventory.initials:
            print(f"\texit fl\t\tinitial does not exist") if self.app_config.debug_mode else False
            return False
        if syl.medial and syl.medial not in self.phoneme_inventory.medials:
            print(f"\texit fl\t\tmedial does not exist") if self.app_config.debug_mode else False
            return False
        if syl.nucleus and syl.nucleus not in self.phoneme_inventory.nuclei:
            print(f"\texit fl\t\tnucleus does not exist") if self.app_config.debug_mode else False
            return False
        if syl.coda and syl.coda not in self.phoneme_inventory.codas:
            print(f"\texit fl\t\tcoda does not exist") if self.app_config.debug_mode else False
            return False

        if self.restrictions == []:
            print("\texit tr\t\tthere are no restrictons") if self.app_config.debug_mode else False
            return True

        for restriction in self.restrictions:

            print(f"\trestr\t\t{restriction}\n\tmode\t{restriction.get("mode")}") if self.app_config.debug_mode else False
            
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

            print(f"\tcmpnts\t\t{inInitials} {inMedials} {inNuclei} {inCodas}")  if self.app_config.debug_mode else False
            
            mode = restriction.get("mode")

            match mode:
                case "and":
                    print("\trestriction is and") if self.app_config.debug_mode else False
                    if true_count == specified_parts and specified_parts > 0:
                        print("\texit fl") if self.app_config.debug_mode else False
                        return False
                case "or": # need to think about this mode
                    print("\trestriction is or") if self.app_config.debug_mode else False
                    if true_count > 0:
                        print("\texit fl") if self.app_config.debug_mode else False
                        return False
            
        return True

    def __str__(self, separator = " "):
        return f"SyllableValidator {{ phoneme_inventory:{self.phoneme_inventory!r},{separator}restrictions:{self.restrictions},{separator}debug_mode:{self.app_config.debug_mode!r} }}"

    def __repr__(self):
        return self.__str__()