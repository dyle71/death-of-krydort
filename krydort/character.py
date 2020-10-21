# ------------------------------------------------------------
# krydort/character.py
#
# This is a Witcher 3 TRPG character.
#
# This file is part of krydort.
#
# (C) Copyright 2020
# Oliver Maurhart, oliver.maurhart@headcode.space
# headcode.space e.U., https://www.headcode.space
# ------------------------------------------------------------

"""This module represents a character in Witcher 3 Tabletop RPG."""

import json


class Attributes(object):
    """The attributes of a character."""
    
    def __init__(self):
        self.set(INT=0, REF=0, DEX=0, BODY=0, SPD=0, EMP=0, CRA=0, WILL=0, LUCK=0)
    
    def __str__(self):
        """Stringify this object"""
        return json.dumps(self.debug_dict())
    
    def debug_dict(self):
        """Turn this object to a dictionary for debug purpose."""
        return {'INT': self.INT, 'REF': self.REF, 'DEX': self.DEX, 'BODY': self.BODY, 'SPD': self.SPD, 'EMP': self.EMP,
                'CRA': self.CRA, 'WILL': self.WILL, 'LUCK': self.LUCK}
    
    @property
    def names(self) -> [str]:
        """Return list of valid attribute names."""
        return ['INT', 'REF', 'DEX', 'BODY', 'SPD', 'EMP', 'CRA', 'WILL', 'LUCK']
    
    def set(self, **kwargs) -> None:
        """Sets attributes at once."""
        for kw in kwargs:
            if kw in self.names and isinstance(kwargs[kw], int):
                self.__setattr__(kw, int(kwargs[kw]))


class Skills(object):
    
    """Skill set of a specific attribute."""

    skill_map = {
        'Awareness': 'INT', 'Business': 'INT', 'Deduction': 'INT', 'Education': 'INT', 'CommonSpeech': 'INT',
        'ElderSpeech': 'INT', 'Dwarven': 'INT', 'MonsterLore': 'INT', 'SocialEtiquette': 'INT',
        'Streetwise': 'INT', 'Tactics': 'INT', 'Teaching': 'INT', 'WildernessSurvival': 'INT',
    
        'Brawling': 'REF', 'DodgingEscape': 'REF', 'Melee': 'REF', 'Riding': 'REF', 'Sailing': 'REF',
        'SmallBlades': 'REF', 'StaffSpear': 'REF', 'Swordsmanship': 'REF',
    
        'Archery': 'DEX', 'Athletics': 'DEX', 'Crossbow': 'DEX', 'SleightOfHand': 'DEX', 'Stealth': 'DEX',
    
        'Physique': 'BODY', 'Endurance': 'BODY',
    
        'Charisma': 'EMP', 'Deceit': 'EMP', 'FineArts': 'EMP', 'Gambling': 'EMP', 'GroomingAndStyle': 'EMP',
        'HumanPerception': 'EMP', 'Leadership': 'EMP', 'Persuasion': 'EMP', 'Performance': 'EMP',
        'Seduction': 'EMP',
    
        'Alchemy': 'CRA', 'Crafting': 'CRA', 'Disguise': 'CRA', 'FirstAid': 'CRA', 'Forgery': 'CRA',
        'PickLock': 'CRA', 'TrapCrafting': 'CRA',
    
        'Courage': 'WILL', 'HexWeaving': 'WILL', 'Intimidation': 'WILL', 'SpellCasting': 'WILL',
        'ResistMagic': 'WILL', 'ResistCoercion': 'WILL', 'RitualCrafting': 'WILL'
    }

    def __init__(self, attribute: str, names: [str]):
        self._attribute = attribute
        self._names = names
        for n in self.names:
            self.__setattr__(n, 0)
    
    def __str__(self):
        """Stringify this object"""
        return json.dumps(self.debug_dict())
    
    def debug_dict(self):
        """Turn this object to a dictionary for debug purpose."""
        skills = {}
        for n in self.names:
            skills[n] = int(getattr(self, n))
        return {'attribute': self.attribute, 'skills': skills}
    
    @property
    def attribute(self) -> str:
        return self._attribute
    
    @property
    def names(self) -> [str]:
        return self._names
    
    @classmethod
    def skills_by_attribute(cls, attribute: str) -> [str]:
        """Returns all known skills by an attribute name."""
        return [skill for skill in cls.skill_map.keys() if cls.skill_map[skill] == attribute]

    def set(self, **kwargs) -> None:
        """Sets skills at once."""
        for kw in kwargs:
            if kw in self.names and isinstance(kwargs[kw], int):
                self.__setattr__(kw, int(kwargs[kw]))


class Character(object):
    """This is a Witcher 3 Tabletop RPG character."""
    
    def __init__(self, name: str = '<unnamed>'):
        """Create a character."""
        self._name = name
        self._attributes = Attributes()
        self._skills = {}
        for a in self._attributes.names:
            self._skills[a] = Skills(a, Skills.skills_by_attribute(a))
            
    def __str__(self):
        """Stringify this object."""
        return json.dumps(self.debug_dict())
    
    def debug_dict(self):
        """Turn this object to a dictionary for debug purpose."""
        skills_dict = {}
        for s in self.skills:
            skills_dict[s] = self.skills[s].debug_dict()
        return {'name': self.name, 'attributes': self.attributes.debug_dict(), 'skills': skills_dict}

    @property
    def name(self):
        return self._name
    
    @property
    def attributes(self):
        return self._attributes
    
    @property
    def skills(self):
        return self._skills

    def values(self, name: str) -> (int, int):
        """Returns first the attribute and then the skill value of the skill by the given name."""
        pass
