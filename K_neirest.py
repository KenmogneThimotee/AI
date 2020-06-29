def distance(x,y):
    import numpy as np
    assert x.shape[1] == y.shape[1]
    dist  = x - y
    dist = np.sqrt(dist)
    dist = np.sum(dist)
    dist = np.sqrt(dist)

    return dist

def majority_vote(labels):
    from collection import Counter
    vote_count = Counter(labels)
    winner , winner_count = vote_count.most_common(1)[0]
    num_winner = len([count for count in vote_count.values() if count == winner_count])

    if num_winner == 1:
        return winner
    else:
        majority_vote(labels[:-1])

def k_neirest_classify(data ,samples,labels ,k):
    import numpy as np
    #sort by distance the data
    samples = np.c_[samples,labels]
    by_distance = sorted(samples ,key=lambda d : distance(d,data))
    k_neirest = by_distance[:k,...]
    k_neirest = k_neirest[]



