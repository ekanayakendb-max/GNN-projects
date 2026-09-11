# VS Workshop GNN (PTV Vissim & Graph Neural Networks)

[![Research Group](https://img.shields.io/badge/Research%20Group-TRANSIIT%20SIIT-blue.svg)](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-green.svg)](https://python.org)
[![Simulation](https://img.shields.io/badge/Simulator-PTV%20Vissim%202024%2F2025-orange.svg)](https://www.ptvgroup.com)
[![PyTorch Geometric](https://img.shields.io/badge/GNN-PyTorch%20Geometric-red.svg)](https://pytorch-geometric.readthedocs.io/)

A collaborative research and workshop repository bridging microscopic traffic simulation using **PTV Vissim** with modern **Graph Neural Network (GNN)** architectures for spatial-temporal traffic state forecasting and intelligent transportation control.

Developed within the **TRANSIIT Research Group** at the **Sirindhorn International Institute of Technology (SIIT)**.

---

## Quick Navigation

- 🚀 **[Getting Started Guide (`start.md`)](start.md):** Complete quickstart, system prerequisites, Vissim COM API setup, and workshop syllabus.
- 📜 **[Activity & Change Log (`history.md`)](history.md):** Chronological log of session activities, observations, and next-step checklists.
- 📊 **[Data (`data/`)](data/):** Sample network representations, including [`nodes.csv`](data/nodes.csv).
- ⚙️ **[Agent Skills & Rules (`.agents/`)](.agents/):** Custom agent capabilities, including the [`end-session`](.agents/skills/end-session/SKILL.md) skill.

---

## Architecture Overview

```
+------------------------+      COM API       +--------------------------+
|       PTV Vissim       | <================> | Python Automation Script |
| (Microscopic Simulator)|                    |      (pywin32 / COM)     |
+------------------------+                    +--------------------------+
            |                                               |
            v                                               v
    [.inpx Network]                                 [Traffic Metrics]
            |                                               |
            +-----------------------+-----------------------+
                                    |
                                    v
                     +-----------------------------+
                     | Graph Construction Pipeline |
                     | Nodes: Intersections/Links  |
                     | Edges: Lanes/Connectors     |
                     | Attributes: Length, Speed   |
                     +-----------------------------+
                                    |
                                    v
                     +-----------------------------+
                     |  PyTorch Geometric / GNN    |
                     | (Spatial-Temporal Modeling) |
                     +-----------------------------+
```

---

## Quickstart

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install pywin32 numpy pandas networkx torch torch_geometric matplotlib pyyaml
```

For full details and COM testing scripts, refer to [`start.md`](start.md).
