from .truth import Truth

truth: Truth = Truth("(X | Y) & (Y == Z) & !W")
print(str(truth))
