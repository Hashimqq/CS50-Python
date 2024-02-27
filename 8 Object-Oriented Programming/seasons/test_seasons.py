from Py8.seasons.seasons import season




def test_seasons():
    assert season(1999,1,1) == "Thirteen million, forty-six thousand, four hundred minutes"

    assert season(1,1,1999) == "Invalid date"
