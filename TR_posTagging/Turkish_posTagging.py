# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:16:21 2020

@author: Asile
"""

from os.path import join
from typing import List

from jpype import JClass, getDefaultJVMPath, java, shutdownJVM, startJVM

ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')
startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')

morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

dictionary = {
    "aç-Verb": "Açmak fiilinin emri hali.",
    "aç-Noun": "Yemek yememiş kimse."   
}

def POS(pos, analysis):
    for i, analysis in enumerate(analysis, start=1):
        pos.append(
            f'{str(analysis.getLemmas()[0])}'
            f'-{analysis.getPos().shortForm}'
        )
    return pos

def printSolution(pos):
    if("aç-Verb" in pos):
        print(dictionary["aç-Verb"])
    elif("aç-Noun" in pos):
        print(dictionary["aç-Noun"])
        
sentence: str = 'Kapıyı tanımadığın kişilere açma lütfen!' 
sentence2: str = 'Sabah kahvaltısı yapamadım çok aç geldim'


analysis: java.util.ArrayList = (
        morphology.analyzeAndDisambiguate(sentence).bestAnalysis()
    )

analysis2: java.util.ArrayList = (
        morphology.analyzeAndDisambiguate(sentence2).bestAnalysis()
    )

print("\n\n")
pos: List[str] = []
print(POS(pos, analysis),"\n\n")
pos2: List[str] = []
print(POS(pos2, analysis2), "\n\n\n")


printSolution(pos)
print("\n")

printSolution(pos2)



shutdownJVM()













