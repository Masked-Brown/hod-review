#!/usr/bin/env python3
"""build_blind_01.py — Deck A (blind-01): AQA 3.2.1.1 Eukaryotic cell structure.

CONSTRUCTED stress-test lesson: 14 slides, mostly clean, four deliberately seeded
flaws (A1..A4). Uses ONLY the shared style module build/_deck_style.py. This script
plants seeded text verbatim; it adds no speaker notes or flaw-revealing annotations.
"""

import os
import sys

from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))   # this run folder
sys.path.insert(0, HERE)  # _deck_style.py lives alongside this script
import _deck_style as ds

th = ds.build_theme("A", "AQA 3.2.1.1",
                    "AQA A-level Biology  ·  3.2.1.1 Eukaryotic cell structure")
prs = ds.new_deck()

# 1. title_slide -- CLEAN
ds.title_slide(
    prs, th,
    title="Eukaryotic cell structure",
    subtitle="Ultrastructure and the structure-function link",
    meta_lines=["Year 12 Biology  -  Lesson 1 of 6", "Class 12B  -  40 minutes"],
)

# 2. staff_slide -- CLEAN
ds.staff_slide(
    prs, th,
    title="Lesson on a page",
    rows=[
        ("Teacher", "Miss A. Brown"),
        ("Class", "12B (24 students, mixed prior attainment)"),
        ("Date", "Monday, period 2"),
        ("Unit", "3.2 Cells  -  lesson 1 of 6"),
        ("Prior learning", "GCSE cell biology; last unit 3.1 biological molecules"),
    ],
    spec_points=[
        "3.2.1.1 Eukaryotic ultrastructure: structure AND function of each organelle",
        "The structure-function link made explicit for each",
        "Compartmentalisation as the organising idea",
    ],
    note="Reference: AQA A-level Biology 7402, section 3.2.1.",
)

# 3. donow_slide -- CLEAN
ds.donow_slide(
    prs, th,
    title="Do Now",
    columns=[
        ("Last lesson", [
            "Name the monomer of a protein.",
            "What bond joins two amino acids?",
        ]),
        ("Earlier this year", [
            "Give one property of water important in cells.",
            "Which ion is part of a haemoglobin molecule?",
        ]),
        ("Stretch", [
            "A gland cell exports a lot of protein.",
            "Predict two organelles it will be rich in.",
        ]),
    ],
    instruction="Five minutes, silent, closed book. Answers on whiteboards.",
)

# 4. objectives_slide -- SEED A3 (skipped required sub-topic: lysosomes promised, never taught)
ds.objectives_slide(
    prs, th,
    tiers=[
        ("ALL",
         "Describe the structure of the main organelles, including the role of lysosomes.",
         "1-mark recall items (AO1)"),
        ("MOST",
         "Explain how each organelle's structure is adapted to its function.",
         "2-3 mark Explain questions (AO2)"),
        ("SOME",
         "Link compartmentalisation to the cell working as a whole system.",
         "6-mark extended prose (AO1/AO2)"),
    ],
    footnote="Success = precise organelle vocabulary and the structure-function link.",
)

# 5. keywords_slide -- CLEAN
ds.keywords_slide(
    prs, th,
    title="Key words",
    pairs=[
        ("Organelle", "A specialised structure in a cell with a specific function."),
        ("Ultrastructure", "Fine cell detail seen only with an electron microscope."),
        ("Compartmentalisation", "Keeping incompatible reactions apart in organelles."),
        ("Cristae", "Folds of the inner mitochondrial membrane."),
        ("Nuclear envelope", "The double membrane with pores around the nucleus."),
        ("Vesicle", "A small membrane sac that transports substances in the cell."),
    ],
)

# 6. content_slide_bullets -- CLEAN (the eukaryotic cell)
ds.content_slide_bullets(
    prs, th,
    title="The eukaryotic cell",
    intro="Eukaryotic cells have membrane-bound organelles, each carrying out a specific function.",
    bullets=[
        "Compartmentalisation lets incompatible reactions run at the same time in one cell.",
        "Each organelle's structure is adapted to the reaction it houses.",
        "The same core organelles appear in animal, plant and fungal cells.",
    ],
    side_title="Watch for",
    side_bullets=[
        "Structure AND function - both are credited.",
        "Precise vocabulary scores; GCSE phrasing does not.",
    ],
    callout="Big idea: structure explains function - state the link, do not just name the part.",
)

# 7. content_slide_bullets -- CLEAN (mitochondria, correct)
ds.content_slide_bullets(
    prs, th,
    title="Mitochondria",
    intro="The site of aerobic respiration.",
    bullets=[
        "A double membrane; the inner membrane is folded into cristae.",
        "Cristae increase the surface area for the enzymes of aerobic respiration.",
        "This is where most of the cell's ATP is produced.",
        "The fluid interior is the matrix, where part of respiration occurs.",
    ],
)

# 8. content_slide_bullets -- SEED A1 (ribosomes: DNA misconception + reject vocab)
ds.content_slide_bullets(
    prs, th,
    title="Ribosomes",
    bullets=[
        "Ribosomes are tiny organelles made of DNA and protein.",
        "They are the site of protein synthesis (translation).",
        "Found free in the cytoplasm and bound to the rough endoplasmic reticulum.",
    ],
)

# 9. content_slide_bullets -- SEED A2 (nucleus "controls all the cell's activities")
ds.content_slide_bullets(
    prs, th,
    title="The nucleus",
    bullets=[
        "The nucleus is surrounded by a nuclear envelope with many pores.",
        "The nuclear pores control what enters and leaves, such as mRNA.",
        "It stores the cell's genetic information and controls all the cell's activities.",
    ],
)

# 10. diagram_slide -- CLEAN (eukaryotic cell; NO lysosomes)
def draw_cell(slide, th, area):
    x, y, w, h = area
    ds.diagram_node(slide, th, x + 0.35, y + 0.35, w - 0.7, h - 0.7, "",
                    th.accent_soft, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                    name="diag::membrane")
    cx, cy = x + w / 2, y + h / 2
    ds.diagram_node(slide, th, cx - 1.0, cy - 0.5, 2.0, 1.0, "Nucleus",
                    th.accent, name="diag::nucleus")
    ds.diagram_node(slide, th, x + 0.75, y + 0.75, 1.8, 0.7, "Mitochondrion",
                    th.accent_deep, name="diag::mito")
    ds.diagram_node(slide, th, x + w - 2.5, y + 0.75, 1.8, 0.7, "Golgi apparatus",
                    th.accent_deep, name="diag::golgi")
    ds.diagram_node(slide, th, x + 0.75, y + h - 1.45, 1.9, 0.7, "Rough ER",
                    th.accent_deep, name="diag::rer")
    ds.diagram_node(slide, th, x + w - 2.4, y + h - 1.45, 1.7, 0.7, "Ribosomes",
                    th.accent, name="diag::ribo")

ds.diagram_slide(
    prs, th,
    title="Inside a eukaryotic cell",
    draw_fn=draw_cell,
    legend_entries=[
        (th.accent, "Nucleus / ribosomes"),
        (th.accent_deep, "Cytoplasmic organelles"),
        (th.accent_soft, "Cell-surface membrane"),
    ],
    caption="Schematic; not to scale. Plant cells also have a cell wall, a vacuole and chloroplasts.",
)

# 11. content_slide_bullets -- CLEAN (rER and Golgi)
ds.content_slide_bullets(
    prs, th,
    title="Rough ER and Golgi apparatus",
    bullets=[
        "Ribosomes on the rough endoplasmic reticulum synthesise proteins for export.",
        "The proteins are folded, then carried in vesicles to the Golgi apparatus.",
        "The Golgi apparatus modifies the proteins, for example adding carbohydrate to form glycoproteins.",
        "It then packages and sorts them into vesicles for transport out of the cell.",
    ],
)

# 12. worked_example_slide -- CLEAN
ds.worked_example_slide(
    prs, th,
    title="Building a structure-function answer",
    i_do=[
        "Cristae are folds of the inner mitochondrial membrane.",
        "The folds increase the surface area.",
        "More surface area holds more respiratory enzymes.",
        "So: cristae -> more surface area -> more ATP produced.",
    ],
    we_do=[
        "Now the rough ER: what is its structure?",
        "What does that structure let it do?",
        "Build the same structure -> function -> consequence chain together.",
    ],
    note="Each link earns a separate mark - never jump straight to the endpoint.",
)

# 13. exam_question_slide -- SEED A4 (assessed AO2 application sent to unmodelled independent work)
ds.exam_question_slide(
    prs, th,
    title="Exam-style question",
    stem_lines=[
        "Figure 1 shows a cell from the pancreas. It has many mitochondria and extensive rough endoplasmic reticulum.",
        "Suggest how these two features are related to the function of the cell.",
    ],
    marks="3 marks",
    ao="AO2",
    command="Suggest",
    instruction="Answer this on your own now and hand it in at the end.",
)

# 14. plenary_slide -- CLEAN
ds.plenary_slide(
    prs, th,
    title="Plenary",
    question="Which statement about mitochondria would score at A-level?",
    options=[
        ("A", "Mitochondria are the powerhouse of the cell."),
        ("B", "Mitochondria make energy for the cell."),
        ("C", "Mitochondria are the site of aerobic respiration, producing ATP."),
        ("D", "Mitochondria store the cell's genetic material."),
    ],
    confidence=True,
)

out = os.path.join(HERE, "blind-lesson-01-eukaryotic.pptx")
prs.save(out)
problems = ds.qa_geometry(prs)
print("SLIDES", len(prs.slides), "QA", len(problems))
for p in problems:
    print(" -", p)
