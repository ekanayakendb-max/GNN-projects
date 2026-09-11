# VS Workshop GNN: Getting Started Guide (`start.md`)

> **Project:** PTV Vissim & Graph Neural Networks (GNN) Workshop  
> **Research Group:** TRANSIIT Research Group, SIIT (Sirindhorn International Institute of Technology)  
> **Topic:** Integrating Microscopic Traffic Simulation (PTV Vissim) with Graph Neural Networks for Spatial-Temporal Traffic Modeling & Control  
> **Status:** Active / Workshop Kickoff  

> [!IMPORTANT]
> **Session End Protocol (`end-session` skill):** Whenever the user indicates to end the session (e.g., "end the session", "wrap up", "stop here"), the assistant activates the [`end-session`](file:///.agents/skills/end-session/SKILL.md) skill to automatically update [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md) by appending a comprehensive session log entry with timestamp, completed work, observations, and next-session action items.

---

## 1. Project Overview

The **VS Workshop GNN** project focuses on bridging microscopic traffic simulation using **PTV Vissim** with modern **Graph Neural Network (GNN)** architectures. 

Urban transportation systems possess inherent spatial network topology (road segments, intersections, ramps) combined with dynamic temporal flow dynamics (speeds, vehicle counts, delays, queue lengths). This project provides the foundational pipeline to:
1. **Model & Simulate:** Run micro-simulations in PTV Vissim via the COM API.
2. **Graph Representation:** Transform road networks (links, connectors, signal heads, detectors) into graph structures $\mathcal{G} = (\mathcal{V}, \mathcal{E})$.
3. **Feature Engineering:** Extract static topological features (link lengths, capacities, speed limits) and dynamic temporal features (flow, occupancy, queue length).
4. **Deep Learning with GNNs:** Train spatial-temporal GNN models (e.g., GCN, GAT, ST-GCN, DCRNN) for traffic state prediction and adaptive control.
5. **Evaluation & Closed-Loop Control:** Feed predicted states or control policies back into the simulation environment.

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

## 2. Directory Structure

Recommended directory layout for this workshop repository:

```text
VS workshop GNN/
├── start.md                 # Project entry point and quickstart instructions (this file)
├── README.md                # General repository description and participant notes
├── requirements.txt         # Python library dependencies
├── configs/                 # Configuration files (YAML / JSON)
│   ├── vissim_config.yaml   # Simulation parameters, layout paths, seeds
│   └── model_config.yaml    # GNN model hyperparameters, learning rates, epochs
├── data/                    # Datasets and simulation files
│   ├── networks/            # PTV Vissim network files (.inpx, .layx)
│   ├── raw/                 # Raw simulation outputs (.fzp, .att, CSVs)
│   └── processed/           # Processed PyG graph datasets (.pt, .npz)
├── models/                  # GNN model implementations
│   ├── __init__.py
│   ├── gcn.py               # Graph Convolutional Network baseline
│   ├── gat.py               # Graph Attention Network
│   └── stgcn.py             # Spatio-Temporal GNN architecture
├── scripts/                 # Core execution and automation scripts
│   ├── vissim_com.py        # PTV Vissim COM interface wrapper
│   ├── extract_graph.py     # Parses .inpx / Vissim objects into graph topology
│   ├── run_simulation.py    # Batch simulation runner and data collector
│   ├── train.py             # Model training loop
│   └── evaluate.py          # Validation and performance metrics (RMSE, MAE)
└── notebooks/               # Interactive Jupyter notebooks for tutorials & workshop
    ├── 01_vissim_com_demo.ipynb
    ├── 02_graph_construction.ipynb
    └── 03_gnn_traffic_prediction.ipynb
```

---

## 3. System Requirements & Prerequisites

### 3.1 Software Requirements
- **Operating System:** Windows 10 / 11 (64-bit required for PTV Vissim COM API)
- **PTV Vissim:** PTV Vissim 2024 / 2025 (with COM interface support enabled)
- **Python:** Python 3.10 – 3.12 (Recommended: 64-bit Python to interface with 64-bit Vissim)
- **CUDA Toolkit (Optional):** CUDA 11.8 or 12.x if training on GPU

### 3.2 Core Python Libraries
- **Simulation & Automation:** `pywin32`
- **Data & Scientific Computing:** `numpy`, `pandas`, `scipy`, `scikit-learn`
- **Graph Processing:** `networkx`, `torch_geometric` (PyG)
- **Deep Learning:** `torch` (PyTorch)
- **Visualization:** `matplotlib`, `seaborn`
- **Development & Notebooks:** `jupyterlab`, `pyyaml`, `tqdm`

---

## 4. Quickstart: Step-by-Step Setup

### Step 1: Create and Activate Virtual Environment

Open PowerShell in this project folder:

```powershell
# Create a virtual environment (named .venv)
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate.ps1
```

> *Tip:* If PowerShell displays an execution policy error, run:  
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### Step 2: Install Dependencies

Create a `requirements.txt` file or install the core libraries:

```powershell
pip install --upgrade pip
pip install pywin32 numpy pandas matplotlib seaborn pyyaml tqdm networkx jupyterlab
```

For **PyTorch** and **PyTorch Geometric (PyG)**, install according to your hardware:

- **CPU Only:**
  ```powershell
  pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
  pip install torch_geometric
  ```
- **GPU (CUDA 12.1):**
  ```powershell
  pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
  pip install torch_geometric
  ```

---

## 5. Verification: Testing the PTV Vissim COM Connection

To verify that Python can communicate with PTV Vissim via COM, run this quick test script:

```python
# test_vissim_connection.py
import win32com.client

def test_vissim():
    print("Attempting to connect to PTV Vissim COM server...")
    try:
        # Launch Vissim instance
        vissim = win32com.client.gencache.EnsureDispatch("Vissim.Vissim")
        print(f"[SUCCESS] Connected to PTV Vissim: {vissim.AttValue('Version')}")
        
        # Close connection without saving
        vissim.Exit()
        print("[INFO] Vissim instance closed successfully.")
    except Exception as e:
        print(f"[ERROR] Could not connect to Vissim COM interface: {e}")

if __name__ == "__main__":
    test_vissim()
```

Run the script:
```powershell
python test_vissim_connection.py
```

---

## 6. Graph Representation Concept

In traffic networks, we can define the graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ in two common representations:

### Representation A: Intersection-Centric (Primal Graph)
- **Nodes ($\mathcal{V}$):** Signalized and unsignalized intersections.
- **Edges ($\mathcal{E}$):** Road links connecting intersections.
- **Node Features ($X$):** Total inflow/outflow, average vehicle delay, current signal phase state.
- **Edge Attributes ($E$):** Road length, number of lanes, free-flow speed.

### Representation B: Link / Detector-Centric (Dual / Segment Graph)
- **Nodes ($\mathcal{V}$):** Individual road segments or loop detectors.
- **Edges ($\mathcal{E}$):** Upstream-to-downstream topological transitions and turning movements.
- **Node Features ($X_t$):** Time-series flow ($q$), spot speed ($v$), occupancy ($o$), queue length ($l$).
- **Edge Weights ($W$):** Connectivity weights (e.g., transition probabilities, inverse Euclidean distances, or adjacency matrix $A \in \{0, 1\}^{N \times N}$).

---

## 7. Workshop Modules & Roadmap

| Module | Topic | Description | Output |
| :--- | :--- | :--- | :--- |
| **01** | **Vissim COM Automation** | Interfacing with Vissim using Python, controlling simulation steps, dynamic inputs. | `vissim_com.py` |
| **02** | **Graph Extraction** | Parsing `.inpx` XML networks and extracting adjacency matrices & link geometries. | `extract_graph.py` |
| **03** | **Dataset Generation** | Collecting multi-step spatial-temporal traffic data across various random seeds. | `data/processed/` |
| **04** | **Spatial GNN (GCN/GAT)** | Implementing static and dynamic graph convolution for traffic speed/flow prediction. | `models/gcn.py` |
| **05** | **Spatio-Temporal Modeling** | Temporal convolutions (GRU/LSTM/TCN) + spatial graph convolution (STGCN/DCRNN). | `models/stgcn.py` |
| **06** | **Evaluation & Insights** | Performance metrics, error heatmaps across network links, and presentation slides. | `results/` |

---

## 8. Common Troubleshooting & FAQs

- **Issue: `win32com.client` cannot find Vissim COM server**  
  *Fix:* Verify that your Python installation bitness matches your PTV Vissim bitness (both must be 64-bit). Also ensure Vissim has been registered once by launching it as Administrator.
- **Issue: PyTorch Geometric CUDA binary mismatch**  
  *Fix:* Check `python -c "import torch; print(torch.__version__, torch.cuda.is_available())"` to ensure compatible CUDA runtime.
- **Issue: Vissim simulation runs slowly via COM**  
  *Fix:* Disable graphics update during batch data collection using:  
  `vissim.Graphics.CurrentNetworkWindow.SetAttValue("QuickMode", True)`

---

## 9. Contacts & References
- **Group:** TRANSIIT Research Group, SIIT, Thammasat University
- **PTV Vissim COM Documentation:** Found under `C:\Program Files\PTV Vision\PTV Vissim [Version]\Doc\Eng\Vissim [Version] - COM Introduction.pdf`
- **PyTorch Geometric Docs:** [https://pytorch-geometric.readthedocs.io/](https://pytorch-geometric.readthedocs.io/)
- **PyTorch Docs:** [https://pytorch.org/docs/stable/index.html](https://pytorch.org/docs/stable/index.html)

---

## 10. Session Workflow Protocol & History Logging Rules

To maintain seamless continuity across research and development sessions, this workflow is formalized as the **[`end-session`](file:///.agents/skills/end-session/SKILL.md)** skill:

- **Trigger:** Whenever the user explicitly states to end or wrap up a session (e.g., *"end the session"*, *"wrap up"*, *"let's stop here for today"*).
- **Mandatory Procedure (defined in [`.agents/skills/end-session/SKILL.md`](file:///.agents/skills/end-session/SKILL.md)):**
  1. The assistant activates the `end-session` skill and appends a new chronological entry to [`history.md`](file:///e:/SIIT/TRANSIIT/Group%20meetings/Projects/VS%20workshop%20GNN/history.md).
  2. The entry records:
     - **Date & Timestamp:** Local date and time (`[YYYY-MM-DD HH:MM:SS ±HH:MM]`).
     - **Activity Log:** Specific summary of tasks completed, files created, tests executed, or code changes made during the session.
     - **Comments / Observations:** Key findings, parameter choices, simulation observations, or technical hurdles encountered.
     - **Action Needed (Checklist):** Clear, actionable `- [ ]` checklist items prepared for immediate pickup in the subsequent session.
     - **Logged By:** Attribution tag.
  3. Confirm to the user that `history.md` is updated and summarize what is queued for the next session.


