def substituter(seq, substitutions):
    for item in seq:
        if item in substitutions:
            yield substitutions[item]
        else:
            yield item

