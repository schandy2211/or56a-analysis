# Mechanistic Analysis of Odorant Antagonism in Drosophila Or56a

This project explores how the agonist **geosmin** and antagonist **linalool** interact with the *Drosophila melanogaster* olfactory receptor Or56a, using a combination of **AlphaFold-based structure prediction**, **fpocket pocket identification**, **AutoDock Vina docking**, and **PyMOL structural alignment**.

The aim is to propose a mechanistic hypothesis for **odorant antagonism**, validating predicted binding pockets through structural overlays with experimental insect olfactory receptors (8V02, 6C70), and identifying features that support allosteric vs orthosteric binding.

---

## 🧪 Key Highlights

- **Structure Prediction & Validation**:
  - Used AlphaFold2-predicted Or56a model.
  - Validated against 8V02 and 6C70 via RMSD analysis (PyMOL).

- **Ligand Docking**:
  - Ligands: Geosmin (agonist) and Linalool (antagonist).
  - RDKit for geometry optimization, Open Babel for Gasteiger charges.
  - Docking via AutoDock Vina into fpocket-identified cavities.

- **Mechanistic Insights**:
  - Geosmin binds deeply to **Pocket 2** → orthosteric activation.
  - Linalool prefers **Pocket 1** → possible noncompetitive/allosteric antagonism.
  - Pose diversity suggests a dual inhibition mechanism.

---

## 🔧 Tools Used

- AlphaFold2 (structure prediction)
- AutoDock Vina (molecular docking)
- RDKit & Open Babel (ligand prep)
- fpocket (binding pocket detection)
- PyMOL (structural validation)
- Py3Dmol, xTB planned for future enhancements

---

## 📂 Contents

- `notebooks/`: Google Colab notebook for running docking pipeline
- `docs/`: Full write-up (Monarch assignment)
- `data/`: Input structures (add `.pdb`, `.pdbqt`)
- `README.md`: Project overview and instructions

---

## 📈 Future Extensions

- MD simulations to evaluate dynamic pocket flexibility
- QM calculations (GFN2-xTB, DFT) for binding energy refinement
- ML integration for pose filtering and predictive modeling

---

## 📄 Report

For full context, please see the detailed report in `docs/Monarch_assignment.pdf`

---

## 📜 License

MIT
