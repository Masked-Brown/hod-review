<!-- M3 gate fixture · EXPECT: MALFORMED_BLOCK · PRINCIPLE and SPEC are in the wrong order, breaking the fixed field sequence. -->

# Findings

SEVERITY: MAJOR
SLIDE: 3
QUOTE: "Mitochondria are the powerhouse of the cell and produce energy for respiration."
SPEC: AQA 3.2.1 — ATP not "energy"
PRINCIPLE: —
WHY: The block puts SPEC before PRINCIPLE, so the fixed field order is broken and the parser cannot trust the block.
QUESTION: Is every field present and in the order the schema fixes?
