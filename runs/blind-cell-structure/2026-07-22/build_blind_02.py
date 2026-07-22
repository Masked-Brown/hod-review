#!/usr/bin/env python3
"""build_blind_02.py — Deck B (constructed blind-test lesson): AQA 3.2.1.2
Prokaryotic cells and viruses. Mostly clean slides with two seeded flaws (B1, B2).
Imports the shared style module; does not re-implement layout. Do NOT edit
build/_deck_style.py. This build script is not committed.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))   # this run folder
sys.path.insert(0, HERE)  # _deck_style.py lives alongside this script
import _deck_style as ds

from pptx.enum.shapes import MSO_SHAPE

th = ds.build_theme("B", "AQA 3.2.1.2",
                    "AQA A-level Biology  -  3.2.1.2 Prokaryotic cells and viruses")
prs = ds.new_deck()

# 1. title_slide — CLEAN
ds.title_slide(
    prs, th,
    title="Prokaryotic cells and viruses",
    subtitle="Simpler cells, and the particles that are not cells at all",
    meta_lines=["Year 12 Biology  -  Lesson 2 of 6", "Class 12B  -  40 minutes"],
)

# 2. staff_slide — CLEAN
ds.staff_slide(
    prs, th,
    title="Lesson on a page",
    rows=[
        ("Teacher", "Miss A. Brown"),
        ("Class", "12B (24 students)"),
        ("Date", "Wednesday, period 4"),
        ("Unit", "3.2 Cells  -  lesson 2 of 6"),
        ("Prior learning", "Eukaryotic ultrastructure (last lesson)"),
    ],
    spec_points=[
        "3.2.1.2 Prokaryotic structure: simpler, smaller, no nucleus",
        "Features in ALL vs SOME prokaryotes (the list rule)",
        "Viruses as acellular and non-living; universal features",
    ],
    note="Reference: AQA A-level Biology 7402, section 3.2.1.",
)

# 3. donow_slide — CLEAN
ds.donow_slide(
    prs, th,
    title="Do Now",
    columns=[
        ("Last lesson", [
            "Name the site of aerobic respiration.",
            "What are ribosomes made of?",
        ]),
        ("Earlier this year", [
            "Define a monomer.",
            "Name the bond in a polysaccharide.",
        ]),
        ("Stretch", [
            "A bacterium has no nucleus.",
            "Where is its DNA, and how is it arranged?",
        ]),
    ],
    instruction="Five minutes, silent, closed book.",
)

# 4. objectives_slide — CLEAN
ds.objectives_slide(
    prs, th,
    tiers=[
        ("ALL", "State the features found in all prokaryotic cells.",
         "1-mark recall (AO1)"),
        ("MOST", "Explain why viruses are described as acellular and as non-living.",
         "2-mark Explain (AO1)"),
        ("SOME", "Explain why antibiotics have no effect on viruses.",
         "1-mark Give (AO1)"),
    ],
    footnote="The list rule decides the mark before the content does - be exact about "
             "ALL vs SOME.",
)

# 5. keywords_slide — CLEAN
ds.keywords_slide(
    prs, th,
    title="Key words",
    pairs=[
        ("Prokaryote", "A cell with no nucleus and no membrane-bound organelles."),
        ("Nucleoid", "The region holding a prokaryote's circular DNA."),
        ("Murein", "The polymer (peptidoglycan) of a bacterial cell wall."),
        ("Plasmid", "A small loop of extra DNA in some prokaryotes."),
        ("Capsid", "The protein coat around a virus."),
        ("Acellular", "Not made of cells."),
    ],
)

# 6. content_slide_bullets — CLEAN
ds.content_slide_bullets(
    prs, th,
    title="Prokaryotic cell structure",
    intro="Prokaryotic cells are smaller and simpler than eukaryotic cells.",
    bullets=[
        "No nucleus: the DNA is circular and not associated with histones, held in "
        "the nucleoid.",
        "No membrane-bound organelles.",
        "Smaller (70S) ribosomes.",
        "A cell wall made of murein (peptidoglycan).",
    ],
)

# 7. content_slide_bullets — CLEAN (list rule taught correctly, flagged)
ds.content_slide_bullets(
    prs, th,
    title="Features: all prokaryotes vs some",
    intro="In ALL prokaryotes:",
    bullets=[
        "Murein (peptidoglycan) cell wall",
        "Cell-surface membrane",
        "70S ribosomes",
        "Circular DNA, not associated with histones",
    ],
    side_title="In SOME only",
    side_bullets=["Capsule", "Plasmids", "Flagella", "Pili"],
    callout="Exam trap: adding one 'some only' feature to an 'all prokaryotes' answer "
            "loses the whole mark.",
)

# 8. table_slide — SEED B1 (murein/chitin SWAPPED)
ds.table_slide(
    prs, th,
    title="Cell walls across the kingdoms",
    headers=["Group", "Cell wall polymer"],
    rows=[
        ["Plant cells", "Cellulose"],
        ["Bacterial cells", "Chitin"],
        ["Fungal cells", "Murein"],
    ],
    caption="Learn the polymer for each group - they are frequently confused.",
    col_widths=[0.42, 0.58],
)

# 9. diagram_slide — CLEAN (prokaryotic cell)
def draw_cell(slide, th, area):
    x, y, w, h = area
    ds.diagram_node(slide, th, x + 0.4, y + 0.4, w - 0.8, h - 0.8, "",
                    th.accent_soft, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                    name="diag::cell")
    ds.diagram_node(slide, th, x + 0.75, y + 0.75, w - 1.5, 0.65, "Murein cell wall",
                    th.accent, name="diag::wall")
    ds.diagram_node(slide, th, x + w / 2 - 1.35, y + 2.0, 2.7, 0.9,
                    "Circular DNA (nucleoid)", th.accent_deep, name="diag::dna")
    ds.diagram_node(slide, th, x + 1.0, y + h - 1.5, 2.0, 0.65, "70S ribosomes",
                    th.accent, name="diag::ribo")
    ds.diagram_node(slide, th, x + w - 3.1, y + h - 1.5, 2.3, 0.65,
                    "Plasmid (some only)", th.accent_deep, name="diag::plasmid")

ds.diagram_slide(
    prs, th,
    title="Inside a prokaryotic cell",
    draw_fn=draw_cell,
    legend_entries=[
        (th.accent, "Cell wall / ribosomes"),
        (th.accent_deep, "DNA / plasmid"),
        (th.accent_soft, "Cytoplasm"),
    ],
    caption="Schematic; not to scale. Capsule, flagella and pili occur in some "
            "prokaryotes only.",
)

# 10. content_slide_bullets — SEED B2 (acellular AND non-living fused)
ds.content_slide_bullets(
    prs, th,
    title="Viruses",
    bullets=[
        "Viruses are acellular and non-living because they have no cytoplasm and "
        "cannot replicate outside a host cell.",
        "In all viruses: genetic material, a capsid (protein coat), and attachment "
        "proteins.",
        "In some only: a lipid envelope, reverse transcriptase, or tail fibres.",
    ],
)

# 11. content_slide_bullets — CLEAN (antibiotics)
ds.content_slide_bullets(
    prs, th,
    title="Why antibiotics do not work on viruses",
    bullets=[
        "Antibiotics target bacterial structures - the murein wall, 70S ribosomes, "
        "and metabolic enzymes.",
        "Viruses have none of these structures.",
        "So there is nothing for the antibiotic to act on.",
    ],
)

# 12. worked_example_slide — CLEAN
ds.worked_example_slide(
    prs, th,
    title="A 'features of all viruses' question",
    i_do=[
        "Question: give three features found in all viruses.",
        "All viruses have: genetic material, a capsid, and attachment proteins.",
        "I do NOT add lipid envelope or tail fibres - those are 'some only'.",
        "Adding one 'some only' feature would lose the mark (the list rule).",
    ],
    we_do=[
        "Now: give the features found in all prokaryotic cells.",
        "Sort each feature into ALL or SOME before you write it.",
        "We build the safe list together.",
    ],
    note="The list rule: one non-universal item collapses the whole answer to zero.",
)

# 13. plenary_slide — CLEAN
ds.plenary_slide(
    prs, th,
    title="Plenary",
    question="Why is a virus classified as acellular?",
    options=[
        ("A", "Because it cannot replicate outside a host cell."),
        ("B", "Because it has no metabolism of its own."),
        ("C", "Because it is not made of cells - it has no cell-surface membrane or "
              "cytoplasm."),
        ("D", "Because it is smaller than a bacterium."),
    ],
    confidence=True,
)

out = os.path.join(HERE, "blind-lesson-02-prokaryotic-viruses.pptx")
prs.save(out)
problems = ds.qa_geometry(prs)
print("SLIDES", len(prs.slides), "QA", len(problems))
[print(" -", p) for p in problems]
