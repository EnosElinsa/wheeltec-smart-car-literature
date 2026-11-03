from tools import vocab
from tools.common import REPO_ROOT


def test_every_controlled_value_is_documented():
    text = (REPO_ROOT / "06-data" / "vocabulary.md").read_text(encoding="utf-8")
    missing = [v for v in vocab.ALL_CONTROLLED_VALUES if f"`{v}`" not in text]
    assert missing == []


def test_every_coding_field_is_documented():
    text = (REPO_ROOT / "06-data" / "vocabulary.md").read_text(encoding="utf-8")
    missing = [f for f in vocab.CODING_FIELDS if f"`{f}`" not in text]
    assert missing == []


def test_template_lists_every_coding_field():
    text = (REPO_ROOT / "03-reviews" / "TEMPLATE.md").read_text(encoding="utf-8")
    missing = [f for f in vocab.CODING_FIELDS if f"- {f}:" not in text]
    assert missing == []
