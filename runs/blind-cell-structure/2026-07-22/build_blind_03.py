#!/usr/bin/env python3
"""build_blind_03.py -- Deck C (blind-01): AQA 3.2.1.3 Methods of studying cells.

CONSTRUCTED stress-test lesson: 12 slides, mostly clean, three deliberately seeded
flaws (C1..C3). Uses ONLY the shared style module build/_deck_style.py. This script
plants seeded text verbatim; it adds no speaker notes or flaw-revealing annotations.
"""

import os
import sys

from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))   # this run folder
sys.path.insert(0, HERE)  # _deck_style.py lives alongside this script
import _deck_style as ds

th = ds.build_theme("C", "AQA 3.2.1.3",
                    "AQA A-level Biology  ·  3.2.1.3 Methods of studying cells")
prs = ds.new_deck()

# 1. title_slide -- CLEAN
ds.title_slide(
    prs, th,
    title="Methods of studying cells",
    subtitle="Microscopy, magnification and cell fractionation",
    meta_lines=["Year 12 Biology  -  Lesson 3 of 6", "Class 12B  -  40 minutes"],
)

# 2. staff_slide -- CLEAN
ds.staff_slide(
    prs, th,
    title="Lesson on a page",
    rows=[
        ("Teacher", "Miss A. Brown"),
        ("Class", "12B (24 students)"),
        ("Date", "Friday, period 1"),
        ("Unit", "3.2 Cells  -  lesson 3 of 6"),
        ("Prior learning", "Eukaryotic and prokaryotic cell structure"),
    ],
    spec_points=[
        "3.2.1.3 Microscopy: resolution vs magnification; light, TEM, SEM",
        "Magnification calculation with unit conversion",
        "Cell fractionation by differential centrifugation",
    ],
    note="Required-practical skill: optical microscopy and scientific drawing.",
)

# 3. donow_slide -- CLEAN
ds.donow_slide(
    prs, th,
    title="Do Now",
    columns=[
        ("Last lesson", [
            "Give one feature found in all prokaryotes.",
            "What is a capsid?",
        ]),
        ("Earlier this year", [
            "Convert 2 mm into micrometres.",
            "How many nm are in 1 um?",
        ]),
        ("Stretch", [
            "A student cannot see mitochondria with a light microscope.",
            "Suggest why - be precise.",
        ]),
    ],
    instruction="Five minutes, silent, closed book.",
)

# 4. objectives_slide -- CLEAN (everything promised is taught)
ds.objectives_slide(
    prs, th,
    tiers=[
        ("ALL",
         "State the difference between magnification and resolution.",
         "1-mark recall (AO1)"),
        ("MOST",
         "Calculate magnification and convert the units correctly.",
         "Calculate (AO2)"),
        ("SOME",
         "Describe how cell fractionation separates organelles.",
         "2-mark Describe (AO1)"),
    ],
    footnote="Calculation marks split method from answer - show every step.",
)

# 5. keywords_slide -- CLEAN
ds.keywords_slide(
    prs, th,
    title="Key words",
    pairs=[
        ("Magnification", "How many times bigger the image is than the object."),
        ("Resolution", "The smallest distance at which two points look separate."),
        ("Differential centrifugation",
         "Spinning a sample at increasing speeds to separate organelles."),
        ("Supernatant", "The liquid above the pellet after centrifuging."),
        ("Pellet", "The solid that collects at the bottom after centrifuging."),
        ("Isotonic", "Having the same water potential as the organelles."),
    ],
)

# 6. content_slide_bullets -- SEED C2 ("clearer" reject vocabulary for resolution)
ds.content_slide_bullets(
    prs, th,
    title="Magnification and resolution",
    intro="These two ideas are not the same - AQA tests them as separate terms.",
    bullets=[
        "Magnification is how many times larger the image is than the object.",
        "Resolution is the smallest distance at which two points can still be told apart.",
        "An electron microscope has a much higher resolution, so it gives a far clearer "
        "image than a light microscope.",
    ],
)

# 7. content_slide_bullets -- CLEAN (three microscopes, paired contrasts)
ds.content_slide_bullets(
    prs, th,
    title="Three microscopes",
    bullets=[
        "Light microscope: resolution about 0.2 um; views living specimens; low resolution.",
        "TEM uses electrons where the light microscope uses light, giving much higher "
        "resolution (about 0.1 nm).",
        "TEM gives a 2-D image of internal detail; SEM gives a 3-D image of the surface.",
        "Both electron microscopes need a vacuum and non-living, prepared specimens.",
    ],
    side_title="Paired contrast",
    side_bullets=[
        "Compare like with like: 'TEM uses electrons, the light microscope uses light.'",
        "State both halves of each contrast to score.",
    ],
)

# 8. content_slide_bullets -- SEED C1 (cell fractionation: spin-faster-to-molecules,
#    omits slow-first / densest-first principle) -- CRITICAL
ds.content_slide_bullets(
    prs, th,
    title="Cell fractionation",
    intro="Cell fractionation separates organelles so they can be studied.",
    bullets=[
        "First, homogenise the tissue in a cold, isotonic, buffered solution, then filter it.",
        "Then spin the sample in a centrifuge and keep increasing the speed.",
        "The faster you spin, the smaller the structure you can separate - right down to "
        "individual molecules such as DNA.",
    ],
)

# 9. diagram_slide -- CLEAN (magnification concept)
def draw_mag(slide, th, area):
    x, y, w, h = area
    cy = y + h / 2
    ds.diagram_node(slide, th, x + 0.7, cy - 0.4, 1.3, 0.8, "Object",
                    th.accent_deep, name="diag::obj")
    ds.diagram_node(slide, th, x + 3.5, cy - 0.95, 1.25, 1.9, "Lens",
                    th.accent_deep, shape=MSO_SHAPE.OVAL, name="diag::lens")
    ds.diagram_node(slide, th, x + w - 3.0, cy - 1.2, 2.6, 2.4, "Magnified image",
                    th.accent, size=13, name="diag::img")

ds.diagram_slide(
    prs, th,
    title="How magnification works",
    draw_fn=draw_mag,
    legend_entries=[
        (th.accent_deep, "Object and lens"),
        (th.accent, "Magnified image"),
    ],
    caption="magnification = image size / actual size. The image is many times larger "
            "than the object.",
)

# 10. worked_example_slide -- CLEAN (magnification calculation modelled correctly)
ds.worked_example_slide(
    prs, th,
    title="Worked example: magnification",
    i_do=[
        "Image size = 40 mm, magnification = x 400. Find the actual size.",
        "Rearrange: actual size = image size / magnification.",
        "actual = 40 / 400 = 0.1 mm.",
        "Convert to micrometres: 0.1 mm x 1000 = 100 um (a separate mark).",
    ],
    we_do=[
        "New values: image size = 25 mm, magnification = x 500.",
        "We rearrange, divide, then convert the units together.",
        "Show method and answer on separate lines.",
    ],
    note="AQA pays the unit conversion as its own mark - never skip it.",
)

# 11. exam_question_slide -- SEED C3 (percentage-error/uncertainty: assessed format to
#     independent practice, unmodelled)
ds.exam_question_slide(
    prs, th,
    title="Exam-style question",
    stem_lines=[
        "A student measures an alveolus on a 1 mm scale as 6 mm across.",
        "Give the uncertainty of this two-point measurement and calculate the "
        "percentage error.",
    ],
    marks="2 marks",
    ao="AO2",
    command="Calculate",
    instruction="Work through questions 1 to 6 on the sheet on your own now.",
)

# 12. plenary_slide -- CLEAN
ds.plenary_slide(
    prs, th,
    title="Plenary",
    question="A light microscope cannot show two organelles that are very close "
             "together. Why?",
    options=[
        ("A", "Its magnification is too low."),
        ("B", "Its resolution is too low - it cannot separate points that close together."),
        ("C", "The image is not clear enough."),
        ("D", "The specimen is too thick."),
    ],
    confidence=True,
)

out = os.path.join(HERE, "blind-lesson-03-studying-cells.pptx")
prs.save(out)
problems = ds.qa_geometry(prs)
print("SLIDES", len(prs.slides), "QA", len(problems))
for p in problems:
    print(" -", p)
