from abc import ABC, abstractmethod

class Metrics(ABC):
    @abstractmethod
    def __call__(self, REC:list[int], REL:list[int]) -> float:pass

class Recall(Metrics):
    def __call__(self, REC:list[int], REL:list[int]) -> float:
        rec = set(REC)
        rel = set(REL)
        rr = rec.intersection(rel)
        return len(rr)/len(rel)

class Precission(Metrics):
    def __call__(self, REC:list[int], REL:list[int]) -> float:
        rec = set(REC)
        rel = set(REL)
        rr = rec.intersection(rel)
        return len(rr)/len(rec)

class FMean(Metrics):
    def __call__(self, REC:list[int], REL:list[int], beta:float = 0.7) -> float:
        R = Recall()(REC,REL)
        P = Precission()(REC,REL)
        return (1 + beta**2)/((1/P) + (beta**2/R)) if P != 0 and R != 0 else 0

class F1Mean(Metrics):
    def __call__(self, REC:list[int], REL:list[int]) -> float:
        R = Recall()(REC,REL)
        P = Precission()(REC,REL)
        return 2/((1/P) + (1/R)) if P != 0 and R != 0 else 0
