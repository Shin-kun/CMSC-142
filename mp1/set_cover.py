def set_cover(universe, universe_subset):
    sets = set(element for universe_set in universe_subset for element in universe_set)
    if sets != universe:
        return 
    
    covered = set()
    cover = []

    while covered != sets:
        subset = max(universe_subset, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    
    return cover


universe = {1,2,3,4,5,6,7,8}
subset = [[1,2],[7,8],[2,3,4,5,6,7],[1,2,3,4],[5,6,7,8],[5,6,7]]
# universe_subset = set(map(frozenset, subset))
universe_subset = [
    set([1,2]),
    set([7,8]),
    set([2,3,4,5,6,7]),
    set([1,2,3,4]),
    set([5,6,7,8]),
    set([5,6,7])]

new_set = set_cover(universe, universe_subset)
print(new_set)