"""
Visualizes the 10-node traffic network from nodes.csv and edges.csv
using their spatial coordinates, node types, and edge attributes.
"""

import os
import shutil
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_traffic_network():
    # 1. Load data
    nodes_df = pd.read_csv("data/nodes.csv")
    edges_df = pd.read_csv("data/edges.csv")

    # 2. Build directed graph
    G = nx.DiGraph()

    # Add nodes with attributes
    pos = {}
    node_colors = []
    node_types = []

    type_color_map = {
        "entry_point": "#2ECC71",       # Green
        "exit_point": "#E74C3C",        # Red
        "signalized": "#3498DB",        # Blue
        "unsignalized": "#F39C12"       # Amber/Orange
    }

    for _, row in nodes_df.iterrows():
        nid = int(row["node_id"])
        G.add_node(nid, **row.to_dict())
        pos[nid] = (row["pos_x"], row["pos_y"])
        ntype = row["node_type"]
        node_colors.append(type_color_map.get(ntype, "#95A5A6"))

    # Add edges
    for _, row in edges_df.iterrows():
        src = int(row["source_node"])
        dst = int(row["target_node"])
        G.add_edge(src, dst, **row.to_dict())

    # 3. Create plot
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, ax = plt.subplots(figsize=(14, 9), dpi=200)
    fig.patch.set_facecolor("#1A1D24")
    ax.set_facecolor("#222631")

    # Draw grid background
    ax.grid(True, linestyle="--", alpha=0.3, color="#4E5569")

    # Draw edges with subtle curve
    nx.draw_networkx_edges(
        G,
        pos,
        ax=ax,
        edge_color="#7F8C8D",
        width=2.0,
        alpha=0.8,
        arrows=True,
        arrowsize=16,
        arrowstyle="-|>",
        connectionstyle="arc3,rad=0.08",
        min_source_margin=18,
        min_target_margin=18
    )

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        ax=ax,
        node_color=node_colors,
        node_size=1100,
        edgecolors="#FFFFFF",
        linewidths=2.5,
        alpha=0.95
    )

    # Draw Node ID labels inside node circles
    node_id_labels = {nid: str(nid) for nid in G.nodes()}
    nx.draw_networkx_labels(
        G,
        pos,
        labels=node_id_labels,
        ax=ax,
        font_size=12,
        font_color="#FFFFFF",
        font_weight="bold",
        font_family="sans-serif"
    )

    # Add informative multi-line annotations next to each node
    for nid, (x, y) in pos.items():
        node_data = G.nodes[nid]
        name = node_data["node_name"]
        flow = int(node_data["base_flow_vph"])
        speed = float(node_data["base_speed_kmh"])
        
        # Offset annotation based on position
        y_offset = 24 if y >= 100 else -36
        
        ax.text(
            x,
            y + y_offset,
            f"{name}\n({flow} veh/h | {speed} km/h)",
            ha="center",
            va="center",
            fontsize=8.5,
            color="#E2E8F0",
            fontweight="medium",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#141821", edgecolor="#3A4154", alpha=0.9)
        )

    # Legend
    legend_patches = [
        mpatches.Patch(color=color, label=ntype.replace("_", " ").title())
        for ntype, color in type_color_map.items()
    ]
    legend = ax.legend(
        handles=legend_patches,
        loc="upper left",
        frameon=True,
        facecolor="#141821",
        edgecolor="#3A4154",
        fontsize=10,
        title="Node Types",
        title_fontsize=11
    )
    plt.setp(legend.get_title(), color="#FFFFFF", fontweight="bold")
    for text in legend.get_texts():
        text.set_color("#CBD5E1")

    # Titles & Labels
    ax.set_title("VS Workshop: 10-Node Traffic Network Spatial Graph Topology", fontsize=15, fontweight="bold", color="#FFFFFF", pad=20)
    ax.set_xlabel("Local X Coordinate (meters)", fontsize=11, color="#CBD5E1", labelpad=10)
    ax.set_ylabel("Local Y Coordinate (meters)", fontsize=11, color="#CBD5E1", labelpad=10)
    ax.tick_params(colors="#94A3B8")

    # Set coordinate margins
    ax.set_xlim(-80, 850)
    ax.set_ylim(-240, 440)

    plt.tight_layout()

    # Save output
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "network_graph.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print(f"[SUCCESS] Network graph visualization saved to: {out_path}")

    # Copy to artifact directory if available
    artifact_dir = r"C:\Users\USER\.gemini\antigravity-ide\brain\d7f1e119-cf83-4566-ac95-c1c3c8dec7da"
    if os.path.exists(artifact_dir):
        artifact_img = os.path.join(artifact_dir, "network_graph.png")
        shutil.copyfile(out_path, artifact_img)
        print(f"[SUCCESS] Copied image to artifact directory: {artifact_img}")

if __name__ == "__main__":
    plot_traffic_network()
