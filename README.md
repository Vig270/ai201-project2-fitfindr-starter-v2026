# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.

     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

FitFindr lets a user search for clothing listings using a description and optional size or maximum-price filters. It finds matching items from the listings data and selects the best match. FitFindr can then suggest outfits using the selected item and pieces from the user's wardrobe. Finally, it creates a short social-media-style fit card describing the clothing find and its outfit.

---

## Tool Inventory

### `search_listings`

* **What it does:** Searches the listings data for items matching a description, with optional size and maximum-price filters.
* **Inputs:** `description` (str), `size` (str | None), `max_price` (float | None).
* **Returns:** A list of matching listing dictionaries, each containing `id`, `title`, `description`, `category`, `style_tags`, `size`, `condition`, `price`, `colors`, `brand`, and `platform`, ordered by best match first and limited to the configured result limit.
* **No matches:** Returns an empty list `[]`. Size matching is case-insensitive and treats the requested size as a distinct size component rather than an arbitrary substring.

### `suggest_outfit`

* **What it does:** Suggests one or two outfits using a new listing and the user's wardrobe.
* **Inputs:** `new_item` (dict), `wardrobe` (dict).
* **Returns:** A non-empty string containing outfit suggestions, using pieces from the user's wardrobe when available.
* **Empty wardrobe:** Returns general styling advice for the new item instead of an empty string or an error.

### `create_fit_card`

* **What it does:** Creates a short social-media-style caption about the new clothing find and its suggested outfit.
* **Inputs:** `outfit` (str), `new_item` (dict).
* **Returns:** A 2–4 sentence string that mentions the item, its price, its platform, and the outfit's vibe, mentioning the price and platform once each.
* **Empty outfit:** Returns a descriptive message instead of raising an error.

### Branch Rule

If `search_listings` returns an empty list, put a message in the session and stop. Otherwise, take the first result and pass it to `suggest_outfit`.

---

## Planning Loop

Branch rule: If search_listings returns an empty list, put a message in session["error"] explaining what the user could change, then return the session without calling suggest_outfit. Otherwise, select the first search result and continue to the outfit step.

Where it lives: agent.py::run_agent

How the query is parsed: The query will be parsed using simple string processing to extract the description, optional size, and optional maximum price. The parsed values are stored in session["parsed"].

What moves through the session: The session stores the original query, parsed search values, search results, selected item, wardrobe, outfit suggestion, fit card, and any error message. Each step reads from the session and saves its result back into the session.

---

## Sample Run

**One full query**

```text
$ python app.py ask '...'
```

**The three tools, tested one at a time**

**`search_listings`**

```text
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))" [{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_012', 'title': 'Oversized Crewneck Sweatshirt — Vintage Navy', 'description': 'Perfectly faded navy crewneck. Genuinely vintage — not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.', 'category': 'tops', 'style_tags': ['vintage', 'basics', 'oversized', 'classic'], 'size': 'XL (fits oversized)', 'condition': 'good', 'price': 20.0, 'colors': ['navy'], 'brand': None, 'platform': 'thredUp'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]
```

**`suggest_outfit`**

```text
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

Here are two outfit suggestions featuring your new Vintage Levi's 501 Jeans and pieces from your wardrobe:

### Outfit 1: Classic Casual Minimal
* **Vibe:** Effortless, everyday cool with a vintage touch.
* **How to style:** Tuck the **white ribbed tank top** into the **Vintage Levi's 501 Jeans**, and cinch the waist with the **brown leather belt**. Throw on the **chunky white sneakers** for a fresh, casual finish, and carry your essentials in the **black crossbody bag**.

### Outfit 2: Streetwear Layered
* **Vibe:** Relaxed, textured streetwear utilizing contrasting tones and layers.
* **How to style:** Layer the **black cropped zip hoodie** over the **white ribbed tank top**, paired with the **Vintage Levi's 501 Jeans** and the **brown leather belt**. Complete the look with the **black combat boots** for a slightly grungier edge and top it off with the **vintage black denim jacket**.
```

**`create_fit_card`**

```text
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Scored these classic vintage Levi's 501 jeans in the best medium wash for just $38! They’ve got that ultimate effortless vibe, especially when paired with crisp white sneakers for an easy, everyday look. Grab them now over on my Depop before they're gone!
```

---

## How I Used AI

**Moment 1**

* **What I asked for:** I asked AI to help me implement the `search_listings` tool based on the project requirements.
* **What came back:** The suggested implementation loaded the listings, filtered by maximum price and size, calculated keyword overlap, sorted the matches, and returned the configured number of results.
* **What I changed:** I used the implementation and tested it with a normal search and an impossible search to make sure it returned `[]` when there were no matches.

**Moment 2**

* **What I asked for:** I asked AI to help implement the `suggest_outfit` and `create_fit_card` tools while following their required return formats and empty-case behavior.
* **What came back:** The implementation used the `generate()` model adapter, created separate prompts for normal and empty wardrobe cases, and returned a descriptive message for an empty outfit.
* **What I changed:** I tested both normal and empty cases for each tool and checked the repeated fit-card output against the project's cache and temperature settings.

---

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════
     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.
     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |       |       |         |
| 2.        |        |       |       |       |       |       |         |
| 3.        |        |       |       |       |       |       |         |
| 4.        |        |       |       |       |       |       |         |
| 5.        |        |       |       |       |       |       |         |

**Real output from one try**, pasted as text, naming the file and function that produced it:

```text
```

---

## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
| - | --------- | ------ | ------- | ------------- |
| 1 |           |        |         |               |
| 2 |           |        |         |               |
| 3 |           |        |         |               |
| 4 |           |        |         |               |
| 5 |           |        |         |               |

**Diagnoses**

---

## Loop Trace

**Happy path**

```text
```

**Empty search**

```text
```

**On the MCP move:**

---

## The Improvement

**What I changed:**

**Which failure it was meant to fix:**

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |       |       |         |
| 2.        |        |       |       |       |       |       |         |
| 3.        |        |       |       |       |       |       |         |
| 4.        |        |       |       |       |       |       |         |
| 5.        |        |       |       |       |       |       |         |

**Did it help, and how do I know:**

---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->

<!-- ═════════════════════════════════════════════════════════════════════
     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
