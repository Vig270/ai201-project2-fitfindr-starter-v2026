"""
The runs your test needs. ← UNIT 4, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
the empty-search branch needs an impossible query. One about the fit card needs
the same item run more than once.

run_eval.py runs everything here five times and writes the run log — five
because your criteria are written out of five.
"""

SCENARIOS = [

    {
        # Criterion 1: matching query completes all three tools.
        "name": "matching query completes",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 1,
    },

    {
        # Criterion 2: impossible query stops before suggest_outfit.
        "name": "impossible query stops early",
        "query": "designer ballgown size XXS under $5",
        "wardrobe": "example",
        "criterion": 2,
    },

    {
        # Diagnostic: one of Unit 4's failure modes.
        "name": "empty wardrobe",
        "query": "denim jacket under $50",
        "wardrobe": "empty",
        "criterion": None,
    },

    {
        # Criterion 3: checks that selected_item matches the item
        # passed to suggest_outfit.
        "name": "selected item state",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 3,
    },

    {
        # Criterion 4: checks that the fit card contains the
        # matched item's name, price, and platform.
        "name": "fit card details",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 4,
    },

    {
        # Criterion 5: checks the maximum-price filter.
        "name": "maximum price filter",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 5,
    },
]

WARDROBES = ("example", "empty")


def validate() -> list[str]:
    """Complain about anything malformed, before a long run rather than during."""
    problems = []

    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("query", "").strip():
            problems.append(f"scenario {i} has no query")

        if scenario.get("wardrobe") not in WARDROBES:
            problems.append(
                f"scenario {i} has wardrobe {scenario.get('wardrobe')!r} — "
                f"it should be one of {WARDROBES}"
            )

    return problems