from set import Set

def test_set():
    test_set = Set()

    test_set.add(1)
    test_set.add(2)
    test_set.add(3)

    assert test_set.contains(1) == True
    assert test_set.contains(4) == False
    assert test_set.length() == 3

    test_set.remove(2)
    test_set.remove(3)

    assert test_set.contains(2) == False
    assert test_set.length() == 1

    test_set.add(2)
    test_set.add(3)

    set_two = Set()

    set_two.add(2)
    set_two.add(6)
    set_two.add(7)
    set_two.add(1)
    set_two.add(0)
    set_two.add(3)

    assert set_two.intersect(test_set).contains(1) == True
    assert set_two.intersect(test_set).contains(7) == False

    assert test_set.is_subset(set_two) == True

