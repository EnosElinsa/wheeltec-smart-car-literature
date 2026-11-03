from tools.textnorm import NormalizedText, normalize


def test_hyphenation_and_dashes():
    assert normalize("short-\nterm geometric") == normalize("short-term geometric")
    assert normalize("LiDAR\u2013inertial") == normalize("LiDAR-inertial")


def test_quotes_ligatures_and_markup():
    assert normalize("the robot\u2019s \ufb01lter") == normalize("the robot's filter")
    assert normalize("**bold** `code` $x$") == "bold code x"


def test_spacing_before_punctuation():
    assert normalize("error ( 6.2 % ) , low") == "error (6.2%), low"


def test_match_exact_fuzzy_missing():
    doc = NormalizedText(
        "While the method handles short-term geometric degeneracy, it fails when "
        "LiDAR returns are absent. Long-term inertial propagation still drifts."
    )
    assert doc.match("it fails when LiDAR returns are absent") == "exact"
    assert doc.match("While the method handles short-term geometric degeneracy, it fails when LiDAR "
                     "returns are missing.") == "fuzzy"
    assert doc.match("the robot never fails in any condition") == "missing"
    assert doc.match("") == "missing"
