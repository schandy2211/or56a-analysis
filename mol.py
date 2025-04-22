from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign
from rdkit.Chem import rdmolfiles

# Define SMILES
ligands = {
    "geosmin": "CC1CCC2(C(C1)CCC3(C2CCC(C3)(C)O)C)C",
    "linalool": "CC(C)=CCCC(C)(C=C)O"
}

# Process each ligand
for name, smiles in ligands.items():
    # Convert SMILES to molecule
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)  # Add hydrogens

    # Generate 3D coordinates
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.UFFOptimizeMolecule(mol)

    # Write to PDB file
    pdb_writer = Chem.rdmolfiles.PDBWriter(f"{name}.pdb")
    pdb_writer.write(mol)
    pdb_writer.close()

    print(f"{name}.pdb written successfully!")
